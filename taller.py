#taller.py
from flask import Flask, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#datos para mostrar
data = [
    {"id":1, "nombre": "Elisa", "color": "rosa" },
    {"id":2, "nombre": "Michelle", "color": "azul" },
    {"id":3, "nombre": "Cris", "color": "verde" }
]

#endpoint para json
@app.route('/data', methods=['GET'])
def recuperar_datos():
    try:
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)