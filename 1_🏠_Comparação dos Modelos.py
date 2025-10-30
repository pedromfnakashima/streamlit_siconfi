import streamlit as st
import pandas as pd
import json

st.set_page_config(
  layout = "wide",
  page_title = "Comparação dos Modelos"
)

# DEFINE LISTAS DE VALORES
li_contas = ["ICMS", "IPVA", "ITCD", "IRRF", "Cota-Parte do FPE", "Receita Corrente Líquida", "Receitas Correntes"]
li_contas_siglas = ["icms", "ipva", "itcd", "irrf", "cpfpe", "rcl", "rc"]
li_UFs = ["MS", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
li_UFs_extenso = ["Mato Grosso do Sul", "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]

str_uf = st.sidebar.selectbox("UF", li_UFs)
str_conta = st.sidebar.selectbox("CONTA", li_contas)
int_indiceConta = li_contas.index(str_conta)
int_indiceUf = li_UFs.index(str_uf)
str_contaSigla = li_contas_siglas[int_indiceConta]
str_ufExtenso = li_UFs_extenso[int_indiceUf]

st.markdown("# Dashboard de previsões de variáveis fiscais dos Estados")

st.markdown("## Comparação dos Modelos")

# INFORMAÇÕES DE SELEÇÃO
st.markdown("Seleção atual (painel à esquerda):")
st.markdown(f"✅ Estado: {str_ufExtenso}")
st.markdown(f"✅ Conta: {str_conta}")

# EXIBE O PERÍODO DO DATASET
strJson = f"./dados/Estados/{str_uf}_{str_contaSigla}_arima_previsoesForaSumario.json"
with open(strJson, 'r', encoding='utf-8') as file:
    dic_previsoesArimaForaSumario = json.load(file)
str_dataset = dic_previsoesArimaForaSumario.get("periodo_treinamento")
st.markdown(f"Dataset: {str_dataset}")


# EXIBE TABELA COMPARATIVA DAS PREVISÕES
st.markdown("### Tabela: Previsões dos modelos para 12 meses")
st.write("")
strCsv = f"./dados/Estados/{str_uf}_{str_contaSigla}_modelosPrevisoes.csv"
df_previsoes = pd.read_csv(strCsv, sep=',', encoding='utf-8', header=0, index_col=0)
df_previsoes = df_previsoes.rename(columns={
    'VP_HW': 'Holt-Winters',
    'VP_ARIMA': 'ARIMA',
    'VP_RN': 'Redes Neurais'
})
st.write(df_previsoes)

# PEGA AS SOMAS DE 12 MESES DAS PREVISÕES
## ARIMA
str_soma12mArima = dic_previsoesArimaForaSumario.get("prevs_soma")
## HOLT-WINTERS
strJson = f"./dados/Estados/{str_uf}_{str_contaSigla}_hw_previsoesForaSumario.json"
with open(strJson, 'r', encoding='utf-8') as file:
    dic_previsoesHWForaSumario = json.load(file)
str_soma12mHW = dic_previsoesHWForaSumario.get("prevs_soma")
## REDES NEURAIS
strJson = f"./dados/Estados/{str_uf}_{str_contaSigla}_rn_previsoesForaSumario.json"
with open(strJson, 'r', encoding='utf-8') as file:
    dic_previsoesRNForaSumario = json.load(file)
str_soma12mRN = dic_previsoesRNForaSumario.get("prevs_soma")

# EXIBBE AS SOMAS DE 12 MESES DAS PREVISÕES
st.markdown("#### Somas dos 12 meses de previsões para cada modelo")
st.markdown(f"- Holt-Winters: {str_soma12mHW}")
st.markdown(f"- ARIMA: {str_soma12mArima}")
st.markdown(f"- Redes Neurais: {str_soma12mRN}")

# EXIBE GRÁFICO COMPARATIVO COM OS VALORES DAS PREVISÕES
st.markdown("### Gráfico: Comparativo das previsões dos modelos **Holt-Winters**, **ARIMA** e **Redes Neurais**")
strPng = f"./dados/Estados/{str_uf}_{str_contaSigla}_previsoesComparacoes.png"
st.write("")
st.image(strPng)

# EXIBE TABELA COMPARATIVA DE DESEMPENHO DOS MODELOS
strCsv = f"./dados/Estados/{str_uf}_{str_contaSigla}_modelosMetricas.csv"
df_metricas = pd.read_csv(strCsv, sep=',', encoding='utf-8', header=0, index_col=0)
st.markdown("## Tabela: Comparativo de desempenho dos modelos **Holt-Winters**, **ARIMA** e **Redes Neurais**")
st.markdown(f"**Melhor modelo** (menor RMSE): {df_metricas.index[0]} (RMSE = {df_metricas.iloc[0,0]} reais)")
st.write("")
st.write(df_metricas)

st.sidebar.markdown("Desenvolvido por:")
st.sidebar.markdown("**Pedro Nakashima**")