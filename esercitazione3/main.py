from Studente import Studente

studente1 = Studente("Django", "Freeman", "Informatica")
studente2 = Studente("Piero", "Della", "Medicina")

#print(f'{studente1}')





print(" Studente uno: \n",studente1.scheda_personale())
print("")
print(" Studente due: \n",studente2.scheda_personale())

studente1.ore_settimanali += 4
print("")
print(" Ore settimanali dello studente uno dopo la modifica:",studente1.ore_settimanali)
print(" Ore settimanali dello studente due dopo la modifica:",studente2.ore_settimanali)
