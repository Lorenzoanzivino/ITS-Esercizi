'''4. Analisi del testo:

Crea una funzione che prenda un paragrafo e conti il numero di occorrenze di ogni parola.
La funzione dovrebbe stampare un report che mostra le parole più frequenti e il loro numero di occorrenze.
Puoi usare un ciclo for per scorrere le parole nel testo e un dizionario per memorizzare le occorrenze.
Implementa la gestione degli errori per gestire file mancanti o altri problemi di input.'''

def paragraph(testo:str, parole_ripetute:str, ripetizioni:int) -> None:
    testo:str = "Il cielo è azzurro, il cielo è sereno. Il vento soffia leggero. Ogni giorno è un nuovo giorno, ogni giorno porta nuove opportunità."
    
    parole_ripetute:list = []

    for parola in testo:
        if parola not in testo:
            parole_ripetute.append(parola)

    return parole_ripetute

print(paragraph())


def paragraph(testo:str) -> None:
    parole = []
    parola = ""
    
    # Itera sui caratteri del testo
    for char in testo:
        if char != " " and char not in ",.!?":  # Continua a raccogliere caratteri che fanno parte della parola
            parola += char
        else:
            if parola:  # Quando finisci una parola (perché c'è uno spazio o un segno di punteggiatura)
                parole.append(parola)
                parola = ""
    
    # Aggiungi l'ultima parola se c'è
    if parola:
        parole.append(parola)
    
    # Conta le occorrenze delle parole
    frequenza = {}
    for parola in parole:
        if parola in frequenza:
            frequenza[parola] += 1
        else:
            frequenza[parola] = 1
    
    # Trova e stampa le parole ripetute
    parole_ripetute = [parola for parola, count in frequenza.items() if count > 1]
    print(parole_ripetute)

# Esegui la funzione
testo = "Il cielo è azzurro, il cielo è sereno. Il vento soffia leggero. Ogni giorno è un nuovo giorno, ogni giorno porta nuove opportunità."
paragraph(testo)

