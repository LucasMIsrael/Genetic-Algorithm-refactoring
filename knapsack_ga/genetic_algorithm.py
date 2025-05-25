import random
from problem import avaliar

def gerar_individuo(num_itens):
    return [random.randint(0, 1) for _ in range(num_itens)]

def gerar_populacao(tam_pop, num_itens):
    return [gerar_individuo(num_itens) for _ in range(tam_pop)]

def selecionar_pais(populacao, pesos, valores, capacidade):
    pais = []
    for _ in range(2):
        i, j = random.sample(range(len(populacao)), 2)
        melhor = populacao[i] if avaliar(populacao[i], pesos, valores, capacidade) > avaliar(populacao[j], pesos, valores, capacidade) else populacao[j]
        pais.append(melhor)
    return pais

def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]

def mutar(individuo, tx_mutacao):
    return [1 - gene if random.random() < tx_mutacao else gene for gene in individuo]

def nova_geracao(populacao, tam_pop, pesos, valores, capacidade, tx_mutacao):
    nova_populacao = []
    while len(nova_populacao) < tam_pop:
        pai1, pai2 = selecionar_pais(populacao, pesos, valores, capacidade)
        filho1, filho2 = crossover(pai1, pai2)
        nova_populacao.append(mutar(filho1, tx_mutacao))
        if len(nova_populacao) < tam_pop:
            nova_populacao.append(mutar(filho2, tx_mutacao))
    return nova_populacao

def algoritmo_genetico(pesos, valores, capacidade, tam_pop=50, num_geracoes=100, tx_mutacao=0.05):
    num_itens = len(pesos)
    populacao = gerar_populacao(tam_pop, num_itens)

    melhor_individuo = max(populacao, key=lambda ind: avaliar(ind, pesos, valores, capacidade))
    melhor_valor = avaliar(melhor_individuo, pesos, valores, capacidade)

    for _ in range(num_geracoes):
        populacao = nova_geracao(populacao, tam_pop, pesos, valores, capacidade, tx_mutacao)
        candidato = max(populacao, key=lambda ind: avaliar(ind, pesos, valores, capacidade))
        valor_candidato = avaliar(candidato, pesos, valores, capacidade)

        if valor_candidato > melhor_valor:
            melhor_valor = valor_candidato
            melhor_individuo = candidato

    peso_final = sum([melhor_individuo[i] * pesos[i] for i in range(num_itens)])
    return {
        "valor_total": melhor_valor,
        "peso_total": peso_final,
        "solucao": melhor_individuo
    }