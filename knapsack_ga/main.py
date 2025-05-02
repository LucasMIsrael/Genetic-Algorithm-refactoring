# main.py
from genetic_algorithm import gerar_populacao, nova_geracao
from problem import avaliar, peso_total

num_geracoes = 50

def executar():
    populacao = gerar_populacao()
    melhor_solucao = None
    melhor_valor = 0

    for geracao in range(num_geracoes):
        populacao = sorted(populacao, key=avaliar, reverse=True)
        if avaliar(populacao[0]) > melhor_valor:
            melhor_valor = avaliar(populacao[0])
            melhor_solucao = populacao[0]
        print(f"Geração {geracao + 1} - Melhor valor: {melhor_valor}")
        populacao = nova_geracao(populacao)

    print("\nMelhor solução encontrada:")
    print("Itens selecionados:", melhor_solucao)
    print("Valor total:", melhor_valor)
    print("Peso total:", peso_total(melhor_solucao))

if __name__ == "__main__":
    executar()
