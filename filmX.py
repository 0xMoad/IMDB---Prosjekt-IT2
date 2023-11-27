# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:43:46 2023

@author: fetra001
"""

import csv
import random as rd


FILNAVN = "test.csv"

L=[]

with open(FILNAVN, encoding="utf-8") as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    """
    overskrifter = next(filinnhold)
    print(overskrifter)
    """ 
    for rad in filinnhold:
        L.append(rad)
        
        

def movieSuggestion(sjanger):
    
    filmIndex = rd.randint(0, len(L) - 1)
    
    filmInfo = L[filmIndex][0]
    filmInfo_list = filmInfo.split(',')

    filmInfo_list = [element.strip('\"') for element in filmInfo_list]
    
    while sjanger not in filmInfo_list:
        filmIndex = rd.randint(0, len(L) - 1)
        filmInfo = L[filmIndex][0]
        filmInfo_list = filmInfo.split(',')

        filmInfo_list = [element.strip('\"') for element in filmInfo_list]
        
    handling=""
    antall=0
    for i in range(7, len(filmInfo_list)-10):
        if len(filmInfo_list[i]) > 10 and i !=0:
            if antall == 0:
                handling = handling + filmInfo_list[i]
                antall += 1
            else:
                handling = handling + "," + filmInfo_list[i]
         
    tittel = filmInfo_list[4]
    årstall = filmInfo_list[5]


    print(f'Tittel: {tittel}')
    print(f'Årstall: {årstall}')
    print(f'Handling: {handling}')

print("Velg ønsket sjanger")
print("Du kan velge mellom disse:")
print("Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Family, Fantasy, History, Horror, Mystery, Music, Musical, Romance, Sci-Fi, Sport, Thriller, War, Western")
print("--------------------------------------")

sjanger=input("Skriv sjanger her: ")
print("--------------------------------------")


movieSuggestion(sjanger)


    

