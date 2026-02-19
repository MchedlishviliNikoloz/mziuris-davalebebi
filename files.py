file = open("files/names.txt")
# print(file.read()) # mtliani file dabechdva
# print(file.readline()) # ukve mdgomi xazis dabechdva
# print(file.readlines()) # satitao xazis listshi chagdeba
# file.seek(0) # wasakitxi (zolis) mititeba(nebismieri ricxvi)/dareseteba (0)
file.close() # daxurva aucilebelia mexsierebistvis

# igive ciklia, gasvla avtomaturi close aris -->
with open("files/names.txt") as file:
    print(file.read()) # mtliani file dabechdva
    print(file.readline()) # ukve mdgomi xazis dabechdva
    print(file.readlines()) # satitao xazis listshi chagdeba
    file.seek(0) # wasakitxi (zolis) mititeba(nebismieri ricxvi)/dareseteba (0)