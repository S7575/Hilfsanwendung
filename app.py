import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode, GridOptionsBuilder

# Define teeth and dropdown options
teeth1 = [11,12,13,14,15,16,17,18]
teeth2 = [21,22,23,24,25,26,27,28]
teeth3 = [31,32,33,34,35,36,37,38]
teeth4 = [41,42,43,44,45,46,47,48]

options = ['ww', 'x', 'a', 'ab', 'abw', 'aw', 'b', 'bw', 'e', 'ew', 'f', 'ix', 'k', 'kw', 'pkw', 'pw', 'r', 'rW', 'sb', 'sbw', 'se', 'sew', 'sk', 'skw', 'so', 'sow', 'st', 'stw', 't', 't2w', 'tw', 'ur', ')(']

# Initialize DataFrames
df1 = pd.DataFrame(index=['B'], columns=[str(tooth) for tooth in teeth1]).fillna('')
df2 = pd.DataFrame(index=['B'], columns=[str(tooth) for tooth in teeth2]).fillna('')
df3 = pd.DataFrame(index=['B'], columns=[str(tooth) for tooth in teeth3]).fillna('')
df4 = pd.DataFrame(index=['B'], columns=[str(tooth) for tooth in teeth4]).fillna('')

# Check if session state already has the dataframes, if not assign them
if 'df1' not in st.session_state:
    st.session_state['df1'] = df1
if 'df2' not in st.session_state:
    st.session_state['df2'] = df2
if 'df3' not in st.session_state:
    st.session_state['df3'] = df3
if 'df4' not in st.session_state:
    st.session_state['df4'] = df4

# Create grid options for each table
gb = GridOptionsBuilder.from_dataframe(st.session_state.df1)
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)

# Configure dropdown for each column
for tooth in teeth1:
    gb.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])

# Configure dropdown for each column
for tooth in teeth2:
    gb.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])

# Configure dropdown for each column
for tooth in teeth3:
    gb.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])

# Configure dropdown for each column
for tooth in teeth4:
    gb.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])



grid_options = gb.build()

# Display the AgGrid
st.header("Tabelle 1")
response = AgGrid(
    st.session_state.df1,
    gridOptions=grid_options,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid1'
)

# Display the AgGrid
st.header("Tabelle 2")
response2 = AgGrid(
    st.session_state.df1,
    gridOptions=grid_options,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid2'
)

# Display the AgGrid
st.header("Tabelle 3")
response3 = AgGrid(
    st.session_state.df1,
    gridOptions=grid_options,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid3'
)

# Display the AgGrid
st.header("Tabelle 4")
response4 = AgGrid(
    st.session_state.df1,
    gridOptions=grid_options,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid4'
)

# Check if the button is pressed
if st.button('Befund aktualisieren'):
    # If the button is pressed, update the dataframe
    st.session_state.df1 = response['data']
    st.session_state.df2 = response2['data']
    st.session_state.df3 = response3['data']
    st.session_state.df4 = response4['data']
    
    # Add new rows 'B' and 'TP'
    for df in [st.session_state.df1, st.session_state.df2, st.session_state.df3, st.session_state.df4]:
        df.loc['TP'] = ""
        df.loc['B'] = ""
        
    # Display the updated tables
    st.header("Aktualisierte Tabelle 1")
    AgGrid(st.session_state.df1)

    st.header("Aktualisierte Tabelle 2")
    AgGrid(st.session_state.df2)

    st.header("Aktualisierte Tabelle 3")
    AgGrid(st.session_state.df3)

    st.header("Aktualisierte Tabelle 4")
    AgGrid(st.session_state.df4)