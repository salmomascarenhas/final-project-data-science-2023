import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

selected = st.sidebar.selectbox('Selecione a página',
                                ['Classificador','DashBoard'])

if(selected == 'Classificador'):
    st.title('Clasificador')
    # st.selectbox('Selecione a página',['Classificador','DashBoard'])
    
    colunas = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
           'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
           'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
           'MonthlyCharges', 'TotalCharges', 'Churn']

    valores = {
        'gender': ['female', 'male'],
        'SeniorCitizen': [0, 1],
        'Partner': ['Yes', 'No'],
        'Dependents': ['Yes', 'No'],
        'PhoneService': ['Yes', 'No'],
        'MultipleLines': ['No phone service', 'No', 'Yes'],
        'InternetService': ['DSL', 'Fiber optic', 'No'],
        'OnlineSecurity': ['Yes', 'No', 'No internet service'],
        'OnlineBackup': ['Yes', 'No', 'No internet service'],
        'DeviceProtection': ['Yes', 'No', 'No internet service'],
        'TechSupport': ['Yes', 'No', 'No internet service'],
        'StreamingTV': ['Yes', 'No', 'No internet service'],
        'StreamingMovies': ['Yes', 'No', 'No internet service'],
        'Contract': ['Month-to-month', 'One year', 'Two year'],
        'PaperlessBilling': ['Yes', 'No'],
        'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
        'Churn': ['Yes', 'No']
    }

    # Criar DataFrame vazio
    df_resultado = pd.DataFrame(columns=colunas)

    # Criar a visualização no Streamlit
    st.title("Visualização do DataFrame")

    # Iterar sobre as colunas
    for coluna in colunas:
        # Verificar se a coluna é numérica ou categórica
        if coluna in ['tenure', 'MonthlyCharges', 'TotalCharges']:
            # Coluna numérica
            valor = st.number_input(coluna)
        else:
            # Coluna categórica
            valor = st.selectbox(coluna, valores[coluna])

        # Atualizar o DataFrame com o valor selecionado
        df_resultado[coluna] = [valor]

    # Exibir o DataFrame resultante
    df = df_resultado
    df['Dependents'] = [0 if x=='No' else 1 for x in df['Partner']]
    df['Dependents'] = df['Dependents'].astype(int)
    df['Partner'] = [0 if x=='No' else 1 for x in df['Partner']]
    df['Partner'] = df['Partner'].astype(int)
    df['PhoneService'] = [0 if x=='No' else 1 for x in df['PhoneService']]
    df['PhoneService'] = df['PhoneService'].astype(int)
    df['TotalCharges'] = df['TotalCharges'].astype('str')

    for i in range(0,len(df)):
        df["TotalCharges"][i]=(df["TotalCharges"][i].strip() or 0)

    df['TotalCharges'] = df['TotalCharges'].astype(float)

    df['TotalCharges'] = df['TotalCharges'].astype(float)

    columns = ['gender', 'PaperlessBilling', 'Churn']
    mapeamento = {'No': 0, 'Yes': 1, 'Female': 0, 'Male': 1, '0': 0, '1': 1}

    for coluna in columns:
        df[coluna] = df[coluna].map(mapeamento)
    df_encoded = pd.get_dummies(df)
    print(len(df_encoded.columns))

    st.write(df_encoded)
else:
    st.title('DashBoard')

    for i in range(12):
        st.subheader('Avaliações por categoria de produto')
        st.image(Image.open(f'images/{i+1}.png'))
    
