import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

from utils.data_processing import load_and_process_data

st.title("📈 Gráficos Interativos")

# Carregamento de dados
csv_path = 'data/wine+quality/winequality-red.csv'
df = load_and_process_data(csv_path)

# 3. Gráfico de pizza interativo da qualidade do vinho
st.subheader("Distribuição da Qualidade do Vinho")
quality_counts = df['qualidade'].value_counts().reset_index()
quality_counts.columns = ['Qualidade', 'Contagem']

fig3 = px.pie(quality_counts, values='Contagem', names='Qualidade', 
              title='Distribuição da Qualidade do Vinho', 
              color_discrete_sequence=px.colors.sequential.Reds)
st.plotly_chart(fig3)

# 6. Gráfico interativo com Dropdown + Slider
st.subheader("Gráfico Interativo: Escolha os Eixos e Filtro de Qualidade")

# widgets
col1, col2 = st.columns(2)
with col1:
    eixo_x = st.selectbox("Eixo X", df.columns[:-1], index=0)
with col2:
    eixo_y = st.selectbox("Eixo Y", df.columns[:-1], index=1)

qualidade_range = st.slider('Filtrar por qualidade (mín. e máx.)',
    int(df['qualidade'].min()), int(df['qualidade'].max()),
    (int(df['qualidade'].min()), int(df['qualidade'].max())))

# Filtro
df_filtrado = df[(df['qualidade'] >= qualidade_range[0]) & (df['qualidade'] <= qualidade_range[1])]

# Plor
fig6, ax6 = plt.subplots(figsize=(6, 3))
ax6.scatter(df_filtrado[eixo_x], df_filtrado[eixo_y], alpha=0.6,
            c=df_filtrado['qualidade'], cmap='Reds', edgecolors='w', s=50)
ax6.set_xlabel(eixo_x, fontsize=10)
ax6.set_ylabel(eixo_y, fontsize=10)
ax6.tick_params(axis='both', labelsize=8)

st.pyplot(fig6)
