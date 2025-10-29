import streamlit as st
from pathlib import Path
import socket
import pandas as pd
import json

st.set_page_config(
  layout = "wide",
  page_title = "Comparação dos Modelos"
)

nome_do_computador = socket.gethostname()

if nome_do_computador == "pedromfn-Ubuntu-Predator":
  GD_dados = Path("/home/pedromfn/Nuvens/GoogleDrive/05-Codigos-Dados-Documentacoes-CheatSheets/Dados")
elif nome_do_computador == "pedromfn-Windows-Predator":
  GD_dados = Path(r"C:\01-MeusArquivos\01-Nuvens\GoogleDrive\05-Codigos-Dados-Documentacoes-CheatSheets\Dados")
elif nome_do_computador == "pedromfn-Ubuntu-desktop":
  GD_dados = Path("/mnt/SSD_2TB_SATA/Nuvens/GoogleDrive")
  pth_wd = Path("/opt/notebooks/projetos/books-llm-opensource/Outros/docx")

pth_pasta_dados = GD_dados / "Siconfi-Dados-Dashboard/" / "Estados"

# DEFINE LISTAS DE VALORES
li_contas = ["ICMS", "IPVA", "ITCD", "IRRF", "Cota-Parte do FPE", "Receita Corrente Líquida", "Receitas Correntes"]
li_contas_siglas = ["icms", "ipva", "itcd", "irrf", "cpfpe", "rcl", "rc"]
li_UFs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
li_UFs_extenso = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]

str_uf = st.sidebar.selectbox("UF", li_UFs)
str_conta = st.sidebar.selectbox("CONTA", li_contas)
int_indiceConta = li_contas.index(str_conta)
int_indiceUf = li_UFs.index(str_uf)
str_contaSigla = li_contas_siglas[int_indiceConta]
str_ufExtenso = li_UFs_extenso[int_indiceUf]


st.markdown("# Visão Geral dos Modelos")

st.markdown("Seleção:")
st.markdown(f"- Estado: {str_ufExtenso}")
st.markdown(f"- Conta: {str_conta}")

# EXIBE O PERÍODO DO DATASET
pth_previsoesArimaForaSumario = pth_pasta_dados / f"{str_uf}_{str_contaSigla}_arima_previsoesForaSumario.json"
with open(pth_previsoesArimaForaSumario, 'r', encoding='utf-8') as file:
    dic_previsoesArimaForaSumario = json.load(file)
str_dataset = dic_previsoesArimaForaSumario.get("periodo_treinamento")
st.markdown(f"Dataset: {str_dataset}")

# EXIBE TABELA COMPARATIVA DAS PREVISÕES
st.markdown("## Tabela: Previsões dos modelos para 12 meses")
st.write("")
df_previsoes = pd.read_csv(pth_pasta_dados / f'{str_uf}_{str_contaSigla}_modelosPrevisoes.csv', sep=',', encoding='utf-8', header=0, index_col=0)
df_previsoes = df_previsoes.rename(columns={
    'VP_HW': 'Holt-Winters',
    'VP_ARIMA': 'ARIMA',
    'VP_RN': 'Redes Neurais'
})
st.write(df_previsoes)

# PEGA AS SOMAS DE 12 MESES DAS PREVISÕES
## ARIMA
str_soma12mArima = dic_previsoesArimaForaSumario.get("prevs_somaProx12meses")
## HOLT-WINTERS
pth_previsoesHWForaSumario = pth_pasta_dados / f"{str_uf}_{str_contaSigla}_hw_previsoesForaSumario.json"
with open(pth_previsoesHWForaSumario, 'r', encoding='utf-8') as file:
    dic_previsoesHWForaSumario = json.load(file)
str_soma12mHW = dic_previsoesHWForaSumario.get("prevs_somaProx12meses")
## REDES NEURAIS
pth_previsoesRNForaSumario = pth_pasta_dados / f"{str_uf}_{str_contaSigla}_rn_previsoesForaSumario.json"
with open(pth_previsoesRNForaSumario, 'r', encoding='utf-8') as file:
    dic_previsoesRNForaSumario = json.load(file)
str_soma12mRN = dic_previsoesRNForaSumario.get("prevs_somaProx12meses")

# EXIBBE AS SOMAS DE 12 MESES DAS PREVISÕES
st.markdown("Somas dos 12 meses de previsões:")
st.markdown(f"- Holt-Winters: {str_soma12mHW}")
st.markdown(f"- ARIMA: {str_soma12mArima}")
st.markdown(f"- Redes Neurais: {str_soma12mRN}")

# EXIBE GRÁFICO COMPARATIVO COM OS VALORES DAS PREVISÕES
st.markdown("## Gráfico: Comparativo das previsões dos modelos **Holt-Winters**, **ARIMA** e **Redes Neurais**.")
pth_previsoesComparacoesPng = pth_pasta_dados / f"{str_uf}_{str_contaSigla}_previsoesComparacoes.png"
st.write("")
st.image(pth_previsoesComparacoesPng)

# EXIBE TABELA COMPARATIVA DE DESEMPENHO DOS MODELOS
df_metricas = pd.read_csv(pth_pasta_dados / f'{str_uf}_{str_contaSigla}_modelosMetricas.csv', sep=',', encoding='utf-8', header=0, index_col=0)
st.markdown("## Tabela: Comparativo de desempenho dos modelos **Holt-Winters**, **ARIMA** e **Redes Neurais**.")
st.markdown(f"**Melhor modelo** (menor RMSE): {df_metricas.index[2]} (RMSE = {df_metricas.iloc[2,0]} reais)")
st.write("")
st.write(df_metricas)

st.sidebar.write("Desenvolvido por Pedro Nakashima")