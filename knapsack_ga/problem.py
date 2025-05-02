# problem.py

# Dados do problema
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
num_itens = len(pesos)

def avaliar(solucao):
    peso = sum([solucao[i] * pesos[i] for i in range(num_itens)])
    valor = sum([solucao[i] * valores[i] for i in range(num_itens)])
    if peso > capacidade:
        return 0  # penalização
    return valor

def peso_total(solucao):
    return sum([solucao[i] * pesos[i] for i in range(num_itens)])
