def Farming(type, saison):
    if type == "fruits" and saison == "hiver":
        harvest = "Orange, mandarine et kiwi"
    elif type == "fruits" and saison == "ete":
        harvest = "Poire, fraise, cassis"
    elif type == "legumes" and saison == "hiver":
        harvest = "Carotte, topinambour, endive"
    elif type == "legumes" and saison == "ete":
        harvest = "Artichaut, aubergine, navet"

    print(harvest)

types = ["fruits", "legumes"]
saisons = ["ete", "hiver"]

for type in types:
    for saison in saisons:
        Farming(type, saison)