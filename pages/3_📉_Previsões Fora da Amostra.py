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
li_modelos = ["Holt-Winters", "ARIMA", "Redes Neurais"]
li_modelos_siglas = ["hw", "arima", "rn"]

str_uf = st.sidebar.selectbox("UF", li_UFs)
str_conta = st.sidebar.selectbox("CONTA", li_contas)
str_modelo = st.sidebar.selectbox("MODELO", li_modelos)
int_indiceConta = li_contas.index(str_conta)
int_indiceUf = li_UFs.index(str_uf)
int_indiceModelo = li_modelos.index(str_modelo)
str_contaSigla = li_contas_siglas[int_indiceConta]
str_ufExtenso = li_UFs_extenso[int_indiceUf]
str_modeloSigla = li_modelos_siglas[int_indiceModelo]

st.markdown("# Previsões Fora da Amostra")

# INFORMAÇÕES DE SELEÇÃO
st.markdown("Seleção atual (painel à esquerda):")
st.markdown(f"✅ **ESTADO**: {str_ufExtenso}")
st.markdown(f"✅ **CONTA**: {str_conta}")
st.markdown(f"✅ **MODELO**: {str_modelo}")

# INFORMAÇÕES GERAIS DO MODELO
strJson = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesForaSumario.json"
with open(strJson, 'r', encoding='utf-8') as file:
    dic_previsoesArimaForaSumario = json.load(file)
str_minimo = dic_previsoesArimaForaSumario.get("prevs_minimo")
str_maximo = dic_previsoesArimaForaSumario.get("prevs_maximo")
str_media = dic_previsoesArimaForaSumario.get("prevs_media")
str_mediana = dic_previsoesArimaForaSumario.get("prevs_mediana")
str_desvioPadrao = dic_previsoesArimaForaSumario.get("prevs_desvioPadrao")
str_soma = dic_previsoesArimaForaSumario.get("prevs_soma")
str_mediaUltimos12m = dic_previsoesArimaForaSumario.get("prevs_mediaUltimos12m")
str_somaUltimos12m = dic_previsoesArimaForaSumario.get("prevs_somaUltimos12m")
str_crescimentoPercentualPrevisto = dic_previsoesArimaForaSumario.get("prevs_crescimentoPercentualPrevisto")
str_periodoTreinamento = dic_previsoesArimaForaSumario.get("periodo_treinamento")
str_periodoPrevisoes = dic_previsoesArimaForaSumario.get("periodo_previsoes")

st.markdown("## 📝 Sumário")

st.markdown("### Períodos")
st.markdown(f"➤ **Período do Treinamento**: {str_periodoTreinamento}")
st.markdown(f"➤ **Período das Previsões (fora da amostra)**: {str_periodoPrevisoes}")

st.markdown("### Estatísticas das Previsões")
st.markdown(f"➤ **Mínimo**: {str_minimo}")
st.markdown(f"➤ **Máximo**: {str_maximo}")
st.markdown(f"➤ **Média**: {str_media}")
st.markdown(f"➤ **Mediana**: {str_mediana}")
st.markdown(f"➤ **Soma**: {str_soma}")
st.markdown(f"➤ **Desvio-padrão**: {str_desvioPadrao}")
st.markdown(f"➤ **Média dos 12 meses anteriores**: {str_mediaUltimos12m}")
st.markdown(f"➤ **Soma dos 12 meses anteriores**: {str_somaUltimos12m}")
st.markdown(f"➤ **Crescimento Percentual Previsto**: {str_crescimentoPercentualPrevisto}")

# TABELA DE PREVISÕES FORA DA AMOSTRA
st.markdown("## 📑 Tabela: Previsões Fora da Amostra")
strCsv = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesForaValores.csv"
df_previsoes = pd.read_csv(strCsv, sep=',', encoding='utf-8', header=0, index_col=0)
st.write(df_previsoes)

# GRÁFICO DE PREVISÕES FORA DA AMOSTRA
st.markdown("## 📈 Gráfico: Previsões Fora da Amostra")
strPng = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesFora.png"
st.image(strPng)




st.sidebar.markdown("Desenvolvido por:")
st.sidebar.markdown("**Pedro Nakashima**")