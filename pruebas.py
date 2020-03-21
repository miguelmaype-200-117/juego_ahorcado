vowels={'a':'á','e':'é','i':'í','o':'ó','u':'ú'}

try:
     print(vowels['l'])
     
except KeyError:
     print('no se encuentra en el diccionario')
