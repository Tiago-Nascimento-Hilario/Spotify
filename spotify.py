import streamlit as st
import pandas as pd

st.set_page_config( layout="wide", page_title="Spotify")
df = pd.read_csv("spotify.csv")

df.set_index("Track", inplace=True)

artistas = df["Artist"].value_counts().index
artista = st.sidebar.selectbox("Selecione um artista", artistas)
df_filtro = df[df["Artist"] == artista]



albuns = df_filtro["Album"].value_counts().index
album = st.sidebar.selectbox("Album", albuns)

df_filtro2 = df[df["Album"] == album]

display = st.checkbox('Display')
if display:
    st.bar_chart(df_filtro2["Stream"])

df
