import streamlit as st
from PIL import Image

st.set_page_config(page_title="Gráficos Interativos", layout="wide")

st.title("🍷 Bem-vindo ao Dashboard de Qualidade de Vinho")
st.markdown("""
    Este dashboard explora os dados do conjunto **Wine Quality (vermelho)** da UCI.
    Use o menu lateral para navegar pelas páginas com gráficos interativos e estáticos.
""")

# Carregar a imagem local
imagem = Image.open('assets/Port_wine.jpg')
# Exibir a imagem
st.image(imagem, use_container_width=True)
