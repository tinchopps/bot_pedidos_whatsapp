# Instrucciones para agentes de IA en este repositorio

Este proyecto implementa un bot de atención de pedidos por WhatsApp usando Flask. Sigue estas pautas para contribuir o modificar el código de manera coherente y productiva:

## Arquitectura y flujo principal
- El bot expone un único endpoint POST `/bot` (ver `rutas_bot.py`).
- El flujo conversacional es:
  1. El bot saluda y solicita el código del pedido.
  2. Al recibir el código, consulta una "API REST" simulada (diccionario `PEDIDOS`).
  3. Devuelve el estado del pedido.
  4. Si el mensaje contiene lenguaje inapropiado (ver lista `PALABRAS_PROHIBIDAS`), responde con advertencia y no consulta la API.
  5. Permite consultar otro pedido o finalizar escribiendo 'salir'.

## Convenciones y patrones
- Todo el código, variables, funciones y comentarios deben estar en español y ser descriptivos.
- El filtro de lenguaje inapropiado es personalizable en la variable `PALABRAS_PROHIBIDAS`.
- La "API" de pedidos es un diccionario Python (`PEDIDOS`). Para agregar pedidos, edítalo directamente.
- No uses dependencias externas innecesarias. Mantén el flujo simple y directo.
- El blueprint principal es `bot_pedidos_bp` y se registra en `app.py` como `aplicacion.register_blueprint(bot_pedidos_bp)`.

## Ejemplo de petición y respuesta
- Petición:
  ```json
  { "mensaje": "ABC123" }
  ```
- Respuesta:
  ```json
  { "respuesta": "El estado de tu pedido ABC123 es: En camino. ¿Deseas consultar otro pedido? (Responde con el código o escribe 'salir' para finalizar)" }
  ```

## Archivos clave
- `app.py`: Inicializa la app Flask y registra el blueprint.
- `rutas_bot.py`: Lógica del bot, filtro de lenguaje y simulación de la API.

## Buenas prácticas específicas
- Si agregas nuevas rutas, mantén la lógica conversacional simple y coherente.
- Si modificas el filtro de lenguaje, documenta las palabras agregadas o quitadas.
- Si cambias el flujo, actualiza el README y este archivo.

---
Para dudas sobre el flujo o convenciones, revisa siempre `rutas_bot.py` y el README.
