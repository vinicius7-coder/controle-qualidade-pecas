# controle-qualidade-pecas
Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

# 🏭 Sistema de Controle de Qualidade de Peças

## 📌 Sobre o projeto
Este projeto foi desenvolvido com o objetivo de simular um sistema de controle de qualidade em uma linha de produção industrial.

A ideia principal é automatizar a verificação de peças produzidas, analisando critérios como peso, cor e comprimento, e classificando automaticamente se a peça está aprovada ou reprovada.

Além disso, o sistema também organiza as peças aprovadas em caixas com capacidade limitada, simulando um processo real de armazenamento, incluindo controle de caixas abertas e fechadas.

---

## ⚙️ Como o sistema funciona
O sistema é executado via terminal e possui um menu interativo com as seguintes opções:

1. Cadastrar nova peça  
2. Listar peças cadastradas  
3. Remover peça  
4. Listar caixas  
5. Gerar relatório final  

Ao cadastrar uma peça, o usuário informa:
- ID da peça (não pode ser duplicado)
- Peso (em gramas)
- Cor
- Comprimento (em centímetros)

Com base nesses dados, o sistema faz a validação automática seguindo os critérios:

- Peso entre 95g e 105g  
- Cor azul ou verde  
- Comprimento entre 10cm e 20cm  

Se a peça estiver dentro dos padrões, ela é considerada **aprovada** e é armazenada em uma caixa.

Cada caixa tem limite de 10 peças. Quando esse limite é atingido, a caixa é fechada automaticamente e uma nova é iniciada.

O sistema também mantém controle de caixas ainda em aberto.

Caso a peça não atenda aos critérios, ela é **reprovada**, e o sistema informa o motivo.

---

## ⚠️ Regras importantes do sistema
- Não é permitido cadastrar duas peças com o mesmo ID  
- Apenas peças aprovadas entram nas caixas  
- Peças que já estão em caixas fechadas não podem ser removidas do armazenamento  
- O sistema valida entradas numéricas (peso e comprimento)  

---

## 📊 Relatório
O sistema gera um relatório final contendo:

- Total de peças aprovadas  
- Total de peças reprovadas  
- Motivos das reprovações  
- Quantidade total de caixas (incluindo caixa em aberto, se houver)  

---

## ▶️ Como executar o projeto

### Pré-requisitos
- Ter o Python instalado na máquina (versão 3 ou superior)

### Passo a passo

1. Baixe ou copie o código do projeto
2. Abra o terminal na pasta onde o arquivo está salvo
3. Execute o comando:

```bash
python controledepecas.py
