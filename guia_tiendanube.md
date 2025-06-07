# 🏪 Guía de Integración en TiendaNube

## Paso 1: Hospedar tu Aplicación Flask

### Opción A: Railway (Recomendado - Gratis)
1. Sube tu código a GitHub
2. Ve a [Railway.app](https://railway.app)
3. Conecta tu repositorio de GitHub
4. Despliega automáticamente
5. Obtienes una URL como: `https://tu-app.railway.app`

### Opción B: Render (Alternativa Gratuita)
1. Crea cuenta en [Render.com](https://render.com)
2. Conecta tu repositorio
3. Configura como "Web Service"
4. URL resultante: `https://tu-app.onrender.com`

## Paso 2: Configurar en TiendaNube

### A) Agregar Widget en Página Principal
1. **Ir a tu panel de TiendaNube**
2. **Diseño → Editor de diseño**
3. **Agregar elemento HTML personalizado**
4. **Pegar el código del widget** (tiendanube_integration.html)
5. **Reemplazar las URLs**:
   - `TU_URL_DEL_QR_AQUI` → URL de tu imagen QR
   - `TU_URL_DEL_FORMULARIO_AQUI` → URL de tu formulario hospedado

### B) Crear Página Personalizada
1. **Contenido → Páginas → Nueva página**
2. **Título**: "Formulario con Video"
3. **Contenido**: Pegar el widget HTML
4. **Guardar y publicar**

### C) Agregar Botón en Menú
1. **Diseño → Menú**
2. **Agregar enlace**: "Formulario Video"
3. **URL**: Link a tu página personalizada o directamente al formulario

## Paso 3: Personalizar para tu Marca Sinestesia

```html
<!-- Versión personalizada para Sinestesia -->
<div style="background: linear-gradient(135deg, #000 0%, #333 100%); color: white; padding: 30px; border-radius: 20px; text-align: center; margin: 20px 0;">
    <h2 style="font-family: 'Arial Black', sans-serif; margin-bottom: 20px;">
        ✨ SINESTESIA COLLECTION ✨
    </h2>
    <p style="margin-bottom: 25px; font-size: 18px;">
        Comparte tu estilo con nosotros
    </p>
    
    <div style="background: white; padding: 15px; border-radius: 15px; display: inline-block; margin-bottom: 20px;">
        <img src="TU_QR_AQUI" alt="QR Sinestesia" style="width: 180px; height: 180px;">
    </div>
    
    <br>
    <a href="TU_FORMULARIO_AQUI" target="_blank" 
       style="background: #ff0080; color: white; padding: 15px 30px; text-decoration: none; border-radius: 30px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">
        📹 Enviar Mi Video
    </a>
</div>
```

## Paso 4: Configuraciones Adicionales

### A) Variables de Entorno para Producción
```python
# En tu app.py, agregar:
import os

# Para producción
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tu-clave-secreta')
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads/')

# URL base para QR
BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')
```

### B) Modificar el Generador de QR
```python
# Actualizar app.py para usar URL de producción
@app.route('/generate_qr')
def generate_qr():
    # Usar la URL de producción
    base_url = "https://tu-app.railway.app"  # Tu URL real
    qr_url = f"{base_url}/"
    
    # ... resto del código
```

## Paso 5: Testing y Verificación

1. **Probar el QR**: Escanear con el móvil
2. **Verificar formulario**: Completar datos y subir video
3. **Revisar responsividad**: Probar en móvil y desktop
4. **Comprobar integración**: Ver cómo se ve en tu tienda

## 🚨 Consideraciones Importantes

- **HTTPS**: TiendaNube requiere HTTPS, asegúrate que tu app hospedada use SSL
- **CORS**: Puede que necesites configurar CORS si hay problemas de dominio cruzado
- **Almacenamiento**: Los videos se guardan en tu servidor externo, no en TiendaNube
- **Backups**: Considera implementar respaldo de los videos enviados

## 📞 Soporte

Si tienes problemas con la integración, revisa:
- Los logs de tu aplicación hospedada
- La consola del navegador para errores JavaScript
- La documentación de TiendaNube sobre HTML personalizado 