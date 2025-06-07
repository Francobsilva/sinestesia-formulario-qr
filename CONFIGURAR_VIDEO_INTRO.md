# 🎬 CONFIGURAR VIDEO INTRO

## ✅ ¡VIDEO INTRO AGREGADO!

He modificado ambas versiones (prueba y final) para incluir un **video introductorio** que se reproduce **antes del formulario**.

### 🎯 **Funcionamiento:**

1. **Se carga la página** → Aparece el video intro automáticamente
2. **Video se reproduce** → Con controles para pausar/reproducir
3. **Usuario puede saltar** → Botón "⏭️ Saltar Video"
4. **Al terminar video** → Aparece "✨ Continuar al Formulario"
5. **Se muestra formulario** → Con todas las funcionalidades

---

## 📁 **OPCIONES PARA EL VIDEO**

### **Opción 1: Video Local (Para Pruebas)**
```html
<!-- En test_local.html ya está configurado para buscar: -->
<source src="uploads/intro_video.mov" type="video/quicktime">
<source src="uploads/intro_video.mp4" type="video/mp4">
<source src="uploads/copy_F5E4631D-A4E8-45A6-A683-9F7863F1B0C7.mov" type="video/quicktime">
```

**Pasos:**
1. Coloca tu video en la carpeta `uploads/`
2. Nómbralo `intro_video.mp4` o `intro_video.mov`
3. Abre `test_local.html` para probarlo

### **Opción 2: Video en la Nube (Para TiendaNube)**
```html
<!-- En tiendanube_completo.html cambiar por: -->
<source src="https://tu-servidor.com/intro_video.mp4" type="video/mp4">
```

**Servicios recomendados:**
- **YouTube** (embed): `https://www.youtube.com/embed/TU_VIDEO_ID`
- **Vimeo**: `https://player.vimeo.com/video/TU_VIDEO_ID`
- **Google Drive**: Link directo al archivo
- **Cloudinary**: Hosting específico para medios

---

## 🔧 **CONFIGURACIÓN PERSONALIZADA**

### **Cambiar URL del Video en TiendaNube:**
```html
<!-- Buscar esta línea en tiendanube_completo.html: -->
<source src="https://tu-servidor.com/intro_video.mp4" type="video/mp4">

<!-- Reemplazar por tu URL real: -->
<source src="https://drive.google.com/uc?id=TU_ID_DE_GOOGLE_DRIVE" type="video/mp4">
```

### **Cambiar Configuración del Video:**
```html
<!-- Video actual: autoplay muted controls -->
<video id="introVideo" controls autoplay muted>

<!-- Opciones: -->
<!-- Sin autoplay: --> controls
<!-- Sin sonido: --> controls muted
<!-- Pantalla completa: --> controls autoplay muted allowfullscreen
<!-- Loop: --> controls autoplay muted loop
```

### **Personalizar Textos:**
```html
<h2>🎬 Conoce Sinestesia</h2>
<p>Descubre nuestra filosofía y estilo único</p>

<!-- Cambiar por: -->
<h2>✨ Tu título aquí</h2>
<p>Tu descripción personalizada</p>
```

---

## 🎨 **PERSONALIZAR DISEÑO**

### **Cambiar Colores de Botones:**
```css
.skip-btn {
    background: rgba(255, 255, 255, 0.2); /* Transparente */
    color: white;
}

.continue-btn {
    background: linear-gradient(45deg, #ff0080, #ff6b6b); /* Sinestesia */
    color: white;
}
```

### **Cambiar Tamaño del Video:**
```html
<!-- Video actual: max-width: 600px -->
<video style="width: 100%; max-width: 800px; border-radius: 15px;">

<!-- Para video más grande o más pequeño -->
<video style="width: 100%; max-width: 400px; border-radius: 15px;">
```

---

## 📱 **RESPONSIVE**

El video intro es **completamente responsive**:
- ✅ Se adapta a móvil
- ✅ Controles touch-friendly
- ✅ Botones accesibles
- ✅ Video escalable

---

## ⚙️ **CONFIGURACIONES AVANZADAS**

### **Auto-saltar después de X segundos:**
```javascript
// Cambiar timeout (actual: 30 segundos)
setTimeout(() => {
    if (videoIntro.style.display !== 'none') {
        showMainContent();
    }
}, 15000); // 15 segundos
```

### **Sin autoplay (por políticas del navegador):**
```html
<!-- Quitar autoplay si hay problemas -->
<video id="introVideo" controls muted>
```

### **Múltiples formatos de video:**
```html
<video id="introVideo" controls autoplay muted>
    <source src="video.webm" type="video/webm">
    <source src="video.mp4" type="video/mp4">
    <source src="video.mov" type="video/quicktime">
    <source src="video.avi" type="video/avi">
</video>
```

---

## 🚨 **FALLBACKS Y SEGURIDAD**

### **Si el video no carga:**
- ✅ Auto-saltar después de 30 segundos
- ✅ Botón "Saltar Video" siempre disponible
- ✅ Mensaje de error en consola
- ✅ Formulario funciona sin video

### **Para navegadores antiguos:**
```html
<video>
    <!-- ... sources ... -->
    <p>Tu navegador no soporta video. 
       <a href="video.mp4">Descarga el video</a>
    </p>
</video>
```

---

## 📊 **CASOS DE USO PARA SINESTESIA**

### **Ideas para tu video intro:**
- 🎬 **Presentación de marca**: Historia de Sinestesia
- 👥 **Testimoniales**: Clientes usando tus prendas
- 🎨 **Proceso creativo**: Cómo diseñas las prendas
- 🔥 **Lookbook**: Outfits y estilos
- 💫 **Filosofía**: Qué representa Sinestesia

### **Duración recomendada:**
- ⏱️ **15-45 segundos**: Perfecto para engagement
- ⏱️ **1-2 minutos**: Máximo recomendado
- ⏱️ **+2 minutos**: Solo si es muy engaging

---

## ✅ **TESTING**

### **Probar en test_local.html:**
1. Coloca video en `uploads/intro_video.mp4`
2. Abre `test_local.html`
3. Video debería reproducirse automáticamente
4. Prueba botón "Saltar Video"
5. Verifica que aparece el formulario

### **Para TiendaNube:**
1. Sube video a servicio en la nube
2. Actualiza URL en `tiendanube_completo.html`
3. Copia y pega en TiendaNube
4. Prueba desde móvil y desktop

¡El video intro está **100% funcional** y listo! 🎉 