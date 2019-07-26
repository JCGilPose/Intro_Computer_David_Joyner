#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute. 
#Each setter should accept a value as an argument. If the 
#value is a valid value, it should set the corresponding 
#attribute to the given value. Otherwise, it should set the 
#attribute to False.
#
#Edit the constructor to use these new setters and getters.
#In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
#new_burrito.meat would be False because "spaghetti" is not
#one of the valid options. Note that you should NOT try to
#check if the new value is valid in both the constructor and
#the setter: instead, just call the setter from the
#constructor using something like self.set_meat(meat).
#
#Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!

class Burrito:

    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = self.set_meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = self.set_rice(rice)
        self.beans = self.set_beans(beans)
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn

    def set_meat(self, meat):
        valid = ["chicken", "pork", "steak", "tofu", False]
        if meat in valid:
            self.meat = meat
        else:
            self.meat = False
        return self.meat
    
    def set_to_go(self, to_go):
        valid = [True, False]
        if to_go in valid:
            self.to_go = to_go
        else:
            self.to_go = False
        return self.to_go
            
    def set_rice(self, rice):
        valid = ["brown", "white", False]
        if rice in valid:
            self.rice = rice
        else:
            self.rice = False
        return self.rice
            
    def set_beans(self, beans):
        valid = ["black", "pinto", False]
        if beans in valid:
            self.beans = beans
        else:
            self.beans = False
        return self.beans
            
    def set_extra_meat(self, extra_meat):
        valid = [True, False]
        if extra_meat in valid:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False
        return self.extra_meat
            
    def set_guacamole(self, guacamole):
        valid = [True, False]
        if guacamole in valid:
            self.guacamole = guacamole
        else:
            self.guacamole = False
        return self.guacamole
            
    def set_cheese(self, cheese):
        valid = [True, False]
        if cheese in valid:
            self.cheese = cheese
        else:
            self.cheese = False
        return self.cheese
    
    def set_pico(self, pico):
        valid = [True, False]
        if pico in valid:
            self.pico = pico
        else:
            self.pico = False
        return self.pico

    def set_corn(self, corn):
        valid = [True, False]
        if corn in valid:
            self.corn = corn
        else:
            self.corn = False
        return self.corn

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole
    
    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn

#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.

my_burrito = Burrito("spaghetti", True, True, False)

print(my_burrito.meat)
print(my_burrito.get_meat())
