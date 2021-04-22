import json
from collections import OrderedDict
from itertools import islice
from openpyxl import load_workbook

# --------------------------------------------------------------------------------------
# POC
# --------------------------------------------------------------------------------------

# Open the workbook and select a worksheet
# wb = load_workbook("C:/Users/lucil/OneDrive/EAE/TFM/poc_xlsx_to_json.xlsx")

# sheet = wb['Cars']

# # List to hold dictionaries
# cars_list = []

# # Iterate through each row in worksheet and fetch values into dict
# for row in islice(sheet.values, 1, sheet.max_row):
#     cars = OrderedDict()
#     cars['car-id'] = row[0]
#     cars['maker'] = row[1]
#     cars['model'] = row[2]
#     cars['miles'] = row[3]

#     print(cars)

#     cars_list.append(cars)

# # Serialize the list of dicts to JSON
# j = json.dumps(cars_list)

# # Write to file
# with open('data.json', 'w') as f:
#     f.write(j)


# --------------------------------------------------------------------------------------
# PHARMACIES
# --------------------------------------------------------------------------------------

wb = load_workbook("C:/Users/lucil/OneDrive/EAE/TFM/datasets/xlsx/turnosmadrid_guardia_2021.xlsx")

sheet = wb['turnosmadrid_guardia_2021']

# List to hold dictionaries
pharmacies_list = []

# Iterate through each row in worksheet and fetch values into dict
for row in islice(sheet.values, 1, sheet.max_row):
    pharmacies = OrderedDict()
    pharmacies['identifier'] = row[3]
    pharmacies['location'] = row[1]
    pharmacies['address'] = row[4]
    pharmacies['service_type'] = row[5]

    # print(pharmacies)

    alreadyExists = False

    if len(pharmacies_list) == 0:
        pharmacies_list.append(pharmacies)
    else:
        for pharmacy in pharmacies_list:
            if pharmacy['identifier'] == pharmacies['identifier']:
                alreadyExists = True
        
        if not alreadyExists:
            pharmacies_list.append(pharmacies)

print(len(pharmacies_list))

# Serialize the list of dicts to JSON
j = json.dumps(pharmacies_list, ensure_ascii=False)

# Write to file
with open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/pharmacies.json', 'w', encoding='utf-8') as f:
    f.write(j)

# --------------------------------------------------------------------------------------
# GREEN ZONES
# --------------------------------------------------------------------------------------

wb = load_workbook("C:/Users/lucil/OneDrive/EAE/TFM/datasets/xlsx/IZVER_ZONAS_VERDES_2019.xlsx")

sheet = wb['IZVERD_2019_CLEANED']

# List to hold dictionaries
greenZones_list = []

# Iterate through each row in worksheet and fetch values into dict
for row in islice(sheet.values, 1, sheet.max_row):
    greenZones = OrderedDict()
    greenZones['identifier'] = row[3]
    greenZones['location'] = row[0]
    greenZones['address'] = row[5]
    greenZones['size'] = row[7]

    # print(greenZones)

    greenZones_list.append(greenZones)

print(len(greenZones_list))

# Serialize the list of dicts to JSON
j = json.dumps(greenZones_list, ensure_ascii=False)

# Write to file
with open('C:/Users/lucil/OneDrive/EAE/TFM/datasets/json/greenZones.json', 'w', encoding='utf-8') as f:
    f.write(j)