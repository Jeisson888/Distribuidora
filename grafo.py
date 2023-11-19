class Nodo:
    def __init__(self, nombre, tipo, ubicacion):
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion

class Arista:
    def __init__(self, nodo_1, nodo_2, costo, tiempo, distancia):
        self.nodo_1 = nodo_1
        self.nodo_2 = nodo_2
        self.costo = costo
        self.tiempo = tiempo
        self.distancia = distancia

    def calcular_peso(self):
        return self.costo + self.tiempo + self.distancia

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_nodo(self, nombre, tipo, ubicacion):
        if nombre not in self.nodos:
            nodo = Nodo(nombre, tipo, ubicacion)
            self.nodos[nombre] = nodo
        else:
            print(f"El nodo con nombre '{nombre}' ya existe en el grafo.")

    def agregar_arista(self, nodo_1, nodo_2, costo, tiempo, distancia):
        if (nodo_1, nodo_2) not in self.aristas and (nodo_2, nodo_1) not in self.aristas:
            if nodo_1 in self.nodos and nodo_2 in self.nodos:
                ruta = Arista(nodo_1, nodo_2, costo, tiempo, distancia)
                self.aristas[(nodo_1, nodo_2)] = ruta
            else:
                print("Uno o ambos nodos no existen en el grafo.")
        else:
            print(f"La arista entre '{nodo_1}' y '{nodo_2}' ya existe en el grafo.")