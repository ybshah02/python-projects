
#A - Part 1s
#==========================================
# Purpose: An object of this class represents an adventurer in a RPG game
# Instance variables:
# name = a string representation for the name of an adventurer object
# level = integer representation for the level of the adventurer object
# strength = integer representation for the strength of the adventurer object
# speed = integer representation for the speed of the adventurer object
# power = integer representation for the power of the adventurer object
# HP = integer representation for the number of hit points (how much damage the adventurer can no longer fight) an adventurer object has
# hidden = boolean representation for whether the adventurer object can be seen or not
# Methods:
# __init__ = initializes all the instance variables of the class listed above
# __repr__ = overrides the __repr__ method to return a string of the object in the format <Name> - HP: <Current HP>
# attack = defines the action of an attack - if the target is hidden, the target dodges the attack. if not, the target is hit with 4 times the strength of the attacker
# __lt__ = overrides the __lt__ method to compare the HP of two adventurer objects
#==========================================

class Adventurer:
    def __init__(self, name='', level=0, strength=0, speed=0, power=0):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level * 6
        self.hidden = False
    def __repr__(self):
        return self.name + ' - HP: ' + str(self.HP)
    def attack(self, target):
        if target.hidden == True:
            print(self.name + " can't see " + target.name)
        else:
            attack_damage = self.strength + 4
            target.HP -= attack_damage
            print(self.name + ' attacks ' + target.name + ' for ' + str(attack_damage) + ' damage')
    def __lt__(self, other):
        if self.HP < other.HP:
            return True
        else:
            return False
        
#A - Part 2
#==========================================
# Purpose: An object of this class represents an Adventurer, specifically a Thief, in a RPG game
# Instance variables:
# name = a string representation for the name of a Thief object
# level = integer representation for the level of the Thief object
# strength = integer representation for the strength of the Thief object
# speed = integer representation for the speed of the Thief object
# power = integer representation for the power of the Thief object
# HP = integer representation for the number of hit points (how much damage the adventurer can no longer fight) an Thief object has
# hidden = boolean representation for whether the Thief object can be seen or not
# Methods:
# __init__ = inherits the initializations from the Adventerur class and changes initial values for the HP and hidden instance variables
# attack = overrides the action of an attack - if the target is hidden, the Thief inherits the Adventurer attack method, if not, the Thief sneak attacks with 5 times the power of its speed and level combined
#==========================================

class Thief(Adventurer):
    def __init__(self, name='', level=0, strength=0, speed=0, power=0):
        super().__init__(name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True
    def attack(self, target):
        if self.hidden == False:
            super().attack(target)
        else:
            sneak_attack = (self.speed + self.level) * 5
            target.HP -= sneak_attack
            self.hidden = False
            target.hidden = False
            print(self.name + ' sneak attacks ' + target.name + ' for ' + str(sneak_attack) + ' damage')

#A - Part 3
#==========================================
# Purpose: An object of this class represents a Ninja, a more powerful version of a Thief, in a RPG game
# Instance variables:
# name = a string representation for the name of a Ninja object
# level = integer representation for the level of the Ninja object
# strength = integer representation for the strength of the Ninja object
# speed = integer representation for the speed of the Ninja object
# power = integer representation for the power of the Ninja object
# HP = integer representation for the number of hit points (how much damage the adventurer can no longer fight) an Ninja object has
# hidden = boolean representation for whether the Ninja object can be seen or not
# Methods:
# attack = overrides the action of an attack - the Ninja attacks similarly as the Thief so it inherits the attack function, but after it attacks, it also hides itself again and gains a regeneration of health equal to its level to 
#==========================================

class Ninja(Thief):
    def attack(self, target):
        super().attack(target)
        self.hidden = True
        self.HP += self.level
        
#A - Part 4
#==========================================
# Purpose: An object of this class represents an Adventurer, specifically a Mage, in a RPG game
# Instance variables:
# name = a string representation for the name of a Mage object
# level = integer representation for the level of the Mage object
# strength = integer representation for the strength of the Mage object
# speed = integer representation for the speed of the Mage object
# power = integer representation for the power of the Mage object
# HP = integer representation for the number of hit points (how much damage the adventurer can no longer fight) an Mage object has
# fireballs_left = the number of fireballs the Mage has left to use for attack
# hidden = boolean representation for whether the Mage object can be seen or not
# Methods:
# __init__ = inherits the initializations from the Adventerur class and initializes the fireballs_left instance variable
# attack = overrides the action of an attack - if the number of fireballs left is 0 is hidden, the Mage inherits the Adventurer attack method, if not, the Mage shoots a fireball with 3 times the power of its level
#==========================================

class Mage(Adventurer):
    def __init__(self, name='', level=0, strength=0, speed=0, power=0):
        super().__init__(name, level, strength, speed, power)
        self.fireballs_left = self.power
    def attack(self, target):
        if self.fireballs_left == 0:
            super().attack(target)
        else:
            fireball_damage = self.level * 3
            target.HP -= fireball_damage
            self.fireballs_left -=1
            target.hidden = False
            print(self.name + ' casts a fireball on ' + target.name + ' for ' + str(fireball_damage) + ' damage')

#A - Part 5
#==========================================
# Purpose: An object of this class represents a Wizard, a more powerful version of a Mage, in a RPG game
# Instance variables:
# name = a string representation for the name of a Wizard object
# level = integer representation for the level of the Wizard object
# strength = integer representation for the strength of the Wizard object
# speed = integer representation for the speed of the Wizard object
# power = integer representation for the power of the Wizard object
# HP = integer representation for the number of hit points (how much damage the adventurer can no longer fight) an Wizard object has
# hidden = boolean representation for whether the Wizard object can be seen or not
# fireballs_left = the number of fireballs the Mage has left to use for attack
# Methods:
# __init__ = inherits the initializations from the Wizard class but changes the initializations of HP and fireballs_left instance variables
#==========================================

class Wizard(Mage):
    def __init__(self, name='', level=0, strength=0, speed=0, power=0):
        super().__init__(name, level, strength, speed, power)
        self.HP = self.level * 4
        self.fireballs_left = self.power * 2

#B

def battle(player_list, enemy_list):

    while len(player_list) >= 1 and len(enemy_list) >= 1:
        print('----------Player Turn----------')
        print('Your team: ')
        for player in player_list:
            print(player)
        print()
        for player in player_list:
            for num in range(len(enemy_list)):
                print('Enemy ' + str(num + 1) + ' : ' + str(enemy_list[num]))
            print()
            attack_who = input('Choose a target for ' + player.name + ': ')
            enemy_target = enemy_list[int(attack_who)-1]
            player.attack(enemy_target)
            if enemy_target.HP <= 0:
                enemy_list.remove(enemy_target)
                print(enemy_target.name + ' was defeated!')
            if len(enemy_list) == 0:
                print('You Win!')
                return player_list
            
        print('----------Enemy Turn----------')
        for enemy in enemy_list:
            player_target = min(player_list)
            enemy.attack(player_target)
            if player_target.HP <= 0:
                player_list.remove(player_target)
                print(player_target.name + ' was defeated!')
            if len(player_list) == 0:
                print('You Lose!')
                return enemy_list
                
        print()
