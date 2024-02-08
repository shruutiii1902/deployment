import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mt
import matplotlib.pyplot as plt
df=pd.read_csv("Iris.csv")
st.header(" IRIS FLOWER DASHBOARD ")
st.divider()
with st.sidebar:
    st.subheader("DISCRIPTION")
    st.write("The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species.")
col1, col2 = st.columns(2)
with col1:
   st.subheader("PIE CHART OF SPECIES")
   x=df['variety'].value_counts()
   fig1,ax1=plt.subplots()
   ax1.pie(x,labels=x.index)
   st.pyplot(fig1)

with col2:
   st.subheader("BAR CHART OF SPECIES")
   fig2,ax2=plt.subplots()
   y=['Iris-setosa','Iris-versicolor','Iris-virginica']
   ax2.bar(y,x)
   st.pyplot(fig2)

st.subheader("LINE CHART")

st.line_chart(df[['sepal.length','sepal.width','petal.length','petal.width']])
col3, col4 = st.columns(2)
with col3:
   st.scatter_chart(df[['sepal.length','sepal.width']])


with col4:
   st.scatter_chart(df[['petal.length','petal.width']])
