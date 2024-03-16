# /*
#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#  */

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def simulate_web_browser(actions):
    browser_history = Stack()
    current_page = None

    for action in actions:
        if action == "back":
            if not browser_history.is_empty():
                current_page = browser_history.pop()
                print("Current Page:", current_page)
        elif action == "forward":
            if current_page:
                browser_history.push(current_page)
                print("Forwarding to:", action)
                current_page = None
        else:
            browser_history.push(action)
            current_page = action
            print("Navigating to:", action)

# Example usage
actions = ["google.com", "yahoo.com", "back", "forward", "facebook.com"]
simulate_web_browser(actions)

def simulate_printer(documents):
    printer_queue = Queue()

    for doc in documents:
        printer_queue.enqueue(doc)

    while not printer_queue.is_empty():
        print("Printing:", printer_queue.dequeue())

# Example usage
documents = ["Document1", "Document2", "Document3"]
simulate_printer(documents)





