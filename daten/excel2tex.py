import pandas as pd
import os
import numpy as np  

def read_excel_data(file_path, sheet_name=0):
    """
    Liest Daten aus einer Excel-Tabelle.

    :param file_path: Pfad zur Excel-Datei
    :param sheet_name: Name oder Index des Blatts (Standard: 0)
    :return: DataFrame mit den Daten
    """
    return pd.read_excel(file_path, sheet_name=sheet_name)

def calculate_data(df):
    """
    Führt Berechnungen mit den Daten durch. Beispiel: Berechnung der Summe und des Mittelwerts pro Zeile.

    :param df: Eingabedaten als DataFrame
    :return: Neuer DataFrame mit den Ergebnissen
    """
    # Konstanten
    g = 9.81  # Erdbeschleunigung in m/s^2

    # Luftdruck aus der Tabelle entnehmen
    p = df['pressure']  # Luftdruck in Pa

    # Radiusberechnung: a = sqrt((b / 2p)^2 + (9 * eta * v_f) / (2 * rho * g)) - (b / 2p)
    df['Radius'] = (
        np.sqrt(
            (df['b'] / (2 * p))**2 + (9 * df['luftviskosität'] * df['v_fall']) / (2 * df['density'] * g)
        ) - (df['b'] / (2 * p))
    )

    # Massenberechnung: m = (4/3) * pi * a^3 * rho
    df['Masse'] = (4 / 3) * np.pi * df['Radius']**3 * df['density']

    # Ladung aus der Tabelle übernehmen
    df['Ladung'] = df['ladung']

    return df[['v_rise', 'v_fall', 'Radius', 'Masse', 'Ladung']]

def save_to_csv(df, output_path):
    """
    Speichert den DataFrame als CSV-Datei.

    :param df: DataFrame mit den Ergebnissen
    :param output_path: Pfad zur Ausgabe-CSV-Datei
    """
    df.to_csv(output_path, index=False, float_format="%.6e")

def format_scientific_to_latex(value):
    """
    Konvertiert einen wissenschaftlichen Wert in LaTeX-kompatibles Format.
    """
    if isinstance(value, (float, int)):
        return f"{value:.2e}".replace('e', ' \\times 10^{').replace('+', '') + '}'
    return value

def generate_latex_table(csv_path, latex_path):
    """
    Erstellt eine LaTeX-Tabelle aus der CSV-Datei.

    Die Werte werden in wissenschaftlicher Schreibweise dargestellt.

    :param csv_path: Pfad zur Eingabe-CSV-Datei
    :param latex_path: Pfad zur Ausgabe-LaTeX-Datei
    """
    df = pd.read_csv(csv_path)
    df = df.applymap(format_scientific_to_latex)  # Wissenschaftliche Werte formatieren
    with open(latex_path, 'w') as f:
        f.write(df.to_latex(index=False, escape=False, caption="Ergebnisse der Berechnung", label="tab:ergebnisse"))

if __name__ == "__main__":
    # Pfade anpassen
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    excel_file = "datenVersuchSchön.xlsx"  # Eingabe-Excel-Datei
    csv_file = "radiusMasseLadung.csv"  # Ausgabe-CSV-Datei
    latex_file = "radiusMasseLadung.tex"  # Ausgabe-LaTeX-Datei

    # Schritte ausführen
    try:
        data = read_excel_data(excel_file)
        result_data = calculate_data(data)
        save_to_csv(result_data, csv_file)
        generate_latex_table(csv_file, latex_file)
        print("Daten erfolgreich verarbeitet und in LaTeX-Tabelle umgewandelt.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
