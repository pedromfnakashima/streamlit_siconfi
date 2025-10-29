import streamlit as st
from pathlib import Path
import socket
import pandas as pd
import json

st.set_page_config(
  layout = "wide",
  page_title = "Comparação dos Modelos"
)

st.sidebar.write("Desenvolvido por Pedro Nakashima")