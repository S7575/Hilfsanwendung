import pandas as pd
import streamlit as st

# Zahnnummern
teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

# Initialisieren Sie ein leeres DataFrame
df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP'])

# Aufforderung zur Benutzereingabe für jede Zahnnummer
for tooth in teeth_numbers:
    st.subheader(f"Bitte geben Sie die Informationen für Zahnnummer {tooth} ein:")
    b = st.text_input(f"Geben Sie den Wert für B ein für Zahnnummer {tooth}: ")
    r = st.text_input(f"Geben Sie den Wert für R ein für Zahnnummer {tooth}: ")
    tp = st.text_input(f"Geben Sie den Wert für TP ein für Zahnnummer {tooth}: ")

    # Speichern Sie die Werte im DataFrame
    df.loc[tooth, 'B'] = b
    df.loc[tooth, 'R'] = r
    df.loc[tooth, 'TP'] = tp

# Eine Schaltfläche, um die Eingabe zu steuern und die CSV-Tabelle auszugeben
if st.button("Erstellen Sie die CSV-Tabelle"):
    # Ausgabe des DataFrame in CSV-Format
    st.write(df.to_csv(sep=';'))
