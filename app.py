import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Define teeth and dropdown options
teeth = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]
options = ['ww', 'x']

# Initialize DataFrame
df = pd.DataFrame(index=['B', 'R', 'TP'], columns=teeth)
df = df.fillna('')

# Configure grid options
grid_options = {
    'defaultColDef': {
        'editable': True,
        'resizable': True,
    },
    'columnDefs': [
        {
            'field': str(teeth),
            'cellEditor': 'agSelectCellEditor',
            'cellEditorParams': {
                'values': options
            }
        } for teeth in teeth
    ]
}

# Create AgGrid
response = AgGrid(
    df,
    gridOptions=grid_options,
    height=600,
    width='100%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

# If the grid's data has been updated...
if response['data'] is not None:
    df = response['data']
    # Update 'R' and 'TP' rows based on the value in the 'B' row
    for tooth in teeth:
        if df.loc['B', tooth] == 'ww':
            df.loc['R', tooth] = 'KV'
            df.loc['TP', tooth] = 'KV'
        elif df.loc['B', tooth] == 'x':
            df.loc['R', tooth] = 'E'
            df.loc['TP', tooth] = 'E'
    st.table(df)
