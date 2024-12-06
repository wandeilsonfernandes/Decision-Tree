# 📊 Projeto de Predição de Diabetes com Árvore de Decisão

Este projeto foi desenvolvido como parte de uma apresentação para a disciplina de **Estrutura de Dados II** no curso de **Ciência da Computação** da **Universidade Estadual de Roraima (UERR)**. 🎓 Ele utiliza machine learning para prever o diagnóstico de diabetes com base em um conjunto de dados médicos. 🚑

---

## 🛠️ Funcionalidades

- Carregamento e manipulação de dados médicos com **Pandas**.
- Implementação de um modelo de **Árvore de Decisão** usando a biblioteca **Scikit-Learn**.
- Treinamento e teste do modelo com divisão de 70%/30% dos dados.
- Cálculo da **acurácia** do modelo e geração de uma **matriz de confusão**.

---

## 📂 Estrutura do Projeto

- `diabetes.csv`: Conjunto de dados com informações médicas dos pacientes.
- `main.py`: Código principal do projeto, incluindo:
  - Preprocessamento dos dados.
  - Treinamento e teste do modelo.
  - Exibição de métricas de desempenho.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python** (>= 3.7) instalado em seu ambiente.
2. Instale as dependências necessárias:
   ```bash
   pip install pandas scikit-learn
   
3. Coloque o arquivo diabetes.csv na mesma pasta do script.
4. Execute o script:
   ```bash
   python main.py

5. O script exibirá:
 - A acurácia do modelo.
 - A matriz de confusão para análise detalhada.

## 📋 Como Funciona

1. Importação dos Dados:

 - Os dados médicos são carregados do arquivo diabetes.csv
   
2. Divisão de Dados:

  - As variáveis independentes (como idade, IMC, níveis de glicose) são separadas da variável dependente (resultado de diabetes: 1 ou 0).
  - O conjunto é dividido em treinamento (70%) e teste (30%).
   
3. Treinamento do Modelo:

  - Um classificador de Árvore de Decisão é treinado com os dados de treinamento.

4. Predição e Avaliação:

  - O modelo faz previsões sobre os dados de teste.
  - A acurácia e a matriz de confusão são calculadas para medir o desempenho.

## 🧠 Aplicação Prática
Este projeto pode ser usado como ponto de partida para criar sistemas de apoio à decisão médica, ajudando profissionais de saúde a identificar casos potenciais de diabetes. 💡

⚠️ Nota: Este modelo é apenas um protótipo e não deve ser usado para diagnósticos médicos reais sem validação adicional.


## 🛡️ Tecnologias Utilizadas
- Python 🐍
- Pandas para manipulação de dados.
- Scikit-Learn para machine learning.

# 📊 Exemplo de Saída
- Acurácia: 0.683982
- Matriz de Confusão:
[[120,  30]
 [ 25,  56]]

## ✨ Contexto Acadêmico
Este projeto foi apresentado na Universidade Estadual de Roraima (UERR) como parte da disciplina de Estrutura de Dados II do curso de Ciência da Computação. O objetivo foi demonstrar a aplicação de conceitos de estrutura de dados e machine learning em um problema do mundo real, conectando teoria e prática. 📚
