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