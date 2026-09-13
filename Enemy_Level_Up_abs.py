import random
import time
import copy
class Level_Up_Enemy:

    def Level_Up_Enemy1(Enemy1,Player_copy):

        Enemy1["Attack"] = round(Enemy1["Attack"] + (Enemy1["Level"] * 4) + (Player_copy["Tower Level"] * 12))
        Enemy1["Defense"] = round(Enemy1["Defense"] + (Enemy1["Level"] * 2) + (Player_copy["Tower Level"] * 2))
        Enemy1["Max Health"] = round(Enemy1["Max Health"] + (Enemy1["Level"] * 6) + (Player_copy["Tower Level"] * 1.5))
        Enemy1["Health"] = copy.deepcopy(Enemy1["Max Health"])
        Enemy1["Stamina"] = round(Enemy1["Stamina"] + (Enemy1["Level"] * 3) + (Player_copy["Tower Level"] * 0.8))
        Enemy1["Speed"] = round(Enemy1["Speed"] + (Enemy1["Level"] * 1.5) + (Player_copy["Tower Level"] * 1.8))
        Enemy1["Accuracy"] = round(Enemy1["Accuracy"] + (Enemy1["Level"] * 0.5) + (Player_copy["Tower Level"] * 0.7))
        Enemy1["Critical Chance"] = round(Enemy1["Critical Chance"] + (Enemy1["Level"] * 0.3) + (Player_copy["Tower Level"] * 0.2))
        Enemy1["Magic Density"] = round(Enemy1["Magic Density"] + (Enemy1["Level"] * 0.4) + (Player_copy["Tower Level"] * 0.25))
        Enemy1["Magic Damage"] = round(Enemy1["Magic Damage"] + (Enemy1["Level"] * 0.6) + (Player_copy["Tower Level"] * 0.15))
        Enemy1["Critical Damage"] = round(Enemy1["Critical Damage"] + (Enemy1["Level"] * 0.8) + (Player_copy["Tower Level"] * 0.5))
        Enemy1["Evasion"] = round(Enemy1["Evasion"] + (Enemy1["Level"] * 0.7) + (Player_copy["Tower Level"] * 5))
        Enemy1["Mana"] = round(Enemy1["Mana"] + (Enemy1["Level"] * 4) + (Player_copy["Tower Level"] * 4))
        Enemy1_Starting_Mana = Enemy1["Mana"]
        return Enemy1,Enemy1_Starting_Mana

    def Level_Up_Enemy2(Enemy2,Player_copy):
        Enemy2["Attack"] = round(Enemy2["Attack"] + (Enemy2["Level"] * 4) + (Player_copy["Tower Level"] * 12))
        Enemy2["Defense"] = round(Enemy2["Defense"] + (Enemy2["Level"] * 2) + (Player_copy["Tower Level"] * 2))
        Enemy2["Max Health"] = round(Enemy2["Max Health"] + (Enemy2["Level"] * 6) + (Player_copy["Tower Level"] * 1.5))
        Enemy2["Health"] = copy.deepcopy(Enemy2["Max Health"])
        Enemy2["Stamina"] = round(Enemy2["Stamina"] + (Enemy2["Level"] * 3) + (Player_copy["Tower Level"] * 0.8))
        Enemy2["Speed"] = round(Enemy2["Speed"] + (Enemy2["Level"] * 1.5) + (Player_copy["Tower Level"] * 1.8))
        Enemy2["Accuracy"] = round(Enemy2["Accuracy"] + (Enemy2["Level"] * 0.5) + (Player_copy["Tower Level"] * 0.7))
        Enemy2["Critical Chance"] = round(Enemy2["Critical Chance"] + (Enemy2["Level"] * 0.3) + (Player_copy["Tower Level"] * 0.2))
        Enemy2["Magic Density"] = round(Enemy2["Magic Density"] + (Enemy2["Level"] * 0.4) + (Player_copy["Tower Level"] * 0.25))
        Enemy2["Magic Damage"] = round(Enemy2["Magic Damage"] + (Enemy2["Level"] * 0.6) + (Player_copy["Tower Level"] * 0.15))
        Enemy2["Critical Damage"] = round(Enemy2["Critical Damage"] + (Enemy2["Level"] * 0.8) + (Player_copy["Tower Level"] * 0.5))
        Enemy2["Evasion"] = round(Enemy2["Evasion"] + (Enemy2["Level"] * 0.7) + (Player_copy["Tower Level"] * 5))
        Enemy2["Mana"] = round(Enemy2["Mana"] + (Enemy2["Level"] * 4) + (Player_copy["Tower Level"] * 4))
        Enemy2_Starting_Mana = Enemy2["Mana"]
        return Enemy2,Enemy2_Starting_Mana
    def Level_Up_Enemy3(Enemy3,Player_copy):
        Enemy3["Attack"] = round(Enemy3["Attack"] + (Enemy3["Level"] * 4) + (Player_copy["Tower Level"] * 12))
        Enemy3["Defense"] = round(Enemy3["Defense"] + (Enemy3["Level"] * 2) + (Player_copy["Tower Level"] * 2))
        Enemy3["Max Health"] = round(Enemy3["Max Health"] + (Enemy3["Level"] * 6) + (Player_copy["Tower Level"] * 1.5))
        Enemy3["Health"] = copy.deepcopy(Enemy3["Max Health"])
        Enemy3["Stamina"] = round(Enemy3["Stamina"] + (Enemy3["Level"] * 3) + (Player_copy["Tower Level"] * 0.8))
        Enemy3["Speed"] = round(Enemy3["Speed"] + (Enemy3["Level"] * 1.5) + (Player_copy["Tower Level"] * 1.8))
        Enemy3["Accuracy"] = round(Enemy3["Accuracy"] + (Enemy3["Level"] * 0.5) + (Player_copy["Tower Level"] * 0.7))
        Enemy3["Critical Chance"] = round(Enemy3["Critical Chance"] + (Enemy3["Level"] * 0.3) + (Player_copy["Tower Level"] * 0.2))
        Enemy3["Magic Density"] = round(Enemy3["Magic Density"] + (Enemy3["Level"] * 0.4) + (Player_copy["Tower Level"] * 0.25))
        Enemy3["Magic Damage"] = round(Enemy3["Magic Damage"] + (Enemy3["Level"] * 0.6) + (Player_copy["Tower Level"] * 0.15))
        Enemy3["Critical Damage"] = round(Enemy3["Critical Damage"] + (Enemy3["Level"] * 0.8) + (Player_copy["Tower Level"] * 0.5))
        Enemy3["Evasion"] = round(Enemy3["Evasion"] + (Enemy3["Level"] * 0.7) + (Player_copy["Tower Level"] * 5))
        Enemy3["Mana"] = round(Enemy3["Mana"] + (Enemy3["Level"] * 4) + (Player_copy["Tower Level"] * 4))
        Enemy3_Starting_Mana = Enemy3["Mana"]
        return Enemy3,Enemy3_Starting_Mana
    def Level_Up_Boss(Boss,Player_copy):
        Boss["Attack"] = round(Boss["Attack"] + (Boss["Level"] * 6) + (Player_copy["Tower Level"] * 12))
        Boss["Defense"] = round(Boss["Defense"] + (Boss["Level"] * 4) + (Player_copy["Tower Level"] * 2))
        Boss["Max Health"] = round(Boss["Max Health"] + (Boss["Level"] * 8) + (Player_copy["Tower Level"] * 1.5))
        Boss["Health"] = copy.deepcopy(Boss["Max Health"])
        Boss["Stamina"] = round(Boss["Stamina"] + (Boss["Level"] * 5) + (Player_copy["Tower Level"] * 0.8))
        Boss["Speed"] = round(Boss["Speed"] + (Boss["Level"] * 2.5) + (Player_copy["Tower Level"] * 1.8))
        Boss["Accuracy"] = round(Boss["Accuracy"] + (Boss["Level"] * 1.5) + (Player_copy["Tower Level"] * 0.7))
        Boss["Critical Chance"] = round(Boss["Critical Chance"] + (Boss["Level"] * 0.6) + (Player_copy["Tower Level"] * 0.2))
        Boss["Magic Density"] = round(Boss["Magic Density"] + (Boss["Level"] * 0.8) + (Player_copy["Tower Level"] * 0.25))
        Boss["Magic Damage"] = round(Boss["Magic Damage"] + (Boss["Level"] * 1.2) + (Player_copy["Tower Level"] * 0.15))
        Boss["Critical Damage"] = round(Boss["Critical Damage"] + (Boss["Level"] * 1.6) + (Player_copy["Tower Level"] * 0.5))
        Boss["Evasion"] = round(Boss["Evasion"] + (Boss["Level"] * 1.4) + (Player_copy["Tower Level"] * 5))
        Boss["Mana"] = round(Boss["Mana"] + (Boss["Level"] * 8) + (Player_copy["Tower Level"] * 4))
        Boss_Starting_Mana = Boss["Mana"]

        return Boss,Boss_Starting_Mana

    
