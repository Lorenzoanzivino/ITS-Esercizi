''' Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.'''


# 1) Inizializzazione delle variabili:
#     • pos_tartaruga = 1  # posizione iniziale della tartaruga
#     • pos_lepre = 1      # posizione iniziale della lepre
#     • percorso = lista di 70 caratteri '_' # percorso con 70 posizioni vuote
# 3) Funzione per visualizzare il percorso:
#     • Creare una funzione che accetta il percorso e visualizza la corsia di gara
#     • Ogni volta che la tartaruga e la lepre si trovano sulla stessa posizione, stampare "OUCH!!!"
#     • Usare il carattere 'T' per la tartaruga, 'H' per la lepre, e '_' per le posizioni vuote.
# 4) Funzione per calcolare la mossa della tartaruga:
#     • Generare un numero casuale (i) da 1 a 10.
#     • Se 1 ≤ i ≤ 5, la tartaruga avanza di 3 quadrati ("passo veloce").
#     • Se 6 ≤ i ≤ 7, la tartaruga arretra di 6 quadrati ("scivolata"), ma non può andare sotto il quadrato 1.
#     • Se 8 ≤ i ≤ 10, la tartaruga avanza di 1 quadrato ("passo lento").
#     • Restituire la nuova posizione della tartaruga, assicurandosi che non scenda sotto 1.
# 5) Funzione per calcolare la mossa della lepre:
#     • Generare un numero casuale (j) da 1 a 10.
#     • Se 1 ≤ j ≤ 2, la lepre non si muove ("riposo").
#     • Se 3 ≤ j ≤ 4, la lepre avanza di 9 quadrati ("grande balzo").
#     • Se 5 ≤ j ≤ 6, la lepre arretra di 12 quadrati ("grande scivolata"), ma non può andare sotto il quadrato 1.
#     • Se 7 ≤ j ≤ 9, la lepre avanza di 1 quadrato ("piccolo balzo").
#     • Se 10, la lepre arretra di 2 quadrati ("piccola scivolata"), ma non può andare sotto il quadrato 1.
#     • Restituire la nuova posizione della lepre, assicurandosi che non scenda sotto 1.
# 6) Ciclo della gara (Tick dell'orologio):
#     • Iniziare un ciclo infinito che simula i tick dell'orologio.
#         1) Calcolare la mossa della tartaruga usando la funzione per la tartaruga.
#         2) Calcolare la mossa della lepre usando la funzione per la lepre.
#         3) Aggiornare il percorso con la nuova posizione della tartaruga e della lepre.
#         4) Se tartaruga e lepre sono nella stessa posizione, inserire "OUCH!!!" nel percorso.
#         5) Chiamare la funzione per visualizzare il percorso aggiornato.
# 7) Controllo se uno dei concorrenti ha vinto:
#     • Se la posizione della tartaruga è >= 70:
#         • Stampare "TORTOISE WINS! || VAY!!!" e terminare il ciclo.
#     • Se la posizione della lepre è >= 70:
#         • Stampare "HARE WINS || YUCH!!!" e terminare il ciclo.
#     • Se entrambi raggiungono o superano il quadrato 70 nello stesso tick:
#         • Stampare "IT'S A TIE." e terminare il ciclo.
# 8) Se nessuno ha vinto, ripetere il ciclo per il prossimo tick

import random

# 1) Inizializzazione delle variabili
pos_tartaruga = 1
pos_lepre = 1
percorso_lista = ['_'] * 70  # Il percorso è composto da 70 caselle

# 2) Funzione per visualizzare il percorso
def percorso():
    percorso_visibile = percorso_lista[:]  # Copia della lista
    '''pos_tartaruga è sulla prima posizione, Quindi dobbiamo fare pos_tartaruga - 1 per ottenere l'indice corretto.'''
    percorso_visibile[pos_tartaruga -1] = 'T'  # Aggiungi 'T' per la tartaruga
    percorso_visibile[pos_lepre -1] = 'H'  # Aggiungi 'H' per la lepre nelle loro posizioni
    
    # Stampare il percorso
    print(''.join(percorso_visibile))
    
    # Se tartaruga e lepre sono sulla stessa posizione
    if pos_tartaruga == pos_lepre:
        print("OUCH!!!")

# 3) Funzione per calcolare la mossa della tartaruga
def mossa_T(pos_tartaruga, piove):
    i = random.randint(1, 10)
    print(f"Mossa tartaruga: {i}")
    
    if 1 <= i <= 5:  # Passo veloce
        pos_tartaruga += 3
    elif 6 <= i <= 7:  # Scivolata
        pos_tartaruga -= 6
        if pos_tartaruga < 1:
            pos_tartaruga = 1
    elif 8 <= i <= 10:  # Passo lento
        pos_tartaruga += 1    

    if piove:
        pos_tartaruga -= 1
        if pos_tartaruga < 1:  # Non può andare sotto 1
            pos_tartaruga = 1
    
    if pos_tartaruga > 70:  # Non può superare la fine del percorso
        pos_tartaruga = 70
    
    return pos_tartaruga

# 4) Funzione per calcolare la mossa della lepre
def mossa_L(pos_lepre, piove):
    j = random.randint(1, 10)
    print(f"Mossa lepre: {j}")
    
    if 1 <= j <= 2:  # Riposo
        pos_lepre += 0
    elif 3 <= j <= 4:  # Grande balzo
        pos_lepre += 9
    elif 5 <= j <= 6:  # Grande scivolata
        pos_lepre -= 12
        if pos_lepre < 1:
            pos_lepre = 1
    elif 7 <= j <= 9:  # Piccolo balzo
        pos_lepre += 1
    elif j == 10:  # Piccola scivolata
        pos_lepre -= 2
        if pos_lepre < 1:
            pos_lepre = 1
    
    if piove:
        pos_lepre -= 1
        if pos_lepre < 1:  # Non può andare sotto 1
            pos_lepre = 1
    
    if pos_lepre > 70:  # Non può superare la fine del percorso
        pos_lepre = 70
    
    return pos_lepre

# 5) Ciclo della gara (Tick dell'orologio)
tick:int = 1  # Iniziamo con il primo tick

# 5) Ciclo della gara (Tick dell'orologio)
tick = 1  # Iniziamo con il primo tick

while True:
    print(f"\nTick: {tick}")  # Mostra il numero di tick
    
    # Meteo
    if (tick // 10) % 2 == 0:  # Ogni 10 tick si alterna
        print('sole')
        piove:bool = False
    else:
        print('piove')
        piove:bool = True

    # 1) Calcolare la mossa della tartaruga
    pos_tartaruga = mossa_T(pos_tartaruga, piove)
    print(pos_tartaruga)
    
    # 2) Calcolare la mossa della lepre
    pos_lepre = mossa_L(pos_lepre, piove)
    print(pos_lepre)
    
    # 3) Aggiornare e visualizzare il percorso
    percorso()
    
    # 4) Condizione di fine gara: se uno dei due raggiunge la fine
    if pos_tartaruga >= 70 and pos_lepre >= 70:
        print("\nIT'S A TIE.")
        break  # Termina il ciclo in caso di pareggio
    
    if pos_tartaruga >= 70:
        print("\nTORTOISE WINS! || VAY!!!")
        break  # Termina il ciclo se la tartaruga vince
    
    if pos_lepre >= 70:
        print("\nHARE WINS || YUCH!!!")
        break  # Termina il ciclo se la lepre vince

    tick += 1  # Aumentiamo il contatore dei tick
