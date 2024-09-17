from pila import Pila
from producto import Producto

def obtenerMayorPrecio(pila):
    if pila.es_vacia():
        return None
    pila_aux = Pila()
    mayor_precio = pila.pop()
    pila_aux.push(mayor_precio)
    while not pila.es_vacia():
        elemento = pila.pop()
        if elemento.get_precio() > mayor_precio.get_precio():
            mayor_precio=elemento
        pila_aux.push(elemento)

    while not pila_aux.es_vacia():
        pila.push(pila_aux.pop())

    return mayor_precio

pila_productos = Pila()
pila_productos.push(Producto(1,"pantalon", 70.0))
pila_productos.push(Producto(2,"zapatos",350.0))
pila_productos.push(Producto(3,"camisa",150.0))

print ("La pila antes: ", pila_productos.mostrar())

mayor = obtenerMayorPrecio(pila_productos)

print (f"El producto con mayor precio es: {mayor}" )

print ("La pila despuess: "), pila_productos.mostrar()