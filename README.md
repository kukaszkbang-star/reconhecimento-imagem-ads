# Teste Assistant Code - Projeto de Aprendizado em Python

Este projeto apresenta uma coleção de scripts Python desenvolvidos para fins educacionais, com foco em boas práticas de programação, refatoração de código e tratamento de erros.

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Arquivos](#arquivos)
- [Requisitos](#requisitos)
- [Como Usar](#como-usar)
- [Conceitos Abordados](#conceitos-abordados)
- [Contribuindo](#contribuindo)

## 🎯 Visão Geral

O projeto é dividido em três módulos principais, cada um focando em um aspecto diferente da programação Python:

1. **Verificação de Números Primos** - Implementação eficiente com validação
2. **Cálculo de Estatísticas** - Refatoração com Clean Code
3. **Sistema de Faturamento** - Correção de erros e debugging

Todos os módulos foram desenvolvidos seguindo as melhores práticas de código limpo, incluindo nomes descritivos, documentação clara e tratamento de erros.

## 📁 Estrutura do Projeto

```
teste-assistent-code/
├── num_primos.py
├── explicacao_num_primo.md
├── refaturacao.py
├── explicacao_refotaracao.md
├── debug.py
└── explicacao_debug.md
```

## 📄 Arquivos

### 1. **num_primos.py** - Verificador de Números Primos

**Objetivo:** Determinar se um número é primo utilizando um algoritmo eficiente.

**Principais Características:**
- Função `is_prime(number: int) -> bool` com validação de entrada
- Tratamento de erros com `ValueError`
- Algoritmo otimizado usando raiz quadrada
- Testes com múltiplos números

**Como Usar:**
```bash
python num_primos.py
```

**Saída Esperada:**
```
1: não é primo
2: é primo
3: é primo
4: não é primo
16: não é primo
17: é primo
19: é primo
20: não é primo
```

**Documentação:** Ver [explicacao_num_primo.md](teste-assistent-code/explicacao_num_primo.md)

---

### 2. **refaturacao.py** - Cálculo de Estatísticas

**Objetivo:** Calcular estatísticas básicas (total, média, maior, menor) de uma lista de números.

**Principais Características:**
- Função `calcular_estatisticas(numeros)` com validação robusta
- Uso de funções built-in do Python (`sum`, `max`, `min`)
- Tratamento de erros para listas vazias e tipos inválidos
- Separação clara entre lógica e execução

**Como Usar:**
```bash
python refaturacao.py
```

**Saída Esperada:**
```
Total: 346
Média: 34.6
Maior: 89
Menor: 2
```

**Documentação:** Ver [explicacao_refotaracao.md](teste-assistent-code/explicacao_refotaracao.md)

---

### 3. **debug.py** - Sistema de Faturamento

**Objetivo:** Calcular recibos de vendas com impostos e descontos, demonstrando como identificar e corrigir erros comuns.

**Principais Características:**
- Entrada de dados do cliente e produtos
- Cálculo automático de subtotal, imposto (10%) e desconto
- Formatação clara do recibo com valores monetários
- Todos os erros foram identificados e corrigidos

**Como Usar:**
```bash
python debug.py
```

**Entrada Necessária:**
- Nome do cliente
- Quantidade e preço de 3 itens
- Percentual de desconto (ou 0 para sem desconto)

**Saída Esperada:**
```
===============================
 Cliente: João
===============================
 Item 1:        R$ 46.00
 Item 2:        R$ 15.00
 Item 3:        R$ 39.00
-------------------------------
 Subtotal:      R$ 100.00
 Imposto (10%): R$ 10.00
 Desconto (10%): -R$ 11.00
===============================
 TOTAL:         R$ 99.00
===============================
```

**Documentação:** Ver [explicacao_debug.md](teste-assistent-code/explicacao_debug.md)

---

## 🔧 Requisitos

- **Python 3.7 ou superior**
- Sem dependências externas

## 🚀 Como Usar

### Execução Individual

Para executar qualquer script, abra o terminal e navigate até a pasta do projeto:

```bash
cd teste-assistent-code
python num_primos.py
python refaturacao.py
python debug.py
```

### Importação em Outro Projeto

Você pode importar as funções em seus próprios scripts:

```python
from num_primos import is_prime
from refaturacao import calcular_estatisticas

# Usar as funções
print(is_prime(17))  # True
stats = calcular_estatisticas([1, 2, 3, 4, 5])
print(stats)  # (15, 3.0, 5, 1)
```

## 📚 Conceitos Abordados

### Clean Code
- ✅ Nomes descritivos para funções e variáveis
- ✅ Funções com responsabilidade única
- ✅ Documentação clara com docstrings
- ✅ Separação entre lógica e execução

### Tratamento de Erros
- ✅ Validação de tipos com `isinstance()`
- ✅ Tratamento de exceções com `ValueError`
- ✅ Mensagens de erro informativas

### Boas Práticas Python
- ✅ Type hints em parâmetros e retornos
- ✅ F-strings para formatação
- ✅ Uso de funções built-in (`sum`, `max`, `min`, `all`)
- ✅ Bloco `if __name__ == "__main__":` para execução segura

### Refatoração
- ✅ Substituição de loops por funções built-in
- ✅ Melhoria de nomenclatura
- ✅ Otimização de algoritmos
- ✅ Adição de validação de entrada

## 🐛 Erros Corrigidos em debug.py

O arquivo `debug.py` foi corrigido de sua versão original com os seguintes erros:

1. **Falta de aspas em string** - `input(Preço do item 1? )`
2. **Tipo incorreto em operações** - String usada em divisão
3. **Falta de prefixo f em f-string** - `print(" Item 2: {total_item2:.2f}")`
4. **Comparação de tipos incompatíveis** - String comparada com int
5. **Indentação faltante** - Bloco if sem indentação
6. **Formatação incorreta** - Tentativa de formatar string como float

Para detalhes completos, consulte [explicacao_debug.md](teste-assistent-code/explicacao_debug.md).

## 📖 Documentação Detalhada

Cada arquivo Python tem um arquivo Markdown correspondente com explicações linha a linha:

- [explicacao_num_primo.md](teste-assistent-code/explicacao_num_primo.md) - Análise do algoritmo de primos
- [explicacao_refotaracao.md](teste-assistent-code/explicacao_refotaracao.md) - Antes e depois da refatoração
- [explicacao_debug.md](teste-assistent-code/explicacao_debug.md) - Identificação e correção de erros

## 🤝 Contribuindo

Este projeto foi desenvolvido como material educacional. Sinta-se livre para:

- Estudar o código
- Fazer modificações e experimentar
- Usar como referência para seus próprios projetos
- Compartilhar melhorias

## 📝 Licença

Este projeto é fornecido como material educacional.

## 👤 Autor

Desenvolvido como parte de atividades de aprendizado em Python.

---

**Última atualização:** Maio de 2026

Para mais informações ou perguntas sobre o código, consulte os arquivos de explicação em Markdown (`.md`) incluídos em cada módulo.
