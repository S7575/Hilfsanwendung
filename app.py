import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode, GridOptionsBuilder

# Define teeth and dropdown options
teeth1 = [11,12,13,14,15,16,17,18]
teeth2 = [21,22,23,24,25,26,27,28]
teeth3 = [31,32,33,34,35,36,37,38]
teeth4 = [41,42,43,44,45,46,47,48]

options = ['ww', 'x', 'a', 'ab', 'abw', 'aw', 'b', 'bw', 'e', 'ew', 'f', 'ix', 'k', 'kw', 'pkw', 'pw', 'r', 'rW', 'sb', 'sbw', 'se', 'sew', 'sk', 'skw', 'so', 'sow', 'st', 'stw', 't', 't2w', 'tw', 'ur', ')(']

# Initialize DataFrames and add a row label column
df1 = pd.DataFrame({"B": ['B'], **{str(tooth): [''] for tooth in teeth1}})
df2 = pd.DataFrame({"B": ['B'], **{str(tooth): [''] for tooth in teeth2}})
df3 = pd.DataFrame({"B": ['B'], **{str(tooth): [''] for tooth in teeth3}})
df4 = pd.DataFrame({"B": ['B'], **{str(tooth): [''] for tooth in teeth4}})

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
gb1 = GridOptionsBuilder.from_dataframe(st.session_state.df1)
gb1.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
for tooth in ["B"] + teeth1:
    gb1.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])
grid_options1 = gb1.build()

# Repeat the same for other tables...
gb2 = GridOptionsBuilder.from_dataframe(st.session_state.df2)
gb2.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
for tooth in ["B"] + teeth2:
    gb2.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])
grid_options2 = gb2.build()

gb3 = GridOptionsBuilder.from_dataframe(st.session_state.df3)
gb3.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
for tooth in ["B"] + teeth3:
    gb3.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])
grid_options3 = gb3.build()

gb4 = GridOptionsBuilder.from_dataframe(st.session_state.df4)
gb4.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
for tooth in ["B"] + teeth4:
    gb4.configure_column(str(tooth), cellEditor='agSelectCellEditor', cellEditorParams={'values': options}, type=["editableColumn"])
grid_options4 = gb4.build()

# Display the AgGrid
st.header("Tabelle 1")
response = AgGrid(
    st.session_state.df1,
    gridOptions=grid_options1,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid1'
)

# Repeat the same for other tables...
st.header("Tabelle 2")
response2 = AgGrid(
    st.session_state.df2,
    gridOptions=grid_options2,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid2'
)

st.header("Tabelle 3")
response3 = AgGrid(
    st.session_state.df3,
    gridOptions=grid_options3,
    height=200, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid3'
)

st.header("Tabelle 4")
response4 = AgGrid(
    st.session_state.df4,
    gridOptions=grid_options4,
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
    
    # Add new rows with row labels 'B' and 'TP'
    for df in [st.session_state.df1, st.session_state.df2, st.session_state.df3, st.session_state.df4]:
        df = df.append(pd.Series({**{'B': 'TP'}, **{str(tooth): '' for tooth in teeth1}}), ignore_index=True)
        df = df.append(pd.Series({**{'B': 'B'}, **{str(tooth): '' for tooth in teeth1}}), ignore_index=True)
        
    # Display the updated tables
    st.header("Aktualisierte Tabelle 1")
    AgGrid(st.session_state.df1)

    st.header("Aktualisierte Tabelle 2")
    AgGrid(st.session_state.df2)

    st.header("Aktualisierte Tabelle 3")
    AgGrid(st.session_state.df3)

    st.header("Aktualisierte Tabelle 4")
    AgGrid(st.session_state.df4)
