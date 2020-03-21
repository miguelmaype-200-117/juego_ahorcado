# -*- coding: utf-8 -*-
import os
import random
import words
images=['''

+--------------------+
║                    ║
║                    ║
║
║
║
║
║
║
║
║
║
║
║
║
║
===============================''','''

+--------------------+
║                    ║
║                  o   o
║                  (x x)
║                   \=/
║
║
║
║
║
║
║
║
║
║
===============================''','''

+--------------------+
║                    ║
║                  o   o
║                  (x x)
║                   \=/
║                  .-"-.
║                   \ /
║                  {,-.}
║
║
║
║
║
║
║
===============================''','''

+--------------------+
║                    ║
║                  o   o
║                  (x x)
║                   \=/
║                  .-"-.
║                 //\ /
║               _// / \
║
║
║
║
║
║
║
║
===============================''', '''

+--------------------+
║                    ║
║                  o   o
║                  (x x)
║                   \=/
║                  .-"-.
║                 //\ /\\
║               _// / \ \\_
║              =./ /   \.=
║
║
║
║
║
║
║
===============================''', '''

+--------------------+
║                    ║
║                  o   o
║                  (x x)
║                   \=/
║                  .-"-.
║                 //\ /\\
║               _// / \ \\_
║              =./ {,-.} \.=
║                  ||
║                __||
║               `---"
║
║
║
║
===============================''','''

+--------------------+
║                    ║
║                  o   o
║                  (x x)
║                   \=/
║                  .-"-.
║                 //\ /\\
║               _// / \ \\_
║              =./ {,-.} \.=
║                  || ||
║                __|| ||__
║               `---" "---'
║
║
║
║
===============================''',
 '''

  .                      .
         ..###'                    '###,.
        '####;       .ooooo.       ;####'
           '##,   .o8P"""""Y8o.   ,##'
            '##, 88'         '88 ,##'
             '##8'             '8##'
              '#8   ,o.   .o,   8#'
                8 8 888; :888 8 8
                8P '88'   '88' Y8
                P   X   8   x  'Y
                b      888      d
                 `8b         d8`
                  88'"88888"'88
                  8 `"""""""` 8
                   `8ooooooo8`
                   ,##'   '##,
                  ,##'     '##,
                 ,##'       '##,
              .#####,       ,#####.
                 `##'       '##`

 ''']

#funcion que regresa un palabra al azar
def random_word():
    idx=random.randint(0,2741)
    return words.WORDS(idx)


#funcion imprime la imgen correspondiente al numero de errores
#tambien imprime la palabra oculta
def display_board(hidden_word,tries):
    os.system("cls")
    print(images[tries])#imprimo la imagen que correspon a numero de errores
    print()
    print(hidden_word)


#funcion principal
def main():
    vowels={'a':'á','e':'é','i':'í','o':'ó','u':'ú'}
    word = random_word().lower()
    hidden_word =['-'] * len(word) #creo la palabra oculta
    tries = 0 #intentos fallidos

    while(True):

        display_board(hidden_word,tries)
        current_letter = str(input("write one word:"))
        #uso esta parte para buscar la mis vocal pero con acento
        try:
            stressed_vowel=vowels[current_letter]
            #si la letra que ingreso no es una volcal capturo el error de llave
        except KeyError:
            # y le doy un valor nulo
            stressed_vowel='Null'


        letter_idx=[]
        for idx in range(len(word)):

            if word[idx] == current_letter: #evaluo si la letra vocal o no este dentro de la palabra
                letter_idx.append(idx)      #si si esta capturo su indice

            if word[idx] == stressed_vowel:#con esto evaluo voval con acento
                letter_idx.append(idx)

            if word[idx] == 'ü':#caso especial con la u
                letter_idx.append(idx)




        if len(letter_idx) == 0:#si la lista de indices es 0 significa que la letra ingresada no esta en la palabra
            tries += 1 #aumento el contador de errores

            if tries == 7:#si lleva 7 errores entonces ya perdio
                display_board(hidden_word,tries)
                os.system("cls")
                print('')
                print('! you lost hahahaha ¡ The word is:[ {} ]'.format(word)) #le  muestro la palabra correpta
                print(images[7])#imprimo la ultiam imagen de mi lista images
                break
        else:
            for idx in letter_idx:
                hidden_word[idx] = word[idx]#itero los indeces y busco la letra dentro de la palabra y la remplaco en mi lista de palabra oculta
            letter_idx = []#limpio la lista de los indices

        try:
            hidden_word.index('-')#compruebo o busco aver si aun hay - esto quiere decir que aun no termina
        except ValueError:#de lo contrario si no lo encuentra capturo el error y doy fin al programa
            os.system("cls")
            y=len(word)
            x=29-y
            print('''
            ______________________________________________________
           |                                                      |
           |    _____________________________________________     |
           |   |                                             |    |
           |   |C:\> _Winner                                 |    |
           |   |                                             |    |
           |   |!congratulations ¡                           |    |
           |   |The word is:[ {} ]{}|    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
:-----------------------------------------------------------------------------:
`---._.-----------------------------------------------------------------._.---´'''.format(word,' '*x))
            break


if __name__ == '__main__':

    while(True):
        print('''W e l c o m e    t o    t h e   h a n g m a n   g a m e''')
        print()
        print()
        print("press a key to start")
        input()
        main()
        val=str(input("Again? --[Y]es  --[N]o :"))
        if val=='Y' or val=='y':
            os.system("cls")
        else:
            os.system("cls")
            break


# At the moment the words are in spanish
# Por el momento las palabras usadas se encuentran en español
