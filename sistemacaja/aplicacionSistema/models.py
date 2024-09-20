from django.db import models

# Create your models here.
class ClienteDb(models.Model):
    nombre = models.CharField(max_length =75, verbose_name ="nombre", null=False)
    telefono = models.CharField(max_length=15, verbose_name ="telefono")
    email = models.EmailField(verbose_name ="email" )
    direccion = models.CharField(max_length =70, verbose_name ="direccion", null=False)
     
    class Meta:
        db_table ="Clientes"
        verbose_name ="Cliente"
        verbose_name_plural="Clientes"
        
    def __str__(self) -> str:    
        return self.nombre  
    
class MetodoPagoDb(models.Model):
    descripcion_metodo_pago = models.CharField(max_length=25, verbose_name="Nombre Metodo de pago", null=False)
    
    class Meta:
        db_table ="Metodo_pagos"
        verbose_name ="Metodo_pago"
        verbose_name_plural="Metodo_pagos"
        
    def __str__(self) -> str:    
        return self.descripcion_metodo_pago  
         
    
    
class TransacionDb(models.Model):
    fechaHora = models.DateField(verbose_name ="fecha y hora", null=False, blank="False")
    tipo_transacional = models.CharField(verbose_name="Tipo de transaccion", max_length =25, null="False")
    subtotal = models.IntegerField(verbose_name="subtotal", null=False)
    inpuesto = models.IntegerField(verbose_name ="inpuesto")
    toal = models.IntegerField(verbose_name="Total", null=False)
    descripcion_metodo_pago = models.ForeignKey(MetodoPagoDb, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(ClienteDb, on_delete=models.CASCADE)
    
    class Meta:
        db_table ="Transaciones"
        verbose_name ="transacion"
        verbose_name_plural="Transaciones"
        
    def __str__(self) -> str:    
        return self.tipo_transacional 

    
    
class Detalle_transacionDb(models.Model):
    id_transacional  = models.ForeignKey(TransacionDb, on_delete=models.CASCADE)
    descripcion_producto = models.CharField(verbose_name ="Descripcion del producto", max_length=30, null="False")
    cantidad = models.IntegerField(verbose_name="Cantidad", null=False)
    precio_unitario = models.IntegerField(verbose_name="Precio unitario", null=False)
    decuento = models.IntegerField(verbose_name="Descuento", null=False)
    
    class Meta:
        db_table ="Detalles_transaciones"
        verbose_name ="Detalle_transacion"
        verbose_name_plural="detalles_transaciones"
        
    def __str__(self) -> str:    
        return self.descripcion_producto
    
class cajaDb(models.Model):
    saldo_inicial = models.IntegerField(verbose_name="Saldo inicial", null=False)
    saldo_final = models.IntegerField(verbose_name="Saldo final", null=False)
    ingreso_totales = models.IntegerField(verbose_name="Ingreso totales", null=False)
    gasto_totales = models.IntegerField(verbose_name="Gasto total",null=False)
    nota = models.TextField(max_length=75, verbose_name="Nota")
    
    
    class Meta:
        db_table ="Cajas"
        verbose_name ="Caja"
        verbose_name_plural="Cajas"
        
    
    
class cajeroDb(models.Model):
    Nombre_cajero = models.CharField(max_length=25, verbose_name="Nombre Cajero", null=False)   
    turno_cajero = models.CharField(max_length=25, verbose_name="Turno cajero", null=False)
    id_caja = models.ForeignKey(cajaDb, on_delete=models.CASCADE)
    
    class Meta:
        db_table ="Cajeros"
        verbose_name ="Cajero"
        verbose_name_plural="Cajeros"
        
    def __str__(self) -> str:    
        return self.Nombre_cajero 
    
    
class inventarioDb(models.Model):
    nombre_producto = models.CharField(max_length=25, verbose_name ="Nombre Producto", null=False)
    stock_disponible = models.IntegerField(verbose_name ="Stock disponible", null=False)
    precio_inventario = models.IntegerField(verbose_name="Precio Inventario", null=False) 
    estado = models.BooleanField(verbose_name="Estado")
    
    class Meta:
        db_table ="Inventarios"
        verbose_name ="Inventario"
        verbose_name_plural="Inventarios"
        
    def __str__(self) -> str:    
        return self.nombre_producto
    
    
class reporte_ventaDb(models.Model):
    id_transacion = models.ForeignKey(TransacionDb, on_delete=models.CASCADE)
    total_venta = models.IntegerField(verbose_name="Total Venta", null=False)
    fecha_reporte = models.DateTimeField(verbose_name="Fecha Reoporte", null=False)
    
    class Meta:
        db_table ="Reportes_Ventas"
        verbose_name ="Reporte_venta"
        verbose_name_plural="Reportes_ventas"
        
    
    
class reporte_devolucion(models.Model):
    id_transacion = models.ForeignKey(TransacionDb, on_delete=models.CASCADE)
    monto_devolucion = models.IntegerField(verbose_name="Monto de devoluciones", null=False)
    fecha_reporte_devoluciones = models.DateField(verbose_name="Fecha Devolucion", null=False)
    
    class Meta:
        db_table ="Reportes_Devoluciones"
        verbose_name ="Reporte_devolucion"
        verbose_name_plural="Reportes_Devoluciones"
        
    def __str__(self) -> str:    
        return self.monto_devolucion
    
class datos_fiscale(models.Model):
    id_transacion = models.ForeignKey(TransacionDb, on_delete =models.CASCADE)
    rnc_cliente = models.CharField(max_length=15, verbose_name="RCN Cliente", null=False)
    detalles_inpuesto = models.IntegerField(verbose_name="Detalles Inpuesto")
    
    class Meta:
        db_table ="Datos_Fiscales"
        verbose_name ="Datos_fiscale"
        verbose_name_plural="Datos_Fiscales"
        
    def __str__(self) -> str:    
        return self.rnc_cliente
    
    
      

    
    
    

    
