import os
import pandas as pd

script_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_directory, 'datenVersuch.csv')

csv_data = pd.read_csv(csv_path, index_col=False, sep=';')

print(csv_data.columns)
if 'ladung' in csv_data.columns:
    print("Die Spalte existiert.")
else:
    print("Die Spalte existiert nicht.")


