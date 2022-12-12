file='nimi.txt'
word = input('Anna nimesi: ')
yht=len(word)
nimi = word[::-1]


if yht>18:
  print('Virhe!')

else: 

  wfile=open(file, 'wt')
  wfile.close()

#for loop, joka kiertää sanan pituuden ajan
  for i in range(len(word)):
    for j in range(len(word)):

      #Kitjainten tulostus
        if yht-i == j+1:
            print(nimi[i], end="")
            wfile=open(file, 'a')

            #lisää merkki tiedostoon
            wfile.write(str(nimi[i]))
            wfile.close()

#välien tulostus
        else:

            print('  ', end="")

            wfile=open(file, 'a')

            #lisää luku tiedostoon
            wfile.write(str('  '))
            wfile.close()
    print()
    wfile=open(file, 'a')

            #lisää luku tiedostoon
    wfile.write(str('\n'))
    wfile.close()