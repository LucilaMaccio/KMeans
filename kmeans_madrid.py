import numpy as np
import json
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

# --------------------------------------------------------------------------------------
# PHARMACIES
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/pharmacies.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

pharmaciesArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    service_type=element["service_type"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    if service_type.find("24") != -1:
        finalElement.append(0)
    elif service_type.find("DIURNO") != -1 or service_type.find("SERVICIO DE 7'00") != -1:
        finalElement.append(1)
    elif service_type.find("NOCTURNO") != -1:
        finalElement.append(2)
    else:
        finalElement.append(-1)

    pharmaciesArray.append(finalElement)

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(pharmaciesArray)):
    if pharmaciesArray[i][0] == 10:
        countCentro += 1
    elif pharmaciesArray[i][0] == 20:
        countArganzuela += 1
    elif pharmaciesArray[i][0] == 30:
        countRetiro += 1
    elif pharmaciesArray[i][0] == 40:
        countSalamanca += 1
    elif pharmaciesArray[i][0] == 70:
        countChamberi += 1

pharmaciesArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print("length newArray after removing null or strange values =", len(pharmaciesArray))
# print(pharmacielsArray)

# --------------------------------------------------------------------------------------
# GREEN ZONES
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/green_zones.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

greenZonesArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    size=element["size"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    index = size.find(".")
    sizeInt = size[:index]
    if sizeInt.isnumeric():
        finalElement.append(int(sizeInt))
    else:
        continue

    greenZonesArray.append(finalElement)

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(greenZonesArray)):
    if greenZonesArray[i][0] == 10:
        countCentro += 1
    elif greenZonesArray[i][0] == 20:
        countArganzuela += 1
    elif greenZonesArray[i][0] == 30:
        countRetiro += 1
    elif greenZonesArray[i][0] == 40:
        countSalamanca += 1
    elif greenZonesArray[i][0] == 70:
        countChamberi += 1

greenZonesArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print("length newArray after removing null or strange values =", len(greenZonesArray))
# print(greenZonesArray)

# --------------------------------------------------------------------------------------
# SECURITY
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/security.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

securityArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    securityRelatedWithPeople=element["security_related_with_people"]
    securityRelatedWithPatrimony=element["security_related_with_patrimony"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    finalElement.append(int(securityRelatedWithPeople))
    finalElement.append(int(securityRelatedWithPatrimony))

    securityArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(securityArray))
# print(securityArray)

# --------------------------------------------------------------------------------------
# ACCIDENTS
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/accidents.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

accidentsArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    accidentsWithVictims=element["accidents_with_victims"]
    accidentsWithoutVictims=element["accidents_without_victims"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    finalElement.append(int(accidentsWithVictims))
    finalElement.append(int(accidentsWithoutVictims))

    accidentsArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(accidentsArray))
# print(accidentsArray)

# --------------------------------------------------------------------------------------
# LIBRARIES
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/libraries.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

librariesArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    librariesArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(librariesArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(librariesArray)):
    if librariesArray[i][0] == 10:
        countCentro += 1
    elif librariesArray[i][0] == 20:
        countArganzuela += 1
    elif librariesArray[i][0] == 30:
        countRetiro += 1
    elif librariesArray[i][0] == 40:
        countSalamanca += 1
    elif librariesArray[i][0] == 70:
        countChamberi += 1

librariesArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(librariesArray)

# --------------------------------------------------------------------------------------
# SCHOOLS
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/middle_schools.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

schoolsArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    schoolsArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(schoolsArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(schoolsArray)):
    if schoolsArray[i][0] == 10:
        countCentro += 1
    elif schoolsArray[i][0] == 20:
        countArganzuela += 1
    elif schoolsArray[i][0] == 30:
        countRetiro += 1
    elif schoolsArray[i][0] == 40:
        countSalamanca += 1
    elif schoolsArray[i][0] == 70:
        countChamberi += 1

schoolsArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(schoolsArray)

# --------------------------------------------------------------------------------------
# MEDICAL ATTENTION 
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/medical_attention.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

medicalAttentionArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find("CENTRO") != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    medicalAttentionArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(medicalAttentionArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(medicalAttentionArray)):
    if medicalAttentionArray[i][0] == 10:
        countCentro += 1
    elif medicalAttentionArray[i][0] == 20:
        countArganzuela += 1
    elif medicalAttentionArray[i][0] == 30:
        countRetiro += 1
    elif medicalAttentionArray[i][0] == 40:
        countSalamanca += 1
    elif medicalAttentionArray[i][0] == 70:
        countChamberi += 1

medicalAttentionArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(medicalAttentionArray)

# --------------------------------------------------------------------------------------
# SOCIAL ATTENTION 
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/social_attention.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

socialAttentionArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find('CENTRO') != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    socialAttentionArray.append(finalElement)

# print(socialAttentionArray)
# print("length newArray after removing null or strange values =", len(socialAttentionArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(socialAttentionArray)):
    if socialAttentionArray[i][0] == 10:
        countCentro += 1
    elif socialAttentionArray[i][0] == 20:
        countArganzuela += 1
    elif socialAttentionArray[i][0] == 30:
        countRetiro += 1
    elif socialAttentionArray[i][0] == 40:
        countSalamanca += 1
    elif socialAttentionArray[i][0] == 70:
        countChamberi += 1

socialAttentionArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(socialAttentionArray)

# --------------------------------------------------------------------------------------
# SPORT CENTERS
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/sport_centers.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

sportCentersArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find('CENTRO') != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    sportCentersArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(sportCentersArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(sportCentersArray)):
    if sportCentersArray[i][0] == 10:
        countCentro += 1
    elif sportCentersArray[i][0] == 20:
        countArganzuela += 1
    elif sportCentersArray[i][0] == 30:
        countRetiro += 1
    elif sportCentersArray[i][0] == 40:
        countSalamanca += 1
    elif sportCentersArray[i][0] == 70:
        countChamberi += 1

sportCentersArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(sportCentersArray)

# --------------------------------------------------------------------------------------
# CATHOLIC CHURCHES
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/cath_churches.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

cathChurchesArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find('CENTRO') != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    cathChurchesArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(cathChurchesArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(cathChurchesArray)):
    if cathChurchesArray[i][0] == 10:
        countCentro += 1
    elif cathChurchesArray[i][0] == 20:
        countArganzuela += 1
    elif cathChurchesArray[i][0] == 30:
        countRetiro += 1
    elif cathChurchesArray[i][0] == 40:
        countSalamanca += 1
    elif cathChurchesArray[i][0] == 70:
        countChamberi += 1

cathChurchesArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(cathChurchesArray)

# --------------------------------------------------------------------------------------
# NON CATHOLIC CHURCHES
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/non_cath_churches.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

nonCathChurchesArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find('CENTRO') != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    nonCathChurchesArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(nonCathChurchesArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(nonCathChurchesArray)):
    if nonCathChurchesArray[i][0] == 10:
        countCentro += 1
    elif nonCathChurchesArray[i][0] == 20:
        countArganzuela += 1
    elif nonCathChurchesArray[i][0] == 30:
        countRetiro += 1
    elif nonCathChurchesArray[i][0] == 40:
        countSalamanca += 1
    elif nonCathChurchesArray[i][0] == 70:
        countChamberi += 1

nonCathChurchesArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(nonCathChurchesArray)

# --------------------------------------------------------------------------------------
# MARKETS
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/markets.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

marketsArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find('CENTRO') != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    marketsArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(marketsArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(marketsArray)):
    if marketsArray[i][0] == 10:
        countCentro += 1
    elif marketsArray[i][0] == 20:
        countArganzuela += 1
    elif marketsArray[i][0] == 30:
        countRetiro += 1
    elif marketsArray[i][0] == 40:
        countSalamanca += 1
    elif marketsArray[i][0] == 70:
        countChamberi += 1

marketsArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(marketsArray)

# --------------------------------------------------------------------------------------
# POOLS
# --------------------------------------------------------------------------------------

file = open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/pools.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

X = dataset1

poolsArray=[]

# print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    location=element["location"]
    
    finalElement=[]

    if location.find('CENTRO') != -1:
        finalElement.append(10)
    elif location.find("ARGANZUELA") != -1: 
        finalElement.append(20)
    elif location.find("RETIRO") != -1: 
        finalElement.append(30)
    elif location.find("SALAMANCA") != -1: 
        finalElement.append(40)
    elif location.find("CHAMBERI") != -1 or location.find("CHAMBERÍ") != -1: 
        finalElement.append(70)
    else: 
        continue

    poolsArray.append(finalElement)

# print("length newArray after removing null or strange values =", len(poolsArray))

countCentro = 0
countArganzuela = 0
countRetiro = 0
countSalamanca = 0
countChamberi = 0

for i in range(0, len(poolsArray)):
    if poolsArray[i][0] == 10:
        countCentro += 1
    elif poolsArray[i][0] == 20:
        countArganzuela += 1
    elif poolsArray[i][0] == 30:
        countRetiro += 1
    elif poolsArray[i][0] == 40:
        countSalamanca += 1
    elif poolsArray[i][0] == 70:
        countChamberi += 1

poolsArray = [[10, countCentro], [20, countArganzuela], [30, countRetiro], [40, countSalamanca], [70, countChamberi]]

# print(poolsArray)