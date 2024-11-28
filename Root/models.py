from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Modelo Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(null=True, blank=True)
    contacto = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre


# Modelo Usuario
class Usuario(models.Model):
    ROL_CHOICES = [
        ('supervisor', 'Supervisor'),
        ('vendedor', 'Vendedor'),
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador')
    ]
    
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    contraseña = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    
    def __str__(self):
        return self.nombre


# Modelo Empresa
class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(null=True, blank=True)
    contacto = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


# Modelo Solicitud
class Solicitud(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Solicitud de {self.cliente.nombre} a {self.empresa.nombre}"


# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_alimento = models.CharField(max_length=255, null=True, blank=True)
    cantidad_disponible = models.IntegerField()

    def __str__(self):
        return self.nombre


# Modelo Tarea
class Tarea(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    trabajador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_asignadas')
    supervisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_supervisadas')
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    horas_dedicadas = models.IntegerField()
    estado = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


# Modelo Notificación
class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación a {self.usuario.nombre}"


# Modelo Venta
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.producto.nombre} a {self.cliente.nombre}"

