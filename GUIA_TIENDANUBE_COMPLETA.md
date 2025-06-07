# 🏪 GUÍA COMPLETA: Integración en TiendaNube

## ✅ ¡CÓDIGO ADAPTADO PARA TIENDANUBE!

He creado una **versión completamente nativa** que funciona **sin servidor Flask**, usando solo HTML/CSS/JavaScript que puedes pegar directamente en TiendaNube.

### 📁 Archivo Principal: `tiendanube_completo.html`

Este archivo tiene **TODA la funcionalidad**:
- ✅ Formulario completo con validación
- ✅ Upload de videos con preview
- ✅ Generación de QR automática
- ✅ Envío por email (EmailJS)
- ✅ Compartir en WhatsApp
- ✅ Diseño responsive
- ✅ Estilo personalizado para Sinestesia

---

## 🚀 PASO A PASO EN TIENDANUBE

### PASO 1: Crear Página Personalizada

1. **Entra a tu Panel de TiendaNube**
2. **Ve a: Contenido → Páginas**
3. **Clic en "Agregar página"**
4. **Configurar:**
   - **Título**: "Formulario con Video"
   - **URL**: `/formulario-video`
   - **Contenido**: Pegar TODO el código de `tiendanube_completo.html`
   - **Publicar**: ✅ Activar

### PASO 2: Configurar EmailJS (Para recibir formularios)

1. **Crear cuenta en EmailJS**: https://www.emailjs.com
2. **Configurar servicio de email** (Gmail, Outlook, etc.)
3. **Crear template de email**
4. **Obtener credenciales:**
   - Service ID
   - Template ID  
   - User ID
5. **Reemplazar en el código:**
   ```javascript
   const CONFIG = {
       emailjs: {
           serviceId: 'TU_SERVICE_ID_REAL',
           templateId: 'TU_TEMPLATE_ID_REAL', 
           userId: 'TU_USER_ID_REAL'
       },
       targetEmail: 'tu@sinestesiastudios.com'
   };
   ```

### PASO 3: Agregar al Menú de tu Tienda

1. **Ve a: Diseño → Menú**
2. **Agregar enlace:**
   - **Texto**: "📹 Comparte tu Estilo"
   - **URL**: `/formulario-video`
3. **Guardar cambios**

### PASO 4: Crear Widget para Página Principal (Opcional)

```html
<!-- Pegar en Diseño → Editor de Diseño → HTML Personalizado -->
<div style="background: linear-gradient(135deg, #000 0%, #333 100%); color: white; padding: 30px; border-radius: 20px; text-align: center; margin: 20px 0;">
    <h2 style="font-family: 'Arial Black', sans-serif; margin-bottom: 20px; background: linear-gradient(45deg, #ff0080, #ff6b6b, #4ecdc4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        ✨ SINESTESIA COMMUNITY ✨
    </h2>
    <p style="margin-bottom: 25px; font-size: 18px;">
        ¡Muéstranos tu estilo único!
    </p>
    
    <a href="/formulario-video" 
       style="background: linear-gradient(45deg, #ff0080, #ff6b6b); color: white; padding: 15px 30px; text-decoration: none; border-radius: 30px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; display: inline-block;">
        📹 Subir Mi Video
    </a>
</div>
```

---

## 🎯 FUNCIONALIDADES INCLUIDAS

### ✅ Formulario Completo
- Campos: Nombre, email, teléfono, edad, ciudad
- Categorías de estilo (streetwear, minimal, etc.)
- Textarea para descripción personal
- Validación en tiempo real

### ✅ Upload de Videos
- Drag & drop funcional
- Preview del video
- Validación de formato y tamaño
- Máximo 50MB

### ✅ Generación de QR
- QR automático de la página
- Botón para descargar QR
- Compartir por WhatsApp
- Copiar link al portapapeles

### ✅ Envío de Formularios
- Integración con EmailJS
- Recibes email con todos los datos
- Mensaje de confirmación
- Auto-limpieza del formulario

---

## 📧 CONFIGURACIÓN DE EMAILJS

### Template de Email Recomendado:
```
Asunto: 🔥 Nuevo formulario Sinestesia - {{from_name}}

Cuerpo:
{{message}}

---
Enviado desde: {{from_email}}
Página: https://tutienda.mitiendanube.com/formulario-video
```

### Variables disponibles:
- `{{from_name}}` - Nombre del usuario
- `{{from_email}}` - Email del usuario  
- `{{message}}` - Todos los datos del formulario

---

## 🎨 PERSONALIZACIÓN

### Cambiar Colores:
```css
/* En el <style> del HTML */
.logo {
    background: linear-gradient(45deg, #TU_COLOR1, #TU_COLOR2);
}

.submit-btn {
    background: linear-gradient(45deg, #TU_COLOR1, #TU_COLOR2);
}
```

### Agregar tu Logo:
```html
<!-- Reemplazar en el header -->
<div class="header">
    <img src="https://tutienda.com/logo.png" alt="Sinestesia" style="max-width: 200px;">
    <div class="subtitle">Comparte tu estilo con nosotros</div>
</div>
```

---

## 🔧 ALTERNATIVAS SIN EMAILJS

### Opción 1: Google Forms
```javascript
// Reemplazar la función handleFormSubmit
const googleFormURL = 'https://docs.google.com/forms/d/e/TU_FORM_ID/formResponse';
const formData = new FormData();
formData.append('entry.123456789', datos.nombre); // IDs de Google Forms
fetch(googleFormURL, { method: 'POST', body: formData, mode: 'no-cors' });
```

### Opción 2: Formspree
```javascript
fetch('https://formspree.io/f/TU_FORM_ID', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datos)
});
```

---

## 📱 TESTING

### Verificar que funcione:
1. **Página carga correctamente**
2. **Formulario se puede completar**
3. **Videos se pueden subir**
4. **QR se genera automáticamente**
5. **Emails llegan correctamente**
6. **Responsive en móvil**

---

## 🚨 NOTAS IMPORTANTES

- **Sin servidor necesario**: Todo funciona en el navegador
- **Videos en memoria**: Los videos se procesan localmente
- **HTTPS requerido**: Para upload de archivos
- **Límite de archivos**: 50MB por video
- **Compatibilidad**: Funciona en todos los navegadores modernos

---

## 🎉 ¡RESULTADO FINAL!

Tendrás un formulario **profesional** y **completamente funcional** integrado en tu tienda TiendaNube que:

- ✅ Se ve **perfectamente** en móvil y desktop
- ✅ **Recibe formularios** directamente en tu email
- ✅ Genera **QR automáticamente** para compartir
- ✅ Permite **subir videos** con preview
- ✅ Tiene el **estilo de Sinestesia**
- ✅ **No requiere servidor externo**

¡Perfecto para generar **contenido de usuarios** con tus prendas! 🔥 