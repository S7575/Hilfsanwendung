import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode

# Zahnnummern
teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

def app():
    # Initialisieren Sie ein DataFrame mit Ausgangswerten, falls es nicht existiert
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP']).fillna('')

        # Legen Sie das DataFrame zurück
        st.session_state.df.reset_index(inplace=True)
        st.session_state.df = st.session_state.df.rename(columns={'index': 'Zähne'})
        st.session_state.df = st.session_state.df.set_index('Zähne').transpose()

    # Optionen für das Dropdown-Menü
    dropdown_values = ['ww', 'x']

    # GridOptionen erstellen
    gb = GridOptionsBuilder.from_dataframe(st.session_state.df)
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=True)
    gb.configure_column("B", cellEditor='agSelectCellEditor', cellEditorParams={"values": dropdown_values})
    gridOptions = gb.build()

    # Erstellen Sie das Grid
    response = AgGrid(
        st.session_state.df, 
        gridOptions=gridOptions,
        height=600, 
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode='VALUE_CHANGED',
        editable=True,
    )

    # Aktualisieren Sie den DataFrame in der Sitzung mit den zurückgegebenen Daten
    st.session_state.df = response['data'].transpose()

    if st.button('Update Data'):
        for tooth in teeth_numbers:
            if st.session_state.df.loc['B', tooth] == 'ww':
                st.session_state.df.loc['R', tooth] = 'K'
                st.session_state.df.loc['TP', tooth] = 'V'
            elif st.session_state.df.loc['B', tooth] == 'x':
                st.session_state.df.loc['R', tooth] = 'E'
                st.session_state.df.loc['TP', tooth] = 'E'

        # Prüfen Sie, ob es Zähne mit dem Befund 'ww' gibt
        ww_teeth = [col for col, val in st.session_state.df.loc['B'].items() if val == 'ww']

        if ww_teeth:
            st.write(f'Für die Zähne {", ".join(map(str, ww_teeth))} wurde der Befund "ww" festgestellt. Befund 1.1 wird benötigt.')

        st.dataframe(st.session_state.df)

app()
