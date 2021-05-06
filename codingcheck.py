#practice coding using lists and functions

costumelst =["socks", "shoes", "bluedress", "solodress"]
clotheslst = ["shorts", "tshirts", "sweaters"]

packinglst = [costumelst + clotheslst]
print(packinglst)

spackinglst = [x for x in clotheslst if "t" in x]
print(spackinglst)
