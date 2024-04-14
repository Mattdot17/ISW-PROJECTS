class Studente:
    ore_settimanali = 32

    def __init__(self, nome, cognome, cds): #costruttore
        self.nome = nome
        self.cognome = cognome
        self.cds = cds



    def scheda_personale(self): #funzione
        return f"Scheda Studente\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso Di Studi:{self.cds}\n Ore settimanali:{self.ore_settimanali}"



