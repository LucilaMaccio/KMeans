import numpy as np
import json
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import os
import pandas as pd

from kmeans_madrid import pharmaciesArray, greenZonesArray, securityArray, accidentsArray, librariesArray, schoolsArray, medicalAttentionArray, socialAttentionArray, sportCentersArray, cathChurchesArray, nonCathChurchesArray, marketsArray, poolsArray

# print("pharmaciesArray")
# print(pharmaciesArray)
# print("greenZonesArray")
# print(greenZonesArray)
# print("securityArray")
# print(securityArray)
# print("accidentsArray")
# print(accidentsArray)
# print("librariesArray")
# print(librariesArray)
# print("schoolsArray")
# print(schoolsArray)
# print("medicalAttentionArray")
# print(medicalAttentionArray)
# print("socialAttentionArray")
# print(socialAttentionArray)
# print("sportCentersArray")
# print(sportCentersArray)
# print("cathChurchesArray")
# print(cathChurchesArray)
# print("nonCathChurchesArray")
# print(nonCathChurchesArray)
# print("marketsArray")
# print(marketsArray)
# print("poolsArray")
# print(poolsArray)

dataset = []
print(type(dataset))

for directory in os.listdir('/Users/pablochamorro/PycharmProjects/WebScraping/data'):
    # print(directory)

    path = os.path.join('/Users/pablochamorro/PycharmProjects/WebScraping/data', directory)

    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r', encoding='utf-8') as file: 
            # print(filename)   
            datasetAux = json.loads(file.read())
            dataset.extend(datasetAux)

X = dataset

# print(X)

fullArray=[]
filteredArray = []

print("length X =", len(X))

