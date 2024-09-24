import streamlit as st
import joblib
import pandas as pd

# Carregar o modelo
model = joblib.load('modelo_diabetes_lightgbm.pkl')

def predict_diabetes(data, threshold=0.38):
    df = pd.DataFrame([data], columns=['gender', 'age', 'hypertension', 'heart_disease', 
                                       'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'])
    df['gender'] = df['gender'].map({'feminino': 0, 'masculino': 1})
    df['smoking_history'] = df['smoking_history'].map({
        'nunca fumou': 0, 'ex-fumante': 1, 'fumante atual': 2, 'fumou algum dia': 3, 'não é fumante atualmente': 4, 'sem informação': 5})
    df['hypertension'] = df['hypertension'].map({'Verdadeiro': True, 'Falso': False})
    df['heart_disease'] = df['heart_disease'].map({'Verdadeiro': True, 'Falso': False})
    
    prediction_prob = model.predict(df)
    
    prediction = 1 if prediction_prob[0] > threshold else 0
    
    return prediction, prediction_prob[0]

# Calcular o IMC
def calcular_imc(peso, altura):
    if altura > 0:
        return peso / (altura ** 2)
    else:
        return 0

st.title("Previsor de Diabetes")

gender = st.selectbox('Gênero', ['feminino', 'masculino'], 
                      help='Selecione o gênero da pessoa (Feminino ou Masculino).')

age = st.slider('Idade', 0, 120, 30, 
                help='Informe a idade da pessoa em anos.')

hypertension = st.selectbox('Hipertensão', ['Verdadeiro', 'Falso'], 
                            help='A pessoa já foi diagnosticada com hipertensão?')

heart_disease = st.selectbox('Doença Cardíaca', ['Verdadeiro', 'Falso'], 
                             help='A pessoa já foi diagnosticada com doenças cardíacas?')

smoking_history = st.selectbox('Histórico de Fumo', 
                               ['nunca fumou', 'ex-fumante', 'fumante atual', 'fumou algum dia', 'não é fumante atualmente', 'sem informação'],
                               help='Informe o histórico de fumo da pessoa.')

peso = st.number_input('Peso (kg)', min_value=30.0, max_value=200.0, value=70.0, 
                      help='Informe o peso da pessoa em quilogramas (kg).')

altura = st.number_input('Altura (m)', min_value=1.0, max_value=2.5, value=1.75, 
                         help='Informe a altura da pessoa em metros (m).')

# Cálculo do IMC
bmi = calcular_imc(peso, altura)
st.write(f"IMC calculado: {bmi:.2f}")

HbA1c_level = st.number_input('Nível de HbA1c', min_value=3.0, max_value=15.0, value=5.0, 
                              help='Informe o nível de HbA1c no sangue. '
                                   'Esse exame indica a quantidade média de glicose nos últimos 2 a 3 meses.')

blood_glucose_level = st.number_input('Nível de Glicose no Sangue', min_value=50, max_value=300, value=100, 
                                      help='Informe o nível de glicose no sangue, medido em mg/dL.')

if st.button('Prever'):
    input_data = {
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'smoking_history': smoking_history,
        'bmi': bmi,
        'HbA1c_level': HbA1c_level,
        'blood_glucose_level': blood_glucose_level
    }

    # Prever o risco de diabetes
    result, probability = predict_diabetes(input_data)
    
    if result == 1:
        st.write(f'Previsão: A pessoa tem risco de diabetes (probabilidade: {(100 * probability):.2f}%).')
        
        # Identificar fatores de risco
        fatores = []
        if age >= 45:
            fatores.append('Idade avançada (maior que 45 anos)')
        if input_data['hypertension'] == 'Verdadeiro':
            fatores.append('Hipertensão')
        if input_data['heart_disease'] == 'Verdadeiro':
            fatores.append('Doença cardíaca')
        if input_data['smoking_history'] in ['fumante atual', 'fumou algum dia']:
            fatores.append('Histórico de fumo')
        if bmi >= 30:
            fatores.append('IMC elevado (maior que 30)')
        if HbA1c_level >= 6.5:
            fatores.append('Nível de HbA1c elevado (maior que 6.5)')
        if blood_glucose_level >= 126:
            fatores.append('Nível de glicose no sangue elevado (maior que 126 mg/dL)')

        if fatores:
            st.write("Principais fatores de risco:")
            for fator in fatores:
                st.write(f"- {fator}")
    else:
        st.write(f'Previsão: A pessoa não tem risco de diabetes (probabilidade: {(100 * probability):.2f}%).')
