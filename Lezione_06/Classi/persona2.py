class Persona:
    def __init__(self):
        self.name:str = ""
        self.lastname:str = ""
        self.age:int = 0

    # funzione che mostri in output i dati relativi ad una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nAnni: {self.age}")