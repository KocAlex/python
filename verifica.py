from IPython.utils.tempdir import TemporaryWorkingDirectory
#-Koca Alex-
#10 Funzioni
def ricerca(chiave):
  if chiave in diz.keys():
    return diz[chiave]
  else:
    return -1

def inserisci():
  nome = input("Inserire il nome dell'giocatore: ")
  cognome = input("Inserire il cognome dell'giocatore: ")
  while ricerca(nome+ " "+ cognome) != -1:
    print("Errore")
    nome = input("Inserire il nome dell'giocatore")
    cognome = input("Inserire il cognome dell'giocatore")

  diz[nome + " " + cognome] = []
  nProve = int(input("Inserisci quante prove ha svolto " + cognome+":"))
  for i in range(nProve):
    diz[nome + " " + cognome].append(inserisciProva())
  
def inserisciProva():
  prova = ""
  categoria = ""
  tempoMin = -1
  tempoSec = -1
  tempoMillis = -1
  while prova != "Corsa campestre" and prova != "Corsa 100mt" and prova != "Corsa 200mt" and prova != "Corsa ad ostacoli 400mt":
    prova = input("Inserire il nome della prova: ")
  while tempoMin < 0:
    tempoMin = int(input("Inserire il tempo (min): "))
  while tempoSec < 0:
    tempoSec = int(input("Inserire il tempo (sec): "))
  while tempoMillis < 0:
    tempoMillis = int(input("Inserire il tempo (millis): "))

  while categoria != "Allievi" and categoria != "Juniores fem" and categoria != "Juniores mas":
    categoria = input("Inserire la categoria: ")

  return (prova, (tempoMin, tempoSec, tempoMillis), categoria)

#1. Popola
diz = {"Giuseppe Gullo": [("Corsa campestre", (40, 21, 0), "Allievi"), ("Corsa 100mt", (0, 12, 0),"Juniores mas"), ("Corsa 200mt", (0, 29, 19), "Juniores mas")], "Antonia Barbera": [("Corsa campestre", (0, 39, 11), "Juniores fem"), ("Corsa 100mt", (0, 18, 0),"Juniores fem"), ("Corsa 200mt", (0, 0, 0), "Juniores fem")], "Nicola Esposito": [("Corsa campestre", (0, 43, 22), "Allievi"), ("Corsa 100mt", (0, 14, 0),"Juniores mas"), ("Corsa 200mt", (0, 36, 19), "Juniores mas")]}

#2. Aggiungi alla struttura il tuo nominativo con valori a scelta
diz["Koca Alex"] = [("Corsa campestre", (7, 0, 9), "Allievi"), ("Corsa 100mt", (0, 5, 5), "Juniores mas"), ("Corsa 200mt", (0, 50, 4), "Juniores mas")]

#3.Aggiungi la 4.disciplina sportiva 'corsa ad ostacoli 400 mt' per ogni atleta con tempo e categoria:
#Giuseppe Gullo (0,40,34) Allievo
#Antonia Barbera (0,39,10) Allieva
#Nicola Esposito (0,40,10) Allievo
#TuoNominativo (0,40,26) Allievo/a.

diz["Giuseppe Gullo"].append(("Corsa ad ostacoli 400mt", (0, 40, 34), "Allievi"))
diz["Antonia Barbera"].append(("Corsa ad ostacoli 400mt", (0, 39, 10), "Allievi"))
diz["Nicola Esposito"].append(("Corsa ad ostacoli 400mt", (0, 40, 10), "Allievi"))
diz["Koca Alex"].append(("Corsa ad ostacoli 400mt", (0, 40, 26), "Allievi"))

#4. Stampa la tupla con le informazioni sulla disciplina sportiva corsa campestre per l'atleta Giuseppe Ciullo
print("---Punto 4---")
print(diz["Giuseppe Gullo"][0])

#5. Stampa i singoli valori della tupla con le informazioni sulla disciplina corsa 200 mt. per Nicola Esposito
print("---Punto 5---")
print("Valori della tupla di Nicola Esposito (200mt): ")
for i in range(len(diz["Nicola Esposito"][2])):
  print(diz["Nicola Esposito"][2][i])

#6. Stampa il tempo di Antonia Barbera nella corsa 100 mt.
print("---Punto 6---")
print("Tempo di Antonia Barbera nei 100mt: " +  str(diz["Antonia Barbera"][1][1][0]) + " : " + str(diz["Antonia Barbera"][1][1][1]) + " : " + str(diz["Antonia Barbera"][1][1][2]))

#Controllati i primi 6 ore 9:23

#7. Stampa il tempo minimo riportato nella corsa 100mt. della categoria Juniores mas
print("---Punto 7---")
min = diz["Giuseppe Gullo"][i][1][0]*60*1000 + diz["Giuseppe Gullo"][i][1][1]*60 + diz["Giuseppe Gullo"][i][1][2]
giocatoreMigliore = "Giuseppe Gullo"
for chiave in diz.keys():
  tempo = 0
  if diz[chiave][1][2] == "Juniores mas":
    tempo += diz[chiave][1][1][0]*60*1000
    tempo += diz[chiave][1][1][1]*60
    tempo += diz[chiave][1][1][2]
    if tempo < min:
      min = tempo
      giocatoreMigliore = chiave
print(f"Il migliore è stato/a {giocatoreMigliore}  con un tempo di {diz[giocatoreMigliore][1][1][0]} : {diz[giocatoreMigliore][1][1][1]} : {diz[giocatoreMigliore][1][1][2]}")

#8. Stampa il tempo massimo riportato nella corsa 200mt della categoria Juniores mas
print("---Punto 8---")
max = diz["Giuseppe Gullo"][i][1][0]*60*1000 + diz["Giuseppe Gullo"][i][1][1]*60 + diz["Giuseppe Gullo"][i][1][2]
giocatorePeggiore = "Giuseppe Gullo"
for chiave in diz.keys():
  tempo = 0
  if diz[chiave][2][2] == "Juniores mas":
    minuti = diz[chiave][2][1][0]*60*1000 
    secondi = diz[chiave][2][1][1]*60
    millisec = diz[chiave][2][1][2]
    tempo = minuti + secondi + millisec
    if tempo > max:
      max = tempo
      giocatorePeggiore = chiave
print(f"Il peggiore è stato/a {giocatorePeggiore}  con un tempo di {int(minuti/1000/60)} : {int(secondi/60)} : {millisec}")

#9. Stampa la media dei tempi nella corsa campestre della categoria allievi.

print("---Punto 9---")

minutiTot = 0
secondiTot = 0
millisecTot = 0
giocatoriTot = 0
for chiave in diz.keys():
  tempo = 0
  if diz[chiave][0][2] == "Allievi":
    minutiTot += diz[chiave][0][1][0]
    secondiTot += diz[chiave][0][1][1]
    millisecTot += diz[chiave][0][1][2]
    tempo = minuti + secondi + millisec

    giocatoriTot += 1

print(f"Il tempo medio di completamento è stato di: " + str(int(minutiTot/giocatoriTot)) + ":" + str(int(secondiTot/giocatoriTot)) + ":" + str(int(millisecTot/giocatoriTot)))


#10. Realizzare le opportune funzioni per aggiungere al dizionario i dati validi relativi alle 4 gare per un atleta.
print("---Punto 10 || EXTRA ---")
inserisci()
print(diz)


