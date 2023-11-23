# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:12:09 2023

@author: trkia001
"""

import csv

FILNAVN = "imdb_top_1000.csv"
titler = []
rangering = []
bilde_link = []

tittelratingDict = {}

with open(FILNAVN, encoding="UTF-8-sig") as datafil:
    innhold = csv.reader(datafil, delimiter =",")
    
    overskrifter = next(innhold)
    print(overskrifter)
    for rad in innhold:
        titler.append(rad[1])
        bilde_link.append(rad[0])

for filmer in titler:
    rangering.append(titler.index(filmer) + 1)
    
print(rangering)
print(titler)
print(bilde_link)