from datetime import datetime
#Write class and imports here!

#main class
class tuote():
    def __init__(self, nimi, hinta, hylly, koodi):
        self.nimi=nimi
        self.hinta=hinta
        self.hylly=hylly
        self.koodi=koodi
    
     #Getterit
    @property
    def nimi(self):
        return self._nimi

    @property
    def hinta(self):
        return self._hinta
    
    @property
    def hylly(self):
        return self._hylly
    
    @property
    def koodi(self):
        return self._koodi

#setterit
    @nimi.setter
    def nimi(self, value):
        self._nimi=value

    @hinta.setter
    def hinta(self, value):
        self._hinta=value

    @hylly.setter
    def hylly(self, value):
        self._hylly=value

    @koodi.setter
    def koodi(self, value):
        self._koodi=value

    def __str__(self):
        # Huomaa, että käytettävä str funktiota numeeriseen tiedon kohdalla
        print( "Nimi:\t" + (self.nimi) +"\n"+ "Hinta:\t" +str(self.hinta) +'\n'+ "Hylly:\t"+ (self.hylly) +'\n'+ "Koodi:\t" + (self.koodi))
        return "Nimi:\t" + (self.nimi) +"\n"+ "Hinta:\t" +str(self.hinta) +'\n'+ "Hylly:\t"+ (self.hylly) +'\n'+ "Koodi:\t" + (self.koodi)
    
class ruoka(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, alkupera, paivays):
        tuote.__init__(self, nimi, hinta, hyllypaikka, koodi)
        self.alkupera=alkupera
        self.paivays=paivays


    @property
    def alkupera(self):
        return self._alkupera

    @property
    def paivays(self):
        return self._paivays

    @alkupera.setter
    def alkupera(self, value):
        self._alkupera=value

    @paivays.setter
    def paivays(self, value):
        self._paivays=value

    def __str__(self):
        super().__str__()
        print('Alkuperä:\t', self.alkupera)
        print('Paivys:\t', self.paivays)
        return ''

   


class vaate(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, koko, materiaali):
        tuote.__init__(self, nimi, hinta, hyllypaikka, koodi)
        self.koko=koko
        self.materiaali=materiaali

    @property
    def koko(self):
        return self._koko

    
    @property
    def materiaali(self):
        return self._materiaali

    @koko.setter
    def koko(self, value):
        self._koko=value

    @materiaali.setter
    def materiaali(self, value):
        self._materiaali=value

    def __str__(self):
        super().__str__()
        print('Koko:\t', self.koko)
        print('Materiaali:\t', self.materiaali)
        return ''


class kodinkone(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, paino, takuu):
        tuote.__init__(self, nimi, hinta, hyllypaikka, koodi)
        self.takuu=takuu
        self.paino=paino

    @property
    def paino(self):
        return self._paino

    @property
    def takuu(self):
        return self._takuu

    @takuu.setter
    def takuu(self, value):
        self._takuu=value

    @paino.setter
    def paino(self, value):
        self._paino=value

    def __str__(self):
        super().__str__()
        print('Takuu:\t', self.takuu)
        print('Paino:\t', self.paino)
        return ''



if __name__ == "__main__":
    #Main program here!

    tuote_lista=[]


    while True:
        alku=input('Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus): ')
        if alku=='1' or alku=='2' or alku=='3':
            nimi=input('Anna tuotteen nimi: ')
            hinta=float(input('Anna hinta: '))
            hylly=input('Anna hyllypaikka: ')
            koodi=input('Anna koodi: ')
            if alku=='1':
                alkupera=input('Ruuan alkuperämaa: ')
                paivays=input('Päiväys: ')
                tuote_lista.append(ruoka(nimi, hinta, hylly, koodi, alkupera, paivays))
            if alku=='2':
                koko=input('Vaatteen koko: ')
                materiaali=input('Vaatteen materiaali: ')
                tuote_lista.append(vaate(nimi, hinta, hylly, koodi, koko, materiaali))
            if alku=='3':
                takuu=input('Takuu: ')
                paino=input('Paino: ')
                tuote_lista.append(kodinkone(nimi, hinta, hylly, koodi, takuu, paino))
        else:
            break

    for i in tuote_lista:
        print(i)
    