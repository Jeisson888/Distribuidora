class Nodo:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

class Arista:
    def __init__(self, nodo_1, nodo_2, costo, tiempo, distancia):
        self.nodo_1 = nodo_1
        self.nodo_2 = nodo_2
        self.costo = costo
        self.tiempo = tiempo
        self.distancia = distancia

    def calcular_peso(self):
        return (self.costo * 2) + self.tiempo + self.distancia

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_nodo(self, nombre, ubicacion):
        if nombre not in self.nodos:
            nodo = Nodo(nombre, ubicacion)
            self.nodos[nombre] = nodo
        else:
            pass

    def borrar_nodo(self, nombre):
        if nombre in self.nodos:
            del self.nodos[nombre]
            self.aristas = {(n1, n2): arista for (n1, n2), arista in self.aristas.items() if nombre not in (n1, n2)}
        else:
            pass
            
    def agregar_arista(self, nodo_1, nodo_2, costo, tiempo, distancia):
        if (nodo_1, nodo_2) not in self.aristas and (nodo_2, nodo_1) not in self.aristas:
            if nodo_1 in self.nodos and nodo_2 in self.nodos:
                ruta = Arista(nodo_1, nodo_2, costo, tiempo, distancia)
                self.aristas[(nodo_1, nodo_2)] = ruta
            else:
                pass
        else:
            pass

    def borrar_arista(self, nodo_1, nodo_2):
        if (nodo_1, nodo_2) in self.aristas:
            del self.aristas[(nodo_1, nodo_2)]
        elif (nodo_2, nodo_1) in self.aristas:
            del self.aristas[(nodo_2, nodo_1)]
        else:
            pass
            
    def existe_arista(self, nodo_1, nodo_2):
        return (nodo_1, nodo_2) in self.aristas or (nodo_2, nodo_1) in self.aristas