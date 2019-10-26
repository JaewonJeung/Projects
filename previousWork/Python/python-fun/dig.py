class Dog():
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
          print(self.name.title() + " rolled over.")

    def update_age(self, age):
          self.age = age
