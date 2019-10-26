import practice
import dig
import rest
import user as u

def nl():
    print("\n")

strf = "ehllo"
for i in strf:
  print ("a count"
  )
Q = [1,2,3]
Q = [x+1 for x in Q]
print(Q)

N = list(enumerate(Q, 1))
print (N)
print (N[0][1])

nl()
li = [5]  #list
liTwo = [1,2,3]
print (li)
print(liTwo)

print(liTwo[0])
nl()

di = {2: 3} #dictionary
di ['Guten'] = "Tag"

print (di)
di[2] = di[2]+1
print (di[2], di["Guten"])

num = "5"
st = int(num)
print (str(st)+"6")

for x in range(1,6,2):
  print(x)

languages = {
  "this": "first",
  "that": "second"
}

print (languages)

name = "mee"
func = practice.pract(name)
print (func)

dog = dig.Dog("james", 6)
print("his name is " + dog.name.title())
print("his age is " + str(dog.age))
dog.sit()
dog.update_age(7)
print("now his age is " + str(dog.age) + "\n")

#restaurant example starts here
print("RESTAURANT EXAMPLE -------------------")

first_restaurant = rest.Restaurant("Joe's", "HomeCook")
second_restaurant = rest.Restaurant("James'", "Italian")
third_restaurant = rest.Restaurant("John's", "Mexican")

first_restaurant.describe_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
print("\n")

first_restaurant.set_number_served(100)
first_restaurant.increment_number_served(50)
nl()

fourth_restaurant = rest.IceCreamStand("Jeni's Icecream", "American")
fourth_restaurant.describe_restaurant()
fourth_restaurant.open_restaurant()
nl()
fourth_restaurant.add_flavors("vanilla")
fourth_restaurant.add_flavors("choco")
fourth_restaurant.add_flavors("strawberry")
fourth_restaurant.get_flavors()
print("\n")

#Users example starts here
print("USER EXAMPLE -------------------")

Joe = u.User("Joe", "Brown", 21, 2215)
Mary = u.User("Mary", "Jane", 17, 5123)
John = u.User("John", "Smith", 53, 1235)
Adam = u.Admin("Adam", "Brown", 24, 5124)
Jane = u.Admin("Jane", "Kost", 25, 1252)

Joe.greet_user()
Joe.describe_user()
print("\n")

Joe.increment_login_attempts()
Joe.increment_login_attempts()
print(Joe.login_attempts)
Joe.reset_login_attempts()
Joe.increment_login_attempts()
print(Joe.login_attempts)
nl()

Adam.describe_user()
nl()
Adam.privileges.add_privileges("Can add post")
Adam.privileges.add_privileges("Can delete post")
Adam.privileges.show_privileges()
nl()
Jane.describe_user()
Jane.privileges.add_privileges("Can delete post")
nl()
Jane.privileges.show_privileges()
