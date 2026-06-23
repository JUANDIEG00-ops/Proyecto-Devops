from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite que el frontend se conecte sin bloqueos de seguridad

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"mensaje": "¡Conexión exitosa desde el contenedor de Python Flask!"})

if __name__ == '__main__':
    # Escucha en todas las redes del contenedor en el puerto 5000
    app.run(host='0.0.0.0', port=5000)