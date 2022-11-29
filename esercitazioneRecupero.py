#Koca Alex
#Funzioni

def popola(codice):
  fila = int(input("Inserire la fila: "))
  numero = int(input("Inserire il numero: "))
  
  altaStagione = int(input("Inserire il costo in alta stagione"))
  bassaStagione = int(input("Inserire il costo in bassa stagione"))
 
  #TODO: controlli
  giorno = int(input("Inserire il giorno: "))
  mese = int(input("Inserire il mese: "))
  anno = int(input("Inserire l'anno: "))
  
  nGiorni = 0
  while nGiorni <= 0:
    nGiorni = int(input("Inserire il numero di giorni prenotati: "))
  
  sdraio = int(input("Inserire sdraio extra (totale max 3): "))
  lettini = int(input("Inserire lettini extra (totale max 3): "))
  while (sdraio + lettini > 3) or sdraio < 0 or lettini < 0:
    print("Troppe!")
    sdraio = int(input("Inserire sdraio extra (totale max 3): "))
    lettini = int(input("Inserire lettini extra (totale max 3): "))

  costoTotale = 0
  if mese == 8 or mese == 7:
    costoTotale = nGiorni*altaStagione
    if sdraio != 0:
      costoTotale += (altaStagione/3)*sdraio*nGiorni
    if lettini != 0:
      costoTotale += (altaStagione/2)*lettini*nGiorni
  elif mese == 6 or mese == 9:
    costoTotale = nGiorni*bassaStagione
    if sdraio != 0:
      costoTotale += (bassaStagione/3)*sdraio*nGiorni
    if lettini != 0:
      costoTotale += (bassaStagione/2)*lettini*nGiorni
  if codice in db:
    codice += int(len(db.keys()))
  db[codice] = [(fila, numero), (bassaStagione, altaStagione), (giorno, mese, anno), nGiorni, (sdraio, lettini), costoTotale]
  


def prenotazioni(fila, numero):
  trovato = False
  for i in range(1, len(db)):
    if(db[i][0][0] == fila and db[i][0][1] == numero):
      trovato = True
      print("Prenotazione: " + str(db[i]))
  if not trovato:
    print("Nessun ombrellone trovato")

def allPrenotazioni():
  for i in range(1, len(db)):
    print(db[i])

def sconto(mese, valSconto):
  for i in range(1, len(db)):
    if(db[i][2][1] == mese):
      db[i][5] -= db[i][5]*valSconto/100

def incassi(mese):
  for i in range(1, len(db)):
    if(db[i][2][1] == mese):
      totaleIncassi += db[i][5]
  return totaleIncassi

def prenotazioniInNMesi(mese):
  for i in range(1, len(db)):
    if(db[i][2][1] == mese):
      print(db[i])

def minimo():
  min = db[1][5]
  iMin = 1
  for i in range(2, len(db)):
    if(db[i][5] < min):
      min = db[i][5]
      iMin = i
  print("Mese: " +str(iMin) + "Incasso: " + str(db[i][5]))
#Main
db = {}
mese = 0
valSconto = 0
#Menù
scelta = -1
while scelta != 0:
  print("0. Esci")
  print("1. Popola")
  print("2. Mostra prenotazioni di un ombrellone")
  print("3. Mostra tutte le prenotazioni")
  print("4. Riduzione prezzo percentuale")
  print("5. Calcolo incasso totale di un mese")
  print("6. Prenotazioni in n mesi")
  scelta = int(input("Inserire la scelta: "))

  if scelta == 1:
    n = int(input("Quante prenotazioni vuoi registrare? "))
    for i in range(n):
      popola(i)
  if scelta == 2:
    #Controllo fila e numero 
    fila = int(input("Inserire la fila dell'ombrellone: "))
    numero = int(input("Inserire il numero dell'ombrellone: "))
    prenotazioni(fila, numero)
  if scelta == 3:
    allPrenotazioni()
  if scelta == 4:
    valSconto = 0
    while mese != 6 and mese != 7 and mese != 8 and mese != 9:
      mese = int(input("Inserire il mese da scontare: "))
    while valSconto <= 0:
      valSconto = int(input("Inserire lo sconto: "))
    sconto(mese, valSconto)
  if scelta == 5:
    while mese != 6 and mese != 7 and mese != 8 and mese != 9:
      mese = int(input("Inserire il mese di cui mostrare gli incassi: "))
    print("Incassi del mese n " + str(mese) + ": " + incassi(mese))
  if scelta == 6:
    mese = int(input("Inserire il mese di cui mostrare le prenotazioni: "))
    while mese != 0:
      while mese != 6 and mese != 7 and mese != 8 and mese != 9:
        mese = int(input("Inserire il mese di cui mostrare le prenotazioni: "))
      prenotazioniInNMesi(mese)
  if scelta == 7:
    minimo()