# data format
for i in range(0,len(X)):
    # print(X[0])
    element=X[i]

    if element == None:
        continue
    else:

        if len(element) != 11:
            # print(X[i])
            continue
        else:
            price=element["price"]
            rooms=element["rooms"]
            bathrooms=element["bathrooms"]
            house_size=element["house_size"]
            location=element["location"]
            homeType=element["type"]
            elevator=element["elevator"]
            parking=element["parking"]
            pool=element["pool"]
            storage_room=element["storage_room"]
            terraze=element["terraze"]
            
            fullApartment=[]

            if price.isnumeric():
                fullApartment.append(int(price))
            else:
                # print("price with wrong format:", price)
                continue

            if rooms.isnumeric():
                fullApartment.append(int(rooms))
            else:
                # print("rooms with wrong format:", rooms)
                continue

            if bathrooms.isnumeric():
                fullApartment.append(int(bathrooms))
            else:
                # print("bathrooms with wrong format:", bathrooms)
                continue

            if house_size.isnumeric():
                fullApartment.append(int(house_size))
            else:
                # print("house_size with wrong format:", house_size)
                continue

            if homeType.find("Casa")  != -1 or homeType.find("Chalet") != -1:
                fullApartment.append(0)
            elif homeType.find("Piso") != -1 or homeType.find("Apartamento") != -1:
                fullApartment.append(1)
            elif homeType.find("Adosada") != -1 or homeType.find("Adosado") != -1:
                fullApartment.append(2)
            elif homeType.find("Dúplex") != -1:
                fullApartment.append(3)
            elif homeType.find("Ático") != -1:
                fullApartment.append(4)
            elif homeType.find("Estudio") != -1:
                fullApartment.append(5)
            elif homeType.find("Planta") != -1 or homeType.find("baja") != -1:
                fullApartment.append(6)
            else:
                fullApartment.append(-1)

            if elevator == True:
                fullApartment.append(1)
            else:
                fullApartment.append(0)

            if storage_room == True:
                fullApartment.append(1)
            else:
                fullApartment.append(0)

            if parking == True:
                fullApartment.append(1)
            else:
                fullApartment.append(0)

            if pool == True:
                fullApartment.append(1)
            else:
                fullApartment.append(0)

            if terraze == True:
                fullApartment.append(1)
            else:
                fullApartment.append(0)

            if location.find("Palacio") != -1 or location.find("Embajadores") != -1 or location.find("Cortes") != -1 or location.find("Justicia") != -1 or location.find("Universidad") != -1 or location.find("Sol") != -1:
                if location.find("Palacio") != -1:
                    fullApartment.append(11)
                if location.find("Embajadores") != -1:
                    fullApartment.append(12)
                if location.find("Cortes") != -1:
                    fullApartment.append(13)
                if location.find("Justicia") != -1:
                    fullApartment.append(14)
                if location.find("Universidad") != -1:
                    fullApartment.append(15)
                if location.find("Sol") != -1:
                    fullApartment.append(16)

                fullApartment.append(pharmaciesArray[0][1])
                fullApartment.append(greenZonesArray[0][1])
                fullApartment.append(securityArray[0][1])
                fullApartment.append(securityArray[0][2])
                fullApartment.append(accidentsArray[0][1])
                fullApartment.append(accidentsArray[0][2])
                fullApartment.append(librariesArray[0][1])
                fullApartment.append(schoolsArray[0][1])
                fullApartment.append(medicalAttentionArray[0][1])
                fullApartment.append(socialAttentionArray[0][1])
                fullApartment.append(sportCentersArray[0][1])
                fullApartment.append(cathChurchesArray[0][1])
                fullApartment.append(nonCathChurchesArray[0][1])
                fullApartment.append(marketsArray[0][1])
                fullApartment.append(poolsArray[0][1])

            elif location.find("Imperial") != -1 or location.find("Acacias") != -1 or location.find("Chopera") != -1 or location.find("Legazpi") != -1 or location.find("Delicias") != -1 or location.find("Palos de Moguer") != -1 or location.find("Atocha") != -1: 
                if location.find("Imperial") != -1:
                    fullApartment.append(21)
                if location.find("Acacias") != -1:
                    fullApartment.append(22)
                if location.find("Chopera") != -1:
                    fullApartment.append(23)
                if location.find("Legazpi") != -1:
                    fullApartment.append(24)
                if location.find("Delicias") != -1:
                    fullApartment.append(25)
                if location.find("Palos de Moguer") != -1:
                    fullApartment.append(26)
                if location.find("Atocha") != -1:
                    fullApartment.append(27)

                fullApartment.append(pharmaciesArray[1][1])
                fullApartment.append(greenZonesArray[1][1])
                fullApartment.append(securityArray[1][1])
                fullApartment.append(securityArray[1][2])
                fullApartment.append(accidentsArray[1][1])
                fullApartment.append(accidentsArray[1][2])
                fullApartment.append(librariesArray[1][1])
                fullApartment.append(schoolsArray[1][1])
                fullApartment.append(medicalAttentionArray[1][1])
                fullApartment.append(socialAttentionArray[1][1])
                fullApartment.append(sportCentersArray[1][1])
                fullApartment.append(cathChurchesArray[1][1])
                fullApartment.append(nonCathChurchesArray[1][1])
                fullApartment.append(marketsArray[1][1])
                fullApartment.append(poolsArray[1][1])

            elif location.find("Pacífico") != -1 or location.find("Adelfas") != -1 or location.find("Estrella") != -1 or location.find("Ibiza") != -1 or location.find("Jerónimos") != -1 or location.find("Niño Jesús") != -1: 
                if location.find("Pacífico") != -1:
                    fullApartment.append(31)
                if location.find("Adelfas") != -1:
                    fullApartment.append(32)
                if location.find("Estrella") != -1:
                    fullApartment.append(33)
                if location.find("Ibiza") != -1:
                    fullApartment.append(34)
                if location.find("Jerónimos") != -1:
                    fullApartment.append(35)
                if location.find("Niño Jesús") != -1:
                    fullApartment.append(36)

                fullApartment.append(pharmaciesArray[2][1])
                fullApartment.append(greenZonesArray[2][1])
                fullApartment.append(securityArray[2][1])
                fullApartment.append(securityArray[2][2])
                fullApartment.append(accidentsArray[2][1])
                fullApartment.append(accidentsArray[2][2])
                fullApartment.append(librariesArray[2][1])
                fullApartment.append(schoolsArray[2][1])
                fullApartment.append(medicalAttentionArray[2][1])
                fullApartment.append(socialAttentionArray[2][1])
                fullApartment.append(sportCentersArray[2][1])
                fullApartment.append(cathChurchesArray[2][1])
                fullApartment.append(nonCathChurchesArray[2][1])
                fullApartment.append(marketsArray[2][1])
                fullApartment.append(poolsArray[2][1])

            elif location.find("Recoletos") != -1 or location.find("Goya") != -1 or location.find("Fuente del Berro") != -1 or location.find("Guindalera") != -1 or location.find("Lista") != -1 or location.find("Castellana") != -1: 
                if location.find("Recoletos") != -1:
                    fullApartment.append(41)
                if location.find("Goya") != -1:
                    fullApartment.append(42)
                if location.find("Fuente del Berro") != -1:
                    fullApartment.append(43)
                if location.find("Guindalera") != -1:
                    fullApartment.append(44)
                if location.find("Lista") != -1:
                    fullApartment.append(45)
                if location.find("Castellana") != -1:
                    fullApartment.append(46)

                fullApartment.append(pharmaciesArray[3][1])
                fullApartment.append(greenZonesArray[3][1])
                fullApartment.append(securityArray[3][1])
                fullApartment.append(securityArray[3][2])
                fullApartment.append(accidentsArray[3][1])
                fullApartment.append(accidentsArray[3][2])
                fullApartment.append(librariesArray[3][1])
                fullApartment.append(schoolsArray[3][1])
                fullApartment.append(medicalAttentionArray[3][1])
                fullApartment.append(socialAttentionArray[3][1])
                fullApartment.append(sportCentersArray[3][1])
                fullApartment.append(cathChurchesArray[3][1])
                fullApartment.append(nonCathChurchesArray[3][1])
                fullApartment.append(marketsArray[3][1])
                fullApartment.append(poolsArray[3][1])

            elif location.find("Gaztambide") != -1 or location.find("Arapiles") != -1 or location.find("Trafalgar") != -1 or location.find("Almagro") != -1 or location.find("Rios Rosas") != -1 or location.find("Vallehermoso") != -1: 
                if location.find("Gaztambide") != -1:
                    fullApartment.append(71)
                if location.find("Arapiles") != -1:
                    fullApartment.append(72)
                if location.find("Trafalgar") != -1:
                    fullApartment.append(73)
                if location.find("Almagro") != -1:
                    fullApartment.append(74)
                if location.find("Rios Rosas") != -1:
                    fullApartment.append(75)
                if location.find("Vallehermoso") != -1:
                    fullApartment.append(76)

                fullApartment.append(pharmaciesArray[4][1])
                fullApartment.append(greenZonesArray[4][1])
                fullApartment.append(securityArray[4][1])
                fullApartment.append(securityArray[4][2])
                fullApartment.append(accidentsArray[4][1])
                fullApartment.append(accidentsArray[4][2])
                fullApartment.append(librariesArray[4][1])
                fullApartment.append(schoolsArray[4][1])
                fullApartment.append(medicalAttentionArray[4][1])
                fullApartment.append(socialAttentionArray[4][1])
                fullApartment.append(sportCentersArray[4][1])
                fullApartment.append(cathChurchesArray[4][1])
                fullApartment.append(nonCathChurchesArray[4][1])
                fullApartment.append(marketsArray[4][1])
                fullApartment.append(poolsArray[4][1])
            else: 
                continue

            # print(fullApartment)
            filteredApartment = []

            # ELEGIR AQUI LOS VALORES QUE SE QUIERAN PROBAR
            filteredApartment.append(fullApartment[1])
            filteredApartment.append(fullApartment[5])
            filteredApartment.append(fullApartment[7])
            filteredApartment.append(fullApartment[8])
            # filteredApartment.append(fullApartment[11])
            # filteredApartment.append(fullApartment[17])

            filteredArray.append(filteredApartment)
            # print(filteredApartment)
            fullArray.append(fullApartment)

