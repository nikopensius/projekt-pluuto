from random import randint

# kujutab valesti vastatud tehet graafiliselt
def kujuta(o):
    liidetavad = []
    for liidetav in o:
        kujutis = ""
        if liidetav == 0:
            kujutis += " "
        else:
            for jupp in range(liidetav):
                kujutis += "o"
        liidetavad.append(kujutis)
    print(liidetavad[0] + " + " + liidetavad[1] + " = " + liidetavad[0] + liidetavad[1])

vea_sagedus = {"järjestatud": 0, "järjestamata": 0, "võrdsed": 0}

kasutaja_nimi = input("Kirjuta oma nimi: ")

aput = int(input("Kui suuri arve täna liidame? "))

# avab programmi töö andmete jaoks kausta
# kui samanimeline kaust on juba olemas, loeb sealt alguses andmed sisse,
# mida programmi töö käigus täiendab
try:
    õpiandmed = open(kasutaja_nimi + str(aput) + ".txt", "r")
    for rida in õpiandmed:
        rida = rida.split()
        vea_sagedus[rida[0]] = int(rida[1])
    õpiandmed.close()
    õpiandmed = open(kasutaja_nimi + str(aput) + ".txt", "w")
except:
    õpiandmed = open(kasutaja_nimi + str(aput) + ".txt", "w")
        

op_list = []

# liigutasin summa arvutamise while-tsükli kehasse (võrreldes mudel1.1ga)
# liidetavate generaator arvestab nüüd ka varasemaid andmeid :)
if vea_sagedus["järjestatud"] < vea_sagedus["järjestamata"]:
    for a in range(aput + 1):
        for b in range(a + 1):
            op_list.append((a, b))
elif vea_sagedus["järjestatud"] > vea_sagedus["järjestamata"]:
    for a in range(aput + 1):
        for b in range(a + 1):
            op_list.append((b, a))
else:
    for a in range(aput + 1):
        for b in range(aput + 1):
            op_list.append((a, b))


while op_list != []:
    operandid = op_list.pop(randint(0, len(op_list) - 1))
    vastus = input(str(operandid) + " ")
    
    if int(vastus) == sum(operandid):
        print("Tubli! Vastasid õigesti.")
    else:
        print("Vastasid valesti. Õige vastus on " + str(operandid[0]))
        op_list.append(operandid)
        
        if operandid[0] > operandid[1]:
            vea_sagedus["järjestatud"] += 1
        elif operandid[0] < operandid[1]:
            vea_sagedus["järjestamata"] += 1
        else:
            vea_sagedus["võrdsed"] += 1

        kujuta(operandid)

for element in vea_sagedus:
    õpiandmed.write(element + " " + str(vea_sagedus[element]) + "\n")
õpiandmed.close()