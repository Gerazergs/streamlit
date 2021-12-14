import streamlit as st
import pandas as pd
import numpy as np
from numpy.random import default_rng
import random

#CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

#icon("search")
#selected = st.text_input("")
button_clicked = st.button("Re-load")




def categorical(palabras:int, listado:list):
    
    return listado[palabras]
    

def create_random_number(numero_1, numero_2):
    return random.randint(numero_1, numero_2)

def create_random_number2(numero_1, numero_2):
    size = numero_2
    rng = default_rng(numero_1)
    return rng.normal(size=size)



df = pd.DataFrame({
    'llave_1': create_random_number2(17,100)
    ,'llave_2': [create_random_number(1,7)*x + 100 for x in create_random_number2(17,100) ]
    ,'llave_3': create_random_number2(70,100)
    ,'llave_4': create_random_number2(80,100)    
    ,'categorical':[categorical(create_random_number(0,1),['group_a','group_b','group_c']) for x in range(0,100)]
    ,'cat_2':[categorical(create_random_number(0,4),['group_1','group_2','group_3','group_4','group_5']) for x in range(0,100)]
    }
)
df = df.sort_values('cat_2', axis= 0)

st.write('Mi first app with stramlit : just ploting random samples')

st.table(df.head())

row2_spacer1, row2_spacer3 = st.columns(
    (.1, .1)
    )




with row2_spacer1:
    with st.echo(code_location='below'):
        
        import plotly.express as px
        fig = px.scatter(
            df,
            x="llave_1",
            y="llave_2",
            facet_col ='cat_2',
            color = 'categorical',
            trendline="ols",
        )
        fig.update_layout(height=300, width=600, title_text="Side By Side Subplots")
    # fig.update_layout(
    #     xaxis=dict(
    #         title="miles per galon"
    #     ),
    #     yaxis=dict(
    #         title="power",
    #     ),
    #     xaxis2=dict(
    #         title="miles per galon",
    #     )
    #)
with row2_spacer3:
    st.write(fig)
#print(df.head())