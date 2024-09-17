class Pila:
    def __init__(self):
        self.items = []
    # Llena la pila
    def push(self, item):
        self.items.append(item)
        #print(f'Item {item} apilado')
    # Saca elementos de la pila
    def pop(self):
        if not self.es_vacia():
            item = self.items.pop()
           # print(f'Item {item} desapilado')
            return item
        else:
            print('La pila está vacía')
            return None
    # Pregunta si la pila está vacía
    def es_vacia(self):
        return len(self.items) == 0
    # Devuelve el último valor de la pila
    def peek(self):
        if not self.es_vacia():
            return self.items[-1]  
        else:
            return None
    # Devuelve el tamaño de la pila
    def size(self):
        return len(self.items)

    # Método para mostrar la pila
    def mostrar(self):
        if not self.es_vacia():
            print("Contenido de la pila:")
            for item in reversed(self.items):
                print(item)
        else:
            print("La pila está vacía")
        return [str(item) for item in reversed(self.items)]