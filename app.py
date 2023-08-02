import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Define teeth and dropdown options
teeth = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]
options = ['ww', 'x']

# Initialize DataFrame
df = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth])
df = df.fillna('')

# Configure grid options
grid_options = {
    'defaultColDef': {
        'editable': True,
        'resizable': True,
    },
    'columnDefs': [
        {
            'field': str(tooth),
            'cellEditor': 'agSelectCellEditor',
            'cellEditorParams': {
                'values': options
            }
        } for tooth in teeth
    ]
}

# Create AgGrid
response = AgGrid(
    df.reset_index().rename(columns={'index':' '}),  # display index in a separate column
    gridOptions=grid_options,
    height=600,
    width='100%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

# If the grid's data has been updated...
if st.button('Update Tabel'):
    if response['data'] is not None:
        updated_df = response['data'].set_index(' ')
        for tooth in teeth:
            if updated_df.loc['B', str(tooth)] == 'ww':
                updated_df.loc['R', str(tooth)] = 'KV'
                updated_df.loc['TP', str(tooth)] = 'KV'
            elif updated_df.loc['B', str(tooth)] == 'x':
                updated_df.loc['R', str(tooth)] = 'E'
                updated_df.loc['TP', str(tooth)] = 'E'

        # Display final table with AgGrid
        AgGrid(updated_df.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True)
