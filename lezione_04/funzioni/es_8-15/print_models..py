'''8-15. Modelli di stampa: mettere le funzioni per l'esempio print-models.py in un file separato chiamato print-functions.py. Scrivi una dichiarazione di importazione nella parte superiore di print-models.py e modifica il file per utilizzare le funzioni importate.'''

# print-models.py
from print_functions import print_stars, print_dashes, print_numbers

# Esempio di utilizzo delle funzioni importate
print_stars(10)
print_dashes(15)
print_numbers(9)
