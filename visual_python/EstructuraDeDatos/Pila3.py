# main.py
from pila import Pila


def obtener_valor_mayor(pila):
    if pila.es_vacia():
        print ("pila vacia")
        return None
    else:
        pila_aux = Pila()
        maximo = pila.peek()
        while not pila.es_vacia():
            item=pila.pop()
            if item > maximo:
                maximo= item
            pila_aux.push(item)

        while not pila_aux.es_vacia:
            pila.push(pila_aux.pop())
        return maximo

pila = Pila()
pila.push(7)
pila.push(8)
pila.push(1)
pila.push(20)
pila.push(10)

max = obtener_valor_mayor(pila)
print(max)



