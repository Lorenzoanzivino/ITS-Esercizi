''' chiedere in input in quale posizione l'utentè è arrivato alla gara. a seconda della posizione aggiungi "st", "nd", "rd", "th"'''

position:int= int(input("Insert finishing position: "))

if position == 1:
    print(f"{position}st!")

elif position == 2:
    print(f"{position}nd!")

elif position == 3:
    print(f"{position}rd!")

else:
    print(f"{position}th!")
