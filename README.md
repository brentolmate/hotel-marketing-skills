# Skills de marketing hotelero · es-MX

Versión 1.1.0 · 22 de octubre de 2026 · ExpertoSEO.mx

Tres skills independientes para hoteles, resorts, retiros y villas. Preparan planes y borradores en español de México. Funcionan sin OpenSEO, CRM, API de envío ni acceso a cursos.

Creado por [ExpertoSEO.mx](https://expertoseo.mx/). Puedes usarlo y adaptarlo con tus propias propiedades, tarifas y condiciones.

| Skill | Resultado |
| --- | --- |
| [hotel-marketing-plan](skills/hotel-marketing-plan/SKILL.md) | Oportunidad, público, oferta, canales, acciones, mapa de contenido e indicadores |
| [hotel-guest-reactivation](skills/hotel-guest-reactivation/SKILL.md) | Segmentos de huéspedes anteriores, campaña de regreso, correos/WhatsApp y reglas de salida |
| [hotel-inquiry-follow-up](skills/hotel-inquiry-follow-up/SKILL.md) | Respuesta a solicitudes, seguimiento de cotizaciones y atención de grupos o retiros |

Cada carpeta dentro de `skills/` contiene `SKILL.md`, plantillas editables y referencias. Se puede compartir una sola carpeta completa o el paquete. Los tres son autónomos; no necesitan instalarse juntos. `agents/openai.yaml` añade metadatos para Codex; el procedimiento común está en `SKILL.md`, sin sintaxis exclusiva de Claude o Codex.

## Instalación rápida con npx

Requiere Node.js 22.20 o posterior y acceso a GitHub. Desde el proyecto donde quieras usarlos:

```bash
npx skills add brentolmate/hotel-marketing-skills
```

El instalador permite elegir skills y agentes. La instalación es del proyecto por defecto; añade `-g` para uso personal entre proyectos. Puedes ver el contenido disponible sin instalar:

```bash
npx skills add brentolmate/hotel-marketing-skills --list
```

Para instalar los tres en Codex y Claude Code sin seleccionar cada uno:

```bash
npx skills add brentolmate/hotel-marketing-skills --skill '*' --agent codex --agent claude-code --copy --yes
```

Usamos el [instalador abierto de Vercel](https://github.com/vercel-labs/skills); este repositorio no publica un paquete npm propio. El instalador copia las instrucciones, no ejecuta campañas hoteleras.

## Instalar como plugin de Claude Code

Dentro de Claude Code:

```text
/plugin marketplace add brentolmate/hotel-marketing-skills
/plugin install hotel-marketing@expertoseo
```

En versiones que admiten instalación directa desde un marketplace, también puedes usar:

```text
/plugin install hotel-marketing --marketplace brentolmate/hotel-marketing-skills
```

Abre una sesión nueva y ejecuta el skill con el prefijo del plugin:

```text
/hotel-marketing:hotel-marketing-plan Prepara el plan para nuestro hotel con la ficha que te comparto.
/hotel-marketing:hotel-guest-reactivation Prepara dos correos de regreso, sin enviarlos.
/hotel-marketing:hotel-inquiry-follow-up Redacta la respuesta a esta consulta anonimizada.
```

El marketplace se llama `expertoseo`; el plugin se llama `hotel-marketing`. Puedes comprobar el contenido desde la terminal con `claude plugin details hotel-marketing`. Debe mostrar tres skills. [Documentación oficial de Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).

## Instalar como plugin de Codex

Con una versión de Codex CLI que incluya `plugin`:

```bash
codex plugin marketplace add brentolmate/hotel-marketing-skills
codex plugin add hotel-marketing@expertoseo
codex plugin list --marketplace expertoseo --json
```

Abre una sesión nueva y selecciona el skill del plugin en el selector. En clientes de escritorio compatibles, también puedes explorar el marketplace configurado desde el panel de plugins. Si tu CLI no reconoce `plugin`, usa la ruta de npx o la copia manual, o actualiza tu instalación de Codex. [Documentación oficial de OpenAI](https://developers.openai.com/plugins/build/plugins).

Los plugins de Claude Code y Codex utilizan el mismo contenido de `skills/`. Elige una ruta de instalación por agente para evitar copias duplicadas. Estos catálogos están alojados en este repositorio; no implican publicación o aprobación en los directorios oficiales de OpenAI o Anthropic.

## Actualizaciones y desinstalación

Si instalaste con npx, desde el mismo proyecto y alcance puedes comprobar y aplicar actualizaciones con `npx skills check` y `npx skills update`. Para instalación personal conserva `-g` según las opciones del instalador.

En Claude Code, actualiza el marketplace con `claude plugin marketplace update expertoseo` y el plugin con `claude plugin update hotel-marketing@expertoseo`. En Codex, actualiza el catálogo con `codex plugin marketplace upgrade expertoseo` y revisa la versión disponible en el gestor de plugins.

Para quitar el plugin usa `claude plugin uninstall hotel-marketing@expertoseo` o `codex plugin remove hotel-marketing@expertoseo`, según el agente. Una copia manual se retira eliminando únicamente la carpeta del skill que instalaste. Conserva tus planes y borradores fuera de las carpetas instaladas para que las actualizaciones no los sustituyan.

## Descargar el repositorio

Puedes descargar el ZIP desde **Code → Download ZIP** en GitHub y descomprimirlo. Si tienes Git instalado, también puedes clonarlo:

```bash
git clone https://github.com/brentolmate/hotel-marketing-skills.git
cd hotel-marketing-skills
```

Ejecuta las instrucciones de instalación desde esta carpeta, donde están `README.md` y `skills/`. Necesitas Codex o Claude Code configurado para usar skills locales. No hay paquetes de Python o Node que instalar para utilizar estas instrucciones y plantillas. Los comandos siguientes son para macOS y Linux; en Windows puedes copiar las carpetas manualmente a la ubicación correspondiente dentro de tu carpeta de usuario.

## Alternativa manual en Codex

Copia las carpetas de los skills a `.agents/skills/` dentro del proyecto donde los quieras usar, o a `~/.agents/skills/` para uso personal entre proyectos. No copies sólo el archivo `SKILL.md`: conserva sus subcarpetas. Evita duplicar una instalación existente con el mismo nombre.

Desde la raíz del paquete descomprimido, para uso personal en macOS/Linux, si esos nombres no están instalados:

```bash
mkdir -p ~/.agents/skills
cp -Rn skills/hotel-marketing-plan skills/hotel-guest-reactivation skills/hotel-inquiry-follow-up ~/.agents/skills/
```

`-n` conserva archivos existentes; para actualizar una versión instalada, compara primero las carpetas y reemplaza deliberadamente la versión elegida. Abre una sesión nueva y comprueba que aparecen en el selector de skills.

Invocación:

```text
Usa $hotel-marketing-plan. Somos un hotel boutique de 18 habitaciones en Mérida. Queremos mejorar las reservas entre semana. Te comparto nuestra ficha con datos agregados. Prepara el plan en español de México.
```

Otros ejemplos para copiar:

```text
Usa $hotel-guest-reactivation. Prepara dos correos para huéspedes anteriores que la propiedad confirmó como elegibles para marketing por correo. No tenemos descuentos aprobados. Usa la ficha de campaña y conserva como pendientes los datos que falten. No envíes nada.
```

```text
Usa $hotel-inquiry-follow-up. Un organizador consulta por un retiro para 16 personas del 15 al 18 de enero de 2027. No tenemos disponibilidad ni tarifas confirmadas. Redacta la respuesta y separa las notas internas del mensaje para el huésped.
```

Rutas e invocación verificadas en la [documentación oficial de Codex](https://learn.chatgpt.com/docs/build-skills), el 22 de octubre de 2026. La disponibilidad puede depender de la configuración de la organización.

## Alternativa manual en Claude Code

Copia las mismas carpetas a `.claude/skills/` dentro del proyecto, o a `~/.claude/skills/` para uso personal. No requieren conversión.

```bash
mkdir -p ~/.claude/skills
cp -Rn skills/hotel-marketing-plan skills/hotel-guest-reactivation skills/hotel-inquiry-follow-up ~/.claude/skills/
```

Abre una sesión nueva. Usa `/hotel-marketing-plan`, `/hotel-guest-reactivation` o `/hotel-inquiry-follow-up`, seguido del contexto. Por ejemplo:

```text
/hotel-inquiry-follow-up Prepara el siguiente mensaje para esta consulta anonimizada de un organizador de retiro. No tenemos disponibilidad ni tarifa confirmadas. Entrega en español de México.
```

También puedes invocar `/hotel-marketing-plan` o `/hotel-guest-reactivation` con los mismos datos de los ejemplos anteriores. Para instalarlos sólo en un proyecto, usa su carpeta `.claude/skills/` en lugar de la ubicación personal. En Codex, la ubicación de proyecto equivalente es `.agents/skills/`.

Si un skill no aparece, comprueba que la ruta termine en `<nombre-del-skill>/SKILL.md`, conserva `assets/`, `references/` y `agents/` dentro de esa carpeta y abre una sesión nueva. Los nombres de invocación se mantienen en inglés; las instrucciones y los resultados de trabajo son en español de México.

Si instalaste el plugin de Claude Code, recuerda el prefijo `/hotel-marketing:`. Las invocaciones sin ese prefijo en esta sección corresponden a la instalación manual o mediante npx.

Rutas e invocación verificadas en la [documentación oficial de Claude Code](https://code.claude.com/docs/en/skills), el 22 de octubre de 2026. Estas instrucciones son para sesiones locales de Claude Code; no equivalen a instalar en Claude.ai o sesiones cloud.

## Cómo usarlos juntos

1. Completa los datos conocidos de `hotel-marketing-plan/assets/ficha-hotel.md` y pide un plan. Puede comenzar con información incompleta y supuestos explícitos.
2. Si la prioridad es invitar a huéspedes anteriores, usa `hotel-guest-reactivation` con una descripción agregada del segmento, condiciones aprobadas y elegibilidad de marketing por canal.
3. Cuando llegue una consulta, usa `hotel-inquiry-follow-up` con un resumen anónimo del hilo, etapa y condiciones verificadas.

No es necesario compartir una base identificable de huéspedes. Tener un correo por una reserva anterior no confirma elegibilidad para marketing. Los skills preparan trabajo; no envían mensajes, apartan habitaciones, cobran ni activan campañas por sí mismos. Una instrucción posterior de ejecución necesita contexto y autorización para la acción concreta.

Las tarifas y el presupuesto son los de cada propiedad. No hay un precio de agencia, descuento, cuota de contenidos ni promesa de resultados incorporados.

## Ejemplos y revisión

- [Ejemplo de plan](examples/01-plan-hotel.md)
- [Ejemplo de reactivación](examples/02-reactivacion.md)
- [Ejemplo de seguimiento de retiro](examples/03-seguimiento-retiro.md)
- [Escenarios para evaluar decisiones](quality/escenarios.md)
- [Resultados de la evaluación en Codex](quality/codex-evaluation.md)
- [Comprobación de instalación y plugins](quality/distribution-tests.md)
- [Ideas aplicadas de otro repositorio de skills](docs/aprendizajes.md)

Los ejemplos usan propiedades y cifras ficticias, no resultados de clientes. Se ejecutaron 15 escenarios en tres sesiones independientes de subagentes de Codex, con revisión de las salidas por el agente principal. Se corrigió una filtración de detalles operativos al texto para huéspedes y se repitieron tres escenarios en una cuarta sesión nueva. Los casos revisados cumplen los criterios; también pasaron estructura, metadatos, enlaces e integridad del ZIP.

Esta evaluación de contenido usó invocación explícita y ejecución local aislada. La instalación y el inventario del plugin se comprobaron también con las CLI de Claude Code y Codex; eso no equivale a evaluar los mensajes generados por un modelo de Claude. No se probaron campañas en producción ni se garantizan salidas idénticas entre modelos o sesiones.

## Procedencia y permiso para compartir

Las instrucciones y plantillas son elaboración original de ExpertoSEO.mx. Adaptan principios consultados de Nathan Gotch y Wolfpack; cada skill incluye atribuciones, aplicación y límites en `references/fuentes.md`. No se redistribuyen materiales de pago, transcripciones ni archivos de esos cursos. Tampoco se atribuye a sus autores un SOP hotelero que no estaba disponible en las fuentes.

Puedes usar, modificar y compartir el contenido original de este paquete bajo [licencia MIT](LICENSE). La licencia no concede derechos sobre cursos, marcas ni documentos externos enlazados. No hay respaldo o afiliación implícitos.
