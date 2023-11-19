from itertools import permutations

def fuerza_bruta(grafo, nodo_inicial):
    nodos = list(grafo.nodos.keys())
    nodos.remove(nodo_inicial)

    mejor_ruta = None
    menor_costo = float('inf')

    for perm in permutations(nodos):
        ruta = [nodo_inicial] + list(perm)
        costo_total = 0

        for i in range(len(ruta) - 1):
            nodo_actual = ruta[i]
            nodo_siguiente = ruta[i + 1]
            arista = grafo.aristas.get((nodo_actual, nodo_siguiente)) or grafo.aristas.get((nodo_siguiente, nodo_actual))
            costo_total += arista.calcular_peso()

        if costo_total < menor_costo:
            menor_costo = costo_total
            mejor_ruta = ruta

    return mejor_ruta