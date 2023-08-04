import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Definieren der Tabellen
data_1 = pd.DataFrame({'Zähne': [11,12,13,14,15,16,17,18], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})
data_2 = pd.DataFrame({'Zähne': [21,22,23,24,25,26,27,28], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})
data_3 = pd.DataFrame({'Zähne': [31,32,33,34,35,36,37,38], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})
data_4 = pd.DataFrame({'Zähne': [41,42,43,44,45,46,47,48], 'B': ['']*8, 'R': ['']*8, 'TP': ['']*8})

# Erzeugen der Check-Kästchen
checkbox_1 = st.checkbox('1. Quadrat einblenden')
checkbox_2 = st.checkbox('2. Quadrat einblenden')
checkbox_3 = st.checkbox('3. Quadrat einblenden')
checkbox_4 = st.checkbox('4. Quadrat einblenden')

# Anzeigen der Tabellen, wenn die Kästchen ausgewählt sind
if checkbox_1:
    AgGrid(data_1)
if checkbox_2:
    AgGrid(data_2)
if checkbox_3:
    AgGrid(data_3)
if checkbox_4:
    AgGrid(data_4)
