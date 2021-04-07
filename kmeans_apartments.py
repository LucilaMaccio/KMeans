import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

X = [
   {
      "Tipo de inmueble":"Casa o chalet",
      "Orientación":"Sur",
      "Estado":"A reformar",
      "Antigüedad":"30 a 50 años",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Calefacción":True,
      "Jardín Privado":True,
      "Terraza":True,
      "Trastero":True,
      "Piscina":True,
      "Alarma":True,
      "Puerta Blindada":True,
      "price":"1975000",
      "rooms":"4",
      "bathrooms":"4",
      "house_size":"600",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Dúplex",
      "Antigüedad":"10 a 20 años",
      "Planta":"2ª planta",
      "Ascensor":"Sí",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Calefacción":True,
      "Gres Cerámica":True,
      "Parquet":True,
      "Trastero":True,
      "Puerta Blindada":True,
      "Cocina Equipada":True,
      "price":"340000",
      "rooms":"3",
      "bathrooms":"2",
      "house_size":"75",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa o chalet",
      "Orientación":"Sureste",
      "Agua caliente":"Gas Natural",
      "Calefacción":"Gas Natural",
      "Estado":"Bien",
      "Antigüedad":"30 a 50 años",
      "Planta":"Bajos",
      "Parking":"Privado",
      "Consumo energía":"C300 kW h m² / año",
      "Emisiones":"C300 kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Gres Cerámica":True,
      "Jardín Privado":True,
      "Parquet":True,
      "Terraza":True,
      "Trastero":True,
      "Cocina Office":True,
      "Suite - con baño":True,
      "Electrodomésticos":True,
      "Horno":True,
      "Lavadora":True,
      "Microondas":True,
      "Nevera":True,
      "TV":True,
      "Balcón":True,
      "Internet":True,
      "Zona Infantil":True,
      "Puerta Blindada":True,
      "Lavadero":True,
      "Cocina Equipada":True,
      "price":"785000",
      "rooms":"5",
      "bathrooms":"4",
      "house_size":"260",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa o chalet",
      "Orientación":"Sureste",
      "Agua caliente":"Gas Natural",
      "Calefacción":"Gas Natural",
      "Estado":"Muy bien",
      "Antigüedad":"10 a 20 años",
      "Planta":"Bajos",
      "Parking":"Privado",
      "Amueblado":"No",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Jardín Privado":True,
      "Terraza":True,
      "Cocina Office":True,
      "Piscina":True,
      "Suite - con baño":True,
      "Electrodomésticos":True,
      "Horno":True,
      "Lavadora":True,
      "Microondas":True,
      "Nevera":True,
      "Balcón":True,
      "Jacuzzi":True,
      "Alarma":True,
      "Puerta Blindada":True,
      "Lavadero":True,
      "Baño de huéspedes":True,
      "Cuarto lavado plancha":True,
      "Cuarto para el servicio":True,
      "Porche cubierto":True,
      "Cocina Equipada":True,
      "price":"1780000",
      "rooms":"5",
      "bathrooms":"5",
      "house_size":"491",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Piso",
      "Parking":"Privado",
      "Ascensor":"Sí",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Calefacción":True,
      "Parquet":True,
      "Trastero":True,
      "Z. Comunitaria":True,
      "Cocina Office":True,
      "Serv. portería":True,
      "Piscina comunitaria":True,
      "price":"750000",
      "rooms":"3",
      "bathrooms":"3",
      "house_size":"144",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa adosada",
      "Orientación":"Sur",
      "Calefacción":"Gas Natural",
      "Estado":"Bien",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Jardín Privado":True,
      "Parquet":True,
      "Terraza":True,
      "Trastero":True,
      "Piscina":True,
      "Electrodomésticos":True,
      "Alarma":True,
      "Puerta Blindada":True,
      "Cocina Equipada":True,
      "price":"1650000",
      "rooms":"5",
      "bathrooms":"6",
      "house_size":"500",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Piso",
      "Orientación":"Suroeste",
      "Estado":"Casi nuevo",
      "Antigüedad":"10 a 20 años",
      "Planta":"1ª planta",
      "Parking":"Privado",
      "Ascensor":"Sí",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Calefacción":True,
      "Parquet":True,
      "Trastero":True,
      "Z. Comunitaria":True,
      "Cocina Office":True,
      "Suite - con baño":True,
      "Zona Infantil":True,
      "Puerta Blindada":True,
      "Piscina comunitaria":True,
      "Lavadero":True,
      "Cocina Equipada":True,
      "price":"748000",
      "rooms":"3",
      "bathrooms":"3",
      "house_size":"144",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa o chalet",
      "Antigüedad":"20 a 30 años",
      "Parking":"Privado",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Calefacción":True,
      "Jardín Privado":True,
      "Terraza":True,
      "Piscina":True,
      "Gimnasio":True,
      "price":"1942500",
      "rooms":"4",
      "bathrooms":"5",
      "house_size":"316",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa o chalet",
      "Antigüedad":"5 a 10 años",
      "Parking":"Privado",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Armarios":True,
      "Calefacción":True,
      "Jardín Privado":True,
      "Terraza":True,
      "Trastero":True,
      "Z. Comunitaria":True,
      "Cocina Office":True,
      "Piscina":True,
      "Suite - con baño":True,
      "Electrodomésticos":True,
      "Serv. portería":True,
      "Alarma":True,
      "Zona Infantil":True,
      "Puerta Blindada":True,
      "Piscina comunitaria":True,
      "Cocina Equipada":True,
      "price":"950000",
      "rooms":"4",
      "bathrooms":"4",
      "house_size":"330",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa o chalet",
      "Calefacción":"Gas Natural",
      "Estado":"Bien",
      "Parking":"Privado",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Jardín Privado":True,
      "Parquet":True,
      "price":"720000",
      "rooms":"5",
      "bathrooms":"4",
      "house_size":"200",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa adosada",
      "Orientación":"Sureste",
      "Agua caliente":"Gas Natural",
      "Estado":"A reformar",
      "Antigüedad":"30 a 50 años",
      "Amueblado":"No",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Calefacción":True,
      "Gres Cerámica":True,
      "Jardín Privado":True,
      "Piscina":True,
      "Puerta Blindada":True,
      "Lavadero":True,
      "price":"985000",
      "rooms":"4",
      "bathrooms":"4",
      "house_size":"374",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa adosada",
      "Agua caliente":"Gas Natural",
      "Calefacción":"Gas Natural",
      "Estado":"Muy bien",
      "Planta":"Principal",
      "Parking":"Privado",
      "Amueblado":"No",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Gres Cerámica":True,
      "Jardín Privado":True,
      "Parquet":True,
      "Terraza":True,
      "Trastero":True,
      "Z. Comunitaria":True,
      "Cocina Office":True,
      "Piscina":True,
      "Suite - con baño":True,
      "Serv. portería":True,
      "Jacuzzi":True,
      "Gimnasio":True,
      "Bodega":True,
      "Sauna":True,
      "Pista de Tenis":True,
      "Alarma":True,
      "Videoportero":True,
      "Zona Deportiva":True,
      "Zona Infantil":True,
      "Puerta Blindada":True,
      "Piscina comunitaria":True,
      "Lavadero":True,
      "Ascensor interior":True,
      "Baño de huéspedes":True,
      "Cuarto lavado plancha":True,
      "Cuarto para el servicio":True,
      "Porche cubierto":True,
      "Cocina Equipada":True,
      "price":"2970000",
      "rooms":"7",
      "bathrooms":"9",
      "house_size":"1100",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Piso",
      "Orientación":"Noroeste",
      "Agua caliente":"Gas Natural",
      "Calefacción":"Gas Natural",
      "Estado":"Bien",
      "Antigüedad":"30 a 50 años",
      "Planta":"1ª planta",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Armarios":True,
      "Parquet":True,
      "Terraza":True,
      "Trastero":True,
      "Electrodomésticos":True,
      "Puerta Blindada":True,
      "Lavadero":True,
      "Cocina Equipada":True,
      "price":"275000",
      "rooms":"2",
      "bathrooms":"1",
      "house_size":"70",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Piso",
      "Orientación":"Noroeste",
      "Agua caliente":"Gas Natural",
      "Calefacción":"Gas Natural",
      "Estado":"Bien",
      "Antigüedad":"20 a 30 años",
      "Planta":"1ª planta",
      "Parking":"Privado",
      "Ascensor":"Sí",
      "Amueblado":"No",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Armarios":True,
      "Gres Cerámica":True,
      "Parquet":True,
      "Terraza":True,
      "Z. Comunitaria":True,
      "Cocina Office":True,
      "Suite - con baño":True,
      "Videoportero":True,
      "Zona Deportiva":True,
      "Zona Infantil":True,
      "Piscina comunitaria":True,
      "Cocina Equipada":True,
      "price":"670000",
      "rooms":"4",
      "bathrooms":"3",
      "house_size":"158",
      "location":"Aravaca"
   },
   {
      "Tipo de inmueble":"Casa o chalet",
      "Estado":"Muy bien",
      "Planta":"Bajos",
      "Parking":"Privado",
      "Consumo energía":"G999 kW h m² / año",
      "Emisiones":"En trámite- kg CO₂ m² / año",
      "Aire acondicionado":True,
      "Jardín Privado":True,
      "Terraza":True,
      "Trastero":True,
      "Piscina":True,
      "Cocina Equipada":True,
      "price":"990000",
      "rooms":"5",
      "bathrooms":"5",
      "house_size":"360",
      "location":"Aravaca"
   }
]

