from random import randint

# programmi alguses küsitakse kasutajalt tema nime
# luuakse vastav tekstifail, kuhu salvestatakse sessiooni tulemused
kasutaja_nimi = input("Kirjuta oma nimi: ")
õpiandmed = open(kasutaja_nimi + ".txt", "w")

# programm, mis genereerib kasutajale lahendamiseks liitmistehteid
# programm registreerib, kas vastus on õige või vale ja fikseerib tulemuse
# kas kasutaja edu sõltub sellest, millises järjekorras on operandid?
# hüpotees: lihtsam on arvutada, kui esimene operand on suurema väärtusega kui talle järgnev

op_list = []

for a in range(3):
    for b in range(3):
        summa = a + b
        op_list.append((summa, a, b))

    # siia kogutakse arvutamise tulemused
    # kui mitu korda eksis kasutaja, kui iga operand oli järgnevast suurem ja vv
vea_sagedus = {"järjestatud": 0, "järjestamata": 0, "võrdsed": 0}

    # tsükkel kestab, kuniks operandide listis on veel operande,
    # mille liitmistehtele pole kasutaja õiget vastust andnud
while op_list != []:
    # eemaldab operandide enniku listist ja väljastab liidetavad kasutajale
    operandid = op_list.pop(randint(0, len(op_list) - 1))
    vastus = input(operandid[1:])
    
    # kui kasutaja vastab õigesti, väljastatakse tagasiside ja järgmine tehe
    # kui kasutaja vastab valesti, pannakse operandid listi tagasi
    # ja väljastatakse tagasiside ning järgmine tehe
    if int(vastus) == operandid[0]:
        print("Tubli! Vastas õigesti.")
    else:
        print("Vastasid valesti. Õige vastus on " + str(operandid[0]))
        op_list.append(operandid)
        
        # järgnev jupp on kirjutatud kahe liidetavaga tehete jaoks
        # tasub ära muuta, et tehe võiks olla kui pikk tahes
        if operandid[1] > operandid[2]:
            vea_sagedus["järjestatud"] += 1
        elif operandid[1] < operandid[2]:
            vea_sagedus["järjestamata"] += 1
        else:
            vea_sagedus["võrdsed"] += 1

# kirjutab kogutud andmed tekstifaili
for element in vea_sagedus:
    õpiandmed.write(element + ": " + str(vea_sagedus[element]))
õpiandmed.close()