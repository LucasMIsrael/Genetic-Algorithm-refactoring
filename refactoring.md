# Refatoração - Algoritmo Genético para o Problema da Mochila

### Autores: Lucas Mendes Israel, Gustavo Henrique Costa
</br>

**Apresentação em Slides**: [Refatoração-problemaDaMochila.pdf](https://github.com/user-attachments/files/20433039/Refatoracao-problemaDaMochila.pdf)

Este documento descreve as mudanças realizadas no código original do algoritmo genético para o problema da mochila binária, explicando a motivação da refatoração e os testes automatizados criados para validar seu funcionamento.

Para refatoração e criação de testes, foi feito o Fork do repositório original, https://github.com/AlexandreTessaro/Genetic-Algorithm, desenvolvido pelo Alexandre Tessaro e equipe.

---

### Objetivos da Refatoração

- Melhorar a **legibilidade**, **manutenção** e **testabilidade** do código.
- Permitir **experimentação com parâmetros flexíveis** no algoritmo.
- Garantir que alterações no código não afetem a **correção funcional**.

---

### Refatorações Realizadas

#### 1. Separação de Responsabilidades

  - `main.py`: arquivo a ser executado que inicia a lógica.
  - `genetic_algorithm.py`: algoritmo principal.
  - `problem.py`: funções auxiliares como `avaliar` e `peso_total`.
  - `tests/`: testes unitários com `pytest`.

#### 2. Clareza e Reutilização com Funções Nomeadas

- Extração de funções para seleção, crossover, mutação e avaliação, facilitando leitura e manutenção.

#### 3. Parâmetros Configuráveis

A função `algoritmo_genetico` agora aceita parâmetros configuráveis:
- `tam_pop`: tamanho da população.
- `num_geracoes`: número de gerações.
- `tx_mutacao`: taxa de mutação.
Isso permite testar diferentes estratégias evolutivas com facilidade.
---

### Técnicas de Refatoração Utilizadas

Durante a refatoração, foram aplicadas técnicas descritas por Martin Fowler e também referenciadas nos sites [Refactoring Guru](https://refactoring.guru/) e [Refactoring Catalog](https://refactoring.com/). As principais técnicas utilizadas foram:

#### Extract Function (Extrair Função)

- O código que realizava múltiplas tarefas foi dividido em funções nomeadas e coesas, como `avaliar`, `mutar`, `cruzar`, `peso_total`.
- Benefício: Redução da complexidade e aumento da legibilidade e reutilização.

#### Move Function (Mover Função)

- Funções que não pertenciam à responsabilidade do algoritmo principal foram movidas para o arquivo `problem.py`.
- Benefício: Melhor separação de responsabilidades.

#### Split Phase (Dividir Fase)

- O algoritmo foi segmentado em fases bem definidas: geração da população, seleção, cruzamento, mutação e avaliação.
- Benefício: Cada etapa pode ser compreendida, testada e alterada separadamente.

#### Rename Variable / Rename Method (Renomear Variável/Método)

- Funções e variáveis com nomes genéricos ou confusos foram renomeadas para refletir melhor seu papel (por exemplo, `melhor_solucao` → `melhor_individuo`, `func` → `avaliar`).
- Benefício: Maior clareza e expressividade no código.

---

### Testes Automatizados com `pytest`

Os testes foram implementados para garantir que as refatorações não impactaram negativamente a lógica do algoritmo.

#### `test_algoritmo_genetico_retorna_solucao_valida`
- **Objetivo**: Verifica se a solução retornada é válida e bem formatada.
- **Validações**:
  - Retorno é um `dict`.
  - Contém as chaves `"solucao"`, `"valor_total"` e `"peso_total"`.
  - O peso total está dentro da capacidade permitida.

#### `test_algoritmo_genetico_melhora_com_mais_geracoes`
- **Objetivo**: Garante que mais gerações resultam em melhor (ou igual) qualidade da solução.
- **Lógica**: Compara os resultados com 10 e 100 gerações.

#### `test_avaliar_valido`
- **Objetivo**: Verifica se a função `avaliar` retorna o valor correto para soluções dentro da capacidade.
- **Exemplo**: Solução `[1, 0, 1]` retorna valor total `25`.

#### `test_avaliar_excede_capacidade`
- **Objetivo**: Soluções acima da capacidade retornam valor `0`.

#### `test_peso_total`
- **Objetivo**: Confirma que `peso_total` retorna a soma correta dos pesos.

---

### Tecnologias e Ferramentas Utilizadas

- **Python**
- **pytest**: testes automatizados
- **VS Code**
- **GitHub**: Para criar o Fork e versionamento de código
- **SonarCloud**: Analisar qualidade do código

### Análise com SonarCloud

A refatoração passou por uma análise com a ferramenta, o que permitiu identificar alguns pontos negativos no código original, como campos e funções sendo passadas por parametro em outras funções mas inutilizaveis na lógica, funções sem uso, etc. Esses pontos foram corrigidos na refatoração e análisados novamaente no Sonar:

![image](https://github.com/user-attachments/assets/d1b406ac-462d-41ef-ba0b-9468aed31d0b)

---

### Análise de Qualidade: Antes vs Depois

| Critério                    | Antes da Refatoração        | Depois da Refatoração          |
|----------------------------|-----------------------------|-------------------------------|
| Organização do código      | Responsabilidades pouco divididas          | Modularizado em arquivos separados |
| Legibilidade               | Baixa                       | Alta, com funções curtas e nomeadas |
| Testabilidade              | Apenas 1 teste de funcionalidade | Vários cenários com `pytest` |
| Flexibilidade              | Limitada                    | Alta, com parâmetros configuráveis |
| Robustez                   | Não testada                 | Validada com testes |

---

### Desafios e Aprendizados

**Desafios enfrentados:**
- Isolar responsabilidades mantendo o funcionamento original.
- Testar funções auxiliares de forma independente.
- Refatorar sem comprometer a performance.

**Aprendizados:**
- A modularização facilita manutenção e extensão.
- Testes automatizados aumentam a segurança ao modificar código.
- Refatorações bem planejadas aumentam a confiabilidade e escalabilidade.

---

### Considerações Finais

A refatoração trouxe melhorias claras na organização, clareza e confiabilidade do projeto. O uso de testes automatizados garante que o sistema continue funcionando corretamente mesmo após alterações estruturais. O projeto está agora mais preparado para evoluir com segurança.
