import pandas as pd

# Zahnnummern
teeth_numbers = [18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28]

# Initialisieren Sie ein leeres DataFrame
df = pd.DataFrame(index=teeth_numbers, columns=['B', 'R', 'TP'])

# Aufforderung zur Benutzereingabe für jede Zahnnummer
for tooth in teeth_numbers:
    print(f"Bitte geben Sie die Informationen für Zahnnummer {tooth} ein:")
    b = input("Geben Sie den Wert für B ein: ")
    r = input("Geben Sie den Wert für R ein: ")
    tp = input("Geben Sie den Wert für TP ein: ")

    # Speichern Sie die Werte im DataFrame
    df.loc[tooth, 'B'] = b
    df.loc[tooth, 'R'] = r
    df.loc[tooth, 'TP'] = tp

# Ausgabe des DataFrame in CSV-Format
print(df.to_csv(sep=';'))
