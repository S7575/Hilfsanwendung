import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode

# Globale Variable zur Speicherung des DataFrames zwischen den Streamlit Aufrufen
global_df = None

def app():
    global global_df

    # Zahnnummern
    teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

    # Initialisieren Sie ein DataFrame mit Ausgangswerten, falls es nicht existiert
    if global_df is None:
        global_df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP']).fillna('')

        # Legen Sie das DataFrame zurück
        global_df.reset_index(inplace=True)
        global_df = global_df.rename(columns={'index': 'Zähne'})

    # Optionen für das Dropdown-Menü
    dropdown_values = ['ww', 'x']

    # GridOptionen erstellen
    gb = GridOptionsBuilder.from_dataframe(global_df)
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=True)
    gb.configure_column("B", cellEditor='agSelectCellEditor', cellEditorParams={"values": dropdown_values})
    gridOptions = gb.build()

    # Erstellen Sie das Grid
    AgGrid(
        global_df, 
        gridOptions=gridOptions,
        height=600, 
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode='VALUE_CHANGED',
        editable=True,
    )

    if st.button('Update Data'):
        global_df.loc[global_df['B'] == 'ww', ['R', 'TP']] = 'K', 'V'
        global_df.loc[global_df['B'] == 'x', ['R', 'TP']] = 'E', 'E'

        # Prüfen Sie, ob es Zähne mit dem Befund 'ww' gibt
        ww_teeth = global_df[global_df['B'] == 'ww']
        
        if not ww_teeth.empty:
            st.write(f'Für die Zähne {", ".join(map(str, ww_teeth["Zähne"].tolist()))} wurde der Befund "ww" festgestellt. Befund 1.1 wird benötigt.')

        st.dataframe(global_df)

app()
