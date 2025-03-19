'''Carrello della Spesa E-Commerce:
Crea una funzione che definisce un prodotto con un nome, un prezzo e una quantità.
Crea una funzione che gestisce il carrello della spesa, consentendo all'utente di aggiungere, rimuovere e visualizzare i prodotti nel carrello.
La funzione dovrebbe calcolare il totale del carrello e applicare eventuali sconti o tasse.
Implementa un ciclo for per iterare sugli articoli nel carrello e stampare informazioni dettagliate su ogni prodotto e il totale.'''


# Funzione che definisce un prodotto
def prodotto(nome: str, prezzo: float, quantita: int) -> dict:
    return {'nome': nome, 'prezzo': prezzo, 'quantita': quantita}

# Funzione per visualizzare il carrello
def visualizza_carrello(carrello):
    if not carrello:
        print("Il carrello è vuoto.")
    else:
        print("Contenuto del carrello:")
        for prodotto in carrello:
            print(f"{prodotto['nome']} - Prezzo: {prodotto['prezzo']}€ - Quantità: {prodotto['quantita']}")
    print()

# Creazione del carrello e aggiunta dei prodotti
carrello = []

# Aggiungiamo alcuni prodotti al carrello
carrello.append(prodotto('Acqua', 2.30, 6))
carrello.append(prodotto('Pasta', 0.89, 3))
carrello.append(prodotto('Pane', 0.70, 5))

# Visualizza il carrello
visualizza_carrello(carrello)

# Calcolo del totale del carrello con sconto e tassa
totale_senza_sconto = 0  # Inizializziamo il totale senza applicare lo sconto
for prodotto in carrello:
    totale_senza_sconto += prodotto['prezzo'] * prodotto['quantita']  # Sommiamo il prezzo * quantità di ogni prodotto

# Calcoliamo lo sconto sul totale
sconto = 10  # Sconto in percentuale
totale_con_sconto = totale_senza_sconto * (1 - (sconto / 100))  # Applichiamo lo sconto

# Calcoliamo la tassa sul totale scontato
tassa = 5  # Tassa in percentuale
totale_con_tassa = totale_con_sconto * (1 + (tassa / 100))  # Aggiungiamo la tassa

# Stampa del totale con sconto e tassa
print(f"Totale del carrello (con sconto e tassa): {totale_con_tassa:.2f}€")
