# 🚀 CÓMO EJECUTAR LA APLICACIÓN

## Pasos Rápidos:

1. **Abrir PowerShell en el directorio del proyecto:**
   ```powershell
   cd qr_formulario_video
   ```

2. **Ejecutar la aplicación:**
   ```powershell
   python app.py
   ```

3. **Acceder desde el navegador:**
   - Formulario: `http://192.168.1.12:5000`
   - Generar QR: `http://192.168.1.12:5000/generate_qr`

## ✅ ¡La aplicación YA FUNCIONÓ!

Según los logs, tu aplicación se ejecutó correctamente y recibió conexiones:
```
192.168.1.12 - - [06/Jun/2025 18:39:24] "GET / HTTP/1.1" 200 -
192.168.1.12 - - [06/Jun/2025 18:39:25] "GET /video/intro HTTP/1.1" 206 -
```

## 🎯 Para usar en TiendaNube:

1. **Hostear externamente** (Railway, Render, etc.)
2. **Usar el widget HTML** que creamos en `tiendanube_integration.html`
3. **Seguir la guía** en `guia_tiendanube.md`

¡Todo guardado! 💾 