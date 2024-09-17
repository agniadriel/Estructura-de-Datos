
from pila import Pila

def obtener_valor_maximo(pila):
    if pila.es_vacia():
        print("La pila esta sin elementos")
        return None
    else:
        pila_aux = Pila()
        maximo = pila.peek()
        while not pila.es_vacia():# recorre la pila buscando el maximo valor
            item = pila.pop()
            if item > maximo:
                maximo = item
            pila_aux.push(item)

        while not pila_aux.es_vacia():
            pila.push(pila_aux.pop())
        return maximo

pila = Pila()
pila.push(5)
pila.push(6)
pila.push(15)
pila.push(4)
pila.push(1)
pila.push(3)

mayor = obtener_valor_maximo(pila)
if mayor is not None:
    print (f"El valor maximo de la pila es {mayor}")

pila.mostrar()