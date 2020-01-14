import random
from random import randint

f = open("küsimused.txt", "r", encoding = "UTF-8")

sõnastik = {}

for rida in f:
    
    rida = rida.strip()
    
    if rida == "": # igale küsimuse-vastuste-plokile järgneb tekstifailis tühi rida, seda pole meil vaja
        pass
    
    elif rida[0].isdigit(): # pmst kui rida on küsimus (algab nr-iga), tehakse temast võti ja tema väärtus on tühi järjend
        võti = rida
        sõnastik[võti] = []
    
    else:
        sõnastik[võti].append(rida) # see lisab kõik küsimusele järgnevad vastused tema väärtuse järjendisse

f.close()

# tekstifail avati, ta sisu loeti sõnastikku,
# järjenumbriga algavad küsimused on sõnastiku võtmed,
# tekstifaili tühjad read jäeti vahele,
# küsimusele järgnenud read (vastused) lisati järjendisse, mis on küsimusele vastav väärtus
# tekstifail pandi kinni



jrk_numbrid = ['1. ','2. ', '3. ', '4. ', '5. ', '6. ', '7. ']

def print_vastus(number, väärtus):
    if len(väärtus) == 0: # rekursiooni baas
        return
    
    else:
        if '+' in väärtus[0]: # õiged vastused on markeeritud '+'-märgiga sõne lõpus
            print(number[0] + väärtus[0][:-1]) # see jupp prindib vastuse ilma '+'-ita
            õige_vastus.append(number[0]) # see jupp paneb õige vastuse jrk-numbri kontrollimiseks vastavasse järjendisse
            
        else:
            print(number[0] + väärtus[0]) # prindib vale vastusevariandi

        print_vastus(number[1:], väärtus[1:]) # prindib järgmise vastuse-variandi

"""def blanker(järjend):
    for lause in järjend:
        
        jada = lause.split() #teeb lausest jada, mida on lihtsam töödelda
        
        mitmes = randint(0, len(jada))
        # loop paneb lause uuesti kokku ja katab ühe lambist valitud sõna kinni
        
        uus_lause = ""
        
        for sõna in jada:
            if jada.index(sõna) == mitmes:
                uus_lause = uus_lause + "====" + " "
            else:
                uus_lause = uus_lause + sõna + " "
                
        print(uus_lause)"""

while True:
    
    võtme_list = list(sõnastik.keys()) # Siin lükkame võtmete listi segamini, et küsimusi lambis järjekorras esitada
    random.shuffle(võtme_list)
    
    for võti in võtme_list: # siin prindime ühe küsimuse ja tema vastusevariandid
        print(võti) # küsimus
        
        random.shuffle(sõnastik[võti]) # vastusevariandid lampi järjekorda
        
        õige_vastus = []
        print_vastus(jrk_numbrid, sõnastik[võti]) # prindib lambis järjekorras vastused ilusti korrastatud jrk-numbritega
    
        kasutaja_vastus = input("Sisesta õige vastuse number: ")
        
        if kasutaja_vastus in õige_vastus[0]:
            print("Õige vastus!")

        
