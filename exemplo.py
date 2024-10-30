import pandas as pd
import seaborn as sns
from sklearn import datasets
import streamlit as st

df = sns.load_dataset('iris')

st.title('analise de dados iris')
st.write(df.head())

st.subheader('estatisticas descritivas')
st.write(df.describe())

st.subheader('gráfico de dispersão')
st.write('vizualizações das caracteristicas de especie do iris')
scatter_plot =sns.scatterplot(data=df, x='sepal_lenght', y='sepal_widht', hue='species')
st.pyplot(scatter_plot.figure)

st.subheader('distribuição de comprimento das pétalas')
st.write('distribuição do comprimento das pétalas para as tres especies')
hist_plot = sns.scatterplot(data=df,x='petal_lenght',hue='species',multiple='stack')
st.pyplot(hist_plot.figure)
