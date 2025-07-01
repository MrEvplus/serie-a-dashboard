import streamlit as st
import pandas as pd
import os

# -------------------------------
# Costanti
# -------------------------------
DATA_FOLDER = "data"
DATA_FILE = "serie a 20-25.xlsx"
DATA_PATH = os.path.join(DATA_FOLDER, DATA_FILE)

st.set_page_config(page_title="Serie A Trading Dashboard", layout="wide")

# -------------------------------
# Sezione Upload file
# -------------------------------
st.title("Serie A Trading Dashboard")

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

uploaded_file = st.file_uploader("Carica il tuo database Excel:", type=["xlsx"])

if uploaded_file is not None:
    # sovrascrive il file esistente
    with open(DATA_PATH, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Database caricato e salvato con successo!")

# -------------------------------
# Caricamento automatico file esistente
# -------------------------------
if os.path.exists(DATA_PATH):
    df = pd.read_excel(DATA_PATH, sheet_name=None)
    df = list(df.values())[0]
    st.success("✅ Database trovato e caricato automaticamente.")
    
    st.write("✅ Ecco un’anteprima del tuo file Excel:")
    st.dataframe(df.head())
else:
    st.warning("⚠️ Nessun database presente. Carica il file Excel per iniziare.")
    st.stop()
