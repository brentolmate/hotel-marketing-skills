# Comprobación de distribución — 1.1.0

Fecha: 22 de octubre de 2026.

## Entorno y resultados locales

| Ruta | Herramienta | Comprobación | Resultado |
| --- | --- | --- | --- |
| Descubrimiento de GitHub | Skills CLI 1.7.4, Node 22.22.3 | `npx skills add brentolmate/hotel-marketing-skills --list` | Encuentra los tres skills |
| Instalación npx | Skills CLI 1.7.4 | Instalar desde GitHub, seleccionar todos, agentes Codex y Claude Code, `--copy --yes`, en proyecto temporal | Copias en `.agents/skills/` y `.claude/skills/`; los 18 archivos coinciden con los evaluados |
| Manifiestos Claude | Claude Code 2.1.307 | Validar marketplace y manifiesto con `--strict` | Validación aprobada; consejo opcional de icono para un futuro envío al directorio oficial |
| Plugin Claude local | Claude Code 2.1.307 | Agregar marketplace local, instalar `hotel-marketing@expertoseo` y consultar inventario | Versión 1.1.0, tres skills, cero agentes, hooks y servidores; los archivos coinciden |
| Plugin Codex local | Codex CLI 0.163.0-alpha.11.1 | Agregar marketplace local, instalar y listar `hotel-marketing@expertoseo` | Versión 1.1.0 instalada y habilitada; los archivos coinciden |
| Plugin Claude desde GitHub | Claude Code 2.1.307 | `claude plugin install hotel-marketing --marketplace brentolmate/hotel-marketing-skills`, con configuración temporal nueva | Clona por HTTPS, instala 1.1.0 y muestra los tres skills; los 18 archivos coinciden |
| Plugin Codex desde GitHub | Codex CLI 0.163.0-alpha.11.1 | Agregar `brentolmate/hotel-marketing-skills` como marketplace e instalar `hotel-marketing@expertoseo` | Instala 1.1.0 desde el catálogo público; los 18 archivos coinciden |
| Consistencia | Python 3 | `python3 scripts/validate.py` | Versiones, metadatos, rutas de catálogo y enlaces coherentes |
| GitHub Actions | Python 3.12 en Ubuntu | Workflow `Validar distribución` del commit de publicación | [Ejecución aprobada](https://github.com/brentolmate/hotel-marketing-skills/actions/runs/39879374777) |

Se utilizó el ejecutable de Codex incluido en la aplicación de escritorio. El comando `codex` antiguo del PATH de esta máquina apuntaba a un binario ausente; no se modificó esa instalación para hacer las pruebas.

Después de publicar los manifiestos se repitió la instalación con npx desde GitHub para comprobar el repositorio con los nuevos archivos de plugins.

La configuración de Claude y el proyecto de npx se aislaron en carpetas temporales. El plugin y la fuente local de Codex usados para probar se retiraron al terminar. No se enviaron mensajes, accedió a bases de huéspedes ni modificaron reservas.

## Qué demuestran estas pruebas

Las tres rutas distribuyen las mismas instrucciones y recursos que pasaron la evaluación de quince escenarios y tres repeticiones en Codex. No se cambió el contenido de los skills en esta entrega. La nueva versión corresponde al empaquetado y su documentación.

La instalación y el inventario de Claude Code son comprobaciones reales de su sistema de plugins; no equivalen a una evaluación de los textos generados por modelos de Claude. Tampoco se ha solicitado entrada en los directorios oficiales de OpenAI o Anthropic.

La compatibilidad puede depender de la versión de cada cliente. Se documentan rutas alternativas de instalación para clientes sin soporte de plugins.
