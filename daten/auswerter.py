from math import pi

B = 8.20E-03

v_tabelle = [
    [2.12E-05, 2.01E-04],
    [2.16E-05, 8.46E-05],
    [1.98E-05, 8.68E-05],
    [2.47E-05, 9.38E-05],
    [2.04E-05, 8.91E-05],
    [1.98E-05, 1.97E-04],
    [2.04E-05, 1.98E-04],
    [1.84E-05, 9.33E-05]
]

def ladung(geschwindigkeiten, spannung, viscosity, d, dichte, druck):
    global B
    ladungen = []
    for geschwindigkeit in geschwindigkeiten:
        q = (4/3)*pi*dichte*9.81*((((B/(2*druck))**2 + ((9*viscosity*geschwindigkeit[0])/(2*9.81*dichte)))**0.5 - (B/(2*druck)))**3)*(((geschwindigkeit[0]+geschwindigkeit[1])*d)/(spannung*geschwindigkeit[0]))

        ladungen.append(q)

    return ladungen

print(ladung(v_tabelle, 585, 1.81E-5, 7.600E-03, 886, 1020000))