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

vea_sagedus = {"järjestatud": [], "järjestamata": [], "võrdsed": []}

kasutaja_nimi = input("Kirjuta oma nimi: ")

aput = int(input("Kui suuri arve täna liidame? "))


# avab programmi töö andmete jaoks kausta
try:
    õpiandmed = open(kasutaja_nimi + str(aput) + ".txt", "r")
    for rida in õpiandmed:
        rida = rida.split()
        vea_sagedus[rida[0]].append(rida[1])
    õpiandmed.close()
    õpiandmed = open(kasutaja_nimi + str(aput) + ".txt", "w")
except:
    õpiandmed = open(kasutaja_nimi + str(aput) + ".txt", "w")
        

op_list = []

# see jupp genereerib liidetavad, võtab arvesse eelmise sessiooni tulemused
if vea_sagedus["järjestatud"] != []:
    if vea_sagedus["järjestatud"][-1] < vea_sagedus["järjestamata"][-1]:
        for a in range(aput + 1):
            for b in range(a + 1):
                op_list.append((a, b))
    elif vea_sagedus["järjestatud"][-1] > vea_sagedus["järjestamata"][-1]:
        for a in range(aput + 1):
            for b in range(a + 1):
                op_list.append((b, a))
    # kui viimati polnud liidetavate järjestuses tulemuse kujunemisel vahet
    else:
        for a in range(aput + 1):
            for b in range(aput + 1):
                op_list.append((a, b))
# kui andmete fail on tühi:
else:
    for a in range(aput + 1):
        for b in range(aput + 1):
            op_list.append((a, b))

# siia loetakse arvutusvead, mis kasutaja teeb programmi töö jooksul
jatud_cnt = 0
jmata_cnt = 0
võrdsed_cnt = 0

# programmi põhitsükkel
# kasutajale esitatakse liitmistehted
# pop-funktsioon tõstab käesoleva liitmistehte operandide järjendist välja
# kasutaja vea korral, tõstetakse liitmistehe järjendisse tagasi ja suurendatakse vea-counterit
while op_list != []:
    operandid = op_list.pop(randint(0, len(op_list) - 1))
    vastus = input(str(operandid) + " ")
    
    if int(vastus) == sum(operandid):
        print("Tubli! Vastasid õigesti.")
    else:
        print("Vastasid valesti. Õige vastus on " + str(operandid[0]))
        op_list.append(operandid)
        
        if operandid[0] > operandid[1]:
            jatud_cnt += 1
        elif operandid[0] < operandid[1]:
            jmata_cnt += 1
        else:
            võrdsed_cnt += 1
        # kasutaja vea korral kujutatakse liitmistehet graafiliselt
        kujuta(operandid)

# kui tsükkel on lõppenud, tõstetakse tulemused (esinenud vigade arvud) vastavasse sõnastikku
vea_sagedus["järjestatud"].append(jatud_cnt)
vea_sagedus["järjestamata"].append(jmata_cnt)
vea_sagedus["võrdsed"].append(võrdsed_cnt)

# kogu sõnastik sisu salvestatakse tekstifaili (sh ka varasemate sessioonide tulemused)
for element in range(len(vea_sagedus["järjestatud"])):
    for järjend in vea_sagedus:
        õpiandmed.write(järjend + " " + str(vea_sagedus[järjend][element]) + "\n")
õpiandmed.close()