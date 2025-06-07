from flask import Flask, request, render_template, jsonify, send_file
import qrcode
import io
import base64
import os

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Aquí puedes procesar los datos del formulario
    data = request.json
    print("Datos recibidos:", data)
    return jsonify({"status": "success", "message": "Formulario enviado correctamente"})

@app.route('/generate_qr')
def generate_qr():
    # URL del formulario usando la IP de la red local
    url = "http://192.168.1.12:5000"
    
    # Crear QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Convertir a imagen
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convertir a base64 para mostrar en web
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return render_template('qr.html', qr_image=img_base64, url=url)

@app.route('/upload_video', methods=['POST'])
def upload_video():
    # Aquí puedes manejar la subida de videos
    if 'video' not in request.files:
        return jsonify({"error": "No se encontró archivo de video"})
    
    file = request.files['video']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó archivo"})
    
    # Crear directorio uploads si no existe
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Guardar el video específico con nombre conocido
    file.save("uploads/intro_video.mov")
    return jsonify({"status": "success", "message": "Video subido correctamente"})

@app.route('/video/intro')
def serve_intro_video():
    # Buscar el video específico en múltiples ubicaciones
    video_files = [
        'static/intro_video.mov',
        'uploads/intro_video.mov',
        'uploads/copy_F5E4631D-A4E8-45A6-A683-9F7863F1B0C7.mov',
        'uploads/intro_video.mp4'
    ]
    
    for video_file in video_files:
        if os.path.exists(video_file):
            return send_file(video_file)
    
    return jsonify({"error": "Video no encontrado"}), 404

if __name__ == '__main__':
    print("🚀 Iniciando servidor Flask...")
    print("📱 Formulario disponible en: http://localhost:5000")
    print("🔗 QR Generator en: http://localhost:5000/generate_qr")
    print("🌐 Red local: http://192.168.1.12:5000")
    print("⏸️  Presiona Ctrl+C para detener el servidor")
    print("-" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000) 