# 🧪 INSTRUCCIONES DE PRUEBA

## 🚀 MÉTODOS PARA PROBAR EL CÓDIGO

### **Método 1: Prueba Local Simple (RECOMENDADO)**

1. **Abrir el archivo de prueba:**
   - Navega a la carpeta `qr_formulario_video`
   - Haz **doble clic** en `test_local.html`
   - Se abrirá automáticamente en tu navegador

2. **Probar funcionalidades:**
   - ✅ Completa el formulario
   - ✅ Sube un video de prueba
   - ✅ Cambia a la pestaña "Generar QR"
   - ✅ Presiona **F12** para ver la consola
   - ✅ Envía el formulario y revisa los datos en la consola

---

### **Método 2: Servidor Local con Python**

```powershell
# En PowerShell
cd qr_formulario_video
python -m http.server 8000
```

Luego ve a: `http://localhost:8000/test_local.html`

---

### **Método 3: Live Server (VS Code)**

Si tienes **VS Code**:
1. Instala la extensión "Live Server"
2. Haz clic derecho en `test_local.html`
3. Selecciona "Open with Live Server"

---

### **Método 4: Simulador Online de TiendaNube**

1. **CodePen**: https://codepen.io
2. **JSFiddle**: https://jsfiddle.net
3. Pega el código completo y prueba

---

## 🔍 QUÉ PROBAR

### ✅ **Checklist de Pruebas:**

#### **Formulario:**
- [ ] Todos los campos se pueden completar
- [ ] Validación de email funciona
- [ ] Campo obligatorio "Categoría" funciona
- [ ] Textarea permite texto largo

#### **Upload de Videos:**
- [ ] Click para seleccionar archivo
- [ ] Drag & drop funciona
- [ ] Preview del video se muestra
- [ ] Validación de tamaño (50MB máx)
- [ ] Solo acepta archivos de video

#### **Generación de QR:**
- [ ] QR se genera automáticamente
- [ ] Botón de descarga funciona
- [ ] QR contiene la URL correcta

#### **Envío del Formulario:**
- [ ] Botón se deshabilita durante envío
- [ ] Mensaje de éxito aparece
- [ ] Datos se muestran en consola (F12)
- [ ] Formulario se limpia automáticamente

#### **Responsive:**
- [ ] Se ve bien en móvil
- [ ] Tabs funcionan en pantalla pequeña
- [ ] Botones se adaptan al tamaño

---

## 📱 PRUEBA EN MÓVIL

### **Opción A: Servidor Local en Red**
```powershell
# Ejecutar servidor accesible en red
python -m http.server 8000 --bind 0.0.0.0
```
Luego desde el móvil: `http://TU_IP:8000/test_local.html`

### **Opción B: Herramientas de Desarrollador**
1. Presiona **F12** en el navegador
2. Clic en el ícono de móvil (📱)
3. Selecciona un dispositivo (iPhone, Samsung, etc.)

---

## 🐛 PROBLEMAS COMUNES Y SOLUCIONES

### **El archivo no se abre:**
- **Solución**: Asegúrate de que esté en la carpeta `qr_formulario_video`
- **Alternativa**: Arrastra el archivo al navegador

### **QR no se genera:**
- **Causa**: Conexión a internet requerida (CDN)
- **Solución**: Verifica tu conexión

### **Videos no se cargan:**
- **Causa**: Archivo muy grande o formato no soportado
- **Solución**: Usa MP4 menor a 50MB

### **Consola no muestra datos:**
- **Solución**: Presiona F12 → pestaña "Console"
- **En Chrome**: Clic derecho → "Inspeccionar" → "Console"

---

## 📊 DATOS DE PRUEBA SUGERIDOS

```
👤 Nombre: Juan Pérez
📧 Email: juan@test.com
📱 Teléfono: +54 9 11 1234-5678
🎂 Edad: 25
🏙️ Ciudad: Buenos Aires
✨ Categoría: Streetwear
💭 Mensaje: Me encanta el estilo urban de Sinestesia...
🎬 Video: Cualquier video MP4 de tu celular
```

---

## 🎯 RESULTADO ESPERADO

Al enviar el formulario deberías ver:

### **En Pantalla:**
- ✅ Mensaje "¡Formulario Probado Exitosamente!"
- ✅ Auto-limpieza del formulario después de 5 segundos

### **En Consola (F12):**
```
🎉 ¡FORMULARIO ENVIADO EXITOSAMENTE!
📝 Datos capturados:
┌─────────────┬──────────────────────────────┐
│   (index)   │           Values             │
├─────────────┼──────────────────────────────┤
│   nombre    │         'Juan Pérez'         │
│    email    │        'juan@test.com'       │
│  telefono   │     '+54 9 11 1234-5678'     │
│    edad     │             '25'             │
│   ciudad    │       'Buenos Aires'         │
│ categoria   │        'streetwear'          │
│  mensaje    │      'Me encanta...'         │
│video_nombre │       'video_test.mp4'       │
│ video_size  │          '15.2 MB'           │
│   fecha     │   '6/6/2025 18:45:30'        │
└─────────────┴──────────────────────────────┘
```

---

## 🔄 DIFERENCIAS CON LA VERSIÓN FINAL

### **En la prueba local:**
- ❌ No se envían emails reales
- ✅ Datos se muestran en consola
- ✅ Todas las demás funciones igual

### **En TiendaNube (versión final):**
- ✅ Emails se envían automáticamente
- ✅ Integración completa
- ✅ URL real de la tienda

---

## ✅ LISTO PARA TIENDANUBE

Si todas las pruebas pasan, el código está **100% listo** para:
1. **Copiar** `tiendanube_completo.html`
2. **Pegar** en TiendaNube
3. **Configurar** EmailJS
4. **¡Funcionar perfectamente!**

¡A probar! 🚀 