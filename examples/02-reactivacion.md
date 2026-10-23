# Ejercicio: campaña sin descuento

Propiedad, segmento y condiciones ficticios para practicar el workflow.

## Entrada

Hotel Patio de la Costa. La propiedad confirma un segmento deduplicado de 120 antiguos huéspedes elegibles para marketing por correo; ya excluyó bajas, quejas abiertas y reservas futuras. No confirmó elegibilidad para WhatsApp. Quiere invitar a revisar estancias entre semana del 9 de noviembre al 10 de diciembre de 2026. La disponibilidad depende de las fechas elegidas. No hay descuento, beneficio ni tarifa aprobada para esta campaña. El correo de respuesta lo atiende reservas. El sistema de correo incorpora el mecanismo de baja aprobado por la propiedad. No hay fecha límite promocional.

## Salida de referencia

**Estado:** borrador para revisión operativa. Audiencia propuesta: esos 120 huéspedes por correo, previa comprobación de supresiones antes de cada contacto. No crear una versión para enviar por WhatsApp.

**Calendario propuesto:** 26 de octubre de 2026 a las 10:00, zona America/Mexico_City; seguimiento el 2 de noviembre a la misma hora sólo para quienes sigan elegibles, sin respuesta ni reserva. Dos contactos bastan para este ejercicio. Confirmar el horario con la propiedad. No inventar un tercer mensaje con plazo falso.

### Invitación

Asunto: ¿Estás pensando en volver a Puerto Vallarta?

Preencabezado: Podemos revisar opciones para una estancia entre semana.

Hola:

Gracias por haberte hospedado en Hotel Patio de la Costa. Si estás pensando en regresar a Puerto Vallarta, podemos revisar opciones entre semana del 9 de noviembre al 10 de diciembre de 2026.

¿Qué fechas tienes en mente y cuántas personas viajarían? Responde a este correo y nuestro equipo de reservas revisará disponibilidad y te compartirá las condiciones vigentes.

Equipo de reservas
Hotel Patio de la Costa

Si prefieres no recibir nuestras novedades, puedes darte de baja con el enlace al final de este correo.

### Seguimiento

Asunto: ¿Te ayudamos a revisar fechas para tu próxima estancia?

Preencabezado: Cuéntanos tus fechas y revisamos opciones vigentes.

Hola:

Te escribimos de Hotel Patio de la Costa para retomar nuestra invitación a volver a Puerto Vallarta. Si buscas una estancia entre semana del 9 de noviembre al 10 de diciembre de 2026, responde con tus fechas y el número de personas que viajarían.

Revisaremos disponibilidad y condiciones para esas fechas. Si ahora no tienes un viaje planeado, no hace falta que respondas.

Equipo de reservas
Hotel Patio de la Costa

Si prefieres no recibir nuestras novedades, puedes darte de baja con el enlace al final de este correo.

**Nota interna:** la alternativa sin nombre ya es el saludo principal. Antes de usar cualquier texto, comprobar que se insertó el enlace real de baja y que el buzón de respuestas está atendido. No afirmar que se ha enviado nada.

**Ramas:** respuesta → pausar y atender; reserva confirmada → retirar; baja → suprimir; queja → servicio; rebote → retirar del canal. Al terminar la ventana de estancia, detener la campaña.

**Medición:** cohorte inicial de hasta 120 personas, ventana de seguimiento propuesta hasta el 10 de diciembre. Registrar destinatarios únicos efectivamente entregados, respuestas, reservas netas vinculadas, cancelaciones y bajas. Si una persona recibe dos correos, no cuenta dos veces como destinataria. Sin integración de atribución, reportar sólo reservas que el equipo pueda vincular de forma documentada; no llamar incremento causal a esa cifra.