# print("length fullArray after removing null or strange values =", len(fullArray))
# print(fullArray)

pd.DataFrame(np.concatenate(fullArray))

columns = ["Price", "Rooms", "Bathrooms", "House Size", "Location", "Type", "Elevator", "Parking", "Pool",
           "Storage Room", "Terraze", "Pharmacies", "Green Zones", "Security related to people",
           "Security related to heritage", "Accidents with victims", "Accidents without victims",
           "Libraries", "Schools", "Medical Attention", "Social Attention", "Sport Centers", "Catholic Churches",
           "Non Catholic Churches", "Markets", "Public Pools"]

pd.set_option('precision', 0)
dataframe = pd.DataFrame(fullArray[0:], columns=[columns])

dataframe = dataframe.astype(int)

dataframe.to_csv(r'/Users/pablochamorro/PycharmProjects/KMeans/export_data.csv', index=True, header=True)
# -----------------------------------------------------------------------------
# TODAS LAS CARACTERISTICAS
# -----------------------------------------------------------------------------
# Elbow method to get best number of clusters
wcss = []
for i in range(1, 9):
    kmeans = KMeans(
        n_clusters=i, 
        init='k-means++', 
        max_iter=300, 
        n_init=10, 
        random_state=0
    )

    kmeans.fit(fullArray)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 9), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Kmeans itself
