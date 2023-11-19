import grafo
import caso_ejemplo
import vecino_mas_cercano as vmc
import fuerza_bruta as fb
import networkx as nx
import matplotlib.pyplot as plt

def vista():
    distribucion = grafo.Grafo()

    while True:
        print("\n1. Cargar datos caso ejemplo")
        print("2. Agregar lugar (nodo)")
        print("3. Agregar ruta (arista)")
        print("4. Visualizar grafo")
        print("5. Calcular mejor ruta (fuerza bruta)")
        print("6. Calcular mejor ruta (vecino mas cercano)")
        print("7. salir")

        opcion = int(input("\nIngrese la opción: "))

        if opcion == 1:
            caso_ejemplo.cargar_datos(distribucion)

        elif opcion == 2:
            nombre = input("Ingrese el nombre del nodo: ")
            tipo = input("Ingrese el tipo del nodo (almacen/punto_venta): ")
            ubicacion = tuple(map(float, input("Ingrese la ubicación (latitud, longitud): ").split(',')))

            distribucion.agregar_nodo(nombre, tipo, ubicacion)
            print(f"Se ha agregado el nodo {nombre}.")

        elif opcion == 3:
            nodo_1 = input("Ingrese el nombre del lugar 1: ")
            nodo_2 = input("Ingrese el nombre del lugar 2: ")
            costo = float(input("Ingrese el costo promedio de la ruta: "))
            tiempo = float(input("Ingrese el tiempo promedio de la ruta: "))
            distancia = float(input("Ingrese la distancia entre los nodos: "))

            distribucion.agregar_arista(nodo_1, nodo_2, costo, tiempo, distancia)
            print(f"Se ha agregado la ruta entre {nodo_1} y {nodo_2}.")

        elif opcion == 4:
            grafo_networkx = nx.Graph()
            for nodo in distribucion.nodos.values():
                grafo_networkx.add_node(nodo.nombre, tipo=nodo.tipo, ubicacion=nodo.ubicacion)
            for arista in distribucion.aristas.values():
                grafo_networkx.add_edge(arista.nodo_1, arista.nodo_2, costo=arista.costo, tiempo=arista.tiempo, distancia=arista.distancia)
            posiciones = nx.get_node_attributes(grafo_networkx, 'ubicacion')
            nx.draw(grafo_networkx, posiciones, with_labels=True, node_color='lightblue', edge_cmap=plt.cm.Blues, arrows=True, node_size=3000)
            plt.show()

        elif opcion == 5:
            origen = input("Ingrese el nombre del nodo de origen: ")
            mejor_ruta = fb.fuerza_bruta(distribucion, origen)
            print(f"La mejor ruta entre es: {mejor_ruta}")

        elif opcion == 6:
            origen = input("Ingrese el nombre del nodo de origen: ")
            mejor_ruta = vmc.vecino_mas_cercano(distribucion, origen)
            print(f"La mejor ruta entre es: {mejor_ruta}")
        
        elif opcion == 7:
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    vista()