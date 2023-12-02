# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:07:52 2023

@author: fetra001
"""

import csv 
import random as rd

FILNAVN="imdb_top_1000.csv"

L=[]    #Liste med informasjon om alle filmene
G=[]    #Liste over alle sjangerene. G for genre 
IG=[]   #Todimensjonal liste som inneholder indexene til hver sjanger. IG -> index to genre

with open(FILNAVN, encoding="utf-8-sig") as fil: 
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    
    for rad in filinnhold:  #Går gjennom alle radene i datastettet
        L.append(rad)   #Legger til radene i listen L
        infoG=rad[5].split(",")    #Finner sjangeren*e på filmen og legger de in en listen infoG (informasjon genre)
        for i in range(len(infoG)):    #Siden det er flere sjangere per film, må jeg noen ganger gå gjennom flere
            if infoG[i].strip().lower() not in G:    #Sjekker om sjangeren er i listen G
                G.append(infoG[i].strip().lower())   #Hvis den ikke er det blir den lagt til i listen G
        G = sorted(G)   #Sorterer listen G alfabetisk 
        
    for i in range(len(G)):    #Går gjennom alle sjangerene
        index=[]    #lager en tom liste
        for j in range(len(L)):    #Går gjennom listen L
            infoG = L[j][5].split(",")    #Finner sjangeren*e til listen filmen L[j] 
            if G[i] in [info.strip().lower() for info in infoG]:    #Og hvis sjangeren*e til filmen L[j] er den samme som G[i] 
                index.append(j)    #Blir indexen til raden der man finner denne sjangeren lagt til i den tomme listen index
        IG.append(index)    #Alle sjangerene får hver sine indexer i listen IG


def filmForslag(sjanger):    #Funksjon som skal foreslå en film basert på sjanger
    if sjanger.lower().strip() == "x":
        filmIndex = rd.randint(0, len(L)-1)   #Hvis man ikke har en preferanse til film får man en helt tilfeldig film
    else:
        indexG = G.index(sjanger.lower())   #Finner indexen til sjangeren i listen G
        filmIndex = IG[indexG][rd.randint(0, len(IG[indexG])-1)]    #Velger ut en tilfeldig film ut ifra indexene til sjangeren i datasettet, ved hjelp av den todemensjonale listen IG
        
    
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
    if satisfiedInput.lower().strip() == "ja":
        sjanger=input("Skriv sjanger her: ")
        filmForslag(sjanger)
    elif satisfiedInput.lower().strip() == "nei":
        satisfied = True
        print("\nHa en fin dag videre!")
    else:
        print("Ugyldig input. Prøv igjen!\n")
 