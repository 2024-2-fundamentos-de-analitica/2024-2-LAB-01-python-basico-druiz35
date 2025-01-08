"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from pathlib import Path

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open(Path(__file__).resolve().parents[1].joinpath("./files/input/data.csv"), "r") as f:
        data = csv.reader(f, delimiter="\t")
        hashmap = {}
        for line in data:
            try:
                hashmap[line[0]] += int(line[1])
            except:
                hashmap[line[0]] = int(line[1])
    result = []
    for key, value in hashmap.items():
        result.append((key,value))
    result.sort()
    return result
