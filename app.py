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
    
    return grid_response['data']

# Wenn der Session State noch nicht initialisiert wurde
if "datasets" not in st.session_state:
    st.session_state["datasets"] = datasets

# Anzeigen der Tabellen, wenn die Kästchen ausgewählt sind
for i in range(4):
    if checkboxes[i]:
        st.session_state.datasets[i] = build_grid(st.session_state.datasets[i], b_options, tp_options)

if st.button('Befund aktualisieren'):
    for i in range(4):
        if checkboxes[i]:
            data = st.session_state.datasets[i]
            for index, row in data.iterrows():
                if row['B'] == 'ww':
                    if 15 <= row['Zähne'] <= 25 or 34 <= row['Zähne'] <= 44:
                        data.loc[index, 'R'] = 'KV'
                    elif 16 <= row['Zähne'] <= 18 or 26 <= row['Zähne'] <= 28 or 35 <= row['Zähne'] <= 38 or 45 <= row['Zähne'] <= 48:
                        data.loc[index, 'R'] = 'K'
                elif row['B'] == 'x':
                    data.loc[index, 'R'] = 'E'
            st.session_state.datasets[i] = data  # Speichern der aktualisierten Daten
            AgGrid(st.session_state.datasets[i])  # Tabelle neu anzeigen
