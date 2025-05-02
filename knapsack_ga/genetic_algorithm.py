import random

# Função para avaliar a solução
def avaliar(solucao, pesos, valores, capacidade):
    """
    Avalia uma solução binária, retornando o valor total se a solução for válida.
    Caso contrário, retorna 0 (penalização).
    """
    peso = sum([solucao[i] * pesos[i] for i in range(len(pesos))])
    valor = sum([solucao[i] * valores[i] for i in range(len(valores))])
    return valor if peso <= capacidade else 0

# Função para gerar um indivíduo aleatório (vetor binário)
def gerar_individuo(num_itens):
    """
    Gera um indivíduo (vetor binário) aleatório de tamanho 'num_itens'.
    """
    return [random.randint(0, 1) for _ in range(num_itens)]

# Função para gerar a população inicial
def gerar_populacao(tam_pop, num_itens):
    """
    Gera uma população inicial de tamanho 'tam_pop', composta por indivíduos aleatórios.
    """
    return [gerar_individuo(num_itens) for _ in range(tam_pop)]

# Função para selecionar pais utilizando roleta
def selecionar_pais(populacao, pesos, valores, capacidade):
    """
    Seleciona dois pais utilizando o método de roleta.
    """
    pais = []
    for _ in range(2):
        i, j = random.sample(range(len(populacao)), 2)
        if avaliar(populacao[i], pesos, valores, capacidade) > avaliar(populacao[j], pesos, valores, capacidade):
            pais.append(populacao[i])
        else:
            pais.append(populacao[j])
    return pais

# Função para realizar o crossover entre dois pais
def crossover(pai1, pai2):
    """
    Realiza o crossover (cruzamento) entre dois pais.
    Retorna dois filhos gerados a partir do crossover.
    """
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

# Função para mutação (modificação aleatória de bits)
def mutar(individuo, tx_mutacao):
    """
    Realiza mutação em um indivíduo com uma certa taxa de mutação.
    """
    return [1 - gene if random.random() < tx_mutacao else gene for gene in individuo]

# Função para criar uma nova geração
def nova_geracao(populacao, tam_pop, pesos, valores, capacidade, tx_mutacao, tx_crossover):
    """
    Gera uma nova população utilizando seleção, crossover e mutação.
    """
    nova_populacao = []
    while len(nova_populacao) < tam_pop:
        pais = selecionar_pais(populacao, pesos, valores, capacidade)
        filho1, filho2 = crossover(pais[0], pais[1])
        nova_populacao.append(mutar(filho1, tx_mutacao))
        if len(nova_populacao) < tam_pop:
            nova_populacao.append(mutar(filho2, tx_mutacao))
    return nova_populacao

# Função principal do algoritmo genético
def algoritmo_genetico(pesos, valores, capacidade, tam_pop=50, num_geracoes=100, tx_crossover=0.8, tx_mutacao=0.05):
    """
    Implementa o Algoritmo Genético para o problema da mochila.
    """
    num_itens = len(pesos)

    # Geração da população inicial
    populacao = gerar_populacao(tam_pop, num_itens)

    # Melhoria das soluções ao longo das gerações
    melhor_individuo = max(populacao, key=lambda ind: avaliar(ind, pesos, valores, capacidade))
    melhor_valor = avaliar(melhor_individuo, pesos, valores, capacidade)

    # Evolução das gerações
    for geracao in range(num_geracoes):
        populacao = nova_geracao(populacao, tam_pop, pesos, valores, capacidade, tx_mutacao, tx_crossover)
        individuo_atual = max(populacao, key=lambda ind: avaliar(ind, pesos, valores, capacidade))
        valor_atual = avaliar(individuo_atual, pesos, valores, capacidade)

        # Atualiza a melhor solução encontrada
        if valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_individuo = individuo_atual

    # Retorna o melhor valor encontrado e seu peso total
    peso_total = sum([melhor_individuo[i] * pesos[i] for i in range(num_itens)])
    return {
        "valor_total": melhor_valor,
        "peso_total": peso_total,
        "geracoes": num_geracoes
    }
