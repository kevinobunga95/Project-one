Cars = {"Subaru Forester" : {"Model":"Subaru", "Year of manufacture": 2017},
"Premo" : {"Model":"Toyota", "Year of manufacture ": 2020},
"x-Trail" : {"MOdel": "Nissan", "Year of manufacture" : 2023}}
print(Cars)

print(Cars["Subaru Forester"])
print(Cars["Premo"])
print(Cars["x-Trail"])

Additional_cars = {"fielder" : {"model": "Toyota", "Year of manufacture": 2019}, "CX5" : {"Model": "Mazda", "Year of manufacture" : 2023}}

Cars.update(Additional_cars)

print(Cars)
