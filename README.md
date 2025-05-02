# Relatório: Solução para o Problema da Mochila 0/1 com Algoritmo Genético

## 🎯 Objetivo

Implementar uma solução para o problema da Mochila 0/1 utilizando **Algoritmo Genético (GA)**, visando:

- Maximizar o valor dos itens dentro da mochila sem ultrapassar sua capacidade
- Utilizar técnicas heurísticas inspiradas na natureza
- Avaliar e comparar desempenho com diferentes volumes de dados

---

## 🧠 Algoritmo Utilizado: Algoritmo Genético (GA)

Cada solução (indivíduo) é representada por um vetor binário, onde:

- `1` indica que o item está na mochila
- `0` indica que o item foi ignorado

Operações aplicadas:

- **População inicial:** gerada aleatoriamente
- **Avaliação (Fitness):** soma dos valores dos itens válidos (sem exceder o peso)
- **Seleção:** torneio entre indivíduos
- **Crossover:** ponto único (single-point)
- **Mutação:** troca aleatória de bits
- **Nova geração:** substituição completa (geração elitista opcional)

---

## ⚙️ Modelagem do Problema

- Vetores de pesos e valores dos itens
- Capacidade total da mochila (W)
- Representação: vetor binário

---

## 🧪 Avaliação das Soluções

### ✅ Penalização de Soluções Inválidas

Qualquer solução cujo peso ultrapasse o limite da mochila recebe **aptidão 0**.

```python
if peso_total > capacidade:
    return 0
```

### ✅ Função de Aptidão

A função de avaliação retorna a **soma dos valores** dos itens escolhidos, caso o peso seja válido.

```python
valor_total = sum(v * i for v, i in zip(valores, individuo))
```

### ✅ Parâmetros utilizados nos testes

| Parâmetro            | Valor Padrão |
|----------------------|--------------|
| Tamanho da população | 50           |
| Taxa de crossover    | 0.8          |
| Taxa de mutação      | 0.05         |
| Gerações             | 100          |

---

## 📊 Testes e Resultados

Testes realizados com instâncias de:

- 5 e 10 itens (depuração e validação)
- 1.000 e 10.000 itens (benchmark)

### Métricas registradas

- Valor total alcançado
- Tempo de execução
- Número de gerações

Resultados salvos automaticamente em: `resultados/resultados.xlsx`

---

## 🧮 Complexidade e Dificuldades

### 📈 Complexidade do Algoritmo Genético

Para `p = população`, `g = gerações`, `n = número de itens`:

- Avaliação: `O(p * n)`
- Crossover/Mutação: `O(p * n)`
- Total: `O(g * p * n)`

> Crescimento linear com o número de itens e gerações, mas exige muitos testes para evitar mínimos locais.

### 🧱 Dificuldades Encontradas

- Controle de soluções inválidas (resolvido com penalização)
- Alto tempo de execução com 10.000 itens em configurações básicas
- Resultados estocásticos: diferentes execuções produzem diferentes soluções
- Visualização CSV inicialmente pouco legível (corrigida com separação clara de colunas)

---

## 📁 Estrutura do Projeto

```
knapsack_ga/
├── genetic_algorithm.py         # Algoritmo Genético completo
├── test_runner.py               # Script para executar os testes em massa
├── utils.py                     # Utilitários para geração de dados e tempo
├── resultados/
│   └── resultados.xsls          # Resultados organizados dos testes
├── docs/
│   └── README.md (este arquivo)
```

---

## 👥 Equipe

- Alexandre Tessaro Vieira
- Edson Borges Polucena
- LeonardoPereira Borges
- Richard Schmitz Riedo
- Wuelliton Christian Dos Santos

---

## ✅ Conclusão

O Algoritmo Genético se mostrou eficaz para o problema da Mochila, especialmente com instâncias pequenas e médias. Com grandes volumes (10.000+), o desempenho depende fortemente da parametrização e do número de gerações. A penalização de soluções inválidas é essencial para manter a eficiência do algoritmo.
