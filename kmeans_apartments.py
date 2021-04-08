import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

X = [
    {
        "price": "259000",
        "rooms": "3",
        "bathrooms": "1",
        "house_size": "73",
        "location": "Guindalera",
        "type": "Piso",
        "parking": "0",
        "elevator": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "299000",
        "rooms": "2",
        "bathrooms": "1",
        "house_size": "90",
        "location": "Guindalera",
        "type": "Piso",
        "elevator": "1",
        "parking": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "490000",
        "rooms": "4",
        "bathrooms": "2",
        "house_size": "110",
        "location": "Guindalera",
        "type": "Piso",
        "elevator": "1",
        "terraze": "1",
        "parking": "0",
        "pool": "0",
        "storage_room": "0"
    },
    {
        "price": "405760",
        "rooms": "4",
        "bathrooms": "2",
        "house_size": "93",
        "location": "Guindalera",
        "type": "Piso",
        "elevator": "1",
        "parking": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "495000",
        "rooms": "4",
        "bathrooms": "2",
        "house_size": "150",
        "location": "Guindalera",
        "type": "Piso",
        "elevator": "1",
        "parking": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "800000",
        "rooms": "4",
        "bathrooms": "3",
        "house_size": "213",
        "location": "Guindalera",
        "type": "Casa o chalet",
        "parking": "0",
        "elevator": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "890000",
        "rooms": "3",
        "bathrooms": "2",
        "house_size": "208",
        "location": "Guindalera",
        "type": "Casa adosada",
        "terraze": "1",
        "parking": "0",
        "elevator": "0",
        "pool": "0",
        "storage_room": "0"
    },
    {
        "price": "535000",
        "rooms": "3",
        "bathrooms": "2",
        "house_size": "110",
        "location": "Guindalera",
        "type": "Piso",
        "parking": "0",
        "elevator": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "397800",
        "rooms": "4",
        "bathrooms": "2",
        "house_size": "106",
        "location": "Guindalera",
        "type": "Piso",
        "elevator": "1",
        "parking": "0",
        "pool": "0",
        "storage_room": "0",
        "terraze": "0"
    },
    {
        "price": "550000",
        "rooms": "3",
        "bathrooms": "1",
        "house_size": "113",
        "location": "Guindalera",
        "type": "Piso",
        "elevator": "1",
        "terraze": "1",
        "parking": "0",
        "pool": "0",
        "storage_room": "0"
    },
    {
        "price": "N/A",
        "rooms": "N/A",
        "house_size": "N/A",
        "location": "N/A",
        "type": "N/A"
    },
    {
        "price": "870000",
        "rooms": "4",
        "bathrooms": "2",
        "house_size": "171",
        "location": "Legazpi de Madrid",
        "type": "Ático",
        "elevator": "1",
        "terraze": "1",
        "storage_room": "1",
        "pool": "1",
        "parking": "0"
    },
    {
        "price": "260000",
        "rooms": "1",
        "bathrooms": "1",
        "house_size": "47",
        "location": "Legazpi de Madrid",
        "type": "Apartamento",
        "elevator": "1",
        "storage_room": "1",
        "pool": "1",
        "parking": "0",
        "terraze": "0"
    },
    {
        "price": "N/A",
        "rooms": "N/A",
        "house_size": "N/A",
        "location": "N/A",
        "type": "N/A"
    },
    {
        "price": "N/A",
        "rooms": "N/A",
        "house_size": "N/A",
        "location": "N/A",
        "type": "N/A"
    },
    {
        "price": "499000",
        "rooms": "3",
        "bathrooms": "2",
        "house_size": "117",
        "location": "Legazpi de Madrid",
        "type": "Piso",
        "elevator": "1",
        "storage_room": "1",
        "pool": "1",
        "parking": "0",
        "terraze": "0"
    }
]

newArray=[]

print("longitud X =", len(X))

# data format
for i in range(0,len(X)):
    element=X[i]

    if len(element) != 11:
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
        finalApartment.append(int(rooms))
        finalApartment.append(int(bathrooms))
        finalApartment.append(int(house_size))

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

        finalApartment.append(int(elevator))
        finalApartment.append(int(storage_room))
        finalApartment.append(int(parking))
        finalApartment.append(int(pool))
        finalApartment.append(int(terraze))
        
        newArray.append(finalApartment)

finalArray = np.array(newArray)

print("longitud finalArray después de eliminar valores nulos =", len(finalArray))
print(finalArray)


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
print("KMEANS")
print(pred_y)

labels, counts = np.unique(pred_y, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()