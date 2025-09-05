import pandas as pd
import plotly.express as px
import streamlit as st

# Dados
df = pd.DataFrame({
    "currentsubject": ["Arte", "Ciências", "Geografia", "História", "Humanas", "Inglês", "Linguagens", "Matemática", "Vida"],
    "botao_criar_plano_aula": [4699, 3150, 4802, 4699, 2, 2414, 11335, 5204, 0],
    "compartilhamento_direto": [5704, 4229, 6577, 10553, 77, 3086, 14199, 7781, 16],
    "download_aula": [57341, 38041, 52832, 60846, 770, 38608, 151647, 72200, 163],
    "outros": [23835, 24338, 30570, 44973, 26, 14556, 72492, 38917, 13],
    "visualizacao_aula": [137525, 102011, 149420, 138116, 956, 97037, 354021, 173844, 214],
    "visualizacao_conteudo_ia": [5427, 4807, 6522, 6212, 4, 3608, 15605, 7350, 0],
    "visualizacao_metodologia_ativa": [22148, 20601, 24675, 18982, 3, 19888, 61041, 27927, 0]
})

# Transformação para formato longo
df_long = df.melt(
    id_vars="currentsubject", 
    var_name="tipo_evento", 
    value_name="quantidade"
)

# ---- Streamlit UI ----
st.title("Quantidade de uso das funcionalidades por matéria")

# Filtro de matérias
materias_selecionadas = st.multiselect(
    "Selecione as matérias:",
    options=df["currentsubject"].unique(),
    default=df["currentsubject"].unique()
)

# Filtro de métricas
metricas_selecionadas = st.multiselect(
    "Selecione os tipos de evento:",
    options=df_long["tipo_evento"].unique(),
    default=df_long["tipo_evento"].unique()
)

# Aplicar filtros
df_filtrado = df_long[
    (df_long["currentsubject"].isin(materias_selecionadas)) &
    (df_long["tipo_evento"].isin(metricas_selecionadas))
]

# Criar gráfico
fig = px.bar(
    df_filtrado,
    x="currentsubject",
    y="quantidade",
    color="tipo_evento",
    barmode="group"
)

# Exibir gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)