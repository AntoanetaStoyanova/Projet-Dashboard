import streamlit as st
import plotly.express as px
import pandas as pd
import xlrd  
import csv 
import os
import warnings 
warnings.filterwarnings('ignore')



st.set_page_config(page_title="Superstore", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Sample Superstore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;</style>',unsafe_allow_html=True)

#upload a file
fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    # Si le fichier est un fichier XLS, le convertir en fichier CSV
    if filename.endswith('.xls'):
        # Charge le fichier XLS dans un DataFrame
        xls_df = pd.read_excel(fl)
        # Crée le chemin complet pour le dossier de destination
        destination_folder = os.path.join("upload")
        # Crée le dossier de destination s'il n'existe pas déjà
        os.makedirs(destination_folder, exist_ok=True)
        # Chemin complet pour le fichier CSV de destination
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        destination_path = os.path.join(destination_folder, csv_filename)
        # Sauvegarde le DataFrame au format CSV
        xls_df.to_csv(destination_path, index=False)
        # Lit le fichier CSV à partir du dossier de destination avec Pandas
        df = pd.read_csv(destination_path, encoding="ISO-8859-1")

    else:
        # Si le fichier n'est pas un fichier XLS, écrire le fichier dans le dossier de destination tel quel
        destination_folder = os.path.join("upload")
        # Crée le dossier de destination s'il n'existe pas déjà
        os.makedirs(destination_folder, exist_ok=True)
        # Chemin complet du fichier de destination
        destination_path = os.path.join(destination_folder, filename)
        # Écrit le fichier téléchargé dans le dossier de destination
        with open(destination_path, "wb") as f:
            f.write(fl.getvalue())
        # Lit le fichier téléchargé à partir du dossier de destination avec Pandas
        df = pd.read_csv(destination_path, encoding="ISO-8859-1")








   