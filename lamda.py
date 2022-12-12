summa = lambda a=1, b=1 : a + b
tulo = lambda a=1, b=1 : a * b

def laske(function, luvut):
    
    if len(luvut)==0:
        return 0

    if len(luvut)==1:
        return luvut[0]

    tulos=function(luvut[0], luvut[1])
    laskuri=0
    for luku in luvut:
        laskuri+=1
        if laskuri <=2:
            continue
        tulos = function(tulos, luku)
    
    return tulos



if __name__ == "__main__":
    luvut = [1,5,8,11,3]
    print(laske(tulo, luvut))
    print(laske(summa, luvut))

    luvut = [4]
    print(laske(tulo, luvut))
    print(laske(summa, luvut))

    luvut = []
    print(laske(tulo, luvut))
    print(laske(summa, luvut))
