"""
definire una funzione che prenda un dizionario
e una stringa in input, costruisca una lista con i valori del
dizionario che hanno come chiave i caratteri che
formano la stringa, infine la funzione deve restituire gli
elementi della lista creata sotto forma di un'unica stringa
"""


def mix(d, s):
    s2 = ''
    for i in range(len(d.items())):
        s2 += str((d.get(s[i])))
    return s2

Dizionario ={'a':1,'b':2,'c':3}
Stringa='abc'

print(mix(Dizionario,Stringa))

