import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Define teeth and dropdown options
teeth1 = [18,17,16,15,14,13,12,11]
teeth2 = [21,22,23,24,25,26,27,28]
options = ['ww', 'x']

# Initialize DataFrame
df1 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth1])
df2 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth2])
df1 = df1.fillna('')
df2 = df2.fillna('')

# Configure grid options
grid_options = {
    'defaultColDef': {
        'editable': True,
        'resizable': True,
        'headerComponentParams': {'menuTabs': ['generalTab']},
    },
    'columnDefs': [
        {
            'headerName': ' ',
            'field': ' ',
            'width': 100,
        }
    ] + [
        {
            'field': str(tooth),
            'cellEditor': 'agSelectCellEditor',
            'cellEditorParams': {
                'values': options
            }
        } for tooth in teeth1+teeth2
    ]
}

# Create AgGrid
response1 = AgGrid(
    df1.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options,
    height=300,
    width='50%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

response2 = AgGrid(
    df2.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options,
    height=300,
    width='50%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

# If the grid's data has been updated...
if st.button('Update Tabel'):
    if response1['data'] is not None and response2['data'] is not None:
        updated_df1 = response1['data'].set_index(' ')
        updated_df2 = response2['data'].set_index(' ')
        for tooth in teeth1+teeth2:
            if str(tooth) in updated_df1.columns:
                df = updated_df1
            else:
                df = updated_df2

            if df.loc['B', str(tooth)] == 'ww':
                df.loc['R', str(tooth)] = 'KV'
                df.loc['TP', str(tooth)] = 'KV'
            elif df.loc['B', str(tooth)] == 'x':
                df.loc['R', str(tooth)] = 'E'
                df.loc['TP', str(tooth)] = 'E'

        # Display final table with AgGrid
        AgGrid(updated_df1.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True)
        AgGrid(updated_df2.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True)
