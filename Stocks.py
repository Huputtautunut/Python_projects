import math



class Osake():
    def __init__(self, nimi='nimi', ostohinta=0, maara=0):
        self.nimi=nimi
        self.ostohinta=ostohinta
        self.maara=maara

    

    #getters
    @property
    def nimi(self): #palauttaa_nimi muuttujan arvon
        return self._nimi

    

    @property
    def ostohinta(self): #palauttaa_ostohinta muuttujan arvon
        return self._ostohinta

    
    @property
    def maara(self): #palauttaa_maara muuttujan arvon
        return self._maara


     #setters  

    @nimi.setter
    def nimi(self, value):
        self._nimi=value

    @ostohinta.setter
    def ostohinta(self, value):
        if value<0:
            value=0
        else:
            self._ostohinta=value

    @maara.setter
    def maara(self, value):
        if value<0:
            value=0
        else:   
            self._maara=value
    
    @staticmethod
    def laske_tuotto_yhdelle_vuodelle(kasvuprosentti, hinta):
        tuotto = hinta*kasvuprosentti/100
        return tuotto

    @classmethod
    def tulosta_arvo (cls, kasvuprosentti, ajanjakso,hinta):
        Amount = hinta * (pow((1 + kasvuprosentti / 100), ajanjakso))
        CI = Amount - hinta
        return CI




if __name__ == "__main__":
    # Write main program here

    lista=[]

    lisaa='k'

while lisaa=='k' or lisaa=='K':
    nimi=input('Anna osakkeen nimi: ')
    ostohinta=float(input('Anna osakkeen ostohinta/kpl: '))
    maara=float(input('Anna ostettujen osakkeiden lukumäärä: '))

    #lisätään tiedot listaan ja niistä tulee Osake olioita?
    lista.append(Osake(nimi, ostohinta, maara))
    
    lisaa=input('Lisää osakkeita (k/e)? ' )

kasvu=float(input('Anna kasvuprosentti: '))
vuodet=int(input('Anna vuodet: '))

print(Osake.laske_tuotto_yhdelle_vuodelle(kasvu, ostohinta))
#10 000


#print(Osake.tulosta_arvo(kasvu, vuodet))

koko=0
for osake in lista:
    #Tuloste esim nokia, 12, 12
    #haetaan listasta osake olio ja tulostetaan se
    print(osake.nimi, osake.maara, str("{:.1f}".format(osake.ostohinta)))
    #osakepotin arvo alussa
    alku=osake.maara * osake.ostohinta
    hinta=osake.ostohinta*osake.maara
    amount=hinta * (pow((1 + kasvu / 100), vuodet))
    CI = amount - hinta
    arvo=(CI)+osake.maara * osake.ostohinta

    print('Osakkeen potin arvo on '+str("{:.2f}".format(arvo))+' ja tuotto '+str("{:.2f}".format(CI)))
    koko = koko+arvo
print('Koko potin arvo on '+ str("{:.2f}".format(koko)))