newArray=[]

print("longitud X =", len(X))

for i in range(0,len(X)):
    element=X[i]
    tipoInmueble=element["Tipo de inmueble"]
    location=element["location"]
    price=element["price"]

    finalApartment=[]

    if tipoInmueble == "Casa o chalet":
        finalApartment.append(0)
    elif tipoInmueble == "Piso":
        finalApartment.append(1)
    elif tipoInmueble == "Casa adosada":
        finalApartment.append(2)
    elif tipoInmueble == "Dúplex":
        finalApartment.append(3)
    else:
        finalApartment.append(-1)

    if location == "Casa de campo":
        finalApartment.append(91)
    elif location == "Argüelles":
        finalApartment.append(92)
    elif location == "Ciudad Universitaria":
        finalApartment.append(93)
    elif location == "Valdezarza":
        finalApartment.append(94)
    elif location == "Valdemarin":
        finalApartment.append(95)
    elif location == "El Plantio":
        finalApartment.append(96)
    elif location == "Aravaca":
        finalApartment.append(97)
    else:
        finalApartment.append(-1)

    finalApartment.append(price)

    newArray.append(finalApartment)

finalArray = np.array(newArray)

print("longitud finalArray =", len(finalArray))
print(finalArray)

wcss = []
for i in range(1, 15):
    kmeans = KMeans(
        n_clusters=i, 
        init='k-means++', 
        max_iter=300, 
        n_init=10, 
        random_state=0
    )

    kmeans.fit(newArray)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 15), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


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

# añadir visualizacion con diagrama de barras o algo similar