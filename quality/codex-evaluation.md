# Evaluación en Codex — versión 1.0.1

Fecha: 22 de octubre de 2026. Quince escenarios únicos, dieciocho ejecuciones y cuatro sesiones independientes de subagentes de Codex. Se usó el modelo heredado de la sesión; la herramienta de subagentes no expuso su identificador exacto en el resultado, por lo que no se atribuye una versión concreta.

## Método

Una sesión por skill en la primera pasada: cuatro casos para plan de marketing, cinco para reactivación y seis para seguimiento. Cada sesión recibió el skill, recursos locales pertinentes y entradas ficticias, sin respuestas esperadas ni ejemplos resueltos. El agente principal leyó las salidas completas y evaluó las decisiones, precisión y utilidad.

Una cuarta sesión recibió el skill de seguimiento corregido y tres entradas para repetir: cotización con total conocido, cotización vencida y retiro de grupo. No recibió la salida anterior ni el cambio esperado. No se trata de una comparación estadística, un benchmark entre modelos ni una prueba por sesión nueva para cada caso.

## Resultados revisados

| Skill | Casos | Resultado |
| --- | --- | --- |
| Plan de marketing | Recursos limitados; villa casi llena sin costos; volumen de una frase nueva; instrucción incrustada | 4 de 4 aceptados: respeta recursos, prioriza diagnóstico/conversión, no inventa margen ni volumen y mantiene alcance |
| Reactivación | Correo sin descuento; base OTA sin permiso; duplicado con baja; solicitud en inglés para WhatsApp; instrucción incrustada | 5 de 5 aceptados: es-MX, exclusiones correctas, canal elegible, villa completa y ausencia de oferta inventada |
| Seguimiento | Retiro de 16 personas; cotización vencida; reserva confirmada; rechazo de contacto; total de villa; instrucción incrustada | 5 aceptados inicialmente; el sexto calculó correctamente pero requirió pulir la separación de notas internas |
| Seguimiento, repetición | Total de villa; cotización vencida; retiro de grupo | 3 de 3 aceptados después del ajuste |

Resultado final: los quince escenarios cumplen los criterios revisados, con una corrección aplicada y comprobada. Los otros dos skills conservaron sus instrucciones porque no se observó un defecto que justificara cambiarlas.

## Corrección observada

En la primera cotización de Villa Brisa, el texto para el huésped incluyó «nos falta que dirección valide» y «no contamos con un enlace de pago autorizado». Aunque el total de 12,400 MXN y las restricciones eran correctos, esos detalles describían el proceso interno.

Se añadió una instrucción breve al skill: comunicar lo confirmado, lo pendiente y el siguiente paso; conservar aprobaciones y configuración en notas. En la nueva salida, el huésped recibió el total, la vigencia, ausencia de apartado y condiciones de pago/cancelación pendientes. Las tareas para dirección y la falta de enlace autorizado quedaron en notas internas. No se inventaron plazos, políticas o medios de pago.

## Alcance de la comprobación

- Ejecución real de instrucciones y generación de documentos por subagentes de Codex, no sólo validación de archivos.
- Invocación explícita; lectura de referencias y plantillas locales. Los tres skills también estaban disponibles en el catálogo de la sesión principal.
- Datos ficticios, sin bases de huéspedes identificables ni acceso a red, envíos, reservas o sistemas externos. Las pruebas de instrucciones incrustadas evalúan las respuestas y decisiones en ese entorno; el aislamiento también impide efectos externos.
- Revisión adicional de YAML, descripción, metadatos de invocación, enlaces locales, igualdad de copias instaladas e integridad del ZIP.
- No se probaron Claude Code, instalación en otro equipo, selección implícita en todo tipo de consulta ni funcionamiento de proveedores de correo/WhatsApp. Esta revisión no garantiza comportamiento idéntico en futuras sesiones.

Las entradas y salidas completas se conservan en el proyecto de origen, separadas de este paquete distribuible. Los escenarios reproducibles están en [escenarios](escenarios.md).
