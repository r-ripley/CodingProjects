import math

class Warrior:
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []
        def experience():
            return warrior.experience
        def level():
            warrior.level = warrior.experience / 100
            return warrior.level
        def rank():
            warrior.rank = int(warrior.level / 10)
            return warrior.rank
        def achievements():
            return warrior.achievements
        
    def training(self, battleInfo):
        # Pushover, Novice, Fighter, Warrior, Veteran, Sage, Elite, Conqueror, Champion, Master, Greatest
        ranks = {0: "Pushover",
                 1: "Novice",
                 2: "Fighter",
                 3: "Warrior",
                 4: "Veteran",
                 5: "Sage",
                 6: "Elite",
                 7: "Conqueror",
                 8: "Champion",
                 9: "Master",
                 10: "Greatest"}
        
        # add achievements if battle is won
        if self.level >= battleInfo[2]:
            self.experience += battleInfo[1]
            # set experiece back if it is capped
            if self.experience > 10000:
                self.experience = 10000
            # reduce experience and add to level
            self.level = math.floor(self.experience / 100)
            self.rank = ranks[int(self.level / 10)]
            self.achievements.append(battleInfo[0])
            return battleInfo[0]
        else:
            return "Not strong enough"
        
    def battle(self, enemyLevel):
        ranks = {0: "Pushover",
                 1: "Novice",
                 2: "Fighter",
                 3: "Warrior",
                 4: "Veteran",
                 5: "Sage",
                 6: "Elite",
                 7: "Conqueror",
                 8: "Champion",
                 9: "Master",
                 10: "Greatest"}
        if enemyLevel < 1 or enemyLevel > 100:
            return "Invalid level"
        else:
            # various edge cases for beating enemy combatants
            if enemyLevel - self.level >= 5 and int(enemyLevel / 10) - int(self.level / 10) >= 1:
                return "You've been defeated"
            if self.level == enemyLevel:
                self.experience += 10
                self.level = math.floor(self.experience / 100)
                self.rank = self.rank
                return "A good fight"
            elif self.level - enemyLevel == 1:
                self.experience += 5
                self.level = math.floor(self.experience / 100)
                self.rank = self.rank
                return "A good fight"
            elif self.level - enemyLevel >= 2:
                return "Easy fight"
            elif self.level < enemyLevel:
                self.experience += 20 * (enemyLevel - self.level) * (enemyLevel - self.level)
                self.level = math.floor(self.experience / 100)
                self.rank = ranks[int(self.level / 10)]
                return "An intense fight"
            if self.rank == "Greatest":
                self.experience = 10000
                self.level = 100