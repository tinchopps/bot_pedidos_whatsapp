from flask import Blueprint, request, jsonify

# Blueprint para el bot de pedidos
bot_pedidos_bp = Blueprint('bot_pedidos', __name__)

# Diccionario simulando la base de datos de pedidos
PEDIDOS = {
    "ABC123": "En camino",
    "XYZ789": "Entregado",
    "QWE456": "Pendiente de pago"
}

# Lista de palabras prohibidas personalizable
PALABRAS_PROHIBIDAS = [
    "maldicion1", "maldicion2", "groseria"
]

def contiene_lenguaje_inapropiado(texto):
    """Devuelve True si el texto contiene alguna palabra prohibida."""
    texto_minuscula = texto.lower()
    return any(palabra in texto_minuscula for palabra in PALABRAS_PROHIBIDAS)

@bot_pedidos_bp.route('/bot', methods=['POST'])
def bot_pedidos():
    """
    Endpoint principal del bot de WhatsApp para pedidos.
    Espera un JSON con el campo 'mensaje'.
    """
    datos = request.get_json()
    mensaje = datos.get('mensaje', '').strip()

    if not mensaje:
        return jsonify({
            "respuesta": "¡Hola! Por favor, envíame el código de tu pedido para consultar el estado."
        })

    if contiene_lenguaje_inapropiado(mensaje):
        return jsonify({
            "respuesta": "⚠️ Tu mensaje contiene lenguaje inapropiado. Por favor, usa un lenguaje adecuado."
        })

    # Si el mensaje parece un código de pedido
    estado = PEDIDOS.get(mensaje.upper())
    if estado:
        return jsonify({
            "respuesta": f"El estado de tu pedido {mensaje.upper()} es: {estado}. ¿Deseas consultar otro pedido? (Responde con el código o escribe 'salir' para finalizar)"
        })
    elif mensaje.lower() == 'salir':
        return jsonify({
            "respuesta": "¡Gracias por usar el bot de pedidos! Hasta luego."
        })
    else:
        return jsonify({
            "respuesta": "No encontré ese código de pedido. Por favor, verifica e inténtalo de nuevo."
        })
