import streamlit as st
import pandas as pd 
from io import StringIO
import matplotlib.pyplot as plt 
st.header('IRIS FLOWER DASHBOARD')
st.divider()
with st.sidebar:
     st.subheader("Description")
     st.text_area(
        ("Iris flowers have an unusual structure and appearance. The petals resemble a classic fleur-de-lis symbol, with some petals rising up while others cascade down. The center petals stand upright and are known botanically as standards. These tall petals stand like signal flags, waving in potential pollinators.")
    )
df=pd.read_csv("iris.csv")
col1,col2=st.columns(2)
with col1:
     st.subheader("Piechart of species")
     fig1,ax1=plt.subplots()

     ax1.pie(x=df['Species'].value_counts().values,
        lables=df['Species'].value_counts().index,autopct="%0.2f%%")
     st.pyplot(fig=fig1)

