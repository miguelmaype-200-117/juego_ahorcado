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

vowels={'a':'á','e':'é','i':'í','o':'ó','u':'ú'}
#funcion que regresa un palabra al azar
def random_word():
    idx = 0
    #random.randint(0,2740)
    return words.WORDS(idx)


#funcion imprime la imgen correspondiente al numero de errores
#tambien imprime la palabra oculta
def display_board(hidden_word,tries):
    os.system("cls")
    print(images[tries])
    print()
    print(hidden_word)


#funcion principal
def main():
    word = random_word().lower()
    hidden_word =['-'] * len(word) #creo la palabra oculta
    tries = 0 #intentos fallidos

    while(True):

        display_board(hidden_word,tries)
        current_letter = str(input("write one word:"))

        try:
            stressed_vowel=vowels[current_letter]
        except KeyError:
            stressed_vowel='Null'


        letter_idx=[]
        for idx in range(len(word)):

            if word[idx] == current_letter:
                letter_idx.append(idx)

            if word[idx] == stressed_vowel:
                letter_idx.append(idx)

            if word[idx] == 'ü':
                letter_idx.append(idx)



        if len(letter_idx) == 0:
            tries += 1

            if tries ==7:
                display_board(hidden_word,tries)
                os.system("cls")
                print('')
                print('! you lost hahahaha ¡ The word is:[ {} ]'.format(word))
                print(images[7])
                break
        else:
            for idx in letter_idx:
                hidden_word[idx] = word[idx]
            letter_idx = []

        try:
            hidden_word.index('-')
        except ValueError:
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
