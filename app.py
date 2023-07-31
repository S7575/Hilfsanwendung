import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode

# Zahnnummern
teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

# Initialisieren Sie ein DataFrame mit Ausgangswerten
df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP']).fillna('')

# Legen Sie das DataFrame zurück
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Zähne'})

# Optionen für das Dropdown-Menü
dropdown_values = ['ww', 'x']

# GridOptionen erstellen
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=True)
gb.configure_column("B", cellEditor='agSelectCellEditor', cellEditorParams={"values": dropdown_values}, onCellValueChanged="""
function(params) {
    if(params.newValue == 'ww') {
        params.node.setDataValue('R', 'K');
        params.node.setDataValue('TP', 'V');
    }
    if(params.newValue == 'x') {
        params.node.setDataValue('R', 'E');
        params.node.setDataValue('TP', 'E');
    }
}
""")
gridOptions = gb.build()

# Erstellen Sie das Grid
response = AgGrid(
    df, 
    gridOptions=gridOptions,
    height=600, 
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    update_mode='VALUE_CHANGED',
    editable=True,
)

# Der aktualisierte DataFrame wird in response['data'] gespeichert.
df = response['data']
