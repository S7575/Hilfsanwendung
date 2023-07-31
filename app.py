import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder

# Zahnnummern
teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

# Initialisieren Sie ein leeres DataFrame
df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP'])

# Legen Sie das DataFrame zurück
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Zähne'})

# Konfigurieren Sie das Gitter
gb = GridOptionsBuilder()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=True)
gridOptions = gb.build()

# Erstellen Sie das Grid
response = AgGrid(df, gridOptions=gridOptions, editable=True, height=600)

# Der aktualisierte DataFrame wird in response['data'] gespeichert.
df = response['data']
