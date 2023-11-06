import sys


def bfs(grafo, visitados, color, vertice, conjunto_actual, otro_conjunto):
    visitados[vertice] = True
    conjunto_actual.add(vertice)

    for vecino in grafo[vertice]:
        if not visitados[vecino]:
            color[vecino] = 1 - color[vertice]
            bfs(grafo, visitados, color, vecino, otro_conjunto, conjunto_actual)

def particionar_grafo(grafo):
    num_vertices = len(grafo)
    visitados = [False] * num_vertices
    color = [-1] * num_vertices
    conjunto_a = set()
    conjunto_b = set()

    for vertice in range(num_vertices):
        if not visitados[vertice]:
            color[vertice] = 0
            bfs(grafo, visitados, color, vertice, conjunto_a, conjunto_b)

    return conjunto_a, conjunto_b

def tiene_ciclo_impar(grafo, vertice, visitados, color):
    visitados[vertice] = True

    for vecino in grafo[vertice]:
        if not visitados[vecino]:
            color[vecino] = 1 - color[vertice]
            if tiene_ciclo_impar(grafo, vecino, visitados, color):
                return True
        elif color[vecino] == color[vertice]:
            return True

    return False

def ciclo_impar_grafo(grafo):
    num_vertices = len(grafo)
    visitados = [False] * num_vertices
    color = [-1] * num_vertices

    for vertice in range(num_vertices):
        if not visitados[vertice]:
            color[vertice] = 0
            if tiene_ciclo_impar(grafo, vertice, visitados, color):
                return False

    conjunto_a, conjunto_b = particionar_grafo(grafo)
    return conjunto_a, conjunto_b



def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0,ncasos):
        grafo = {}
        lista = linea.split(",")
        for x in lista:
            y = x.split(" ")
            y = [int(cadena) for cadena in y]
            grafo[y[0]] = y[1:]
            
        z = ciclo_impar_grafo(grafo)
        if z == False:            
            print("NO es bipartito")
        else:
            print(z)
        linea = sys.stdin.readline()
    
main()





