'''8-15. Modelli di stampa: mettere le funzioni per l'esempio print-models.py in un file separato chiamato print-functions.py. Scrivi una dichiarazione di importazione nella parte superiore di print-models.py e modifica il file per utilizzare le funzioni importate.'''

# printing_functions.py

def print_stars(n):
    """ stampa una riga di asterischi """
    print('*' * n)

def print_dashes(n):
    """ stampa una riga di trattini """
    print('-' * n)

def print_numbers(n):
    """ stampa numeri da 1 a ... """
    for i in range(1, n + 1):
        print(i, end=' ')
    print()
