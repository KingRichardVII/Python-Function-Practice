
class Hero:
    #constructor/ special initializer function
    def __init__(self, health, atk, mana):
    #what kinds of attributes does a hero have?
        self.health = health
        self.atk = atk
        self.mana = mana
        #what kinds of actions does a hero do? (methods)
    def attack(self):
        print("The hero attacks")

    def flee(self):
        print("The hero flees")

#create object
Erdrick = Hero(100,50,50)
#print object attributes
print(Erdrick.health)
#make object perform actions/method
Erdrick.attack()