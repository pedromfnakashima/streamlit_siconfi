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
li_UFs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
li_UFs_extenso = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]
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
str_somaProx12meses = dic_previsoesArimaForaSumario.get("prevs_somaProx12meses")
str_mediaUltimos12m = dic_previsoesArimaForaSumario.get("prevs_mediaUltimos12m")


st.markdown("## 📝 Sumário")
st.markdown(f"➤ **Mínimo**: {str_minimo}")
st.markdown(f"➤ **Máximo**: {str_maximo}")
st.markdown(f"➤ **Média**: {str_media}")
st.markdown(f"➤ **Mediana**: {str_mediana}")
st.markdown(f"➤ **Desvio-padrão**: {str_desvioPadrao}")
st.markdown(f"➤ **Soma das previsões**: {str_somaProx12meses}")
st.markdown(f"➤ **Média dos últimos 12 meses**: {str_mediaUltimos12m}")








st.sidebar.markdown("Desenvolvido por:")
st.sidebar.markdown("**Pedro Nakashima**")