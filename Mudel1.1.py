from random import randint

# kujutab valesti vastatud tehet graafiliselt
def kujuta(o):
    liidetavad = []
    for liidetav in o[1:]:
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
# kasutaja saab liidetavate suurust valida
aput = int(input("Kui suuri arve täna liidame? "))

# kui varasemalt on sama kasutaja sama suuri arve liitnud,
# loetakse varasemad tulemused programmi sisse
# eri kordade tulemusi veel võrrelda ei saa, kõik tulemused liidetakse praegu veel kokku
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

for a in range(aput):
    for b in range(aput):
        summa = a + b
        op_list.append((summa, a, b))


while op_list != []:
    operandid = op_list.pop(randint(0, len(op_list) - 1))
    vastus = input(str(operandid[1:]) + " ")
    
    if int(vastus) == operandid[0]:
        print("Tubli! Vastasid õigesti.")
    else:
        print("Vastasid valesti. Õige vastus on " + str(operandid[0]))
        op_list.append(operandid)
        
        if operandid[1] > operandid[2]:
            vea_sagedus["järjestatud"] += 1
        elif operandid[1] < operandid[2]:
            vea_sagedus["järjestamata"] += 1
        else:
            vea_sagedus["võrdsed"] += 1

        kujuta(operandid)

for element in vea_sagedus:
    õpiandmed.write(element + " " + str(vea_sagedus[element]) + "\n")
õpiandmed.close()