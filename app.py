import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

# Definieren der Tabellen
data_1 = pd.DataFrame({'Zähne': [11,12,13,14,15,16,17,18], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})
data_2 = pd.DataFrame({'Zähne': [21,22,23,24,25,26,27,28], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})
data_3 = pd.DataFrame({'Zähne': [31,32,33,34,35,36,37,38], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})
data_4 = pd.DataFrame({'Zähne': [41,42,43,44,45,46,47,48], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})

datasets = [data_1, data_2, data_3, data_4]

# Dropdown Optionen
b_options = ['ww', 'x', 'a', 'ab', 'abw', 'aw', 'b', 'bw', 'e', 'ew', 'f', 'ix', 'k', 'kw', 'pkw', 'pw', 'r', 'rW', 'sb', 'sbw', 'se', 'sew', 'sk', 'skw', 'so', 'sow', 'st', 'stw', 't', 't2w', 'tw', 'ur', ')(']
tp_options = ["A", "ABV", "ABM", "B", "BM", "BV", "E", "EO", "H", "K", "KH", "KM", "KMH"]

# Erzeugen der Check-Kästchen
checkboxes = [
    st.checkbox('1. Quadrat einblenden'),
    st.checkbox('2. Quadrat einblenden'),
    st.checkbox('3. Quadrat einblenden'),
    st.checkbox('4. Quadrat einblenden'),
]

def build_grid(data, options, tp_options):
    # Konfigurieren der Spalten
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_column("B", cellEditor="agSelectCellEditor", cellEditorParams={"values": options}, editable=True)
    gb.configure_column("TP", cellEditor="agSelectCellEditor", cellEditorParams={"values": tp_options}, editable=True)
    gb.configure_grid_options(domLayout='autoHeight')
    gridOptions = gb.build()

    # Ag-Grid anzeigen
    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        height=200,
        width='100%',
        data_return_mode='as_input',  # Updates werden beim Editieren automatisch in den Dataframe übernommen
        fit_columns_on_grid_load=True,
        allow_unsafe_jscode=True,     # Erlaubt das Ausführen von Javascript Code
    )
    
    # Aktualisieren der R-Spalte, wenn die B-Spalte geändert wird
    for index, row in grid_response['data'].iterrows():
        if row['B'] == 'ww':
            if 15 <= row['Zähne'] <= 25 or 34 <= row['Zähne'] <= 44:
                grid_response['data'].loc[index, 'R'] = 'KV'
            elif 16 <= row['Zähne'] <= 18 or 26 <= row['Zähne'] <= 28 or 35 <= row['Zähne'] <= 38 or 45 <= row['Zähne'] <= 48:
                grid_response['data'].loc[index, 'R'] = 'K'
        elif row['B'] == 'x':
            grid_response['data'].loc[index, 'R'] = 'E'
                
    return grid_response['data']

# Anzeigen der Tabellen, wenn die Kästchen ausgewählt sind
for checkbox, data in zip(checkboxes, datasets):
    if checkbox:
        data = build_grid(data, b_options, tp_options)
        AgGrid(data)  # Tabelle neu anzeigen
