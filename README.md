# projekt-pluuto

23.12 18:50
Mudel1.1 - Tuleks juurde kirjutada rekursiivne funktsioon, mis
		1) väljastab juhuslikus järjekorras liitmistehted, kus vastavalt eelistusele on esimene liige
		   ainult väiksem-võrdne või ainult suurem-võrdne kui talle järgnev liidetav.
		2) seejärel väljastab ülejäänud liitmistehted vastupidises järjekorras, nii et üks versioon
		   programmi tööst näeks välja selline:
		   (2, 0)
		   (1, 1)
		   (1, 0)
		   (2, 1)
		   (2, 2)
		   (1, 2)
		   (0, 1)
		   (0, 2)
		   Sedamoodi tekib justkui palindroom.
		*) selle, missuguses järjekorras tehted väljastatakse, otsustab programm vastavalt olemasolevatele
		   andmetele, mida ta loeb tekstifailidest, mis on moodustatud programmi varasema töö käigus.
		   See on harjutus, et panna programmi juhinduma varasemalt kogutud andmetest.

24.12 13:00
Mudel1.2 - Rekursiivne funktsioon kirjutamata. See-eest oskab programm arvestada varasemalt kogutud andmetega:
		esitab õppurile tehted tema jaoks lihtsamal kujul - liidetavate generaator järjestab liidetavad
		vastavalt eelnevalt kogutud andmetele, kas suurem liidetav enne või väiksem liidetav enne
	   Edasine samm:
		Programm peab arvestama ka kasutaja edusamme ning tooma sisse keerulisemaid ülesandeid:
			*) kui õppuril on "2 + 1 = 3" väga hästi selge, esitab programm pärast järgmist
			   "2 + 1 = 3" tehet "1 + 2 = 3" tehte.

25.12 13:40
Mudel 1.2.1 - Eri sessioonide tulemused on tekstifailis eristatavad,
	      tulemused salvestatakse sõnastikuse asuvasse järjendisse.