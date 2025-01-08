"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from pathlib import Path

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open(Path(__file__).resolve().parents[1].joinpath("./files/input/data.csv"), "r") as f:
        data = csv.reader(f, delimiter="\t")
        hashmap = {}
        for line in data:
            letter = line[0]
            num = line[1]
            try:
                hashmap[letter].append(int(num))
            except:
                hashmap[letter] = [int(num)]
    result = []
    for key, value in hashmap.items():
        result.append((key, max(value), min(value)))
    result.sort()
    return result