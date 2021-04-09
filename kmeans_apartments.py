import numpy as np
import json
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

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

        finalApartment.append(price)

        if house_size.isnumeric():
            finalApartment.append(int(rooms))
        else:
            # print("rooms with wrong format:", rooms)
            continue

        if house_size.isnumeric():
            finalApartment.append(int(bathrooms))
        else:
            # print("bathrooms with wrong format:", bathrooms)
            continue

        if house_size.isnumeric():
            finalApartment.append(int(house_size))
        else:
            # print("house_size with wrong format:", house_size)
            continue

        if location.find("Palacio") != -1:
            finalApartment.append(11)
        elif location.find("Embajadores") != -1: 
            finalApartment.append(12)
        elif location.find("Cortes") != -1: 
            finalApartment.append(13)
        elif location.find("Justicia") != -1: 
            finalApartment.append(14)
        elif location.find("Universidad") != -1: 
            finalApartment.append(15)
        elif location.find("Sol") != -1: 
            finalApartment.append(16)

        elif location.find("Imperial") != -1: 
            finalApartment.append(21)
        elif location.find("Acacias") != -1: 
            finalApartment.append(22)
        elif location.find("Chopera") != -1: 
            finalApartment.append(23)
        elif location.find("Legazpi") != -1: 
            finalApartment.append(24)
        elif location.find("Delicias") != -1: 
            finalApartment.append(25)
        elif location.find("Palos de Moguer") != -1: 
            finalApartment.append(26)
        elif location.find("Atocha") != -1: 
            finalApartment.append(27)

        elif location.find("Pacífico") != -1: 
            finalApartment.append(31)
        elif location.find("Adelfas") != -1: 
            finalApartment.append(32)
        elif location.find("Estrella") != -1: 
            finalApartment.append(33)
        elif location.find("Ibiza") != -1: 
            finalApartment.append(34)
        elif location.find("Jerónimos") != -1: 
            finalApartment.append(35)
        elif location.find("Niño Jesús") != -1: 
            finalApartment.append(36)

        elif location.find("Recoletos") != -1: 
            finalApartment.append(41)
        elif location.find("Goya") != -1: 
            finalApartment.append(42)
        elif location.find("Fuente del Berro") != -1: 
            finalApartment.append(43)
        elif location.find("Guindalera") != -1: 
            finalApartment.append(44)
        elif location.find("Lista") != -1: 
            finalApartment.append(45)
        elif location.find("Castellana") != -1: 
            finalApartment.append(46)

        elif location.find("Gaztambide") != -1: 
            finalApartment.append(71)
        elif location.find("Arapiles") != -1: 
            finalApartment.append(72)
        elif location.find("Trafalgar") != -1: 
            finalApartment.append(73)
        elif location.find("Almagro") != -1: 
            finalApartment.append(74)
        elif location.find("Rios Rosas") != -1: 
            finalApartment.append(75)
        elif location.find("Vallehermoso") != -1: 
            finalApartment.append(76)
        else: 
            finalApartment.append(-1)

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

        newArray.append(finalApartment)

finalArray = np.array(newArray)

print("length finalArray after removing null or strange values =", len(finalArray))
# print(finalArray)


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
    n_clusters=5, 
    init='k-means++', 
    max_iter=300, 
    n_init=10, 
    random_state=0
)
pred_y = kmeans.fit_predict(newArray)
print("KMEANS")
print(pred_y)

labels, counts = np.unique(pred_y, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()