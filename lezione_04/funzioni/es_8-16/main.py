'''8-16. Importazioni: Utilizzando un programma che hai scritto che contiene una funzione, memorizza quella funzione in un file separato. Importa la funzione nel tuo file principale e chiama la funzione utilizzando ciascuno di questi approcci: importa nome_modulo da nome_modulo importa nome_funzione da nome_modulo importa nome_funzione come fn importa nome_modulo come mn da nome_modulo importa *'''

# 1. Importare l'intero modulo
import my_module
my_module.saluta("Mario")

# 2. Importare solo la funzione
from my_module import saluta
saluta("Luigi")

# 3. Importare la funzione con un alias
from my_module import saluta as s
s("Anna")

# 4. Importare l'intero modulo con un alias
import my_module as mm
mm.saluta("Giulia")

# 5. Importare tutte le funzioni dal modulo
from my_module import *
saluta("Marco")
