class Producto:
    def __init__(self, codigo_prod, nombre_prod, precio_prod):
        self.codigo_prod = codigo_prod
        self.nombre_prod = nombre_prod
        self.precio_prod = precio_prod

    def get_precio(self):
        return self.precio_prod

    def __str__(self):
        return f"{self.nombre_prod} -- {self.precio_prod}"
