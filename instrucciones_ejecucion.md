# 🚀 Instrucciones de Ejecución - Windows

## ✅ Pasos para ejecutar la aplicación:

### 1. Abrir PowerShell como Administrador
- Presiona `Win + X` y selecciona "Windows PowerShell (Administrador)"

### 2. Navegar al directorio del proyecto
```powershell
cd C:\Users\MSI\qr_formulario_video
```

### 3. Instalar dependencias (solo la primera vez)
```powershell
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```powershell
python app.py
```

## 🌐 URLs de Acceso:

Una vez que la aplicación esté corriendo, verás estos mensajes:

```
🚀 Iniciando servidor Flask...
📱 Formulario disponible en: http://localhost:5000
🔗 QR Generator en: http://localhost:5000/generate_qr
🌐 Red local: http://192.168.1.12:5000
⏸️  Presiona Ctrl+C para detener el servidor
```

### Accesos:
- **Formulario**: http://localhost:5000 o http://192.168.1.12:5000
- **Generador QR**: http://localhost:5000/generate_qr
- **Desde otros dispositivos**: http://192.168.1.12:5000

## 🔧 Solución de Problemas:

### Error: "ERR_CONNECTION_REFUSED"
- Verifica que la aplicación esté corriendo (`python app.py`)
- Comprueba que no haya otro programa usando el puerto 5000
- Asegúrate de estar en el directorio correcto

### Error: "No such file or directory"
- Verifica que estés en el directorio correcto: `cd qr_formulario_video`
- Lista los archivos: `dir` (debe mostrar app.py)

### Error: "ModuleNotFoundError"
- Instala las dependencias: `pip install -r requirements.txt`

## 🛑 Para detener el servidor:
- Presiona `Ctrl + C` en la ventana de PowerShell

## 📱 Uso desde móvil:
1. Asegúrate de que tu móvil esté en la misma red WiFi
2. Ve a http://192.168.1.12:5000 desde el navegador del móvil
3. O escanea el QR generado en http://192.168.1.12:5000/generate_qr

¡Listo! 🎉 