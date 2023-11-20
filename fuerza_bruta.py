from itertools import permutations  # Importa la función 'permutations' de la librería 'itertools'

def fuerza_bruta(grafo, nodo_inicial):
    nodos = list(grafo.nodos.keys())  # Obtiene una lista de nodos del grafo
    nodos.remove(nodo_inicial)  # Remueve el nodo inicial de la lista de nodos

    mejor_ruta = None  # Inicializa la mejor ruta encontrada como vacía
    menor_peso = float('inf')  # Inicializa el peso de la ruta como infinito

    # Genera todas las permutaciones posibles de los nodos restantes
    for perm in permutations(nodos):
        ruta = [nodo_inicial] + list(perm)  # Genera una ruta con el nodo inicial y la permutación actual
        peso_total = 0  # Inicializa el peso total de la ruta actual como cero
        ruta_valida = True  # Inicializa la bandera para verificar si la ruta es válida

        # Calcula el peso total de la ruta y verifica su validez
        for i in range(len(ruta) - 1):
            nodo_actual = ruta[i]
            nodo_siguiente = ruta[i + 1]

            arista = grafo.aristas.get((nodo_actual, nodo_siguiente))  # Obtiene la arista entre nodos
            if arista is None:
                arista = grafo.aristas.get((nodo_siguiente, nodo_actual))

            if arista is not None:  # Si la arista existe, suma su peso al peso total
                peso_total += arista.calcular_peso()
            else:  # Si la arista no existe, marca la ruta como inválida y sale del bucle
                ruta_valida = False
                break

        # Si la ruta es válida y su peso es menor al menor peso encontrado hasta ahora
        if ruta_valida and peso_total < menor_peso:
            menor_peso = peso_total  # Actualiza el menor peso encontrado
            mejor_ruta = ruta  # Actualiza la mejor ruta encontrada

    return mejor_ruta  # Devuelve la mejor ruta encontrada
