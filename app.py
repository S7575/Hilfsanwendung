import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Define teeth and dropdown options
teeth1 = [18,17,16,15,14,13,12,11]
teeth2 = [28,27,26,25,24,23,22,21]
options = ['ww', 'x']

# Initialize DataFrames
df1 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth1])
df1 = df1.fillna('')

df2 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth2])
df2 = df2.fillna('')

# Configure grid options for both dataframes
grid_options1 = {
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
        } for tooth in teeth1
    ]
}

grid_options2 = {
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
        } for tooth in teeth2
    ]
}

# Create AgGrids
response1 = AgGrid(
    df1.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options1,
    height=150,
    width='100%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,
)

response2 = AgGrid(
    df2.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options2,
    height=150,
    width='100%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,
)

# If the grid's data has been updated...
if st.button('Update Tabel'):
    for response, teeth in [(response1, teeth1), (response2, teeth2)]:
        if response['data'] is not None:
            updated_df = response['data'].set_index(' ')
            for tooth in teeth:
                if updated_df.loc['B', str(tooth)] == 'ww':
                    updated_df.loc['R', str(tooth)] = 'KV'
                    updated_df.loc['TP', str(tooth)] = 'KV'
                elif updated_df.loc['B', str(tooth)] == 'x':
                    updated_df.loc['R', str(tooth)] = 'E'
                    updated_df.loc['TP', str(tooth)] = 'E'

            # Display final tables with AgGrid
            AgGrid(updated_df.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True)
