import matplotlib.pyplot as plt

nimi = input("nimi: ")

for num in range(10):
    try:
        vea_sagedus = {"järjestatud": [], "järjestamata": [], "võrdsed": []}
        f = open(nimi + str(num) + ".txt")
        for rida in f:
            rida = rida.split()
            vea_sagedus[rida[0]].append(rida[1])
        for kat in vea_sagedus:
            plt.plot(vea_sagedus[kat], label = str(kat))
        plt.ylabel("Vigade arv")
        plt.xlabel("Sessioon")
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
        plt.show()
    except:
        pass
    
