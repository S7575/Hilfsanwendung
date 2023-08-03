import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Define teeth and dropdown options
teeth1 = [11,12,13,14,15,16,17,18]
teeth2 = [21,22,23,24,25,26,27,28]
options = ['ww', 'x', 'a', 'ab', 'abw', 'aw', 'b', 'bw', 'e', 'ew', 'f', 'ix', 'k', 'kw', 'pkw', 'pw', 'r', 'rW', 'sb', 'sbw', 'se', 'sew', 'sk', 'skw', 'so', 'sow', 'st', 'stw', 't', 't2w', 'tw', 'ur', ')(']

# Initialize DataFrame
df1 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth1])
df2 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth2])
df1 = df1.fillna('')
df2 = df2.fillna('')

# Create grid options for each table
grid_options1 = {
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
        } for tooth in teeth1
    ]
}

grid_options2 = grid_options1.copy()
grid_options2['columnDefs'] = [
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
    } for tooth in teeth2
]

# Create AgGrid
response1 = AgGrid(
    df1.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options1,
    height=150,
    width='50%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

response2 = AgGrid(
    df2.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options2,
    height=150,
    width='50%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

# If the grid's data has been updated...
if st.button('Befund aktualisieren'):
    if response1['data'] is not None:
        updated_df1 = response1['data'].set_index(' ')
        # Check if there is any input in 'B' row
        if not updated_df1.loc['B'].eq('').all():  # if all are empty strings, we assume there's no input
            for tooth in teeth1:
                if updated_df1.loc['B', str(tooth)] == 'ww':
                    updated_df1.loc['R', str(tooth)] = 'KV'
                    updated_df1.loc['TP', str(tooth)] = 'KV'
                elif updated_df1.loc['B', str(tooth)] == 'x':
                    updated_df1.loc['R', str(tooth)] = 'E'
                    updated_df1.loc['TP', str(tooth)] = 'E'

            # Display final table with AgGrid
            AgGrid(updated_df1.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True, height=150)

    if response2['data'] is not None:
        updated_df2 = response2['data'].set_index(' ')
        # Check if there is any input in 'B' row
        if not updated_df2.loc['B'].eq('').all():  # if all are empty strings, we assume there's no input
            for tooth in teeth2:
                if updated_df2.loc['B', str(tooth)] == 'ww':
                    updated_df2.loc['R', str(tooth)] = 'KV'
                    updated_df2.loc['TP', str(tooth)] = 'KV'
                elif updated_df2.loc['B', str(tooth)] == 'x':
                    updated_df2.loc['R', str(tooth)] = 'E'
                    updated_df2.loc['TP', str(tooth)] = 'E'

        # Display final table with AgGrid
        AgGrid(updated_df1.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True, height=150)
        AgGrid(updated_df2.reset_index().rename(columns={'index':' '}), editable=False, fit_columns_on_grid_load=True, height=150)
