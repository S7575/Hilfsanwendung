import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

# Zahnnummern
teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

# Initialisieren Sie ein DataFrame mit Ausgangswerten
df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP']).fillna('')

# Legen Sie das DataFrame zurück
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Zähne'})

# Erstellen Sie das Grid
AgGrid(df, editable=True, height=600)
