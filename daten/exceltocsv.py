import os
import pandas as pd
from math import pi

# change dir to current working dir
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)
# print(os.getcwd())

# create both paths
excel_path = os.path.join(script_directory, 'datenVersuchNeu.xlsx')
excel_path_old = os.path.join(script_directory, 'datenVersuchSchön.xlsx')
csv_path = os.path.join(script_directory, 'datenVersuch.csv')

# load excel file
data = pd.read_excel(excel_path_old)

# load data into csv file
data.to_csv(csv_path, index=False, sep=';')
print('data were succesfully written to csv file')

# load csvdata
csv_data = pd.read_csv(csv_path, index_col=False, sep=';')

# zeilen finden in der ladung noch nicht drin ist
fehlen_ladung = csv_data[csv_data['ladung'].isna()]

# berechnung ladung für diese Zeilen
csv_data.loc[csv_data['ladung'].isna(), 'ladung'] = (
    (4/3)*pi*csv_data['density']*9.81*((((csv_data['b']/(2*csv_data['pressure']))**2 + ((9*csv_data['luftviskosität']*csv_data['v_fall'])/(2*9.81*csv_data['density'])))**0.5 - (csv_data['b']/(2*csv_data['pressure'])))**3)*(((csv_data['v_fall']+csv_data['v_rise'])*csv_data['d'])/(csv_data['spannung']*csv_data['v_fall']))
)

# aktualisierte Datei speichern
csv_data.to_csv(csv_path, index=False, sep=';')

print('die fehlenden Ladungen wurden berechnet und hinzugefügt')

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    csv_data.to_excel(writer, index=False, sheet_name='Sheet1')

    # zugriff auf das arbeitsblatt
    workbook = writer.book
    sheet = workbook['Sheet1']

    # Spaltenbreite anpassen
    for col in sheet.columns:
        max_len = 20
        column = col[0].column_letter
        # breite anpassen
        sheet.column_dimensions[column].width = max_len

print('daten wurden erfolgreich der Exceldatei hinzugefügt und spaltenbreite wurde auf 20 gesetzt')