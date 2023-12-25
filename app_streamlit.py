import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
df = pd.read_csv('bank_data.csv')
column = st.sidebar.multiselect('Выберите переменную', df.columns.values.tolist())
import plotly.figure_factory as ff
import numpy as np

df_corr = df.corr()

x = list(df_corr.columns)
y = list(df_corr.index)
z = np.array(df_corr)

hist = px.histogram(df[column])
st.plotly_chart(hist)
st.text("Median: "+str(df[column].median()))
st.text("Mean: "+str(df[column].mean()))
st.text("Max: "+str(df[column].max()))
st.text("Min: "+str(df[column].min()))
if st.button('Построить зависимость от выбранной переменной ') and column is not None:
    fig = px.line(pd.concat((df['TARGET'], df[column]), axis =1), title='Зависимость Target от выбранной переменной')

    st.plotly_chart(fig)
if (st.button('Построить корреляционную матрицу')):
    fig1 = ff.create_annotated_heatmap(
       z,
     x = x,
     y = y ,
     annotation_text = np.around(z, decimals=2),
      hoverinfo='z',
      colorscale='Viridis'
    )

    st.plotly_chart(fig1)

#%%

#%%
