def LuoNimetJaArvosanat():
    lista = {}

    while True:

        # Jos käyttäjä sanoo loppu, ohjelma loppuu
        nimi = input("Anna nimi. Jos haluat lopettaa kirjoita LOPPU: ")
        if nimi == "LOPPU":
            break
# Jos henkilön nimi on jo listassa annetaan ilmoitus
        elif nimi in lista:
            print('Henkilön tiedot jo syötetty')

# Kysytään henkilön arvosanaa ja lisätään tiedot listaan
        else:
            while True:
                try:
                    arvo = int(input("Anna arvosana: "))
                except ValueError:
                    print("Virheellinen vastus")
                    continue
                else:
                    break
            if arvo>5:
                arvo=5
            elif arvo<0:
                arvo=0

            lista[nimi]=arvo
    return lista




def TulostaKaikki(para):
    for key, value in para.items():
        print(key, value)

#Saa parametrina listan ja tulostaa sieltä kaikki nimit jotka ovat saaneet hylätyn
def TulostaHylatyt(para):
    for key, value in para.items():
        if value == 0:
            print(key, value)
       

def PalautaHylattyjenMaara(para):
    i=0
    for key, value in para.items():
        if value == 0:
            i=i+1
            
    print(i)




if __name__ == "__main__":
    # Write main program below this line
    #teen funktiosta helposti käytettävän muutujan
    paras= LuoNimetJaArvosanat()
    TulostaKaikki(paras)
    PalautaHylattyjenMaara(paras)
    TulostaHylatyt(paras)