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


st.markdown("# Previsões Dentro da Amostra")

st.markdown("Seleção:")
st.markdown(f"- Estado: {str_ufExtenso}")
st.markdown(f"- Conta: {str_conta}")


st.sidebar.write("Desenvolvido por Pedro Nakashima")
