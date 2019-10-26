class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.servedNum = 0
    
    def describe_restaurant(self):
        ret_string = ""
        ret_string = (self.restaurant_name) + " " +(self.cuisine_type)
        print (ret_string)
    
    def open_restaurant(self):
        print("%s is now open!" %(self.restaurant_name))

    def set_number_served(self, num):
        self.servedNum = num
        print("%s: Updated number served to %d" %(self.restaurant_name, num))

    def increment_number_served(self, inc):
        self.servedNum += inc
        print("%s: Added %d serves. Updated number served to %d" %(self.restaurant_name, inc, self.servedNum))

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors=None):
        if flavors is None:
            self.flavors = []
        super().__init__(restaurant_name, cuisine_type)
    
    def add_flavors(self, new_flavor):
        self.flavors.append(new_flavor)

    def get_flavors(self):
        print("Here is the list of flavors for %s:" %(self.restaurant_name))
        for flavor in self.flavors:
            print (flavor)


