from itertools import permutations

def fuerza_bruta(grafo, nodo_inicial):
    nodos = list(grafo.nodos.keys())
    nodos.remove(nodo_inicial)

    mejor_ruta = None
    menor_peso = float('inf')

    for perm in permutations(nodos):
        ruta = [nodo_inicial] + list(perm)
        peso_total = 0
        ruta_valida = True

        for i in range(len(ruta) - 1):
            nodo_actual = ruta[i]
            nodo_siguiente = ruta[i + 1]

            arista = grafo.aristas.get((nodo_actual, nodo_siguiente))
            if arista is None:
                arista = grafo.aristas.get((nodo_siguiente, nodo_actual))

            if arista is not None:
                peso_total += arista.calcular_peso()
            else:
                ruta_valida = False
                break

        if ruta_valida and peso_total < menor_peso:
            menor_peso = peso_total
            mejor_ruta = ruta

    return mejor_ruta