# kriittinen piste
KR_PISTE = 90

# Hypyn pituus


def KysyHypynPituus():

    while True:
       # kysytään pisteet
        try:
            hyppy = float(input('Mikä oli hypyn pituus '))

            # jos annetaan jotain muuta kuin nro, kysytään uudestaan
        except ValueError:
            print("Virheellinen vastus")
            continue
        else:
            return hyppy


# Tuomaripisteet
def KysyTuomareidenPisteet():

    # luodaan lista
    tuomarit = []
    count = 0

    while count < 5:

        count = count+1

# tuomari + kyseinen kierros
        Tuomari = 'Tuomari ' f'{count}'

        pisteet = -1

# loop kiertää kunnes pisteet on väliltä 0-20
        while(pisteet < 0 or pisteet > 20):
#loop kiertää kunnes annetaan numero
            while True:
                try:
                    # kysytään pisteet
                    pisteet = float(input(Tuomari + ' pisteet: '))
                    # jos annetaan jotain muuta kuin nro, kysytään uudestaan
                except ValueError:
                    print("Virheellinen vastus")
                    continue
                else:
                    break
                    # isketään pisteet listaan
        tuomarit.append(pisteet)
    return tuomarit


def LaskeHypynPisteet(pituus, piste):

#tuomaripisteet yhteensä
    a = sum(piste)


    suurin= max(piste)#suurin
    pienin=min(piste)#pienin

#Vähennetään se suurin ja pienin niistä yhteispisteistä
    yht=a-suurin-pienin

#lasketaan lopulliset pisteet
    pisteet = (pituus - KR_PISTE) * 1.8 + yht + 60

    print(round(pisteet))


if __name__ == "__main__":
    # Write main program below this line

    

    pituus = KysyHypynPituus()
    piste = KysyTuomareidenPisteet()
    print(round(pituus))
    LaskeHypynPisteet(pituus, piste)