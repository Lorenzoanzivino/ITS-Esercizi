'''Fare tre diverse somme, sotto indicate. Esempio per spiegare le Funzioni. Creo 3 somme con i cicli, ma per fare la stessa cosa posso usare 1 sola funzione e i pèarametri li cambio nei print()'''

# 1 Somma tra 1 e 10
'''sum:int = 0
for i in range(1, 11):
    sum += i
print("La somma tra 1 e 10 è:", sum)'''

# 2 Somma tra 20 e 37
'''sum:int = 0
for i in range(20, 38):
    sum += i
print("La somma tra 20 e 37 è:", sum)'''

# 3 Somma tra 35 e 49
'''sum:int = 0
for i in range(35, 50):
    sum += i
print("La somma tra 35 e 49 è:", sum)'''


# FUNZIONI 
def sumInRange(a:int, b:int):
# definire una somma
    result:int = 0
# calcolare la somma
    for i in range(a,b+1):
        result = result + i
# restituisce il valore di somma come output della funzione somma
    return result

# salvo la funzione in una variabile cosi da inserire nel print solo il nome della variabile
my_sum:int = sumInRange(1, 10)
# utilizzare la funzione sumInRange per calcolare una somma di numeri da 1 to 10
print(f"Sum from 1 to 10 is {sumInRange(1, 10)}")
# oppure
print(f"Sum from 1 to 10 is {my_sum}")
# utilizzare la funzione sumInRange per calcolare una somma di numeri da 20 to 37
print(f"Sum from 20 to 37 is {sumInRange(20, 37)}")
# utilizzare la funzione sumInRange per calcolare una somma di numeri da 35 to 49
print(f"Sum from 35 to 49 is {sumInRange(35, 49)}")