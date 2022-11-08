#Popola la struttura dati con i dati qui sopra.
datab = {"AA123BB" : [("Giugno", 9, 1293), ("Luglio", 7, 3231), ("Agosto", 7, 4020), ("Settembre", 6, 3928)], "AB345CD" : [("Giugno", 8, 1391), ("Luglio", 6, 1234), ("Agosto", 9, 4932), ("Settembre", 8, 2872)], "CD456FF" : [("Giugno", 7, 2872), ("Luglio", 6, 3273), ("Agosto", 4, 3211), ("Settembre", 8, 2827)]}

#Aggiungi i dati di un nuovo noleggio con targa ZZ999CN, (CN iniziali del tuo Cognome Nome) con 10 noleggi in ogni mese e 1000*N km per ogni mese (N il tuo numero di registro).
datab["ZZ999KA"] = [("Giugno", 10, 13000), ("Luglio", 10, 13000), ("Agosto", 10, 13000), ("Settembre", 10, 13000)]

#Stampa la tupla con tutte le informazioni sul mese di Luglio per la targa AA123BB
print(datab["AA123BB"][1])

#Stampa solo il numero di noleggi sul mese di Luglio per la targa AA123BB
print(datab["AA123BB"][1][1])

#Stampa la somma di tutti i km in tutti i mesi per la targa AB345CD
somma = 0
for i in range(len(datab["AB345CD"])):
  somma += datab["AB345CD"][i][2]
print(somma)

#Stampa la somma di tutti i km in tutti i mesi per tutte le macchine
somma = 0
for key in datab.keys():
  for j in range(len(datab)):
    somma += datab[key][j][2]
print(somma)

#Stampa il mese in cui sono stati fatti più km per la macchina targata CD456FF
maxKm = 0
mese = ""
for i in range(len(datab["CD456FF"])):
  if(datab["CD456FF"][i][2] > maxKm):
    maxKm = datab["CD456FF"][i][2]
    mese = datab["CD456FF"][i][0]
print(mese)
