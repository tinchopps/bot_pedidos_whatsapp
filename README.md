
# Bot de Consulta de Pedidos por WhatsApp

Este proyecto es un bot sencillo hecho con Flask que simula la atención de clientes por WhatsApp para consultar el estado de sus pedidos.

## 🚦 Flujo Conversacional
1. El bot solicita el código del pedido al usuario.
2. Al recibir el código, consulta una "API REST" simulada (un diccionario en el código).
3. Devuelve el estado del pedido al usuario.
4. Si el mensaje contiene lenguaje inapropiado, muestra una advertencia y no consulta la API.
5. Permite consultar otro pedido o finalizar la conversación escribiendo 'salir'.

## �️ Requisitos
- Python 3.8+
- Flask

## ▶️ Cómo ejecutar
Instala Flask si no lo tienes:
```bash
pip install flask
```
Ejecuta la app:
```bash
python app.py
```

## � Endpoint
- `POST /bot`
- Espera un JSON como:
```json
{
  "mensaje": "ABC123"
}
```
- Responde con:
```json
{
  "respuesta": "El estado de tu pedido ABC123 es: En camino. ¿Deseas consultar otro pedido? (Responde con el código o escribe 'salir' para finalizar)"
}
```

## � Personalización
- Puedes modificar la lista de palabras prohibidas en `rutas_bot.py` (variable `PALABRAS_PROHIBIDAS`).
- Los pedidos simulados están en el diccionario `PEDIDOS`.

## � Archivos principales
- `app.py`: Inicializa la app Flask y registra el blueprint.
- `rutas_bot.py`: Contiene la lógica del bot, el filtro de lenguaje y la simulación de la API.

## � Notas
- No requiere Twilio ni Ngrok para pruebas locales.
- El flujo es completamente personalizable.

---
¡Listo para usar y adaptar a tus necesidades!

---
**Autor:** Martin Lucero (Tinchopps)
Sitio web: [www.tinchopps.com.ar](http://www.tinchopps.com.ar)
