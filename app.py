from flask import Flask
from rutas_bot import bot_pedidos_bp

# Inicializa la aplicación Flask
aplicacion = Flask(__name__)

# Registra el Blueprint principal del bot de pedidos
aplicacion.register_blueprint(bot_pedidos_bp)

if __name__ == "__main__":
    # Ejecuta la aplicación en modo desarrollo
    aplicacion.run(debug=True, port=5000)
