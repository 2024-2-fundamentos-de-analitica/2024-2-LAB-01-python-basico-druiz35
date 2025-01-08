"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
from pathlib import Path

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open(Path(__file__).resolve().parents[1].joinpath("./files/input/data.csv"), "r") as f:
        data = csv.reader(f, delimiter="\t")
        hashmap = dict()
        for line in data:
            values = line[4].split(",")
            letter = line[0]
            values_sum = sum([int(value[4:]) for value in values])
            try:
                hashmap[letter] += values_sum
            except:
                hashmap[letter] = values_sum
    return hashmap