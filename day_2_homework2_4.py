class Person:
    def __init__(self,firstName,lastName) -> None:
        self.firstName = firstName
        self.lastName = lastName

customer1 = Person("Ahmet","Demirog")
customer2 = Person("Kerem", "Varis")
customer3 = Person("Ilker", "Tural")

print(customer1.firstName)