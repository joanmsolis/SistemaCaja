from django.contrib import admin
from .models import ClienteDb, MetodoPagoDb, TransacionDb, Detalle_transacionDb, cajaDb,cajeroDb,inventarioDb, reporte_ventaDb, reporte_devolucion, datos_fiscale

# Register your models her

class ClienteAdmin(admin.ModelAdmin):
    fields =["nombre","telefono","email","direccion"]
    list_display =["nombre", "telefono"]
    
admin.site.register(ClienteDb, ClienteAdmin)



class MetodoPagoAdmin(admin.ModelAdmin):
    fields = ["descripcion_metodo_pago"]
    list_display=["descripcion_metodo_pago"]
    
admin.site.register(MetodoPagoDb, MetodoPagoAdmin)


class TransacionAdmin(admin.ModelAdmin):
    fields =["fechaHora","tipo_transacional","subtotal","inpuesto","toal","descripcion_metodo_pago"]
    list_display =["fechaHora","tipo_transacional","subtotal","inpuesto","toal","descripcion_metodo_pago"]
    
admin.site.register(TransacionDb, TransacionAdmin)


class cajaAdmin(admin.ModelAdmin):
    fields =["saldo_inicial","saldo_final","ingreso_totales","gasto_totales","nota"]
    list_display =["saldo_inicial","saldo_final","ingreso_totales","gasto_totales","nota"]
    
admin.site.register(cajaDb, cajaAdmin)

class Detalle_transacionAdmin(admin.ModelAdmin):
    fields =["descripcion_producto","cantidad","precio_unitario","decuento"]
    list_display =["descripcion_producto","cantidad","precio_unitario","decuento"]
    
admin.site.register(Detalle_transacionDb, Detalle_transacionAdmin)

class cajeroAdmin(admin.ModelAdmin):
    fields =["Nombre_cajero","turno_cajero"]
    list_display =["Nombre_cajero","turno_cajero"]
    
admin.site.register(cajeroDb, cajeroAdmin)


class inventarioAdmin(admin.ModelAdmin):
    fields =["nombre_producto","stock_disponible","precio_inventario","estado"]
    list_display =["nombre_producto","stock_disponible","precio_inventario","estado"]
    
admin.site.register(inventarioDb, inventarioAdmin)

class reporte_ventaAdmin(admin.ModelAdmin):
    fields =["total_venta","fecha_reporte"]
    list_display =["total_venta","fecha_reporte"]
    
admin.site.register(reporte_ventaDb, reporte_ventaAdmin)

    
