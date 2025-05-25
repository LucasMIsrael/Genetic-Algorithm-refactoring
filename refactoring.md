# Refatoração e Validação - Algoritmo Genético para o Problema da Mochila
### Feito por: Lucas Mendes Israel, Gustavo Henrique Costa

Este documento descreve as mudanças realizadas no código original do algoritmo genético para o problema da mochila binária, explicando a motivação da refatoração e os testes automatizados criados para validar seu funcionamento.


## Refatorações Realizadas

### 1. Separação de Responsabilidades

- O código foi modularizado em diferentes arquivos:
  - `genetic_algorithm.py`: contém o algoritmo genético principal.
  - `problem.py`: contém as funções auxiliares como `avaliar` e `peso_total`.
  - `tests/`: contém os testes automatizados com `pytest`.

### 2. Uso de Funções Nomeadas

- Foram extraídas funções específicas para seleção, crossover, mutação e avaliação, tornando o código mais legível e reutilizável.

### 3. Parâmetros Flexíveis

- A função `algoritmo_genetico` agora aceita parâmetros configuráveis como `tam_pop`, `num_geracoes` e `tx_mutacao`, permitindo testar diferentes estratégias evolutivas.

---

## Testes Automatizados

Os testes foram escritos utilizando a biblioteca `pytest` para garantir a robustez e a correção do algoritmo.

### Teste: `test_algoritmo_genetico_retorna_solucao_valida`

- **Objetivo**: Garantir que o algoritmo genético retorne uma solução válida no formato esperado.
- **Justificativa**: É necessário validar se a função principal está retornando um dicionário com os campos esperados e se a solução respeita a capacidade máxima da mochila.
- **Resultado esperado**:
  - O retorno deve ser um `dict`.
  - Deve conter as chaves: `"solucao"`, `"valor_total"`, `"peso_total"`.
  - O peso total da solução não pode ultrapassar a capacidade definida.
- **Resultado obtido**: ✅ Teste passou com sucesso.

---

### Teste: `test_algoritmo_genetico_melhora_com_mais_geracoes`

- **Objetivo**: Verificar se o aumento do número de gerações melhora (ou mantém) a qualidade da solução.
- **Justificativa**: O algoritmo genético deve convergir para soluções melhores com mais iterações. Esse teste compara o valor total obtido com poucas gerações (10) e com mais gerações (100).
- **Resultado esperado**: A solução com 100 gerações deve ter um `valor_total` maior ou igual à de 10 gerações.
- **Resultado obtido**: ✅ Teste passou com sucesso.

---

### Teste: `test_avaliar_valido`

- **Objetivo**: Verificar se a função `avaliar` calcula corretamente o valor de uma solução válida dentro da capacidade.
- **Justificativa**: Testa o comportamento esperado quando o cromossomo selecionado está dentro do limite de peso da mochila.
- **Resultado esperado**: Valor total retornado igual a 25 (10 + 15), respeitando a capacidade de 5.
- **Resultado obtido**: ✅ Teste passou com sucesso.

---

### Teste: `test_avaliar_excede_capacidade`

- **Objetivo**: Verificar se a função `avaliar` penaliza corretamente soluções que excedem a capacidade da mochila.
- **Justificativa**: Soluções inválidas (com peso total superior à capacidade) devem ser desconsideradas pelo algoritmo com valor de aptidão igual a 0.
- **Resultado esperado**: Valor retornado igual a 0.
- **Resultado obtido**: ✅ Teste passou com sucesso.

---

### Teste: `test_peso_total`

- **Objetivo**: Garantir que a função `peso_total` calcule corretamente o peso total de uma solução.
- **Justificativa**: O cálculo de peso total é fundamental para avaliar se uma solução é válida dentro da capacidade da mochila.
- **Resultado esperado**: Soma dos pesos dos itens selecionados deve ser igual a 5.
- **Resultado obtido**: ✅ Teste passou com sucesso.

---

## Documentação da Refatoração

### Quais partes foram refatoradas

- **Algoritmo principal**: a função do algoritmo genético foi extraída para um módulo separado (`genetic_algorithm.py`), isolando a lógica principal da resolução do problema.
- **Funções auxiliares**: funções como `avaliar` e `peso_total` foram movidas para o módulo `problem.py`, facilitando testes unitários e reutilização.
- **Estrutura de diretórios**: o projeto foi organizado com uma pasta `tests/`, contendo testes automatizados com `pytest`.
- **Parâmetros da função principal**: os parâmetros do algoritmo foram tornados flexíveis (`tam_pop`, `num_geracoes`, `tx_mutacao`) para facilitar experimentações e ajustes finos.

### Técnicas aplicadas

- **Refatoração baseada em modularização**: separação de responsabilidades entre arquivos e funções para melhorar legibilidade e manutenção.
- **Test-Driven Development (TDD) a posteriori**: os testes foram escritos para validar funcionalidades existentes, contribuindo com a confiabilidade e a robustez do código.
- **Design orientado à clareza**: nomes de funções e variáveis foram ajustados para expressar claramente suas responsabilidades.

### Ferramentas utilizadas

- **Python 3.10+**
- **pytest**: framework de testes unitários automatizados.
- **VS Code** e/ou **Google Colab**: ambientes de desenvolvimento e experimentação.
- **Git** (opcional): controle de versão do projeto.

### Resultados da análise de qualidade antes e depois

| Critério                    | Antes da Refatoração        | Depois da Refatoração          |
|----------------------------|-----------------------------|-------------------------------|
| Organização do código       | Código monolítico e misto   | Modularizado em arquivos separados |
| Legibilidade               | Baixa, com funções longas   | Alta, com funções curtas e nomeadas |
| Testabilidade              | Inexistente                 | Testes automatizados com `pytest` |
| Flexibilidade de parâmetros | Limitada                    | Alta, com parâmetros configuráveis |
| Robustez                   | Não testada                 | Validada por múltiplos testes  |

### Desafios e aprendizados

**Desafios**:
- Definir uma estrutura modular que mantivesse o funcionamento original do algoritmo sem efeitos colaterais.
- Garantir que as funções auxiliares (`avaliar`, `peso_total`) fossem testáveis de forma isolada.
- Avaliar o impacto da refatoração no desempenho do algoritmo genético, mantendo a mesma capacidade de encontrar boas soluções.

**Aprendizados**:
- A importância de testes automatizados para dar segurança nas refatorações.
- Como a modularização facilita a leitura, a manutenção e a extensão futura do código.
- A refatoração, mesmo simples, pode trazer ganhos significativos na confiabilidade e na escalabilidade de um projeto.



## Considerações Finais

A refatoração melhorou a organização, a clareza e a testabilidade do código. Os testes garantem que o algoritmo continua funcionando conforme o esperado, mesmo com alterações estruturais. O uso de testes automatizados permite verificar rapidamente a correção do sistema após qualquer mudança futura.
