def avaliar(solucao, pesos, valores, capacidade):
    peso = sum(solucao[i] * pesos[i] for i in range(len(pesos)))
    valor = sum(solucao[i] * valores[i] for i in range(len(valores)))
    return valor if peso <= capacidade else 0

def peso_total(solucao, pesos):
    return sum(solucao[i] * pesos[i] for i in range(len(pesos)))