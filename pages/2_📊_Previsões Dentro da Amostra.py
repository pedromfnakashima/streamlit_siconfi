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


st.markdown("# Previsões Dentro da Amostra")

# INFORMAÇÕES DE SELEÇÃO
st.markdown("Seleção atual (painel à esquerda):")
st.markdown(f"✅ **ESTADO**: {str_ufExtenso}")
st.markdown(f"✅ **CONTA**: {str_conta}")
st.markdown(f"✅ **MODELO**: {str_modelo}")

# INFORMAÇÕES GERAIS DO MODELO
strJson = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesDentroSumario.json"
with open(strJson, 'r', encoding='utf-8') as file:
    dic_previsoesArimaForaSumario = json.load(file)
str_periodoDeTreinamento = dic_previsoesArimaForaSumario.get("periodo_de_treinamento")
str_periodoDeTeste = dic_previsoesArimaForaSumario.get("periodo_de_teste")
str_erroAbsolutoMedio = dic_previsoesArimaForaSumario.get("erro_absoluto_medio")
str_erroAbsolutoMaximo = dic_previsoesArimaForaSumario.get("erro_absoluto_maximo")
str_erroAbsolutoMinimo = dic_previsoesArimaForaSumario.get("erro_absoluto_minimo")
str_erroPercentualMedio = dic_previsoesArimaForaSumario.get("erro_percentual_medio")
str_erroPercentualMaximo = dic_previsoesArimaForaSumario.get("erro_percentual_maximo")
str_erroPercentualMinimo = dic_previsoesArimaForaSumario.get("erro_percentual_minimo")

st.markdown("## 📝 Sumário")

st.markdown("### Períodos")
st.markdown(f"➤ **Período do treinamento**: {str_periodoDeTreinamento}")
st.markdown(f"➤ **Período das Previsões (dentro da amostra)**: {str_periodoDeTeste}")

st.markdown("### Estatísticas das Previsões")
st.markdown(f"➤ **Erro Absoluto Médio**: {str_erroAbsolutoMedio}")
st.markdown(f"➤ **Erro Absoluto Máximo**: {str_erroAbsolutoMaximo}")
st.markdown(f"➤ **Erro Absoluto Mínimo**: {str_erroAbsolutoMinimo}")
st.markdown(f"➤ **Erro Percentual Médio**: {str_erroPercentualMedio}")
st.markdown(f"➤ **Erro Percentual Máximo**: {str_erroPercentualMaximo}")
st.markdown(f"➤ **Erro Percentual Mínimo**: {str_erroPercentualMinimo}")

# MÉTRICAS DE DESEMPENHO DO MODELO
st.markdown("## 📝 Métricas de Desempenho do Modelo")
strCsv = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesDentroMetricas.csv"
df_metricas = pd.read_csv(strCsv, sep=',', encoding='utf-8', header=0, index_col=0)
df_metricas_selecao = df_metricas[["Valor_formatado"]]
df_metricas_selecao = df_metricas_selecao.rename(columns={"Valor_formatado": "Valor"})
st.write(df_metricas_selecao)

# TABELA DE PREVISÕES DENTRO DA AMOSTRA
st.markdown("## 📑 Tabela: Previsões Dentro da Amostra")
strCsv = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesDentroValores.csv"
df_previsoes = pd.read_csv(strCsv, sep=',', encoding='utf-8', header=0, index_col=0)
st.write(df_previsoes)

# GRÁFICO DE PREVISÕES DENTRO DA AMOSTRA
st.markdown("## 📈 Gráfico: Previsões Dentro da Amostra")
strPng = f"./dados/Estados/{str_uf}_{str_contaSigla}_{str_modeloSigla}_previsoesDentro.png"
st.image(strPng)

st.sidebar.markdown("Desenvolvido por:")
st.sidebar.markdown("**Pedro Nakashima**")
