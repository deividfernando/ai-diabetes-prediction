# Previsor de Risco de Diabetes

Este é um projeto de um previsor de risco de diabetes utilizando **Machine Learning** com o algoritmo **LightGBM**. A aplicação permite que o usuário insira diversos fatores relacionados à saúde e, com base nesses dados, o modelo calcula a probabilidade de a pessoa ter diabetes.

## Objetivo

O objetivo deste projeto é desenvolver um sistema que possa prever o risco de diabetes com base em fatores de saúde fornecidos pelo usuário. O modelo foi treinado utilizando o algoritmo **LightGBM** e otimizado com base na métrica **AUC (Área Sob a Curva ROC)** para encontrar o melhor **threshold** de classificação.

## Fatores Utilizados

A previsão de risco de diabetes é baseada nos seguintes fatores de entrada:

- **Gênero**: feminino ou masculino
- **Idade**: idade do paciente
- **Hipertensão**: se o paciente tem ou não hipertensão
- **Doença Cardíaca**: se o paciente tem ou não uma doença cardíaca
- **Histórico de Fumo**: histórico de fumo do paciente (nunca fumou, ex-fumante, fumante atual, etc.)
- **IMC (Índice de Massa Corporal)**: calculado a partir do peso e da altura
- **Nível de HbA1c**: uma medida do nível médio de açúcar no sangue nos últimos 2-3 meses
- **Nível de Glicose no Sangue**: medido em mg/dL

## Dataset Utilizado

O modelo foi treinado com um conjunto de dados público sobre saúde e diabetes, que contém informações de diversos pacientes. Os dados incluem:
- Informações demográficas
- Condições de saúde (hipertensão, doença cardíaca, etc.)
- Medidas de saúde (IMC, níveis de HbA1c, níveis de glicose)

Esse conjunto de dados foi processado e ajustado para garantir que as previsões de diabetes fossem feitas de forma precisa.

## Como Executar o Projeto

Siga os passos abaixo para rodar o projeto localmente:

### Pré-requisitos

- **Python 3.7 ou superior**
- **pip** instalado
- **Git** instalado (para clonar o repositório)

### 1. Clone o repositório

Clone este repositório GitHub no seu ambiente local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### 2. Instale as dependências

Após clonar o repositório, navegue até o diretório do projeto e instale as dependências listadas no arquivo requirements.txt

```bash
cd nome-do-repositorio
pip install -r requirements.txt
```

### 3. Execute o aplicativo Streamlit
Execute o aplicativo Streamlit com o comando:

```bash
streamlit run app.py
```

### 4. Abra o aplicativo no navegador

Após executar o comando acima, o Streamlit fornecerá um link para acessar o aplicativo no navegador. Geralmente, o endereço será algo como:

http://localhost:8501

Abra esse link no navegador para começar a utilizar a aplicação.

## Como Usar

No aplicativo, insira os valores correspondentes aos fatores de risco, como idade, IMC, histórico de fumo, níveis de HbA1c e glicose no sangue. Após preencher todos os campos, clique no botão "Prever" para ver o resultado da previsão de risco de diabetes.

Se o modelo identificar que há risco de diabetes, ele também listará os principais fatores de risco com base nos dados fornecidos.

## Contribuição

Sinta-se à vontade para contribuir com melhorias para o projeto. Para isso, basta abrir uma issue ou fazer um fork do projeto e enviar um pull request com as suas melhorias.