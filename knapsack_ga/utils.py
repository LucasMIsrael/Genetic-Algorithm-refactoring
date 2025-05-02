import random

def gerar_instancia(num_itens):
    """
    Gera uma instância do problema da mochila com 'num_itens' itens.
    Retorna: (pesos, valores, capacidade)
    """
    # Gerando pesos e valores aleatórios para os itens
    pesos = [random.randint(1, 10) for _ in range(num_itens)]
    valores = [random.randint(1, 20) for _ in range(num_itens)]
    
    # Capacidade aleatória da mochila, maior que a soma dos pesos
    capacidade = sum(pesos) // 2  # Capacidade arbitrária, metade da soma dos pesos
    return pesos, valores, capacidade