from genetic_algorithm import algoritmo_genetico
from problem import peso_total

def executar():
    # Exemplo simples
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 6]
    capacidade = 5

    resultado = algoritmo_genetico(pesos, valores, capacidade, tam_pop=50, num_geracoes=50)

    print("Melhor solução encontrada:")
    print("Itens selecionados:", resultado["solucao"])
    print("Valor total:", resultado["valor_total"])
    print("Peso total:", resultado["peso_total"])

if __name__ == "__main__":
    executar()