========================================
CODE
========================================

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Super Power: {self.super_power}\n"
                f"Weapon: {self.weapon}")

    def is_leader(self):
        return self.leader


super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]

captain_america = Avenger("Captain America", 105, "Male", "Super strength", "Shield", leader=True)
iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 39, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 45, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir")
hawkeye = Avenger("Hawkeye", 43, "Male", "Fighting skills", "Bow and Arrows")

avengers_team = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]

for avenger in avengers_team:
    print(avenger.get_info())
    print("Is Leader:", avenger.is_leader())
    print("-" * 30)


========================================
OUTPUT
========================================

Name: Captain America
Age: 105
Gender: Male
Super Power: Super strength
Weapon: Shield
Is Leader: True
------------------------------
Name: Iron Man
Age: 48
Gender: Male
Super Power: Technology
Weapon: Armor
Is Leader: False
------------------------------
Name: Black Widow
Age: 39
Gender: Female
Super Power: Superhuman
Weapon: Batons
Is Leader: False
------------------------------
Name: Hulk
Age: 45
Gender: Male
Super Power: Unlimited Strength
Weapon: No Weapon
Is Leader: False
------------------------------
Name: Thor
Age: 1500
Gender: Male
Super Power: Super Energy
Weapon: Mjolnir
Is Leader: False
------------------------------
Name: Hawkeye
Age: 43
Gender: Male
Super Power: Fighting skills
Weapon: Bow and Arrows
Is Leader: False
------------------------------
