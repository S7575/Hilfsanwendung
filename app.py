import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

# Define teeth and dropdown options
teeth1 = [11,12,13,14,15,16,17,18]
teeth2 = [21,22,23,24,25,26,27,28]
teeth3 = [31,32,33,34,35,36,37,38]
teeth4 = [41,42,43,44,45,46,47,48]

options = ['ww', 'x', 'a', 'ab', 'abw', 'aw', 'b', 'bw', 'e', 'ew', 'f', 'ix', 'k', 'kw', 'pkw', 'pw', 'r', 'rW', 'sb', 'sbw', 'se', 'sew', 'sk', 'skw', 'so', 'sow', 'st', 'stw', 't', 't2w', 'tw', 'ur', ')(']

# Initialize DataFrame
df1 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth1])
df2 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth2])
df3 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth3])
df4 = pd.DataFrame(index=['B', 'R', 'TP'], columns=[str(tooth) for tooth in teeth4])
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

grid_options3 = grid_options1.copy()
grid_options3['columnDefs'] = [
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
    } for tooth in teeth3
]

grid_options4 = grid_options1.copy()
grid_options4['columnDefs'] = [
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
    } for tooth in teeth4
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

response3 = AgGrid(
    df3.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options3,
    height=150,
    width='50%',
    data_return_mode='as_input',
    update_mode='value_changed',
    fit_columns_on_grid_load=True,
    allow_unsafe_js_code=True,  # This is required to enable onCellValueChanged callback
)

response4 = AgGrid(
    df4.reset_index().rename(columns={'index':' '}),
    gridOptions=grid_options4,
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
            AgGrid(updated_df1.reset_index().rename(columns={'index':' '}), 
                   editable=False, 
                   fit_columns_on_grid_load=True, 
                   height=150, 
                   key='AgGrid1')

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
            AgGrid(updated_df2.reset_index().rename(columns={'index':' '}), 
                   editable=False, 
                   fit_columns_on_grid_load=True, 
                   height=150, 
                   key='AgGrid2')
            
    if response3['data'] is not None:
        updated_df3 = response3['data'].set_index(' ')
        if not updated_df3.loc['B'].eq('').all():
            for tooth in teeth3:
                if updated_df3.loc['B', str(tooth)] == 'ww':
                    updated_df3.loc['R', str(tooth)] = 'KV'
                    updated_df3.loc['TP', str(tooth)] = 'KV'
                elif updated_df3.loc['B', str(tooth)] == 'x':
                    updated_df3.loc['R', str(tooth)] = 'E'
                    updated_df3.loc['TP', str(tooth)] = 'E'

            # Display final table with AgGrid
            AgGrid(updated_df3.reset_index().rename(columns={'index':' '}), 
                   editable=False, 
                   fit_columns_on_grid_load=True, 
                   height=150, 
                   key='AgGrid3')
            

    if response4['data'] is not None:
        updated_df4 = response4['data'].set_index(' ')
        if not updated_df4.loc['B'].eq('').all():
            for tooth in teeth4:
                if updated_df4.loc['B', str(tooth)] == 'ww':
                    updated_df4.loc['R', str(tooth)] = 'KV'
                    updated_df4.loc['TP', str(tooth)] = 'KV'
                elif updated_df4.loc['B', str(tooth)] == 'x':
                    updated_df4.loc['R', str(tooth)] = 'E'
                    updated_df4.loc['TP', str(tooth)] = 'E'

            # Display final table with AgGrid
            AgGrid(updated_df4.reset_index().rename(columns={'index':' '}), 
                   editable=False, 
                   fit_columns_on_grid_load=True, 
                   height=150, 
                   key='AgGrid4')

