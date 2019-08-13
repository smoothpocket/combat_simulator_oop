from colored import fg
import random

class entity(object):
    # global variables // might wanna remove these
    name = "entity"
    
    
# instantiate the entity object
    def __init__(self, arg_name = "Default Entity", arg_health = 100, arg_damage = random.randrange(1, 100), arg_defense = random.randrange(1, 100)):
        self.name = arg_name
        self.health = arg_health
        self.damage = arg_damage
        self.defense = arg_defense

    def render_status(self):
        print("\n\nName: ", self.name)        
        print("Health: ", self.health) 
        print("Damage: ", self.damage) 
        print("Defense: ", self.defense) 

# A function for damage and defense must exist. Having --random.randrange(1, 100)-- does not work properly when stored as an entity variable. 
# Once the object is initialized, the random integer is stored permenantly. Each entity needs to have a random amount of damage for each round.
    def roll_for_damage(self):
        self.damage = random.randrange(1, 100)
        print("New Damage Stat: ", self.damage)

    def roll_for_defense(self):
        self.defense = random.randrange(1, 100)
        print("New Defense Stat: ", self.defense)

    def eat_apple(self):
        calculated_health_buff = random.randrange(-25, 200)
        print("%s\nWow! That apple gave you: " % fg(117), calculated_health_buff, "hp! That's crazy!")
        print('UwU, that was so tasty! Current hp:', self.health, "+ hp from apple:", calculated_health_buff, "hp")
        self.health = calculated_health_buff + self.health
        print("You now have: ", self.health, "hp. Good luck next round!!")
