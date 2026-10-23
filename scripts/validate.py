#!/usr/bin/env python3
"""Comprobar metadatos, rutas de distribución y enlaces sin instalar dependencias."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def validate():
    portable = load("plugin.json")
    codex = load(".codex-plugin/plugin.json")
    claude = load(".claude-plugin/plugin.json")
    for manifest in (codex, claude):
        for key in ("name", "version", "description", "author", "repository", "license"):
            assert manifest[key] == portable[key], f"Metadatos distintos: {key}"
        assert "mcpServers" not in manifest and "hooks" not in manifest
    assert codex["interface"] == portable["extensions"]["com.openai"]["interface"]
    assert (ROOT / codex["skills"]).resolve() == ROOT / "skills"
    assert re.fullmatch(r"\d+\.\d+\.\d+", portable["version"])
    for relative in (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
        marketplace = load(relative)
        assert marketplace["name"] == "expertoseo"
        assert len(marketplace["plugins"]) == 1
        entry = marketplace["plugins"][0]
        assert entry["name"] == portable["name"]
        source = entry["source"]
        path = source if isinstance(source, str) else source["path"]
        assert (ROOT / path).resolve() == ROOT
    expected = {"hotel-marketing-plan", "hotel-guest-reactivation", "hotel-inquiry-follow-up"}
    assert {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()} == expected
    for name in expected:
        folder = ROOT / "skills" / name
        content = (folder / "SKILL.md").read_text(encoding="utf-8")
        assert content.startswith(f"---\nname: {name}\ndescription: ")
        assert f"${name}" in (folder / "agents/openai.yaml").read_text(encoding="utf-8")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if re.match(r"https?://|#|mailto:", link):
                continue
            target = (path.parent / link.split("#")[0]).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), f"Enlace roto: {path}: {link}"
    print(f"OK: versión {portable['version']}, tres skills, manifiestos, catálogos y enlaces locales.")


if __name__ == "__main__":
    validate()