kmeans = KMeans(
    n_clusters=5, 
    init='k-means++', 
    max_iter=300, 
    n_init=10, 
    random_state=0
)
pred_y = kmeans.fit_predict(fullArray)
print("KMEANS for n_clusters = 5")
print(pred_y)

# if score is near to 1, the clustering is good
silhouetteScore = silhouette_score(fullArray, kmeans.labels_, metric='euclidean')
print(silhouetteScore)

# if score is near to 0, the clustering is good
dbScore = davies_bouldin_score(fullArray, kmeans.labels_)
print(dbScore)

labels, counts = np.unique(pred_y, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.suptitle('Number of elements/cluster')
plt.title("n_clusters = 5")
plt.xlabel('Cluster')
plt.ylabel('Number of elements')
plt.show()


# -----------------------------------------------------------------------------
# SOLO CARACTERISTICAS SELECCIONADAS
# -----------------------------------------------------------------------------
# Elbow method to get best number of clusters
wcss = []
for i in range(1, 9):
    kmeans = KMeans(
        n_clusters=i, 
        init='k-means++', 
        max_iter=300, 
        n_init=10, 
        random_state=0
    )

    kmeans.fit(filteredArray)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 9), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
# plt.show()


# Kmeans itself
kmeans = KMeans(
    n_clusters=5, 
    init='k-means++', 
    max_iter=300, 
    n_init=10, 
    random_state=0
)
pred_y = kmeans.fit_predict(filteredArray)
print("KMEANS for n_clusters = 4")
print(pred_y)

labels, counts = np.unique(pred_y, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.suptitle('Number of elements/cluster')
plt.title("n_clusters = 4")
plt.xlabel('Cluster')
plt.ylabel('Number of elements')
# plt.show()

# if score is near to 1, the clustering is good
silhouetteScore = silhouette_score(filteredArray, kmeans.labels_, metric='euclidean')
print(silhouetteScore)

# if score is near to 0, the clustering is good
dbScore = davies_bouldin_score(filteredArray, kmeans.labels_)
print(dbScore)


# output = []

# for i in range(0, len(pred_y)):
#     if pred_y[i] == 2:
#         output.append(filteredArray[i])

# print('Los pisos que le recomendamos son:')
# print(output)