import sys
import numpy as np
from IPython import embed
import logging

logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[logging.StreamHandler()]
        )
log = logging.getLogger("Valkyrie")
log.setLevel(logging.INFO)
log.info("Logger initialized")

CREATURE_TYPES = ["Abberation","Animal","Celestial","Construct", "Dragon",\
"Elemental","Fey","Fiend","Giant","Humanoid","Magical Beast","Monstrous Humanoid",\
"Ooze","Outsider","Plant","Undead","Vermin"] #exhaustive list

DAMAGE_TYPES = ["Acid","Bludgeoning","Cold","Fire","Force","Lightning","Necrotic", \
                "Piercing","Poison","Psychic","Radiant","Slashing","Thunder"]

CONDITIONS = ["Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated",\
              "Invisible", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", \
              "Stunned", "Unconcious", "Exhausted"]

class Creature():
    ''' Creature class, embodies all elements related to a single creature '''
    def __init__(self, name: str, ac: int, hp: int, type: str,\
                 resistances=[],vulnerabilities=[],immunities=[],\
                 conditions=[],\
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
            if(type in CREATURE_TYPES):
                self.type = type
            else:
                raise ValueError(f"Type must be in the 5e creature type list, not {type}!")
        else:
            raise TypeError(f"Type must be a string, and in the 5e creature type list, not {type}")

        #Sets creature resistances
        if resistances:
            self.resistances = [x.capitalize() for x in resistances if x.capitalize() in DAMAGE_TYPES]
        else:
            self.resistances = resistances

        #Sets creature vulnerabilites
        if vulnerabilities:
            self.vulnerabilities = [x.capitalize() for x in vulnerabilities if x.capitalize() in DAMAGE_TYPES]
        else:
            self.vulnerabilities = vulnerabilities
     
        #Sets creature conditions
        if conditions:
            self.conditions = [x.capitalize() for x in conditions if x.capitalize() in CONDITIONS]
        else:
            self.conditions = conditions

        #Sets creature immunities
        if immunities:
            self.immunities = [x.capitalize() for x in immunities if x.capitalize() in DAMAGE_TYPES]
        else:
            self.immunities = immunities

    def __str__(self):
        description = f"<{self.type}: {self.name}, (HP: {self.hp}, AC: {self.ac})>"
        return description

    def __repr__(self):
        return self.__str__()

    def hit(self,damage,type=None):
        if isinstance(damage, int):
            if type is None or type not in DAMAGE_TYPES: #TODO: Update this to interface
                print("Damage type needed, please select type:")
                for index, damage_type in zip(range(len(DAMAGE_TYPES)), DAMAGE_TYPES):
                    print(f"{damage_type} : {index}")
                idx = int(input("Select damage type by index: "))
                type = DAMAGE_TYPES[idx]
                print(f"You've selected {type}")
        if type in self.resistances:
            damage = np.floor(0.5*damage)
            log.info(f"{self.name} is resistant to {type}!")
        elif type in self.vulnerabilities:
            damage = 2*damage 
            log.info(f"{self.name} is vulnerable to {type}!")
        elif type in self.immunities: 
            damage = 0
            log.info(f"{self.name} is immune to {type}!")
        self.hp -= damage 
        log.info(f"{self.name} takes {damage} {type}: hitpoints reduced to {self.hp}")
        if self.hp <= 0:
            self.conditions.append("Unconcious") 

if __name__ == '__main__':
    Bandit = Creature("Yorick",14,50,"Humanoid")
    print(Bandit)
    Bandit_2 = Creature("Edward", 14, 50, "Undead", ("Cold","Fire"))
    embed()

#TODO:
# Implement attacks, weapons, spells 
