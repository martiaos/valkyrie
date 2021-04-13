import sys
import numpy as np
from IPython import embed

creature_types = ["Abberation","Animal","Celestial","Construct", "Dragon",\
"Elemental","Fey","Fiend","Giant","Humanoid","Magical Beast","Monstrous Humanoid",\
"Ooze","Outsider","Plant","Undead","Vermin"] #exhaustive list

damage_types = ["None", "Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic", \
                "Piercing","Poison","Psychic","Radiant","Slashing","Thunder"]

class Creature():
    ''' Creature class, embodies all elements related to a single creature '''
    def __init__(self, name: str, ac: int, hp: int, type: str,\
                 resistances=[],vulnerabilities=[],immunities=[],\
                 attributes={"str":10, "con":10, "dex":10, "int":10, "wis":10, "cha":10},\
                 senses=[], languages=[], CR=None):
        ''' Initiates the class, requires name, hp, ac and type '''
        #Sets name
        if(isinstance(name, str)):
            self.name = name
        else:
            raise TypeError(f"Name must be a string, not {name}!")

        #Sets AC
        if(isinstance(ac, int)):
            if 0 <= ac <= 30:
                self.ac = ac
            else:
                raise ValueError(f"Be reasonable, Armor Class cannot be {ac}!")
        else:
            raise TypeError(f"Armor class must be an integer, not {ac}!")

        #Sets HP
        if(isinstance(hp, int)):
            if 0 <= hp <= 999:
                self.hp = hp
            else:
                raise ValueError(f"Be reasonable, HP cannot be {hp}!")
        else:
            raise TypeError(f"HP must be an integer, not {hp}!")

        #Sets creature type
        if(isinstance(type, str)):
            if(type in creature_types):
                self.type = type
            else:
                raise ValueError(f"Type must be in the 5e creature type list, not {type}!")
        else:
            raise TypeError(f"Type must be a string, and in the 5e creature type list, not {type}")

        #Sets creature resistances
        if resistances is not None:
            if (x in damage_types for x in resistances):
                self.resistances = resistances
            else:
                raise TypeError(f"Resistances must be amongst the damage types, not {resistances}")
        else:
            self.resistances = resistances

    def __str__(self):
        description = f"Name: {self.name} AC: {self.ac} HP: {self.hp}"
        return description

    def hit(self,damage,type=None):
        if isinstance(damage, int):
            if type is None or type not in damage_types:
                print("Damage type needed, please select type:")
                for index, damage_type in zip(range(len(damage_types)), damage_types):
                    print(f"{damage_type} : {index}")
                idx = int(input("Select damage type by index: "))
                type = damage_types[idx]
                print(f"You've selected {type}")
        if damage >= 1 :
            print(type)
            if type in self.resistances:
                damage = 2*damage
                print(f"{self.name} is vulnerable to {type}!")
            self.hp -= damage
            print(f"{self.name} takes {damage} {type} damage: hitpoints reduced to {self.hp}")
            if self.hp <= 0:
                print(f"{self.name} is defeated!")

if __name__ == '__main__':
    Bandit = Creature("Yorick",14,50,"Humanoid")
    print(Bandit)
    Bandit_2 = Creature("Edward", 14, 50, "Undead", ("Cold","Fire"))
    embed()
