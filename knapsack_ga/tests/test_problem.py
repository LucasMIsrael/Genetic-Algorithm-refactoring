from problem import avaliar, peso_total

def test_avaliar_valido():
    solucao = [1, 0, 1]
    pesos = [2, 4, 3]
    valores = [10, 20, 15]
    capacidade = 5
    assert avaliar(solucao, pesos, valores, capacidade) == 25  # 2 + 3 = 5, dentro da capacidade

def test_avaliar_excede_capacidade():
    solucao = [1, 1, 1]
    pesos = [2, 4, 3]
    valores = [10, 20, 15]
    capacidade = 5
    assert avaliar(solucao, pesos, valores, capacidade) == 0  # Excede capacidade

def test_peso_total():
    solucao = [1, 0, 1]
    pesos = [2, 4, 3]
    assert peso_total(solucao, pesos) == 5