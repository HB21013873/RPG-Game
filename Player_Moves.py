import random
import time
import sys
import builtins
from Text_Writing_Style import TypeWriter as TW
tw = TW(delay=0.02, jitter=True)
typewriter = True
def print(*args, sep=" ", end="\n"):
    if typewriter:
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
    else:
        builtins.print(*args, sep=sep, end=end)
class Player_Move:
    class Melee_Moves:
        class Head:
            def Headbutt(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs ):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Headbutt"]["Time"]:
                    if Combat_Skill_list["Headbutt"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int(( Combat_Skill_list["Headbutt"]["Damage"] * Player_copy["Attack"]/  target["Defense"]) )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( Combat_Skill_list["Headbutt"]["Damage"] * Player_copy["Attack"]/ ( target["Defense"]))
                        Combat_cost = Combat_Skill_list["Headbutt"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Headbutt"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                if target == Enemy1:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy1_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy2:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy2_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy3:
                                    chance = random.randint(1,5)
                                    if chance == 3:
                                        Enemy3_Skip = True
                                        print("The Enemy is stunned!\n")

                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")

                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Headbutt"]["Time"]
                else:
                    print("Not enough time")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip

            def Bite(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs ):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Bite"]["Time"]:
                    if Combat_Skill_list["Bite"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int(( Combat_Skill_list["Bite"]["Damage"] * Player_copy["Attack"]/  target["Defense"]) + (Body_Condition["Head"]["Strength"]) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int(( Combat_Skill_list["Bite"]["Damage"] * Player_copy["Attack"]/  target["Defense"]) + (Body_Condition["Head"]["Strength"]) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Bite"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Bite"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (target["Max Health"] * 0.05) <= Damage:
                                bleed_chance = random.random()
                                if bleed_chance < 0.15 and (Damage >= (target["Max Health"] * 0.05) and Damage <= (target["Max Health"] * 0.1) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.35 and (Damage >= (target["Max Health"] * 0.1) and Damage <= (target["Max Health"] * 0.15) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.6 and (Damage >= (target["Max Health"] * 0.15) and Damage <= (target["Max Health"] * 0.2) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.85 and (Damage >= (target["Max Health"] * 0.2) and Damage <= (target["Max Health"] * 0.3) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 1 and (Damage >= target["Max Health"] * 0.3):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)

                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")

                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Bite"]["Time"]
                else:
                    print("Not enough time")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 


        class Legs:

            def Front_Kick(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Straight Punch"]["Time"]:
                    if Combat_Skill_list["Straight Punch"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Straight Punch"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ( Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Straight Punch"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+( Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Straight Punch"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Front Kick"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Straight Punch"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip
            
            def Axe_Kick(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Axe Kick"]["Time"]:
                    if Combat_Skill_list["Axe Kick"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Axe Kick"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ (Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                            Damage = int( (Combat_Skill_list["Axe Kick"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ (Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Axe Kick"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Axe Kick"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                if target == Enemy1:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy1_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy2:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy2_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy3:
                                    chance = random.randint(1,5)
                                    if chance == 3:
                                        Enemy3_Skip = True
                                        print("The Enemy is stunned!\n")

                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                            target["Health"] -= Damage
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Axe Kick"]["Time"]
                else:
                    print("Not enough Time")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip


            def Spinning_Back_Kick(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Spinning Back Kick"]["Time"]:
                    if Combat_Skill_list["Spinning Back Kick"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Spinning Back Kick"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ (Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Spinning Back Kick"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ (Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Spinning Back Kick"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Spinning Back Kick"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                if target == Enemy1:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy1_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy2:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy2_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy3:
                                    chance = random.randint(1,5)
                                    if chance == 3:
                                        Enemy3_Skip = True
                                        print("The Enemy is stunned!\n")
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                            target["Health"] -= Damage
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Spinning Back Kick"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip
            def Groundbreaker(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Combat_Skill_list["Groundbreaker"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Combat_Skill_list["Groundbreaker"]["Damage"]    * Player_copy["Attack"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Combat_Skill_list["Groundbreaker"]["Damage"]    * Player_copy["Attack"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))

                        choice = "Groundbreaker"
                        Breaker = True
                        if Mana_Amount < Player_copy["Stamina"]:
                            Player_copy["Stamina"] -= Combat_Skill_list["Groundbreaker"]["Cost"]
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Groundbreaker"
                                Breaker = True
                                if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                    if target == Enemy1:
                                        chance = random.randint(1,5)
                                        if chance == 1:
                                            Enemy1_Skip = True
                                            print("The enemy is inflicted with stagger!\n")
                                            target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                            target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                    if target == Enemy2:
                                        chance = random.randint(1,5)
                                        if chance == 1:
                                            Enemy2_Skip = True
                                            print("The enemy is inflicted with stagger!\n")
                                            target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                            target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                    if target == Enemy3:
                                        chance = random.randint(1,5)
                                        if chance == 3:
                                            Enemy3_Skip = True
                                            print("The enemy is inflicted with stagger!\n")
                                            target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                            target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Combat_Skill_list["Groundbreaker"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip

        class Arms:
            def Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Straight Punch"]["Time"]:
                    if Combat_Skill_list["Straight Punch"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Straight Punch"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Straight Punch"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Straight Punch"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Straight Punch"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            target["Health"] -= Damage
                            print(f"\n{choice} is used\n")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Straight Punch"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip

            def Aimed_Shot(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs ):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Bite"]["Time"]:
                    if Combat_Skill_list["Aimed Shot"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int(( Combat_Skill_list["Aimed Shot"]["Damage"] * Player_copy["Attack"]/  target["Defense"]) + (Body_Condition["Head"]["Strength"]) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                            Damage = int(( Combat_Skill_list["Aimed Shot"]["Damage"] * Player_copy["Attack"]/  target["Defense"]) + (Body_Condition["Head"]["Strength"]) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Aimed Shot"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Aimed Shot"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/20))))):
                            if (target["Max Health"] * 0.05) <= Damage:
                                bleed_chance = random.random()
                                if bleed_chance < 0.15 and (Damage >= (target["Max Health"] * 0.05) and Damage <= (target["Max Health"] * 0.1) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.35 and (Damage >= (target["Max Health"] * 0.1) and Damage <= (target["Max Health"] * 0.15) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.6 and (Damage >= (target["Max Health"] * 0.15) and Damage <= (target["Max Health"] * 0.2) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.85 and (Damage >= (target["Max Health"] * 0.2) and Damage <= (target["Max Health"] * 0.3) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 1 and (Damage >= target["Max Health"] * 0.3):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)

                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")

                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Aimed Shot"]["Time"]
                else:
                    print("Not enough time")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 


            def Tackle(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Tackle"]["Time"]:
                    if Combat_Skill_list["Tackle"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Tackle"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Shoulder"]["Strength"] + Body_Condition["Legs"]["Strength"] + Body_Condition["Back"]["Strength"]) /3) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Tackle"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Shoulder"]["Strength"] + Body_Condition["Legs"]["Strength"] + Body_Condition["Back"]["Strength"]) /3) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Tackle"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Tackle"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Tackle"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 

            def Slash(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Slash"]["Time"]:
                    if Combat_Skill_list["Slash"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 50
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Slash"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/75))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Slash"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Slash"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Slash"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (Player_copy["Max Health"] * 0.05) <= Damage:
                                bleed_chance = random.random()
                                if bleed_chance < 0.15 and (Damage >= (target["Max Health"] * 0.05) and Damage <= (target["Max Health"] * 0.1) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.35 and (Damage >= (target["Max Health"] * 0.1) and Damage <= (target["Max Health"] * 0.15) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.6 and (Damage >= (target["Max Health"] * 0.15) and Damage <= (target["Max Health"] * 0.2) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.85 and (Damage >= (target["Max Health"] * 0.2) and Damage <= (target["Max Health"] * 0.3) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 1 and (Damage >= target["Max Health"] * 0.3):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                            Damage = round(Damage)
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Slash"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip



            def Quick_Stab(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Slash"]["Time"]:
                    if Combat_Skill_list["Slash"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 50
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Slash"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/75))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Slash"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Slash"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Quick Stab"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (Player_copy["Max Health"] * 0.05) <= Damage:
                                bleed_chance = random.random()
                                if bleed_chance < 0.15 and (Damage >= (target["Max Health"] * 0.05) and Damage <= (target["Max Health"] * 0.1) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.35 and (Damage >= (target["Max Health"] * 0.1) and Damage <= (target["Max Health"] * 0.15) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.6 and (Damage >= (target["Max Health"] * 0.15) and Damage <= (target["Max Health"] * 0.2) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 0.85 and (Damage >= (target["Max Health"] * 0.2) and Damage <= (target["Max Health"] * 0.3) ):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                if bleed_chance < 1 and (Damage >= target["Max Health"] * 0.3):
                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                        target["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                        target["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                        target["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                        print(f"{target} is bleeding")
                            Damage = round(Damage)
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Slash"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip

            def Impulsive_Swing(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Axe Kick"]["Time"]:
                    if Combat_Skill_list["Impulsive Swing"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Impulsive Swing"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ (Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                            Damage = int( (Combat_Skill_list["Impulsive Swing"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ (Body_Condition["Legs"]["Strength"]) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Impulsive Swing"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Impulsive Swing"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * 3))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                if target == Enemy1:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy1_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy2:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Enemy2_Skip = True
                                        print("The Enemy is stunned!\n")
                                if target == Enemy3:
                                    chance = random.randint(1,5)
                                    if chance == 3:
                                        Enemy3_Skip = True
                                        print("The Enemy is stunned!\n")

                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                            target["Health"] -= Damage
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Impulsive Swing"]["Time"]
                else:
                    print("Not enough Time")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip

            def Jab(Player_copy,Enemy,Combat_Skill_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = False
                target = kwargs.get("target", None)
                Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                name = kwargs.get("name",None)
                POI = kwargs.get("POI",None)
                Body_Condition = kwargs.get("Body_Condition",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                if Turn_Time >= Combat_Skill_list["Jab"]["Time"]:
                    if Combat_Skill_list["Jab"]["Cost"] < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( (Combat_Skill_list["Jab"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int( (Combat_Skill_list["Jab"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"] )
                        Combat_cost = Combat_Skill_list["Jab"]["Cost"] * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Jab"
                        Breaker = True
                        if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                print("You hit a weakpoint!\n")
                                Damage = round(Damage* 1.5)
                            target["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"{name} does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= Combat_Skill_list["Jab"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 

 
    class Spell_Moves:
        class Elemental:

            class Fire:
                def Fireball(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Fireball"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Fireball"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Fireball"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Fireball"]["Damage"] / Spell_list["Fireball"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Fireball"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                if target["Type"] == "Venom Spider":
                                    Damage *= 2
                                choice = "Fireball"
                                Breaker = True
                                if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:
                                    burn_chance = random.randint(1,5)
                                    if burn_chance == 1:
                                        if target["Status Effects"]["Status 1"]["Type"] == "None":
                                            target["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            target["Status Effects"]["Status 1"]["Duration"] = 3
                                            print("They have been burnt")
                                        elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                            target["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            target["Status Effects"]["Status 2"]["Duration"] = 3
                                            print("They have been burnt")
                                        elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                            target["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            target["Status Effects"]["Status 3"]["Duration"] = 3
                                            print("They have been burnt")
                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:
                                                burn_chance = random.randint(1,5)
                                                if burn_chance == 1:
                                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                                        target["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                        target["Status Effects"]["Status 1"]["Duration"] = 3
                                                        print("They have been burnt")
                                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                                        target["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                        target["Status Effects"]["Status 2"]["Duration"] = 3
                                                        print("They have been burnt")
                                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                                        target["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                        target["Status Effects"]["Status 3"]["Duration"] = 3
                                                        print("They have been burnt")
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Fireball"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 
            class Ice:
                def Ice_Shard(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Ice Shard"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Ice Shard"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Ice Shard"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Ice Shard"]["Damage"] / Spell_list["Ice Shard"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Ice Shard"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                if "Fire" in target["Type"] or "Flame" in target["Type"] or "Burning" in target["Type"] or "Molten" in target["Type"] or "Inferno" in target["Type"] or  "Demon" in target["Type"] or "Ash" in target["Type"]:
                                    Damage *= 2
                                choice = "Ice Shard"
                                Breaker = True
                                if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:
                                    freeze_chance = random.randint(1,5)
                                    if freeze_chance == 1:
                                        if target["Status Effects"]["Status 1"]["Type"] == "None":
                                            target["Status Effects"]["Status 1"]["Type"] = "Freeze"
                                            target["Status Effects"]["Status 1"]["Duration"] = 2
                                            print("They have been Frozen")
                                        elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                            target["Status Effects"]["Status 2"]["Type"] = "Freeze"
                                            target["Status Effects"]["Status 2"]["Duration"] = 2
                                            print("They have been Frozen")
                                        elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                            target["Status Effects"]["Status 3"]["Type"] = "Freeze"
                                            target["Status Effects"]["Status 3"]["Duration"] = 2
                                            print("They have been Frozen")

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:
                                                freeze_chance = random.randint(1,5)
                                                if freeze_chance == 1:
                                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                                        target["Status Effects"]["Status 1"]["Type"] = "Freeze"
                                                        target["Status Effects"]["Status 1"]["Duration"] = 2
                                                        print("They have been Frozen")
                                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                                        target["Status Effects"]["Status 2"]["Type"] = "Freeze"
                                                        target["Status Effects"]["Status 2"]["Duration"] = 2
                                                        print("They have been Frozen")
                                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                                        target["Status Effects"]["Status 3"]["Type"] = "Freeze"
                                                        target["Status Effects"]["Status 3"]["Duration"] = 2
                                                        print("They have been Frozen")
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Ice Shard"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip
            class Lightning:
                def Shock(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Shock"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        Percentage2 = random.random()
                        Percentage3 = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Shock"]["Damage"]    * Player_copy["Magic Damage"]    / (Enemy1["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Shock"]["Damage"]    * Player_copy["Magic Damage"]    / (Enemy1["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        if Enemy2 != None:
                            if Percentage2 <= Player_copy_Critical_Chance:
                                Damage2 = int( Spell_list["Shock"]["Damage"]    * Player_copy["Magic Damage"]    / (Enemy2["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                                Damage2 *= (1 + (Player_copy["Critical Damage"]/100))
                            else:
                                Damage2 = int( Spell_list["Shock"]["Damage"]    * Player_copy["Magic Damage"]    / (Enemy2["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        if Enemy3 != None:
                            if Percentage3 <= Player_copy_Critical_Chance:
                                Damage3 = int( Spell_list["Shock"]["Damage"]    * Player_copy["Magic Damage"]    / (Enemy3["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                                Damage3 *= (1 + (Player_copy["Critical Damage"]/100))
                            else:
                                Damage3 = int( Spell_list["Shock"]["Damage"]    * Player_copy["Magic Damage"]    / (Enemy3["Defense"])    * (1 + Player_copy["Magic Density"] / 100))

                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Shock"]["Damage"] / Spell_list["Shock"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Shock"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                if Enemy2 != None:
                                    Damage2 += Damage_Amount
                                    Damage2 = round(Damage2)
                                if Enemy3 != None:
                                    Damage3  += Damage_Amount
                                    Damage3 = round(Damage3)
                                    
                                choice = "Shock"
                                Breaker = True

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint):
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and Enemy2 != None:
                                    print("You hit a weakpoint!\n")
                                    Damage2 = round(Damage2 * 1.5)
                                if (POI == Enemy3_Weakpoint) and Enemy3 != None:
                                    print("You hit a weakpoint!\n")
                                    Damage3 = round(Damage3 * 1.5)
                                Enemy1["Health"] -= Damage
                                if Enemy2 != None:
                                    Enemy2["Health"] -= Damage2
                                if Enemy3 != None:
                                    Enemy3["Health"] -= Damage3
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage to",Enemy1["Type"])
                                if Enemy2 != None:
                                    print(f"{name} does {Damage2} damage to",Enemy2["Type"])
                                if Enemy3 != None:
                                    print(f"{name} does {Damage3} damage to",Enemy3["Type"])
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            Enemy1["Health"] -= Damage
                                            if Enemy2 != None:
                                                Enemy2["Health"] -= Damage2
                                            if Enemy3 != None:
                                                Enemy3["Health"] -= Damage3
                                            print(f"{choice} is used")
                                            print(f"{name} does {Damage} damage to",Enemy1["Type"])
                                            if Enemy2 != None:
                                                print(f"{name} does {Damage2} damage to",Enemy2["Type"])
                                            if Enemy3 != None:
                                                print(f"{name} does {Damage3} damage to",Enemy3["Type"])
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Shock"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip
            class Water:
                def River_Fist(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["River Fist"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["River Fist"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100)/2)
                            Damage += int( ((Combat_Skill_list["River Fist"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"])/2)
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                            Damage = int( Spell_list["River Fist"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage += int( ((Combat_Skill_list["River Fist"]["Damage"] * Player_copy["Attack"]/  target["Defense"])+ ((Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"]) /3) / target["Defense"])/2)
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["River Fist"]["Damage"] / Spell_list["River Fist"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "River Fist"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                if "Fire" in target["Type"] or "Flame" in target["Type"] or "Burning" in target["Type"] or "Molten" in target["Type"] or "Inferno" in target["Type"] or  "Demon" in target["Type"] or "Ash" in target["Type"]:
                                    Damage *= 2
                                choice = "River Fist"
                                Breaker = True

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["River Fist"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 
            class Earth:
                def Mud_Shot(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Mud Shot"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Mud Shot"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Mud Shot"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Mud Shot"]["Damage"] / Spell_list["Mud Shot"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Mud Shot"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Mud Shot"
                                Breaker = True
                                mud_chance = random.randint(1,5)
                                if mud_chance == 1 and target == Enemy1:
                                    Enemy1["Accuracy"] -= (Enemy1["Accuracy"] * 0.1)
                                    print(Enemy1["Type"]," Accuracy has decreased by 10%")
                                if mud_chance == 1 and target == Enemy2:
                                    Enemy2["Accuracy"] -= (Enemy2["Accuracy"] * 0.1)
                                    print(Enemy2["Type"]," Accuracy has decreased by 10%")
                                if burn_chance == 1 and target == Enemy3:
                                    Enemy3["Accuracy"] -= (Enemy3["Accuracy"] * 0.1)
                                    print(Enemy3["Type"]," Accuracy has decreased by 10%")
                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            mud_chance = random.randint(1,5)
                                            if mud_chance == 1 and target == Enemy1:
                                                Enemy1["Accuracy"] -= (Enemy1["Accuracy"] * 0.1)
                                                print(Enemy1["Type"]," Accuracy has decreased by 10%")
                                            if mud_chance == 1 and target == Enemy2:
                                                Enemy2["Accuracy"] -= (Enemy2["Accuracy"] * 0.1)
                                                print(Enemy2["Type"]," Accuracy has decreased by 10%")
                                            if burn_chance == 1 and target == Enemy3:
                                                Enemy3["Accuracy"] -= (Enemy3["Accuracy"] * 0.1)
                                                print(Enemy3["Type"]," Accuracy has decreased by 10%")
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Mud Shot"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip
                
                def Tremor(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Tremor"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Tremor"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Tremor"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Tremor"]["Damage"] / Spell_list["Tremor"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Tremor"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Tremor"
                                Breaker = True
                                if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                    if target == Enemy1:
                                        chance = random.randint(1,5)
                                        if chance == 1:
                                            Enemy1_Skip = True
                                            print("The enemy is inflicted with stagger!\n")
                                            target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                            target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                    if target == Enemy2:
                                        chance = random.randint(1,5)
                                        if chance == 1:
                                            Enemy2_Skip = True
                                            print("The enemy is inflicted with stagger!\n")
                                            target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                            target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                    if target == Enemy3:
                                        chance = random.randint(1,5)
                                        if chance == 3:
                                            Enemy3_Skip = True
                                            print("The enemy is inflicted with stagger!\n")
                                            target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                            target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            if (target["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                                if target == Enemy1:
                                                    chance = random.randint(1,5)
                                                    if chance == 1:
                                                        Enemy1_Skip = True
                                                        print("The enemy is inflicted with stagger!\n")
                                                        target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                                        target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                                if target == Enemy2:
                                                    chance = random.randint(1,5)
                                                    if chance == 1:
                                                        Enemy2_Skip = True
                                                        print("The enemy is inflicted with stagger!\n")
                                                        target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                                        target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                                if target == Enemy3:
                                                    chance = random.randint(1,5)
                                                    if chance == 3:
                                                        Enemy3_Skip = True
                                                        print("The enemy is inflicted with stagger!\n")
                                                        target["Speed"] -= (target["Speed"] * random.randint(0.1,0.2))
                                                        target["Evasion"] -= (target["Evasion"] * random.randint(0.1,0.2))
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Tremor"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 
            class Wind:
                def Stone_Slipstream(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Stone Slipstream"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Stone Slipstream"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Stone Slipstream"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Stone Slipstream"]["Damage"] / Spell_list["Stone Slipstream"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Stone Slipstream"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Stone Slipstream"
                                Breaker = True

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                Damage /= 4
                                Damage = round(Damage)
                                num_Moves = random.randint(1,6)
                                for x in range(num_Moves):
                                    target["Health"] -= Damage
                                    chance = random.randint(1,8)
                                    if chance == 1 or chance == 2:
                                        target["Defense"] -= 1
                                    elif chance == 3 or chance == 4:
                                        target["Defense"] -= 5
                                Damage *= num_Moves
                                Damage = round(Damage)
                                print(f"\n{choice} is used\n")
                                print(f"\nYou hit {num_Moves} times")
                                print(f"{name} does {Damage} damage")
                                Damage /= num_Moves
                                Damage = round(Damage)
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            num_Moves = random.randint(1,6)
                                            for x in range(num_Moves):
                                                target["Health"] -= Damage
                                                chance = random.randint(1,8)
                                                if chance == 1 or chance == 2:
                                                    target["Defense"] -= 1
                                                elif chance == 3 or chance == 4:
                                                    target["Defense"] -= 5
                                            Damage *= num_Moves
                                            Damage = round(Damage)
                                            print(f"\nYou hit {num_Moves} times")
                                            print(f"{name} does {Damage} damage")
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Stone Slipstream"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 
            class Dark:
                def Life_Drain(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Life Drain"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Life Drain"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Life Drain"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Life Drain"]["Damage"] / Spell_list["Life Drain"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Life Drain"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Life Drain"
                                Breaker = True

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)

                                Damage = Damage * 0.8
                                Damage = round(Damage)
                                target["Health"] -= Damage
                                Health_Gained = round(Damage/2)
                                Player_copy["Health"] += Health_Gained
                                Player_copy["Health"] = round(Player_copy["Health"])
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                print("Health is now ",Player_copy["Health"])
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            Player_copy["Health"] += Health_Gained
                                            Player_copy["Health"] = round(Player_copy["Health"])
                                            print(f"{name} does {Damage} damage")
                                            print("Health is now ",Player_copy["Health"])
                                            Worked = True
                                        else:
                                            chance = False
                                
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Corrupting Touch"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip


                def Devour_Essence(Player_copy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    if Turn_Time >= Spell_list["Devour Essence"]["Time"]:
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                Mana_Amount = int(input(""))
                                Power_Amount = Mana_Amount * (Spell_list["Devour Essence"]["Power"] / Spell_list["Devour Essence"]["Cost"])
                                Power_Amount = round(Power_Amount)
                                Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                            except:
                                print("Not a number")
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                choice = "Devour Essence"
                                stat = random.choice(["Max Health","Health","Attack","Defense","Accuracy","Speed","Evasion","Mana","Stamina","Magic Damage","Magic Density","Critical Chance","Critical Damage"])
                                if stat == "Max Health":
                                    Player_copy["Max Health"] += Power_Amount
                                    target["Max Health"] -= Power_Amount
                                if stat == "Health":
                                    Player_copy["Health"] += Power_Amount
                                    target["Health"] -= Power_Amount
                                if stat == "Health":
                                    Player_copy["Health"] += Power_Amount
                                    target["Health"] -= Power_Amount
                                if stat == "Attack":
                                    Player_copy["Attack"] += Power_Amount
                                    target["Attack"] -= Power_Amount
                                if stat == "Defense":
                                    Player_copy["Defense"] += Power_Amount
                                    target["Defense"] -= Power_Amount
                                if stat == "Accuracy":
                                    Player_copy["Accuracy"] += Power_Amount
                                    target["Accuracy"] -= Power_Amount
                                if stat == "Speed":
                                    Player_copy["Speed"] += Power_Amount
                                    target["Speed"] -= Power_Amount
                                if stat == "Evasion":
                                    Player_copy["Evasion"] += Power_Amount
                                    target["Evasion"] -= Power_Amount
                                if stat == "Mana":
                                    Player_copy["Mana"] += Power_Amount
                                    target["Mana"] -= Power_Amount
                                if stat == "Stamina":
                                    Player_copy["Stamina"] += Power_Amount
                                    target["Stamina"] -= Power_Amount
                                if stat == "Magic Damage":
                                    Player_copy["Magic Damage"] += Power_Amount
                                    target["Magic Damage"] -= Power_Amount
                                if stat == "Magic Density":
                                    Player_copy["Magic Density"] += Power_Amount
                                    target["Magic Density"] -= Power_Amount
                                if stat == "Critical Chance":
                                    Player_copy["Critical Chance"] += Power_Amount
                                    target["Critical Chance"] -= Power_Amount
                                if stat == "Critical Damage":
                                    Player_copy["Critical Damage"] += Power_Amount
                                    target["Critical Damage"] -= Power_Amount
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            stat = random.choice(["Max Health","Health","Attack","Defense","Accuracy","Speed","Evasion","Mana","Stamina","Magic Damage","Magic Density","Critical Chance","Critical Damage"])
                                            if stat == "Max Health":
                                                Player_copy["Max Health"] += Power_Amount
                                                target["Max Health"] -= Power_Amount
                                            if stat == "Health":
                                                Player_copy["Health"] += Power_Amount
                                                target["Health"] -= Power_Amount
                                            if stat == "Health":
                                                Player_copy["Health"] += Power_Amount
                                                target["Health"] -= Power_Amount
                                            if stat == "Attack":
                                                Player_copy["Attack"] += Power_Amount
                                                target["Attack"] -= Power_Amount
                                            if stat == "Defense":
                                                Player_copy["Defense"] += Power_Amount
                                                target["Defense"] -= Power_Amount
                                            if stat == "Accuracy":
                                                Player_copy["Accuracy"] += Power_Amount
                                                target["Accuracy"] -= Power_Amount
                                            if stat == "Speed":
                                                Player_copy["Speed"] += Power_Amount
                                                target["Speed"] -= Power_Amount
                                            if stat == "Evasion":
                                                Player_copy["Evasion"] += Power_Amount
                                                target["Evasion"] -= Power_Amount
                                            if stat == "Mana":
                                                Player_copy["Mana"] += Power_Amount
                                                target["Mana"] -= Power_Amount
                                            if stat == "Stamina":
                                                Player_copy["Stamina"] += Power_Amount
                                                target["Stamina"] -= Power_Amount
                                            if stat == "Magic Damage":
                                                Player_copy["Magic Damage"] += Power_Amount
                                                target["Magic Damage"] -= Power_Amount
                                            if stat == "Magic Density":
                                                Player_copy["Magic Density"] += Power_Amount
                                                target["Magic Density"] -= Power_Amount
                                            if stat == "Critical Chance":
                                                Player_copy["Critical Chance"] += Power_Amount
                                                target["Critical Chance"] -= Power_Amount
                                            if stat == "Critical Damage":
                                                Player_copy["Critical Damage"] += Power_Amount
                                                target["Critical Damage"] -= Power_Amount
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They evaded the attack!")
                        else:
                            print("Not enough Mana...")
                            
                        Turn_Time -= Spell_list["Devour Essence"]["Time"]
                    else:
                        print("Not enough Time...")
                        
                    
                    return Player_copy,target,Turn_Time,Breaker
                
                def Corrupting_Touch(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Corrupting Touch"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Corrupting Touch"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Corrupting Touch"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Corrupting Touch"]["Damage"] / Spell_list["Corrupting Touch"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Corrupting Touch"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Corrupting Touch"
                                Breaker = True

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)

                                if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:

                                    poison_chance = random.randint(1,5)
                                    if poison_chance == 1:
                                        if target["Status Effects"]["Status 1"]["Type"] == "None":
                                            target["Status Effects"]["Status 1"]["Type"] = "Poison"
                                            target["Status Effects"]["Status 1"]["Duration"] = 2
                                            print("They have been Corrupted")
                                        elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                            target["Status Effects"]["Status 2"]["Type"] = "Poison"
                                            target["Status Effects"]["Status 2"]["Duration"] = 2
                                            print("They have been Corrupted")
                                        elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                            target["Status Effects"]["Status 3"]["Type"] = "Poison"
                                            taregt["Status Effects"]["Status 3"]["Duration"] = 2
                                            print("They have been Corrupted")
                                    
                                Damage = Damage / 5
                                Damage = round(Damage)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:

                                                poison_chance = random.randint(1,5)
                                                if poison_chance == 1:
                                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                                        target["Status Effects"]["Status 1"]["Type"] = "Poison"
                                                        target["Status Effects"]["Status 1"]["Duration"] = 2
                                                        print("They have been Corrupted")
                                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                                        target["Status Effects"]["Status 2"]["Type"] = "Poison"
                                                        target["Status Effects"]["Status 2"]["Duration"] = 2
                                                        print("They have been Corrupted")
                                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                                        target["Status Effects"]["Status 3"]["Type"] = "Poison"
                                                        taregt["Status Effects"]["Status 3"]["Duration"] = 2
                                                        print("They have been Corrupted")
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Corrupting Touch"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip

                def Toxin_Spray(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Toxin Spray"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Toxin Spray"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Toxin Spray"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Toxin Spray"]["Damage"] / Spell_list["Toxin Spray"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Toxin Spray"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Toxin Spray"
                                Breaker = True

                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)

                                if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:

                                    poison_chance = random.randint(1,2)
                                    if poison_chance == 1:
                                        if target["Status Effects"]["Status 1"]["Type"] == "None":
                                            target["Status Effects"]["Status 1"]["Type"] = "Poison"
                                            target["Status Effects"]["Status 1"]["Duration"] = 2
                                            print("They have been Poisoned")
                                        elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                            target["Status Effects"]["Status 2"]["Type"] = "Poison"
                                            target["Status Effects"]["Status 2"]["Duration"] = 2
                                            print("They have been Poisoned")
                                        elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                            target["Status Effects"]["Status 3"]["Type"] = "Poison"
                                            taregt["Status Effects"]["Status 3"]["Duration"] = 2
                                            print("They have been Poisoned")
                                    
                                Damage = round(Damage)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            if (target["Max Health"] * random.uniform(0.05,0.15)) <= Damage:

                                                poison_chance = random.randint(1,2)
                                                if poison_chance == 1:
                                                    if target["Status Effects"]["Status 1"]["Type"] == "None":
                                                        target["Status Effects"]["Status 1"]["Type"] = "Poison"
                                                        target["Status Effects"]["Status 1"]["Duration"] = 2
                                                        print("They have been Poisoned")
                                                    elif target["Status Effects"]["Status 2"]["Type"] == "None":
                                                        target["Status Effects"]["Status 2"]["Type"] = "Poison"
                                                        target["Status Effects"]["Status 2"]["Duration"] = 2
                                                        print("They have been Poisoned")
                                                    elif target["Status Effects"]["Status 3"]["Type"] == "None":
                                                        target["Status Effects"]["Status 3"]["Type"] = "Poison"
                                                        taregt["Status Effects"]["Status 3"]["Duration"] = 2
                                                        print("They have been Poisoned")
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Toxin Spray"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip
                
                    
            class Light:
                def Purify(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Purify"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Purify"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Purify"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Purify"]["Damage"] / Spell_list["Purify"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Purify"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                if target["Category"] == "Demon" or target["Category"] == "Undead":
                                    Damage *= 2
                                choice = "Purify"
                                Breaker = True
                                Damage = round(Damage)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"{name} does {Damage} damage")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            target["Health"] -= Damage
                                            print(f"{name} does {Damage} damage")
                                            Worked = True
                                        else:
                                            chance = False
                                
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Purify"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 
        class Mind:
            def Dominate(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Dominate"]["Time"]:
                        choice = "Dominate"
                        Breaker = True
                        if Spell_list["Dominate"]["Cost"] < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Spell_list["Dominate"]["Cost"]
                            if Player_copy["Level"] > target["Level"]:
                                print(f"\n\n{choice} is used\n")
                                print("Choose the enemy to attack:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")",dead_enemy1,"\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")",dead_enemy2,"\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],dead_enemy3,")","")
                                enemy_choice = input("")
                                enemy_choice = enemy_choice.lower()
                                if enemy_choice in ["1","enemy1","enemy 1"]:
                                        target2 = Enemy1
                                elif enemy_choice in ["2","enemy2","enemy 2"]:
                                        target2 = Enemy2
                                elif enemy_choice in ["3","enemy3","enemy 3"]:
                                        target2 = Enemy3
                                if target["Spell Caster"] == True:
                                    target2["Health"] -= target["Magic Damage"]
                                    print(target["Type"],"uses mana blast on",target2["Type"])
                                elif target["Spell Caster"] == False:
                                    target2["Health"] -= target["Damage"]
                                    print(target["Type"],"strikes",target2["Type"])
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            if target["Spell Caster"] == True:
                                                target2["Health"] -= target["Magic Damage"]
                                                print(target["Type"],"uses mana blast on",target2["Type"])
                                            elif target["Spell Caster"] == False:
                                                target2["Health"] -= target["Damage"]
                                                print(target["Type"],"strikes",target2["Type"])
                                            Worked = True
                                        else:
                                            chance = False
                            else:
                                print("\nThey resisted!\n")
                        else:
                            print("\nIt failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Dominate"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,target2 
        class Nature:
                def Grappling_Vines(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Grappling Vines"]["Time"]:

                        choice = "Grappling Vines"
                        Breaker = True
                        if Spell_list["Grappling Vines"]["Cost"] < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Spell_list["Grappling Vines"]["Cost"]
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                chance = random.random()
                                print(f"\n\n{choice} is used\n")
                                if target == Enemy1 and chance > 0.3:
                                    Enemy1_Skip = True
                                    print(Enemy1["Type"],"is immobile!\n\n")
                                elif target == Enemy2 and chance > 0.3:
                                    Enemy2_Skip = True
                                    print(Enemy2["Type"],"is immobile!\n\n")
                                elif target == Enemy3 and chance > 0.3:
                                    print(Enemy3["Type"],"is immobile!\n\n")
                                    Enemy3_Skip = True
                                else:
                                    print("\nIt Failed... \n\n")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            print(" Arcane Echo activated\n")
                                            print(f"\n\n{choice} is used\n")
                                            if target == Enemy1 and chance > 0.3:
                                                Enemy1_Skip = True
                                                print(Enemy1["Type"],"is immobile!\n\n")
                                            elif target == Enemy2 and chance > 0.3:
                                                Enemy2_Skip = True
                                                print(Enemy2["Type"],"is immobile!\n\n")
                                            elif target == Enemy3 and chance > 0.3:
                                                print(Enemy3["Type"],"is immobile!\n\n")
                                                Enemy3_Skip = True
                                            else:
                                                print("\nIt Failed... \n\n")
                                            Worked = True
                                        else:
                                            chance = False

                                
                            else:
                                print("\nThey avoided the attack!\n")
                        else:
                            print("\nIt failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Grappling Vines"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip 
        class Arcane:
            def Mana_Blast(Player_copy,Enemy,Spell_list,Skill_Tree,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    Breaker = False
                    target = kwargs.get("target", None)
                    Enemy1_Weakpoint = kwargs.get("Enemy1_Weakpoint", None)
                    Enemy2_Weakpoint = kwargs.get("Enemy2_Weakpoint", None)
                    Enemy3_Weakpoint = kwargs.get("Enemy3_Weakpoint", None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    name = kwargs.get("name",None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1_Skip = kwargs.get("Enemy1_Skip",False)
                    Enemy2_Skip = kwargs.get("Enemy2_Skip",False)
                    Enemy3_Skip = kwargs.get("Enemy3_Skip",False)
                    if Turn_Time >= Spell_list["Mana Blast"]["Time"]:
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( Spell_list["Mana Blast"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( Spell_list["Mana Blast"]["Damage"]    * Player_copy["Magic Damage"]    / (target["Defense"])    * (1 + Player_copy["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (Spell_list["Mana Blast"]["Damage"] / Spell_list["Mana Blast"]["Cost"])
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                        choice = "Mana Blast"
                        Breaker = True
                        if Mana_Amount < Player_copy["Mana"]:
                            Player_copy["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(target["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                                Damage *= (1+ Mana_Amount / 100)
                                if (POI == Enemy1_Weakpoint) and target == Enemy1:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy2_Weakpoint) and target == Enemy2:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                if (POI == Enemy3_Weakpoint) and target == Enemy3:
                                    print("You hit a weakpoint!\n")
                                    Damage = round(Damage* 1.5)
                                target["Health"] -= Damage
                                print(f"{choice} is used\n")
                                print(f"{name} does {Damage} damage\n")
                                if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                                    chance = True
                                    Worked = False
                                    while chance == True:
                                        if Worked == False:
                                            print("...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(2)
                                        A = random.random()
                                        if A <= 0.1:
                                            chance = True
                                            target["Health"] -= Damage
                                            Worked = True
                                            print(" Arcane Echo activated\n")
                                            print(f"{choice} is used\n")
                                            print(f"{name} does {Damage} damage\n")
                                        else:
                                            chance = False
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= Spell_list["Mana Blast"]["Time"]
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip


            def Empower(Player_copy,Spell_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = True
                Turn_Time = kwargs.get("Turn_Time",None)
                if Turn_Time >= Spell_list["Empower"]["Time"]:
                    while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Power_Amount = Mana_Amount * (Spell_list["Empower"]["Power"] / Spell_list["Empower"]["Cost"])
                                    Power_Amount = round(Power_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                    if Mana_Amount < Player_copy["Mana"]:
                        Player_copy["Buff"]["Value"] = Power_Amount
                        Player_copy["Buff"]["Type"] = "Attack"
                        Player_copy["Buff"]["Duration"] = 3
                        Player_copy["Attack"] += Player_copy["Buff"]["Value"]
                        Player_copy["Mana"] -= Mana_Amount
                        print("\n Empower is used\n")
                        print(f" {Power_Amount} Attack is gained for 3 turns\n")
                        if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                            chance = True
                            Worked = False
                            while chance == True:
                                if Worked == False:
                                    print("...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(2)
                                A = random.random()
                                if A <= 0.1:
                                    chance = True
                                    Player_copy["Buff"]["Value"] += Power_Amount
                                    Player_copy["Attack"] += Power_Amount
                                    Power_Amount *= 2
                                    Worked = True
                                    print(" Arcane Echo activated\n")
                                    print(f" {Power_Amount} Attack is gained for 3 turns\n")
                                else:
                                    chance = False
                                    
                                    
                    else:
                        print("Not Enough Mana")
                    Breaker = True
                    Turn_Time -= Spell_list["Empower"]["Time"]
                else:
                    print("\nNot enough Time\n")
                

                return Player_copy,Turn_Time,Breaker


                
        class Support:
            def Heal(Player_copy,Enemy,Spell_list,typewriters,Statistics,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = True
                Turn_Time = kwargs.get("Turn_Time",None)
                if Turn_Time >= Spell_list["Heal"]["Time"]:
                    while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Power_Amount = Mana_Amount * (Spell_list["Heal"]["Power"] / Spell_list["Heal"]["Cost"])
                                    Power_Amount = round(Power_Amount)
                                    Mana_Amount = Mana_Amount * (1- Player_copy["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except:
                                print("Not a number")
                    if Mana_Amount < Player_copy["Mana"]:
                        Power_Amount = round(Power_Amount)
                        Player_copy["Health"] += Power_Amount
                        if Player_copy["Max Health"] < Player_copy["Health"]:
                            Player_copy["Health"] = Player_copy["Max Health"]
                        Statistics["Health Healed"] += Power_Amount
                        Player_copy["Mana"] -= Mana_Amount
                        print(f"{Power_Amount} Health has been healed")
                        if Skill_Tree["General"]["Arcane Echo"]["Status"] == "(Unlocked)":
                            chance = True
                            Worked = False
                            while chance == True:
                                if Worked == False:
                                    print("...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(2)
                                A = random.random()
                                if A <= 0.1:
                                    chance = True
                                    Player_copy["Health"] += Power_Amount
                                    if Player_copy["Max Health"] < Player_copy["Health"]:
                                        Player_copy["Health"] = Player_copy["Max Health"]
                                    Statistics["Health Healed"] += Power_Amount
                                    Worked = True
                                    print(" Arcane Echo activated\n")
                                    print(f" {Power_Amount} Health has been healed\n")
                                else:
                                    chance = False
                    else:
                        print("Not Enough Mana")
                    Breaker = True
                    Turn_Time -= Spell_list["Heal"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,Breaker,Turn_Time,Statistics
        class Detection:
            def Analyse(Player_copy,Enemy,Spell_list,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Breaker = True
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                if Turn_Time >= Spell_list["Analyse"]["Time"]:
                    while True:
                        try:
                            print("How much mana do you want to use?")
                            Mana_Amount = int(input(""))
                            break
                        except:
                            print("Not a number")
                    if Mana_Amount < Player_copy["Mana"]:
                        Power =  Player_copy["Magic Density"] *  (Mana_Amount /100)
                        Power = round(Power)
                        if Power >= target["Level"]:
                            for key,value in target.items():
                                print(key,":",value,"\n")
                            back = input("---------------\n\nPress enter to return\n\n")
                        else:
                            print("It Failed...")
                    else:
                        print("Not enough Mana")
                    Breaker = True
                    Turn_Time -= Spell_list["Analyse"]["Time"]
                else:
                    print("\nNot enough Time\n")
                return Player_copy,Breaker,Turn_Time
            




    class Methods:
        def Blood_Offering(Player_copy,typewriters):
            global typewriter
            typewriter = typewriters
            health_lost =  random.choice([0.05,0.1,0.15,0.2])

            if health_lost == 0.05:
                Player_copy["Health"] -= (Player_copy["Max Health"] * health_lost)
                Player_copy["Buff"]["Value"] = ( (Player_copy["Damage"] * 0.1) + (Player_copy["Magic Damage"] * 0.1))  // 2
                Player_copy["Buff"]["Type"] = "Attack And Magic Attack"
                Player_copy["Buff"]["Duration"] = 3
                print("You offer thier blood to the Gods \n\n gain 10% more attack and magic attack\n\nLose 5% of max health")
            if health_lost == 0.1:
                Player_copy["Health"] -= (Player_copy["Max Health"] * health_lost)
                Player_copy["Buff"]["Value"] = ( (Player_copy["Damage"] * 0.25) + (Player_copy["Magic Damage"] * 0.25))  // 2
                Player_copy["Buff"]["Type"] = "Attack And Magic Attack"
                Player_copy["Buff"]["Duration"] = 3
                print("You offer thier blood to the Gods \n\n gain 25% more attack and magic attack\n\nLose 10% of max health")
            if health_lost == 0.15:
                Player_copy["Health"] -= (Player_copy["Max Health"] * health_lost)
                Player_copy["Buff"]["Value"] = ( (Player_copy["Damage"] * 0.4) + (Player_copy["Magic Damage"] * 0.4))  // 2
                Player_copy["Buff"]["Type"] = "Attack And Magic Attack"
                Player_copy["Buff"]["Duration"] = 3
                print("You offer thier blood to the Gods \n\n gain 40% more attack and magic attack\n\nLose 15% of max health")
            if health_lost == 0.2:
                Player_copy["Health"] -= (Player_copy["Max Health"] * health_lost)
                Player_copy["Buff"]["Value"] = ( (Player_copy["Damage"] * 0.6) + (Player_copy["Magic Damage"] * 0.6))  // 2
                Player_copy["Buff"]["Type"] = "Attack And Magic Attack"
                Player_copy["Buff"]["Duration"] = 3
                print("You offer thier blood to the Gods \n\n gain 60% more attack and magic attack\n\nLose 20% of max health")
            Breaker = True
            return Player_copy,Breaker
        def Blood_Frenzy(Player_copy,typewriters):
            global typewriter
            typewriter = typewriters
            Player_copy["Attack"] += (Player_copy["Attack"] * 0.5)
            Player_copy["Accuracy"] -= (Player_copy["Accuracy"] * 0.5)
            print("\n\nYou start breathing heavily eminating a dangerous presence\n")
            print("\nTheir physical attack increases by 50%\n")
            print("\nTheir accuracy decreases by 50%\n")
            Breaker = True
            return Player_copy,Breaker
