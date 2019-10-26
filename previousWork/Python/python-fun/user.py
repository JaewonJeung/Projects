class User():
    def __init__ (self, first_n, last_n, age, last_four):
        self.first_n = first_n
        self.last_n = last_n
        self.age = age
        self.last_four = last_four
        self.full_n = first_n + " " + last_n
        self.login_attempts = 0
  
    def greet_user(self):
        print("Welcome back, {}!".format(self.first_n))
    
    def describe_user(self):
        print("You have inquired information of %s. His/Her age is %d, and the last four digit of His/Her SSN is %d." %(self.full_n, self.age, self.last_four))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, first_n):
        self.first_n = first_n
        self.priv_list = []
    
    def add_privileges(self, new_priv):
        self.priv_list.append(new_priv)

    def show_privileges(self):
        print("Here are some privileges of %s:" %(self.first_n))
        for privilege in self.priv_list:
            print(privilege)
        
class Admin(User):
    def __init__(self, first_n, last_n, age, last_four):
        super().__init__(first_n, last_n, age, last_four)
        self.privileges = Privileges(self.first_n)
    
    def describe_user(self):
       print("You have inquired information of %s. \n%s is an admin. His/Her age is %d, and the last four digit of His/Her SSN is %d." %(self.full_n, self.first_n, self.age, self.last_four))