def vecino_mas_cercano(grafo, nodo_inicial):
    # Conjunto de nodos que aún no han sido visitados.
    nodos_no_visitados = set(grafo.nodos.keys())
    # Inicializa la ruta con el nodo inicial y lo remueve de los no visitados.
    ruta = [nodo_inicial]
    nodos_no_visitados.remove(nodo_inicial)

    # Mientras haya nodos no visitados.
    while nodos_no_visitados:
        # Selecciona el nodo actual de la ruta.
        nodo_actual = ruta[0]
        # Inicializa el vecino más cercano y la distancia más corta.
        vecino_mas_cercano = None
        distancia_mas_corta = float('inf')

        # Busca el vecino más cercano al nodo actual.
        for nodo in nodos_no_visitados:
            # Busca la arista entre el nodo actual y el nodo actualmente revisado.
            arista = grafo.aristas.get((nodo_actual, nodo)) or grafo.aristas.get((nodo, nodo_actual))
            if arista:
                # Calcula el peso de la arista.
                peso = arista.calcular_peso()
                # Si el peso es menor que la distancia más corta encontrada hasta ahora,
                # actualiza la distancia más corta y el vecino más cercano.
                if peso < distancia_mas_corta:
                    distancia_mas_corta = peso
                    vecino_mas_cercano = nodo

        # Agrega el vecino más cercano a la ruta y lo elimina de los no visitados.
        ruta.append(vecino_mas_cercano)
        nodos_no_visitados.remove(vecino_mas_cercano)

    # Retorna la ruta resultante.
    return ruta
