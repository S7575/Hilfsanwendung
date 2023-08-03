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
    height=100, 
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
    height=100, 
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
    height=100, 
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
    height=100, 
    width='100%',
    data_return_mode='as_input', 
    update_mode=GridUpdateMode.VALUE_CHANGED,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,  # Set it to True to allow jsfunction to be injected
    key='grid4'
)

# Function to add R and TP rows and update their values based on dropdown selection
def update_values(df, teeth_set):
    # Add 'R' and 'TP' rows if they don't exist
    if 'R' not in df.index:
        R_series = pd.Series({**{'B': 'R'}, **{str(tooth): '' for tooth in teeth_set}}, name='R')
        df = pd.concat([df, R_series])
    if 'TP' not in df.index:
        TP_series = pd.Series({**{'B': 'TP'}, **{str(tooth): '' for tooth in teeth_set}}, name='TP')
        df = pd.concat([df, TP_series])

    # Update the values of 'R' and 'TP' based on 'B' row value
    for col in df.columns:
        if col != 'B':
            B_value = df.loc['B', col]
            if B_value == 'ww':
                df.loc['R', col] = 'KV'
                df.loc['TP', col] = 'KV'
    return df

# Check if the button is pressed
if st.button('Befund aktualisieren', key='button1'):
    # If the button is pressed, update the dataframe
    for tooth_set, df_name in zip([teeth1, teeth2, teeth3, teeth4], ['df1', 'df2', 'df3', 'df4']):
        st.session_state[df_name] = update_values(st.session_state[df_name], tooth_set)

    # Add new rows 'B' and 'TP'
    for tooth_set, df_name in zip([teeth1, teeth2, teeth3, teeth4], ['df1', 'df2', 'df3', 'df4']):
        TP_series = pd.Series({**{'B': 'TP'}, **{str(tooth): '' for tooth in tooth_set}}, name='TP')
        B_series = pd.Series({**{'B': 'B'}, **{str(tooth): '' for tooth in tooth_set}}, name='B')
        st.session_state[df_name] = pd.concat([st.session_state[df_name], TP_series, B_series])
        
        # Ensure all column names are strings
        st.session_state[df_name].columns = st.session_state[df_name].columns.astype(str)
        
    # Display the updated tables
    st.header("Aktualisierte Tabelle 1")
    AgGrid(st.session_state.df1)

    st.header("Aktualisierte Tabelle 2")
    AgGrid(st.session_state.df2)

    st.header("Aktualisierte Tabelle 3")
    AgGrid(st.session_state.df3)

    st.header("Aktualisierte Tabelle 4")
    AgGrid(st.session_state.df4)
