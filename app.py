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
gb.set_default_editable(True)  # Stellen Sie dies auf 'True' um alle Zellen bearbeitbar zu machen
gb.set_column_def("B", editable=True)  # Dies ermöglicht die Bearbeitung speziell für die Spalte 'B'
gridOptions = gb.build()

# Erstellen Sie das Grid
response = AgGrid(df, gridOptions=gridOptions)

# Der aktualisierte DataFrame wird in response['data'] gespeichert.
df = response['data']

