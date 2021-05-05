import numpy as np
import json
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

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

file = open('C:\\Users\lucil\Downloads\data912478214.json', 'r', encoding='utf-8')
dataset1 = json.loads(file.read())

file = open('C:\\Users\lucil\Downloads\data445531806.json', 'r', encoding='utf-8')
dataset2 = json.loads(file.read())

dataset1.extend(dataset2)
X = dataset1

newArray=[]

print("length X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

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
        
        finalApartment=[]

        if price.isnumeric():
            finalApartment.append(int(price))
        else:
            # print("price with wrong format:", price)
            continue

        if rooms.isnumeric():
            finalApartment.append(int(rooms))
        else:
            # print("rooms with wrong format:", rooms)
            continue

        if bathrooms.isnumeric():
            finalApartment.append(int(bathrooms))
        else:
            # print("bathrooms with wrong format:", bathrooms)
            continue

        if house_size.isnumeric():
            finalApartment.append(int(house_size))
        else:
            # print("house_size with wrong format:", house_size)
            continue

        if homeType.find("Casa")  != -1 or homeType.find("Chalet") != -1:
            finalApartment.append(0)
        elif homeType.find("Piso") != -1 or homeType.find("Apartamento") != -1:
            finalApartment.append(1)
        elif homeType.find("Adosada") != -1 or homeType.find("Adosado") != -1:
            finalApartment.append(2)
        elif homeType.find("Dúplex") != -1:
            finalApartment.append(3)
        elif homeType.find("Ático") != -1:
            finalApartment.append(4)
        else:
            finalApartment.append(-1)

        if elevator == True:
            finalApartment.append(1)
        else:
            finalApartment.append(0)

        if storage_room == True:
            finalApartment.append(1)
        else:
            finalApartment.append(0)

        if parking == True:
            finalApartment.append(1)
        else:
            finalApartment.append(0)

        if pool == True:
            finalApartment.append(1)
        else:
            finalApartment.append(0)

        if terraze == True:
            finalApartment.append(1)
        else:
            finalApartment.append(0)

        if location.find("Palacio") != -1 or location.find("Embajadores") != -1 or location.find("Cortes") != -1 or location.find("Justicia") != -1 or location.find("Universidad") != -1 or location.find("Sol") != -1:
            finalApartment.append(10)
            finalApartment.append(pharmaciesArray[0][1])
            finalApartment.append(greenZonesArray[0][1])
            finalApartment.append(securityArray[0][1])
            finalApartment.append(securityArray[0][2])
            finalApartment.append(accidentsArray[0][1])
            finalApartment.append(accidentsArray[0][2])
            finalApartment.append(librariesArray[0][1])
            finalApartment.append(schoolsArray[0][1])
            finalApartment.append(medicalAttentionArray[0][1])
            finalApartment.append(socialAttentionArray[0][1])
            finalApartment.append(sportCentersArray[0][1])
            finalApartment.append(cathChurchesArray[0][1])
            finalApartment.append(nonCathChurchesArray[0][1])
            finalApartment.append(marketsArray[0][1])
            finalApartment.append(poolsArray[0][1])

        elif location.find("Imperial") != -1 or location.find("Acacias") != -1 or location.find("Chopera") != -1 or location.find("Legazpi") != -1 or location.find("Delicias") != -1 or location.find("Palos de Moguer") != -1 or location.find("Atocha") != -1: 
            finalApartment.append(20)
            finalApartment.append(pharmaciesArray[1][1])
            finalApartment.append(greenZonesArray[1][1])
            finalApartment.append(securityArray[1][1])
            finalApartment.append(securityArray[1][2])
            finalApartment.append(accidentsArray[1][1])
            finalApartment.append(accidentsArray[1][2])
            finalApartment.append(librariesArray[1][1])
            finalApartment.append(schoolsArray[1][1])
            finalApartment.append(medicalAttentionArray[1][1])
            finalApartment.append(socialAttentionArray[1][1])
            finalApartment.append(sportCentersArray[1][1])
            finalApartment.append(cathChurchesArray[1][1])
            finalApartment.append(nonCathChurchesArray[1][1])
            finalApartment.append(marketsArray[1][1])
            finalApartment.append(poolsArray[1][1])

        elif location.find("Pacífico") != -1 or location.find("Adelfas") != -1 or location.find("Estrella") != -1 or location.find("Ibiza") != -1 or location.find("Jerónimos") != -1 or location.find("Niño Jesús") != -1: 
            finalApartment.append(30)
            finalApartment.append(pharmaciesArray[2][1])
            finalApartment.append(greenZonesArray[2][1])
            finalApartment.append(securityArray[2][1])
            finalApartment.append(securityArray[2][2])
            finalApartment.append(accidentsArray[2][1])
            finalApartment.append(accidentsArray[2][2])
            finalApartment.append(librariesArray[2][1])
            finalApartment.append(schoolsArray[2][1])
            finalApartment.append(medicalAttentionArray[2][1])
            finalApartment.append(socialAttentionArray[2][1])
            finalApartment.append(sportCentersArray[2][1])
            finalApartment.append(cathChurchesArray[2][1])
            finalApartment.append(nonCathChurchesArray[2][1])
            finalApartment.append(marketsArray[2][1])
            finalApartment.append(poolsArray[2][1])

        elif location.find("Recoletos") != -1 or location.find("Goya") != -1 or location.find("Fuente del Berro") != -1 or location.find("Guindalera") != -1 or location.find("Lista") != -1 or location.find("Castellana") != -1: 
            finalApartment.append(40)
            finalApartment.append(pharmaciesArray[3][1])
            finalApartment.append(greenZonesArray[3][1])
            finalApartment.append(securityArray[3][1])
            finalApartment.append(securityArray[3][2])
            finalApartment.append(accidentsArray[3][1])
            finalApartment.append(accidentsArray[3][2])
            finalApartment.append(librariesArray[3][1])
            finalApartment.append(schoolsArray[3][1])
            finalApartment.append(medicalAttentionArray[3][1])
            finalApartment.append(socialAttentionArray[3][1])
            finalApartment.append(sportCentersArray[3][1])
            finalApartment.append(cathChurchesArray[3][1])
            finalApartment.append(nonCathChurchesArray[3][1])
            finalApartment.append(marketsArray[3][1])
            finalApartment.append(poolsArray[3][1])

        elif location.find("Gaztambide") != -1 or location.find("Arapiles") != -1 or location.find("Trafalgar") != -1 or location.find("Almagro") != -1 or location.find("Rios Rosas") != -1 or location.find("Vallehermoso") != -1: 
            finalApartment.append(70)
            finalApartment.append(pharmaciesArray[4][1])
            finalApartment.append(greenZonesArray[4][1])
            finalApartment.append(securityArray[4][1])
            finalApartment.append(securityArray[4][2])
            finalApartment.append(accidentsArray[4][1])
            finalApartment.append(accidentsArray[4][2])
            finalApartment.append(librariesArray[4][1])
            finalApartment.append(schoolsArray[4][1])
            finalApartment.append(medicalAttentionArray[4][1])
            finalApartment.append(socialAttentionArray[4][1])
            finalApartment.append(sportCentersArray[4][1])
            finalApartment.append(cathChurchesArray[4][1])
            finalApartment.append(nonCathChurchesArray[4][1])
            finalApartment.append(marketsArray[4][1])
            finalApartment.append(poolsArray[4][1])
        else: 
            continue

        print(finalApartment)
        newArray.append(finalApartment)

print("length newArray after removing null or strange values =", len(newArray))
# print(newArray)

# Elbow method to get best number of clusters
wcss = []
for i in range(1, 7):
    kmeans = KMeans(
        n_clusters=i, 
        init='k-means++', 
        max_iter=300, 
        n_init=10, 
        random_state=0
    )

    kmeans.fit(newArray)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 7), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# Kmeans itself
kmeans = KMeans(
    n_clusters=4, 
    init='k-means++', 
    max_iter=300, 
    n_init=10, 
    random_state=0
)
pred_y = kmeans.fit_predict(newArray)
print("KMEANS for n_clusters = 4")
print(pred_y)

labels, counts = np.unique(pred_y, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.suptitle('Number of elements/cluster')
plt.title("n_clusters = 4")
plt.xlabel('Cluster')
plt.ylabel('Number of elements')
plt.show()