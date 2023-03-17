class Mathematic:
    def total(self,number1,number2):
        return number1 + number2
    def minus(self,number1,number2):
        return number1 - number2
    def multilication(self,number1,number2):
        return number1 * number2
    def division(self,number1,number2):
        return number1 / number2

mathematic = Mathematic()
result1 = mathematic.total(3,5)
print("Total Result : " + str(result1))
result2 = mathematic.minus(5,3)
print("Minus Result : " + str(result2))