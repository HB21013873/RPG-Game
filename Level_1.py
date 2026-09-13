import random
import time
import copy
import sys
import os
from datetime import datetime
from gamalgo import gamalgo   
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Enemy_Level_Up_abs import Level_Up_Enemy as L
class Level_1:
    def Level_1 (Enemy,Player_copy,b,place):
            now = datetime.now()
            Weakpoints = ["head", "leftleg", "rightleg", "leftarm", "rightarm", "chest", "back"]

            Enemy1_Weakpoint = random.choice(Weakpoints)
            Enemy2_Weakpoint = random.choice(Weakpoints)
            Enemy3_Weakpoint = random.choice(Weakpoints)
            if place == "Burning Armory":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Fire Imp": 30,
                        "Rust Golem": 10,
                        "Bandit": 20,
                        "Scavenger": 25,
                        "Goblin": 35
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Fire Mage": 15,
                        "Orc Warrior": 5,
                        "Bandit": 30,
                        "Steel Automaton": 15,
                        "Armory Guard": 25
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Fire Imp": 35,
                        "Orc Warrior": 5,
                        "Flame Warden": 10,
                        "Ash Soldier": 15,
                        "Burning Spirit": 15
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Flame Wraith": 20,
                        "Ash Golem": 10,
                        "Molten Knight": 5,
                        "Inferno Elemental": 15,
                        "Cursed Blacksmith": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Frozen Cavern":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Wolf": 20,
                        "Frozen Rat": 35,
                        "Ice Kobold": 40,
                        "Snow Spider": 45,
                        "Ice Bat": 30
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Ice Kobold": 40,
                        "Frost Skeleton": 20,
                        "Ice Archer": 10,
                        "Frost Wolf": 15,
                        "Ice Slime": 30
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Ice Golem": 25,
                        "Frost Knight": 5,
                        "Glacier Beast": 15,
                        "Snow Stalker": 15,
                        "Frozen Warrior": 15
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Frost Wraith": 30,
                        "Blizzard Spirit": 25,
                        "Ancient Ice Beast": 20,
                        "Ice Demon": 15,
                        "Frozen Lich": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Poison Swamp Chamber":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Wolf": 15,
                        "Venom Spider": 40,
                        "Swamp Rat": 35,
                        "Bog Snake": 20,
                        "Mud Crawler": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Venom Spider": 40,
                        "Swamp Goblin": 25,
                        "Poison Slime": 30,
                        "Bog Serpent": 20,
                        "Rot Beast": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Poison Slime": 40,
                        "Swamp Beast": 5,
                        "Plague Crow": 30,
                        "Rot Walker": 20,
                        "Acid Elemental": 15
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Plague Spirit": 30,
                        "Swamp Horror": 25,
                        "Venom Wraith": 20,
                        "Toxic Horror": 15,
                        "Disease Demon": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint



            if place == "Storm Tower Top":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Cultist": 35,
                        "Lightning Sprite": 25,
                        "Storm Crow": 18,
                        "Initiate Mage": 12,
                        "Tower Apprentice": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Cultist": 30,
                        "Wind Spirit": 25,
                        "Lightning Elemental": 20,
                        "Storm Mage": 15,
                        "Thunder Archer": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Lightning Elemental": 30,
                        "Storm Spirit": 25,
                        "Storm Knight": 20,
                        "Thunder Beast": 15,
                        "Charged Golem": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Thunder Wraith": 30,
                        "Lightning Phantom": 25,
                        "Storm Knight": 20,
                        "Sky Demon": 15,
                        "Tempest Lord": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Shadow Realm Floor":

                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Void Spawn": 35,
                        "Void Wraith": 25,
                        "Nightmare Beast": 18,
                        "Abyss Walker": 14,
                        "Shadow Lord": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Blood Arena":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Bandit": 35,
                        "Goblin Fighter": 30,
                        "Pit Dog": 20,
                        "Arena Trainee": 10,
                        "Rogue Fighter": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Orc Warrior": 30,
                        "Shield Fighter": 25,
                        "Spearman": 20,
                        "Gladiator": 15,
                        "Arena Archer": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Berserker": 30,
                        "Executioner": 25,
                        "War Demon": 20,
                        "Arena Champion": 15,
                        "Champion Spirit": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Duelist": 30,
                        "Heavy Knight": 25,
                        "War Beast": 20,
                        "Blood Knight": 15,
                        "Arena Champion": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint


            if place == "Alchemist Lab":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Slime": 40,
                        "Tiny Ooze": 25,
                        "Mutant Rat": 18,
                        "Failed Experiment": 10,
                        "Chemical Spider": 7
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Poison Slime": 35,
                        "Mutant Rat": 30,
                        "Acid Slime": 20,
                        "Experiment Soldier": 10,
                        "Potion Spirit": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Living Potion": 35,
                        "Failed Experiment": 25,
                        "Acid Beast": 20,
                        "Alchemical Horror": 15,
                        "Mutation Ogre": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Homunculus": 30,
                        "Toxic Elemental": 25,
                        "Plague Experiment": 20,
                        "Alchemical Horror": 15,
                        "Mad Alchemist Spirit": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Crumbling Bridge":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Goblin": 35,
                        "Wolf": 30,
                        "Bridge Thief": 15,
                        "Traveler Bandit": 12,
                        "Rogue Archer": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Bandit": 35,
                        "Goblin Archer": 25,
                        "Bridge Guard": 18,
                        "Spearman": 15,
                        "Rogue Knight": 7
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "War Hound": 35,
                        "Ambush Rogue": 25,
                        "Heavy Bandit": 20,
                        "Stone Golem": 12,
                        "Bridge Troll": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Ghost": 35,
                        "Lost Traveler Spirit": 25,
                        "Bridge Wraith": 18,
                        "Night Stalker": 12,
                        "Phantom Knight": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Dark Ritual Room":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Cultist": 35,
                        "Bone Servant": 25,
                        "Dark Acolyte": 18,
                        "Ritual Guard": 14,
                        "Shadow Mage": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Cultist": 35,
                        "Demon Imp": 30,
                        "Dark Mage": 18,
                        "Ritual Knight": 12,
                        "Summoner": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Summoned Demon": 35,
                        "Ritual Beast": 25,
                        "Bone Golem": 18,
                        "Demon Warrior": 14,
                        "Blood Mage": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Void Spawn": 35,
                        "Shadow Demon": 25,
                        "Ritual Demon": 20,
                        "Demon Lord Servant": 12,
                        "Abyss Summoner": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint

            if place == "Collapsing Ruins":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Ruin Rat": 35,
                        "Bone Dog": 25,
                        "Skeleton": 20,
                        "Zombie": 15,
                        "Broken Knight": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Skeleton": 35,
                        "Zombie": 30,
                        "Tomb Robber": 18,
                        "Ancient Archer": 12,
                        "Stone Guardian": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Dust Spirit": 35,
                        "Bone Warrior": 30,
                        "Tomb Knight": 15,
                        "Ruin Golem": 12,
                        "Ancient Guardian": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Lich Servant": 35,
                        "Curse Spirit": 25,
                        "Bone Golem": 20,
                        "Ruin Wraith": 15,
                        "Ancient Lich": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint


            if place == "Wilderness":
                start_hour = 0
                end_hour = 12
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Slime": 40,
                        "Goblin": 30,
                        "Wolf": 20,
                        "Kobold": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 12
                end_hour = 18
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Wolf": 40,
                        "Goblin": 35,
                        "Bandit": 20,
                        "Orc Warrior": 5
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)
                        

                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 18
                end_hour = 21
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Kobold": 20,
                        "Bandit": 15,
                        "Venom Spider": 12,
                        "Orc Warrior": 8
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)


                            
                    if b >= 3:
                        return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                    elif b >= 2:
                        return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                    elif b >= 1:
                        return Enemy1,Enemy1_Weakpoint
                start_hour = 21
                end_hour = 24
                if start_hour <= now.hour < end_hour:
                    Enemy_Chances = {
                        "Ghost": 35,
                        "Night Wolf": 25,
                        "Void Spawn": 20,
                        "Shadow Beast": 10
                    }
                    if b >= 1:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy1 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy1["Level"] = random.randint(1,3)
                        Enemy1,Enemy1_Starting_Mana = L.Level_Up_Enemy1(Enemy1,Player_copy)
                    if b >= 2:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy2 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy2["Level"] = random.randint(1,3)
                        Enemy2,Enemy2_Starting_Mana = L.Level_Up_Enemy2(Enemy2,Player_copy)
                    if b >= 3:
                        Enemy_Name = gamalgo.ratio(Enemy_Chances)
                        Enemy3 = copy.deepcopy(Enemy["Tier 1"][Enemy_Name])
                        Enemy3["Level"] = random.randint(1,3)
                        Enemy3,Enemy3_Starting_Mana = L.Level_Up_Enemy3(Enemy3,Player_copy)

                    
                if b>= 3:
                    return Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint
                elif b >= 2:
                    return Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint
                elif b >= 1:
                    return Enemy1,Enemy1_Weakpoint


