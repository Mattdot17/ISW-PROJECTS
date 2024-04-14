"""
data una lista di parole, restituire il dizionario in
cui la chiave è l’iniziale della parola in maiuscolo, il valore
è la lunghezza della parola
"""

parole = ["ciao", "gigi", "martello", "bicchiere"]
print("lista di parole:",parole)

dizionario = {parola[0].upper(): len(parola) for parola in parole} # vedi pag 6 set slides 3
print(dizionario)
