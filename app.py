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

    # Optionen für das Dropdown-Menü
    dropdown_values = ['ww', 'x']

    # GridOptionen erstellen
    gb = GridOptionsBuilder.from_dataframe(st.session_state.df)
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=True)
    gb.configure_column("B", cellEditor='agSelectCellEditor', cellEditorParams={"values": dropdown_values})
    gridOptions = gb.build()

    # Erstellen Sie einen Platzhalter für das Grid
    grid_placeholder = st.empty()

    # Füllen Sie den Platzhalter mit dem Grid
    response = AgGrid(
        st.session_state.df, 
        gridOptions=gridOptions,
        height=600, 
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode='VALUE_CHANGED',
        editable=True,
        key='grid1'
    )

    # Aktualisieren Sie den DataFrame in der Sitzung mit den zurückgegebenen Daten
    st.session_state.df = response['data']

    if st.button('Update Data'):
        st.session_state.df.loc[st.session_state.df['B'] == 'ww', ['R', 'TP']] = 'K', 'V'
        st.session_state.df.loc[st.session_state.df['B'] == 'x', ['R', 'TP']] = 'E', 'E'

        # Prüfen Sie, ob es Zähne mit dem Befund 'ww' gibt
        ww_teeth = st.session_state.df[st.session_state.df['B'] == 'ww']
        
        if not ww_teeth.empty:
            st.write(f'Für die Zähne {", ".join(map(str, ww_teeth["Zähne"].tolist()))} wurde der Befund "ww" festgestellt. Befund 1.1 wird benötigt.')

        # Umstrukturierung des DataFrames
        df_pivot = st.session_state.df.pivot_table(index=['B', 'R', 'TP'], columns='Zähne', aggfunc='first')
        df_pivot.reset_index(inplace=True)
        st.session_state.df = df_pivot.rename_axis(None, axis=1)

        # Ersetzen Sie das Grid mit dem aktualisierten DataFrame
        grid_placeholder.empty()
        AgGrid(st.session_state.df, gridOptions=gridOptions, key='grid2')

app()
