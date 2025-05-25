import random

def gerar_instancia(num_itens):
    pesos = [random.randint(1, 10) for _ in range(num_itens)]
    valores = [random.randint(10, 100) for _ in range(num_itens)]
    capacidade = sum(pesos) // 2
    return pesos, valores, capacidade