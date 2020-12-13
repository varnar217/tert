import csv
import pandas as pd
import numpy as np
import math
import openpyxl
from geopy.distance import geodesic


streets={}
def isNaN(num):
    if num != num:
        return False

    else:
        return True

name_stat=[]

with open('data-398-2020-12-02.csv', 'r', encoding="cp1251") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        state_bufer=[]
        street_bufer=''

        if row['geoData']!='geoData':
            state_bufer.append(row['Name'])

            street_bufer=str(row['geoData']).split('=')[2]
            street_bufer=street_bufer.split('}')[0]

            number_1=float((street_bufer.split(',')[0]).split('[')[1] )
            number_2=float((street_bufer.split(',')[1]).split(']')[0] )

            number_3=(number_1,number_2 )
            state_bufer.append(number_3)


            name_stat.append(state_bufer)

        if row['Street'] in streets:
            streets[row['Street']] += 1
        else:
            streets[row['Street']] = 1


a=(sorted(streets.items(), key=lambda item: item[1], reverse=True))

def funccc(a_1):
    j=0
    for i in range(len(a_1)):
        if a_1[i][0] =='проезд без названия':
            j=j+1
            continue
        else:
            break

    return a_1[j][0]
print(funccc(a))


metro=[]

with open('data-397-2020-12-08.csv', 'r', encoding="cp1251") as f:
    reader_2 = csv.DictReader(f, delimiter=";")
    for row in reader_2:
        metro_bufer=[]

        if len(row['RepairOfEscalators']) !=0:

            metro_bufer.append(row['NameOfStation'])
            metro_bufer.append(row['Name'])
            street_bufer=str(row['geoData']).split('=')[2]
            street_bufer=street_bufer.split('}')[0]
            number_1=float((street_bufer.split(',')[0]).split('[')[1] )
            number_2=float((street_bufer.split(',')[1]).split(']')[0] )
            number_3=(number_1,number_2 )
            #state_bufer.append(number_3)
            metro_bufer.append(number_3)


            metro.append(metro_bufer)





bufer=[]
for metro_name in metro:
    bufer.append(metro_name[0])

a_1 = set(  bufer )
print(a_1) # 2 lesson

namme_metro_spis=[]
for row_2 in metro :

    kolkata=(row_2[2])
    metro_bufer=[]
    i_number=0
    for row_1 in name_stat:
        delhi=row_1[1]

        if abs(geodesic(kolkata, delhi).km) <= 0.5:
            i_number=i_number+1
            #print(i_number)
    #print(row_2[0])
    metro_bufer.append(row_2[0])
    metro_bufer.append(i_number)

    namme_metro_spis.append(metro_bufer)

#print(namme_metro_spis)
sorted(namme_metro_spis  , key=lambda x: x[1])
print(namme_metro_spis[0])
#for  ii in namme_metro_spis:
    #if  l==0 :
        #l=

    #print(ii[0],ii[1])
