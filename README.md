# Wine_Quality_Streamlit
![3b771c5b58ad19d893f042e8b38de934e0b75e6d62a5df9c1d15bb35](https://github.com/user-attachments/assets/a45f24c4-42f0-4ff2-9bdb-f8296999b5f2)
# 🍷 Dashboard de Qualidade de Vinho

Exploração interativa com Streamlit  
*Autor:* [Nícolas Pastorio de Moura e Tainara Schenkel]  
*Data:* [01/07/2025]

---

## 🎯 Objetivo do Projeto

Criar um dashboard interativo com *Streamlit* que:

- Visualize dados de qualidade de vinho tinto
- Facilite a análise de padrões, correlações e insights
- Utilize filtros e componentes interativos

---

## 🧪 Fonte dos Dados

*Dataset:* [Wine Quality Data Set (UCI)](https://archive.ics.uci.edu/dataset/186/wine+quality)

*Utilizado:* winequality-red.csv  
*Amostras:* 1599  
*Variáveis:*
- 11 físico-químicas (pH, álcool, etc.)
- 1 alvo: qualidade (nota de 0 a 10)

---

## 🧩 Funcionalidades Gerais

- Múltiplas páginas com Streamlit
- Dados carregados e tratados com Pandas
- Gráficos estáticos (matplotlib / seaborn)
- Gráficos interativos (Plotly, widgets)
- Layout limpo e responsivo

---

## 🏠 Página Inicial

- Título e boas-vindas
- Banner ilustrativo (imagem da pasta assets/)
- Navegação lateral para outras páginas

---

## 📊 Página 1: Gráficos Estáticos

1. *Histograma de pH*  
   Frequência e distribuição dos níveis de acidez

2. *Mapa de Calor (heatmap)*  
   Correlações entre todas as variáveis

3. *Gráfico de Barras*  
   Média de álcool por nota de qualidade

4. *Gráfico de Dispersão*  
   Álcool vs Densidade colorido por qualidade

---

## 📈 Página 2: Gráficos Interativos

- *Pizza com Plotly:*  
  Distribuição percentual das notas

- *Gráfico com Widgets:*  
  Sliders para faixa de qualidade  
  Dropdowns para seleção dos eixos X e Y  
  → Permite análise dinâmica das variáveis

---

## ⚙ Processamento dos Dados

- Leitura e tratamento com Pandas
- Renomeação e tradução das colunas
- Conversão de tipos
- Lógica modularizada (data_processing.py)

---

## 💡 Benefícios do Dashboard

- Exploração intuitiva dos dados
- Fácil identificação de padrões
- Ferramenta prática para análise ou ensino
- Pronto para ser hospedado ou expandido

---

## 🚀 Execução do Projeto

*Local:*

```bash
streamlit run App.py
