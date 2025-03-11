'''8-15. Modelli di stampa: mettere le funzioni per l'esempio print-models.py in un file separato chiamato print-functions.py. Scrivi una dichiarazione di importazione nella parte superiore di print-models.py e modifica il file per utilizzare le funzioni importate.'''

# print-models.py
from print_functions import print_asterischi, print_trattini, print_numeri, print_punti

# Esempio di utilizzo delle funzioni importate
print_asterischi(10)
print_trattini(15)
print_numeri(9)
print_punti(18)