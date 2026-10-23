# Mantenimiento del repositorio

Este repositorio distribuye skills hoteleros en español de México mediante npx, copia manual y plugins. La fuente de instrucciones está en `skills/`; no crear copias distintas por agente.

- Mantener iguales nombre, versión y metadatos compartidos de `plugin.json`, `.codex-plugin/plugin.json` y `.claude-plugin/plugin.json`.
- Cambios publicados bajo `skills/` requieren incrementar la versión de los tres manifiestos y actualizar `CHANGELOG.md`. Cambios de distribución también deben versionarse cuando afecten al usuario.
- El marketplace se llama `expertoseo` y el plugin `hotel-marketing` en ambos catálogos. Las rutas de catálogo se resuelven desde la raíz del repositorio.
- Cada skill debe funcionar instalado individualmente; usar referencias internas a su propia carpeta.
- Mantener README, ejemplos, plantillas y documentación para usuarios en español de México. No introducir tarifas, descuentos, disponibilidad o resultados de hoteles inventados fuera de ejemplos identificados como ficticios.
- No añadir contactos reales, credenciales, capturas privadas de cursos ni rutas personales.
- Antes de publicar: `python3 scripts/validate.py`, `claude plugin validate . --strict` y `claude plugin validate .claude-plugin/plugin.json --strict`. Comprobar instalación real cuando cambien las rutas o manifiestos.
- Distinguir validación de archivos, instalación, inventario y evaluación de salidas de modelos. Documentar los límites de cada prueba en `quality/`.
- La invocación de un skill autoriza preparar su entregable; no enviar mensajes, modificar CRM ni reservar alojamiento por el hecho de invocarlo.
