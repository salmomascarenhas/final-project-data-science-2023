import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

selected = st.sidebar.selectbox('Selecione a página',
                                ['Classificador','DashBoard'])



if(selected == 'Classificador'):
    st.title('Clasificador')
else:
    st.title('DashBoard')

    for i in range(12):
        st.subheader('Avaliações por categoria de produto')
        st.image(Image.open(f'images/{i+1}.png'))
    
