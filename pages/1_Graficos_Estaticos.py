import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from utils.data_processing import load_and_process_data

st.title("📉 Gráficos Estáticos")

# Carregamento de dados
csv_path = 'data/wine+quality/winequality-red.csv'
df = load_and_process_data(csv_path)

# 1. Histograma: pH Vs Frequência
st.subheader("Distribuição do pH dos Vinhos")
fig1, ax1 = plt.subplots(figsize=(6,3))
sns.histplot(df['pH'], bins=30, kde=True, ax=ax1, color='darkred')

ax1.set_xlabel('pH', fontsize=10)
ax1.set_ylabel('Frequência', fontsize=10)
ax1.tick_params(axis='both', labelsize=8)

st.pyplot(fig1)

# 2. Heatmap de correlação
st.subheader("Mapa de Calor das Correlaçõs")
fig2, ax2 = plt.subplots(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap='Reds', ax=ax2)
st.pyplot(fig2)

# 4. Gráfico de barras da média de álcool por qualidade
st.subheader("Média de Álcool por Qualidade do Vinho")

mean_alcohol = df.groupby('qualidade')['álcool'].mean().reset_index()

fig4, ax4 = plt.subplots(figsize=(6, 3))
sns.barplot(x='qualidade', y='álcool', data=mean_alcohol,
            palette='Reds', ax=ax4)
ax4.set_xlabel('Qualidade', fontsize=10)
ax4.set_ylabel('Álcool Médio', fontsize=10)
ax4.tick_params(axis='both', labelsize=8)

st.pyplot(fig4)

# 5. Gráfico de dispersão: Álcool Vs Densidade
st.subheader("Dispersão: Álcool Vs Densidade do Vinho")
fig5, ax5 = plt.subplots(figsize=(6, 3))
scatter = ax5.scatter(df['álcool'], df['densidade'], c=df['qualidade'],
                      cmap='Reds', alpha=0.7, edgecolors='w', s=50)
ax5.set_xlabel('Álcool', fontsize=10)
ax5.set_ylabel('Densidade', fontsize=10)
ax5.tick_params(axis='both', labelsize=8)
legend = ax5.legend(*scatter.legend_elements(), title="Qualidade", loc='upper right', fontsize=8)
ax5.add_artist(legend)

st.pyplot(fig5)