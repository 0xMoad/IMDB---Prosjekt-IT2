# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 23:42:47 2023

@author: trkia001
"""

import csv
FILNAVN = "imdb_top_1000.csv"
titler = []

with open(FILNAVN, encoding="UTF-8-sig") as datafil:
    innhold = csv.reader(datafil, delimiter =",")
    
    overskrifter = next(innhold)
    for rad in innhold:
        titler.append(rad[1])

tittel_rating = {}

for filmer in titler:
    rangering = titler.index(filmer) + 1
    tittel_rating[filmer] = rangering

print(tittel_rating)