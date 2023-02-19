
class Person:
    def __init__(self,name,rost,color):
        self.name = name
        self.rost = rost
        self.color = color
        self.weight = None
    def say_hello(self):
        print(f"My name is {self.name} and my rost {self.rost}")
        
    def __eq__(self,other):
        if self.name == other.name:
            return "Они тезки"
        else:
            return "Они не тезки"        
        
Ivan = Person("Ivan",190,"brown")
print(Ivan.name,Ivan.rost,Ivan.color)
Vasya = Person("vasya",180,"green")
print(Vasya.name,Vasya.rost,Vasya.color)
print(Ivan == Vasya)
Ivan.say_hello()
Vasya.say_hello()