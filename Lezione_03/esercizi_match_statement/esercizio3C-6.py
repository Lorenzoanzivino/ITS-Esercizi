'''Esercizio 3C-6.
Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.
'''

mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]

# Habitat validi
habitat_list = ["acqua", "aria", "terra"]

# Input utente
animal = input("Digita il nome di un animale: ").lower()
habitat = input(f"Digita l'habitat in cui vive l'animale {animal}: ").lower()

# Classificazione dell'animale
if animal in mammiferi:
    animal_type = "Mammifero"
elif animal in rettili:
    animal_type = "Rettili"
elif animal in uccelli:
    animal_type = "Uccelli"
elif animal in pesci:
    animal_type = "Pesci"
else:
    animal_type = "Unknown"

# Creazione del dizionario
animale_info = {"Nome": animal,"Categoria": animal_type,"Habitat": habitat}

# Controllo della compatibilità dell'habitat
match animal_type:
    case "Mammifero":
        if animal in ["balena", "delfino"]:
            habitat_corretto = "acqua"
        else:
            habitat_corretto = "terra"
    
    case "Rettili":
        if animal == "tartaruga":
            habitat_corretto = "acqua"
        else:
            habitat_corretto = "terra"

    case "Uccelli":
        habitat_corretto = "aria"

    case "Pesci":
        habitat_corretto = "acqua"
    
    case _:
        habitat_corretto = "unknown"

# Verifica della corrispondenza habitat
if habitat_corretto == "unknown":
    print(f"Errore: non conosco la categoria dell'animale '{animal}'.")
elif habitat == habitat_corretto:
    print(f"Sì! Un {animal} può vivere in {habitat}.")
else:
    print(f"Attenzione: Un {animal} non vive in {habitat}, dovrebbe stare in {habitat_corretto}.")

# Output del dizionario
print("\nDati registrati:", animale_info)
