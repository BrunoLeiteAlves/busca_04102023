import random
import math

#O algoritmo genético é uma técnica de otimização inspirada no processo de evolução natural.
# Ele começa com uma população de soluções para um problema e, ao longo de várias gerações,
# gera novas soluções através de cruzamento e mutação. As soluções mais bem-sucedidas têm
# mais chances de serem escolhidas como pais para a próxima geração, enquanto soluções menos
# bem-sucedidas têm menos chances. Com o tempo, o algoritmo converge para uma solução que
# representa uma boa aproximação para a melhor solução possível para o problema.

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
    # Adiciona a distância de volta à cidade de origem
    distancia_total += calcular_distancia(cidades[rota[-1]], cidades[rota[0]])
    return distancia_total


# Função para gerar uma população inicial aleatória
def gerar_populacao_inicial(cidades, tamanho_populacao):
    num_cidades = len(cidades)
    populacao_inicial = [list(range(num_cidades)) for _ in range(tamanho_populacao)]
    for individuo in populacao_inicial:
        random.shuffle(individuo)
    return populacao_inicial


# Função para calcular o fitness (inverso da distância) de cada indivíduo
def calcular_fitness(populacao, cidades):
    fitness = []
    for individuo in populacao:
        distancia_total = calcular_distancia_total(individuo, cidades)
        fitness.append(1 / distancia_total)  # Quanto menor a distância, maior o fitness
    return fitness


# Função para selecionar pais com base no fitness
def selecionar_pais(populacao, fitness, num_pais):
    pais_selecionados = []
    total_fitness = sum(fitness)
    probabilidade_selecao = [f / total_fitness for f in fitness]
    for _ in range(num_pais):
        pai = random.choices(populacao, probabilidade_selecao)[0]
        pais_selecionados.append(pai)
    return pais_selecionados


# Função para realizar crossover de dois pais
def crossover(pai1, pai2):
    ponto_crossover = random.randint(0, len(pai1) - 1)
    filho1 = pai1[:ponto_crossover] + [cidade for cidade in pai2 if cidade not in pai1[:ponto_crossover]]
    filho2 = pai2[:ponto_crossover] + [cidade for cidade in pai1 if cidade not in pai2[:ponto_crossover]]
    return filho1, filho2


# Função para realizar mutação em um indivíduo
def mutacao(individuo, taxa_mutacao):
    if random.random() < taxa_mutacao:
        indice1, indice2 = random.sample(range(len(individuo)), 2)
        individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    return individuo


# Algoritmo genético para o TSP
def algoritmo_genetico_tsp(cidades, tamanho_populacao, num_geracoes, taxa_mutacao):
    populacao = gerar_populacao_inicial(cidades, tamanho_populacao)

    for geracao in range(num_geracoes):
        print(f"Geração {geracao + 1}:")
        fitness = calcular_fitness(populacao, cidades)

        melhor_individuo = populacao[fitness.index(max(fitness))]
        melhor_distancia = calcular_distancia_total(melhor_individuo, cidades)
        print(f"Melhor distância na geração {geracao + 1}: {melhor_distancia:.2f}")

        pais = selecionar_pais(populacao, fitness, tamanho_populacao)
        proxima_geracao = []

        while len(proxima_geracao) < tamanho_populacao:
            pai1, pai2 = random.sample(pais, 2)
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            proxima_geracao.extend([filho1, filho2])

        populacao = proxima_geracao

    melhor_individuo = populacao[fitness.index(max(fitness))]
    melhor_distancia = calcular_distancia_total(melhor_individuo, cidades)

    return melhor_individuo, melhor_distancia