<<<<<<< HEAD
# 📱 Generador de QR para Formulario con Video

Una aplicación web que genera códigos QR que llevan a un formulario elegante con espacio dedicado para videos.

## ✨ Características

- 🎬 **Formulario con espacio para video**: Área dedicada para subir y mostrar videos
- 📱 **Generación de QR**: Código QR que lleva directamente al formulario  
- 🎨 **Diseño moderno**: Interfaz elegante y responsive
- 💾 **Descarga de QR**: Posibilidad de descargar el código QR generado
- 📝 **Formulario completo**: Campos para información personal y categorización

## 🚀 Instalación

1. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la aplicación:**
   ```bash   
   python app.py
   ```

3. **Abrir en el navegador:**
   - Formulario: `http://localhost:5000`
   - Generar QR: `http://localhost:5000/generate_qr`

## 📋 Uso

### Para generar el QR:
1. Ejecuta la aplicación
2. Ve a `http://localhost:5000/generate_qr`
3. Escanea el código QR generado o compártelo

### Para usar el formulario:
1. Escanea el QR o ve a `http://localhost:5000`
2. Completa los campos del formulario
3. Sube tu video usando el botón "Seleccionar Video"
4. Haz clic en "Enviar Formulario"

## 📁 Estructura del Proyecto

```
qr_formulario_video/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias de Python
├── README.md             # Este archivo
├── templates/            # Plantillas HTML
│   ├── formulario.html   # Página del formulario
│   └── qr.html          # Página del código QR
└── uploads/             # Carpeta para videos subidos
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **QR**: qrcode library
- **Diseño**: CSS Grid/Flexbox con gradientes modernos

## 🌐 Rutas Disponibles

- `/` - Formulario principal
- `/generate_qr` - Generador de código QR  
- `/submit` - Endpoint para envío de formularios (POST)
- `/upload_video` - Endpoint para subida de videos (POST)

## 📱 Responsive Design

La aplicación está optimizada para:
- 📱 Dispositivos móviles
- 💻 Tablets  
- 🖥️ Computadoras de escritorio

¡Disfruta creando formularios con QR! 🎉 
=======
# sinestesia-formulario-qr
>>>>>>> 406c315398804ea027d722df2e11c159969af2fe
