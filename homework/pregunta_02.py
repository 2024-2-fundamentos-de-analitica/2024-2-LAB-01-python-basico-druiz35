"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from pathlib import Path

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open(Path(__file__).resolve().parents[1].joinpath("./files/input/data.csv"), "r") as f:
        data = csv.reader(f, delimiter="\t")
        hashmap = {}
        for line in data:
            try:
                hashmap[line[0]] += 1
            except:
                hashmap[line[0]] = 1
    result = []
    for key, value in hashmap.items():
        result.append((key,value))
    result.sort()
    return result