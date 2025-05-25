import pytest
from genetic_algorithm import algoritmo_genetico

@pytest.fixture
def dados_exemplo():
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 6]
    capacidade = 5
    return pesos, valores, capacidade

def test_algoritmo_genetico_retorna_solucao_valida(dados_exemplo):
    pesos, valores, capacidade = dados_exemplo
    resultado = algoritmo_genetico(pesos, valores, capacidade, tam_pop=30, num_geracoes=50, tx_mutacao=0.05)

    assert isinstance(resultado, dict)
    assert "solucao" in resultado
    assert "valor_total" in resultado
    assert "peso_total" in resultado
    assert resultado["peso_total"] <= capacidade

def test_algoritmo_genetico_melhora_com_mais_geracoes():
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 6]
    capacidade = 5

    resultado1 = algoritmo_genetico(pesos, valores, capacidade, tam_pop=30, num_geracoes=10)
    resultado2 = algoritmo_genetico(pesos, valores, capacidade, tam_pop=30, num_geracoes=100)

    assert resultado2["valor_total"] >= resultado1["valor_total"]