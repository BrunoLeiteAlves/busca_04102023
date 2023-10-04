import random
import math

#A busca em feixe local é um algoritmo de otimização que começa com um conjunto inicial
# de soluções candidatas e, a cada iteração, gera novas soluções próximas às melhores
# soluções atuais.

# Função para calcular a distância entre duas cidades
def calcular_distancia(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Função para calcular a distância total de uma rota
def calcular_distancia_total(rota, cidades):
    distancia_total = 0
    for i in range(len(rota) - 1):
        cidade_atual = cidades[rota[i]]
        proxima_cidade = cidades[rota[i + 1]]
        distancia = calcular_distancia(cidade_atual, proxima_cidade)
        distancia_total += distancia
        print(f"Distância de {rota[i]} para {rota[i + 1]}: {distancia:.2f}")
    # Adiciona a distância de volta à cidade de origem
    distancia_de_volta = calcular_distancia(cidades[rota[-1]], cidades[rota[0]])
    distancia_total += distancia_de_volta
    print(f"Distância de volta à cidade de origem: {distancia_de_volta:.2f}")
    return distancia_total


# Função para gerar uma solução inicial aleatória
def gerar_solucao_inicial(cidades):
    num_cidades = len(cidades)
    rota_inicial = list(range(num_cidades))
    random.shuffle(rota_inicial)
    return rota_inicial


# Função para gerar vizinhos de uma solução (troca de duas cidades)
def gerar_vizinhos(solucao):
    vizinhos = []
    num_cidades = len(solucao)
    for i in range(num_cidades - 1):
        for j in range(i + 1, num_cidades):
            vizinho = solucao[:]
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos


# Algoritmo de busca em feixe local para o TSP
def busca_em_feixe_local_tsp(cidades, tamanho_feixe, num_iteracoes):
    feixe = [gerar_solucao_inicial(cidades) for _ in range(tamanho_feixe)]

    for iteracao in range(num_iteracoes):
        print(f"Iteração {iteracao + 1}:")
        novos_feixe = []
        for i, solucao in enumerate(feixe):
            print(f"\nSolução {i + 1}: {solucao}")
            vizinhos = gerar_vizinhos(solucao)
            melhor_vizinho = min(vizinhos, key=lambda x: calcular_distancia_total(x, cidades))
            novos_feixe.append(melhor_vizinho)
            print(f"Melhor vizinho encontrado: {melhor_vizinho}")
        feixe = novos_feixe

    melhor_rota = min(feixe, key=lambda x: calcular_distancia_total(x, cidades))
    melhor_distancia = calcular_distancia_total(melhor_rota, cidades)

    return melhor_rota, melhor_distancia