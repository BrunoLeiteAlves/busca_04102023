# Função de exemplo para o TSP
from busca_feixe_local import busca_em_feixe_local_tsp
from busca_genetica import algoritmo_genetico_tsp


# Função de exemplo para o TSP
def exemplo_feixe_local_tsp():
    # Lista de cidades com coordenadas (x, y)
    cidades = [(0, 0), (1, 2), (3, 4), (4, 1), (2, 3)]
    tamanho_feixe = 5
    num_iteracoes = 1000

    melhor_rota, melhor_distancia = busca_em_feixe_local_tsp(cidades, tamanho_feixe, num_iteracoes)

    print("\nMelhor rota encontrada:", melhor_rota)
    print("Melhor distância:", melhor_distancia)


# Função de exemplo para o TSP usando algoritmo genético
def exemplo_algoritmo_genetico_tsp():
    # Lista de cidades com coordenadas (x, y)
    cidades = [(0, 0), (1, 2), (3, 4), (4, 1), (2, 3)]
    tamanho_populacao = 50
    num_geracoes = 100
    taxa_mutacao = 0.2

    melhor_rota, melhor_distancia = algoritmo_genetico_tsp(cidades, tamanho_populacao, num_geracoes, taxa_mutacao)

    print("\nMelhor rota encontrada:", melhor_rota)
    print("Melhor distância:", melhor_distancia)


if __name__ == "__main__":
    #exemplo_feixe_local_tsp()
    exemplo_algoritmo_genetico_tsp()