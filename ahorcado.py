# -*- coding: utf-8 -*-
import os
import random

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
WORDS=[
    'lavadora',
    'secadora',
    'transformers',
    'diputado',
    'fime',
    'sistemas_computacionales',
    'ella_no_te_ama',
    'gobierno',
    'heroe',
    'teatro',
    'jarra',
    'cinta',
    'jurado',
    'pantano',
    'ola_de_mar',
    'sorfista_de_3_metros',
    'pato',
    'oso',
    'perro',
    'animal',
    'selva',
    'mono',
    'computadora',
    'teclado']


def random_word():
    idx = random.randint(0, len(WORDS) - 1 )
    return WORDS[idx]

def display_board(hidden_word,tries):
    os.system("cls")
    print(images[tries])
    print()
    print(hidden_word)

def run():
    word = random_word()
    hidden_word =['-'] * len(word)
    tries = 0

    while(True):

        display_board(hidden_word,tries)
        current_letter = str(input("write one word:"))

        letter_idx=[]

        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_idx.append(idx)

        if len(letter_idx) == 0:
            tries += 1

            if tries ==7:
                display_board(hidden_word,tries)
                print('')
                print('! you lost hahahaha ¡ The word is {}'.format(word))
                print(images[7])
                break
        else:
            for idx in letter_idx:
                hidden_word[idx] = current_letter
            letter_idx = []

        try:
            hidden_word.index('-')
        except ValueError:
            os.system("cls")
            y=len(word)
            x=33-y
            print('''
            ______________________________________________________
           |                                                      |
           |    _____________________________________________     |
           |   |                                             |    |
           |   |C:\> _Winner                                 |    |
           |   |                                             |    |
           |   |!congratulations ¡                           |    |
           |   |The word is:{}{}|    |
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
        run()
        val=str(input("Again? --[Y]es  --[N]o :"))
        if val=='Y' or val=='y':
            os.system("cls")
        else:
            os.system("cls")
            break
