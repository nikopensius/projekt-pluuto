from random import randint

f = open("küsimused.txt", "r", encoding = "UTF-8")

sõnastik = {}
võti = ""
jada = []

for rida in f:
    if rida[0].isdigit():
        if jada != []:
            sõnastik[võti] = jada
        võti = rida
        jada = []
    else:
        jada.append(rida)

while True:
    i = randint(0, len(sõnastik))
    küss = list(sõnastik.keys())[i]
    print(küss)
    for j in sõnastik[küss]:
        if "+" in j:
            print(j[:-2] + "\n")
        else:
            print(j)
    vastus = input("Trüki õige vastuse täht")
        







"""
from random import randint
# Pluuto 2 - kinnikatja

lause = "Tere, mina olen Gustav Nikopensius"
jada = lause.split()

uus_lause = ""

# mitmes sõna lukku läheb
mitmes = randint(0, len(jada))

# loop paneb lause uuesti kokku ja katab ühe lambist valitud sõna kinni
for sõna in jada:
    if jada.index(sõna) == mitmes:
        uus_lause = uus_lause + "====" + " "
    else:
        uus_lause = uus_lause + sõna + " "
print(uus_lause)"""