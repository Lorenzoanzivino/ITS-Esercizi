'''8-6. Nomi della città: scrivi una funzione chiamata city-country() che prende il nome di una città e del suo paese. La funzione dovrebbe restituire una stringa formattata in questo modo: "Santiago, Cile". Chiama la tua funzione con almeno tre coppie di città-paese e stampa i valori che vengono restituiti.'''

def city_country(citta:str, paese:str):
    print(citta, paese, sep=', ')

city_country("Roma", "Italia")
city_country("Parigi", "Francia")
city_country("Santiago", "Cile")