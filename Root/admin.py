from django.contrib import admin
from .models import Cliente, Usuario, Empresa, Solicitud, Producto, Tarea, Notificacion, Venta

# Registro de los modelos en el admin de Django
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'direccion', 'contacto')
    search_fields = ('nombre', 'email')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'rol')
    search_fields = ('nombre', 'email')
    list_filter = ('rol',)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'direccion')
    search_fields = ('nombre', 'contacto')

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'empresa', 'fecha_solicitud', 'estado')
    search_fields = ('cliente__nombre', 'empresa__nombre')
    list_filter = ('estado',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_alimento', 'cantidad_disponible')
    search_fields = ('nombre',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'trabajador', 'supervisor', 'fecha_inicio', 'estado')
    search_fields = ('titulo', 'trabajador__nombre', 'supervisor__nombre')
    list_filter = ('estado',)

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensaje', 'fecha_envio')
    search_fields = ('usuario__nombre', 'mensaje')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'precio_unitario', 'fecha_venta', 'total')
    search_fields = ('cliente__nombre', 'producto__nombre')
    list_filter = ('fecha_venta',)
