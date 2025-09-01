import streamlit as st
import pandas as pd
import plotly.express as px

# Criar o dataframe
df = pd.DataFrame({
    "Materia": ["Arte","Ciências","Geografia","História","Humanas",
                "Inglês","Linguagens","Matemática","Vida"],
    "Ativos":  [4433, 3356, 4458, 4223, 38, 3133, 11930, 6311, 13],
    "Inativos":[13561, 9442, 13626, 13112, 200, 6681, 39542, 17989, 37]
})

st.title("Ativos e Inativos por Matéria")

# Sidebar - seleção de matérias
materias = st.sidebar.multiselect(
    "Selecione as matérias:",
    options=df["Materia"].tolist(),
    default=df["Materia"].tolist()
)

# Sidebar - escolha do status
status = st.sidebar.radio(
    "O que exibir?",
    options=["ambos", "ativos", "inativos"],
    format_func=lambda x: {
        "ambos": "Ativos e Inativos",
        "ativos": "Apenas Ativos",
        "inativos": "Apenas Inativos"
    }[x]
)

# Filtrar matérias selecionadas
sel = df[df["Materia"].isin(materias)]

# Transformar dados para formato "longo" (como no R)
long = pd.melt(sel, id_vars=["Materia"], 
               value_vars=["Ativos", "Inativos"], 
               var_name="Status", value_name="Quantidade")

# Filtrar status
if status == "ativos":
    long = long[long["Status"] == "Ativos"]
elif status == "inativos":
    long = long[long["Status"] == "Inativos"]

# Gráfico com Plotly
if long.empty:
    st.warning("Nenhum dado para exibir. Selecione pelo menos uma opção.")
else:
    fig = px.bar(
        long,
        x="Materia",
        y="Quantidade",
        color="Status",
        barmode="group" if status == "ambos" else "stack",
        color_discrete_map={"Ativos": "green", "Inativos": "red"}
    )
    fig.update_layout(
        title="Ativos e Inativos por Matéria",
        xaxis_title="Matéria",
        yaxis_title="Quantidade",
        xaxis_tickangle=25
    )
    st.plotly_chart(fig, use_container_width=True)