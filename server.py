from flask import Flask, jsonify, request
from detector import recognize_faces_base64  # Add the missing import statement

app = Flask(__name__)

@app.route('/', methods=['GET'])
def bienvenida():
    return "hola"

@app.route('/', methods=['POST'])
def recognize_faces():
    # Asumiendo que el cliente envía la imagen en formato base64 en el cuerpo de la solicitud
    data = request.get_json()
    image_base64 = data['image']

    # Llama a la función del script detector que procesa la imagen en base64
    result = recognize_faces_base64(image_base64)  # Update the function call
    return jsonify({"name": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5055, debug=True)
    # El servidor (de la laptop) y el cliente (el telefono) deben estar conectada
    # al mismo wifi
    # IP FIJA DE LA LAPTOP 172.25.235.199