"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from pathlib import Path

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    with open(Path(__file__).resolve().parents[1].joinpath("./files/input/data.csv"), "r") as f:
       data = csv.reader(f, delimiter="\t")
       result = []
       for line in data:
            letter = line[0]
            len_col4 = len(line[3].split(","))
            len_col5 = len(line[4].split(","))
            result.append((letter, len_col4, len_col5))
    return result