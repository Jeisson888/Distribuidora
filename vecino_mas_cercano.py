def vecino_mas_cercano(grafo, nodo_inicial):
    nodos_no_visitados = set(grafo.nodos.keys())
    ruta = [nodo_inicial]
    nodos_no_visitados.remove(nodo_inicial)

    while nodos_no_visitados:
        nodo_actual = ruta[0]
        vecino_mas_cercano = None
        distancia_mas_corta = float('inf')

        for nodo in nodos_no_visitados:
            arista = grafo.aristas.get((nodo_actual, nodo)) or grafo.aristas.get((nodo, nodo_actual))
            if arista:
                peso = arista.calcular_peso()
                if peso < distancia_mas_corta:
                    distancia_mas_corta = peso
                    vecino_mas_cercano = nodo

        ruta.append(vecino_mas_cercano)
        nodos_no_visitados.remove(vecino_mas_cercano)

    return ruta