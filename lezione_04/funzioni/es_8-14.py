'''8-14. Auto: scrivi una funzione che memorizza le informazioni su un'auto in un dizionario. La funzione deve sempre ricevere un produttore e un nome modello. Dovrebbe quindi accettare un numero arbitrario di argomenti di parole chiave. Chiama la funzione con le informazioni richieste e altre due coppie di nome-valore, come un colore o una caratteristica opzionale. La funzione dovrebbe funzionare per una chiamata come questa: auto - make-car('subaru', 'outback', color', 'blue', tow-package-True) Stampare il dizionario che è stato restituito per assicurarsi che tutte le informazioni fossero memorizzate correttamente.'''

def car(casa_produttrice, model, **kwargs):
    kwargs["casa_produttrice"] = casa_produttrice
    kwargs["model"] = model
    return kwargs

valori = car("Fiat", "panda", motore="1200 cc", colore = "rosso", anno = "2000")
print(valori)