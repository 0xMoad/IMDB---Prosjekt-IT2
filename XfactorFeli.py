# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:07:52 2023

@author: fetra001
"""

import csv 
import random as rd

FILNAVN="imdb_top_1000.csv"

L=[]
G=[]
IG=[]

with open(FILNAVN, encoding="utf-8-sig") as fil: 
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    
    for rad in filinnhold:
        L.append(rad)
        infoG=rad[5].split(",")
        for i in range(len(infoG)):
            if infoG[i].strip().lower() not in G:
                G.append(infoG[i].strip().lower())
        G = sorted(G)
        
    for i in range(len(G)):
        index=[]
        for j in range(len(L)):
            infoG = L[j][5].split(",")
            if G[i] in [info.strip().lower() for info in infoG]:
                index.append(j)
        IG.append(index)


def filmForslag(sjanger):
    if sjanger.lower() == "x":
        filmIndex = rd.randint(0, len(L)-1)   
    else:
        indexG = G.index(sjanger.lower())
        filmIndex = IG[indexG][rd.randint(0, len(IG[indexG])-1)]
        
    
    tittel=L[filmIndex][1]
    aar=L[filmIndex][2]
    lengde=L[filmIndex][4]
    sjanger=L[filmIndex][5]
    plot=L[filmIndex][7]
    
    print("---------------------------")
    print(f'IMDB rating: {filmIndex+1}/1000')
    print("---------------------------")
    print(f'Tittel: {tittel}')
    print(f'Årstall: {aar}')
    print(f'Lengde: {lengde}')
    print(f'Sjanger: {sjanger}')
    print(f'Plot: {plot}')
    print("---------------------------")
    

print("Velkommen til film anbefaleren!")
print("---------------------------")
print("Du kan velge mellom disse sjangerene:", ', '.join(G))
print("---------------------------")
print("Skriv inn ønsket sjanger nedenfor")
print("Tast x nedenfor dersom du ikke har en preferanse for sjanger")
print("---------------------------")
sjanger=input("Skriv sjanger her: ")

filmForslag(sjanger)

satisfied = False
 
while not satisfied:
    print("Ønsker du en annen anbefaling? ")
    satisfiedInput = input("\nSvar: ")
    if satisfiedInput.lower() == "ja":
        sjanger=input("Skriv sjanger her: ")
        filmForslag(sjanger)
    elif satisfiedInput.lower() == "nei":
        satisfied = True
        print("\nHa en fin dag videre!")
    else:
        print("Ugyldig input. Prøv igjen!\n")
 