import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Dados
df = pd.DataFrame({
    "currentsubject": [
        "Arte","Ciências","Geografia","História","Humanas",
        "Inglês","Linguagens","Matemática","Vida"
    ],
    "media_de_interacoes": [
        20.029575,20.738010,21.297502,23.205304,8.509259,
        23.744137,19.625570,18.541231,8.638298
    ],
    "media_tempo_sessao": [
        217.281139,218.869744,199.992550,219.731461,262.852065,
        233.367861,198.134755,209.082218,323.706976
    ]
})
# ---- Streamlit UI ----
st.title("ScatterPlot - Análise de Interações por Matéria")

# Filtro de matérias
materias_selecionadas = st.multiselect(
    "Selecione as matérias:",
    options=df["currentsubject"].unique(),
    default=df["currentsubject"].unique()
)

# Aplicar filtros
df_filtrado = df[
    (df["currentsubject"].isin(materias_selecionadas))
]

# Criar gráfico

fig = px.scatter(
    df_filtrado,
    x="media_de_interacoes",
    y="media_tempo_sessao",
    color="currentsubject",
    opacity=0.9
)

# Exibir gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)