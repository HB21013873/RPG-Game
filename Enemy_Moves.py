import random
import time
import sys
from Text_Writing_Style import TypeWriter as TW
import builtins
tw = TW(delay=0.02, jitter=True)
typewriter = True
def print(*args, sep=" ", end="\n"):
    if typewriter:
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
    else:
        builtins.print(*args, sep=sep, end=end)
class Enemy_Move:
    class Melee_Moves:
        class Head:
            def Headbutt(Player_Skip,Player_copy,typewriters,**kwargs ):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                if Turn_Time >= 1:
                    if 50 < target["Stamina"]:
                        Percentage = random.random()
                        Enemy_Critical_Chance = target["Critical Chance"] / 100
                        if Percentage <= Enemy_Critical_Chance:
                            Damage = int(( 25 * target["Attack"]/  Player_copy["Defense"]) )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                            Damage = int( 25 * target["Attack"]/ ( Player_copy["Defense"]))
                        Combat_cost = 50 * ( 1 - target["Magic Density"] /  500 )
                        target["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Headbutt"
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            if (Player_copy["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                chance = random.randint(1,5)
                                if chance == 1:
                                    Player_Skip = True
                                    print("You are stunned!\n")

                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(target["Type"],f"does {Damage} damage")
                        else:
                            print("They avoided the attack!")

                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= 1
                else:
                    print("Not enough time")
                return Player_copy,target,Turn_Time,Player_Skip
            
            def Bite(Player_copy,typewriters,**kwargs ):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)

                if Turn_Time >= 0.5:
                    if 10 < Player_copy["Stamina"]:
                        Percentage = random.random()
                        Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int(( 50 * Player_copy["Attack"]/  Player_copy["Defense"]) )
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                            print("\n\nCritical Hit!\n")
                        else:
                                Damage = int(( 50 * Player_copy["Attack"]/  Player_copy["Defense"]) )
                        Combat_cost = 10 * ( 1 - Player_copy["Magic Density"] /  500 )
                        Player_copy["Stamina"] -= Combat_cost
                        Evasion_Chance = random.randint(1,100)
                        choice = "Bite"
                        Breaker = True
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (Player_copy["Accuracy"]/100))))):
                            if (Player_copy["Max Health"] * 0.05) <= Damage:
                                bleed_chance = random.random()
                                
                                if bleed_chance < 0.15 and (Damage >= (Player_copy["Max Health"] * 0.05) and Damage <= (Player_copy["Max Health"] * 0.1) ):
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                        print("You are bleeding")
                                if bleed_chance < 0.35 and (Damage >= (Player_copy["Max Health"] * 0.1) and Damage <= (Player_copy["Max Health"] * 0.15) ):
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                        print("You are bleeding")
                                if bleed_chance < 0.6 and (Damage >= (Player_copy["Max Health"] * 0.15) and Damage <= (Player_copy["Max Health"] * 0.2) ):
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                        print("You are bleeding")
                                if bleed_chance < 0.85 and (Damage >= (Player_copy["Max Health"] * 0.2) and Damage <= (Player_copy["Max Health"] * 0.3) ):
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                        print("You are bleeding")
                                if bleed_chance <= 1 and Damage >= (Player_copy["Max Health"] * 0.3):
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                        print("You are bleeding")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                        print("You are bleeding")

                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"They do {Damage} damage")
                        else:
                            print("They avoided the attack!")

                    else:
                        print("Not enough Stamina\n")
                    Turn_Time -= 0.5
                else:
                    print("Not enough time")
                return Player_copy,target,Turn_Time

        class Legs:

            def Front_Kick(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (15 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (15 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Front Kick"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        target["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.5
                return Player_copy,target,Turn_Time
            
            def Axe_Kick(Player_Skip,Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                
                if 50 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (25 * target["Attack"])/  Player_copy["Defense"])
                        Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                        Damage = int( (25 * target["Attack"]) /  Player_copy["Defense"])
                    Combat_cost = 50 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Axe Kick"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        if (Player_copy["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                            chance = random.randint(1,5)
                            if chance == 1:
                                Player_Skip = True
                                print("You are stunned!\n")

                        print(f"{choice} is used")
                        print(target["Type"],f" does {Damage} damage")
                        Player_copy["Health"] -= Damage
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 1
                return Player_copy,target,Turn_Time,Player_Skip


            def Spinning_Back_Kick(Player_Skip,Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 50 < Player_copy["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]) )
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (25 * Player_copy["Attack"]/  target["Defense"]) )
                    Combat_cost = 50 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Spinning Back Kick"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        if (Player_copy["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                            chance = random.randint(1,5)
                            if chance == 1:
                                Enemy1_Skip = True
                                print("The Enemy is stunned!\n")

                        print(f"{choice} is used")
                        print(target["Type"],f"does {Damage} damage")
                        Player_copy["Health"] -= Damage
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 1
                return Player_copy,target,Turn_Time,Player_Skip
            def Groundbreaker(Player_copy,Enemy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target", None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    if Turn_Time >= 1:
                        Target_Critical_Chance = target["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Target_Critical_Chance:
                            Damage = int( 25   * target["Attack"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                            Damage *= (1 + (target["Critical Damage"]/100))
                        else:
                            Damage = int( 25    * target["Attack"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))

                        choice = "Tremor"
                        if 50 < target["Stamina"]:
                            target["Stamina"] -= 50
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Tremor"
                                if (Player_copy["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Player_Skip = True 
                                        print("You are inflicted with stagger!\n")
                                        Player_copy["Speed"] -= (Player_copy["Speed"] * random.randint(0.1,0.2))
                                        Player_copy["Evasion"] -= (Player_copy["Evasion"] * random.randint(0.1,0.2))
                            

                                Player_copy["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"They do {Damage} damage")
                                
                            else:
                                print("You avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= 1
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Turn_Time,Player_Skip

        class Arms:
            def Aimed_Shot(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                        Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Aimed Shot"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/20))))):
                        target["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.5
                return Player_copy,target,Turn_Time
            
            def Straight_Punch(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (10 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (10 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Straight Punch"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        target["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.5
                return Player_copy,target,Turn_Time

            def Tackle(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (15 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (15 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Tackle"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        target["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.5
                return Player_copy,target,Turn_Time

            def Slash(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 50
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/75))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Slash"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        if (Player_copy["Max Health"] * 0.05) <= Damage:
                            bleed_chance = random.random()
                            
                            if bleed_chance < 0.15 and (Damage >= (Player_copy["Max Health"] * 0.05) and Damage <= (Player_copy["Max Health"] * 0.1) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance < 0.35 and (Damage >= (Player_copy["Max Health"] * 0.1) and Damage <= (Player_copy["Max Health"] * 0.15) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance < 0.6 and (Damage >= (Player_copy["Max Health"] * 0.15) and Damage <= (Player_copy["Max Health"] * 0.2) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance < 0.85 and (Damage >= (Player_copy["Max Health"] * 0.2) and Damage <= (Player_copy["Max Health"] * 0.3) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance <= 1 and Damage >= (Player_copy["Max Health"] * 0.3):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                        target["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.5
                return Player_copy,target,Turn_Time


            def Quick_Stab(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 50
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/75))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (25 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Quick Stab"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        if (Player_copy["Max Health"] * 0.05) <= Damage:
                            bleed_chance = random.random()
                            
                            if bleed_chance < 0.15 and (Damage >= (Player_copy["Max Health"] * 0.05) and Damage <= (Player_copy["Max Health"] * 0.1) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance < 0.35 and (Damage >= (Player_copy["Max Health"] * 0.1) and Damage <= (Player_copy["Max Health"] * 0.15) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance < 0.6 and (Damage >= (Player_copy["Max Health"] * 0.15) and Damage <= (Player_copy["Max Health"] * 0.2) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance < 0.85 and (Damage >= (Player_copy["Max Health"] * 0.2) and Damage <= (Player_copy["Max Health"] * 0.3) ):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                            if bleed_chance <= 1 and Damage >= (Player_copy["Max Health"] * 0.3):
                                if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 1"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 2"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                    print("You are bleeding")
                                elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                    Player_copy["Status Effects"]["Status 3"]["Type"] = "Bleed"
                                    Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                    print("You are bleeding")
                        Player_copy["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.5
                return Player_copy,target,Turn_Time

            def Impulsive_Swing(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 100 < Player_copy["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (75 * target["Attack"]/  Player_copy["Defense"]) )
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (75 * Player_copy["Attack"]/  target["Defense"]) )
                    Combat_cost = 100 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Impulsive Swing"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * 3))):
                        if (Player_copy["Max Health"] * random.uniform(0.1,0.25)) <= Damage:
                            chance = random.randint(1,5)
                            if chance == 1:
                                Enemy1_Skip = True
                                print("The Enemy is stunned!\n")

                        print(f"{choice} is used")
                        print(target["Type"],f"does {Damage} damage")
                        Player_copy["Health"] -= Damage
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 1
                return Player_copy,target,Turn_Time,Player_Skip
            def Jab(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                Enemy1 = kwargs.get("Enemy1",None)
                Enemy2 = kwargs.get("Enemy2",None)
                Enemy3 = kwargs.get("Enemy3",None)
                
                if 25 < target["Stamina"]:
                    Percentage = random.random()
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( (10 * target["Attack"]/  Player_copy["Defense"]))
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                            Damage = int( (10 * target["Attack"]/  Player_copy["Defense"]))
                    Combat_cost = 25 * ( 1 - target["Magic Density"] /  500 )
                    target["Stamina"] -= Combat_cost
                    Evasion_Chance = random.randint(1,100)
                    choice = "Straight Punch"
                    if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                        Player_copy["Health"] -= Damage
                        print(f"{choice} is used")
                        print(target["Type"], f" does {Damage} damage")
                    else:
                        print("They avoided the attack!")
                else:
                    print("Not enough Stamina\n")
                Turn_Time -= 0.1
                return Player_copy,target,Turn_Time
 
    class Spell_Moves:
        class Elemental:

            class Fire:
                def Fireball(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)

                
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( 25    *  target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25    * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Fireball"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Fireball"
                            if (Player_copy["Max Health"] * random.uniform(0.05,0.15)) <= Damage:
                                burn_chance = random.randint(1,5)
                                if burn_chance == 1:
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Burn"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 3
                                        print("They have been burnt")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Burn"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 3
                                        print("They have been burnt")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Burn"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 3
                                        print("They have been burnt")

                            Damage = round(Damage)

                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(target["Type"],f"does {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Breaker,Turn_Time
            class Ice:
                def Ice_Shard(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                
                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( 25 * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25 * Player_copy["Magic Damage"]/ (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Ice Shard"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Ice Shard"
                            if (Player_copy["Max Health"] * random.uniform(0.05,0.15)) <= Damage:
                                freeze_chance = random.randint(1,5)
                                if freeze_chance == 1:
                                    if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 1"]["Type"] = "Freeze"
                                        Player_copy["Status Effects"]["Status 1"]["Duration"] = 2
                                        print("They have been Frozen")
                                    elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 2"]["Type"] = "Freeze"
                                        Player_copy["Status Effects"]["Status 2"]["Duration"] = 2
                                        print("They have been Frozen")
                                    elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                        Player_copy["Status Effects"]["Status 3"]["Type"] = "Freeze"
                                        Player_copy["Status Effects"]["Status 3"]["Duration"] = 2
                                        print("They have been Frozen")
                            Damage = round(Damage)
                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(f"They do {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time
            class Lightning:
                def Shock(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    

                    Enemy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Enemy_Critical_Chance:
                        Damage = int( 25 * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25 * Player_copy["Magic Damage"]/ (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Shock"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Shock"
                            Damage = round(Damage)
                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(target["Type"],f"does {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time
            class Water:
                def River_Fist(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    Player_copy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Player_copy_Critical_Chance:
                        Damage = int( 25   * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage += int( ((25 * target["Attack"]/  Player_copy["Defense"])/2))
                        Damage *= (1 + (target["Critical Damage"]/100))
                        print("\n\nCritical Hit!\n")
                    else:
                        Damage = int( 25    * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage += int( ((25 * target["Attack"]/  Player_copy["Defense"])/2))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "River Fist"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "River Fist"

                            Damage = round(Damage)
                            Player_copy["Health"] -= Damage
                            print(f"\n{choice} is used\n")
                            print(target["Type"],f" does {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time
            class Earth:
                def Mud_Shot(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    Player_copy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Player_copy_Critical_Chance:
                        Damage = int( 25    * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25   * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Mud Shot"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Mud Shot"
                            mud_chance = random.randint(1,5)
                            if mud_chance == 1:
                                Player_copy["Accuracy"] -= (Player_copy["Accuracy"] * 0.1)
                                print(Player_copy["Type"]," Accuracy has decreased by 10%")
                            Damage = round(Damage)
                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(target["Type"],f" does {Damage} damage")
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time
                
                def Tremor(Player_copy,Enemy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target", None)
                    POI = kwargs.get("POI",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    if Turn_Time >= 1:
                        Target_Critical_Chance = target["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Target_Critical_Chance:
                            Damage = int( 25   * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                            Damage *= (1 + (target["Critical Damage"]/100))
                        else:
                            Damage = int( 25    * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                    Mana_Amount = int(input(""))
                                    Damage_Amount = Mana_Amount * (25 / 50)
                                    Damage_Amount = round(Damage_Amount)
                                    Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except Exception as e:
                                print("Error:", e)
                        choice = "Tremor"
                        if Mana_Amount < target["Mana"]:
                            target["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Tremor"
                                if (Player_copy["Max Health"] * random.uniforn(0.1,0.25)) <= Damage:
                                    chance = random.randint(1,5)
                                    if chance == 1:
                                        Player_Skip = True 
                                        print("You are inflicted with stagger!\n")
                                        Player_copy["Speed"] -= (Player_copy["Speed"] * random.randint(0.1,0.2))
                                        Player_copy["Evasion"] -= (Player_copy["Evasion"] * random.randint(0.1,0.2))
                            

                                Player_copy["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"They do {Damage} damage")
                                
                            else:
                                print("You avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= 1
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Turn_Time,Player_Skip
            class Wind:
                def Stone_Slipstream(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    Player_copy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Player_copy_Critical_Chance:
                        Damage = int( 25  * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25  * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Stone Slipstream"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Stone Slipstream"

                            Damage = round(Damage)
                            Damage /= 4
                            Damage = round(Damage)
                            num_Moves = random.randint(1,6)
                            for x in range(num_Moves):
                                Player_copy["Health"] -= Damage
                                chance = random.randint(1,8)
                                if chance == 1 or chance == 2:
                                    target["Defense"] -= 1
                                    print("\nDefense decreased by 1")
                                elif chance == 3 or chance == 4:
                                    target["Defense"] -= 5
                                    print("\nDefense decreased by 4")
                            Damage *= num_Moves
                            Damage = round(Damage)
                            print(f"\n{choice} is used\n")
                            print(f"\nYou hit {num_Moves} times")
                            print(target["Type"], f" does {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time
            class Dark:
                def Life_Drain(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    Player_copy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Player_copy_Critical_Chance:
                        Damage = int( 25   * Player_copy["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25    * Player_copy["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Life Drain"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Life Drain"

                            Damage = round(Damage)
                            Damage = Damage * 0.8
                            Damage = round(Damage)
                            Player_copy["Health"] -= Damage
                            Health_Gained = round(Damage/2)
                            target["Health"] += Health_Gained
                            target["Health"] = round(target["Health"])
                            print(f"{choice} is used")
                            print(target["Type"],f" does {Damage} damage")
                            print(target["Type"],"Health is now",target["Health"])
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time

                def Devour_Essence(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    

                    if Turn_Time >= 0.25:
                        while True:
                            print("How much mana do you want to use?")
                            try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Power_Amount = Mana_Amount * (25 / 50)
                                Power_Amount = round(Power_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                            except Exception as e:
                                print("Error:", e)
                        if Mana_Amount < target["Mana"]:
                            target["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                                choice = "Devour Essence"
                                stat = random.choice(["Max Health","Health","Attack","Defense","Accuracy","Speed","Evasion","Mana","Stamina","Magic Damage","Magic Density","Critical Chance","Critical Damage"])
                                if stat == "Max Health":
                                    target["Max Health"] += Power_Amount
                                    Player_copy["Max Health"] -= Power_Amount
                                if stat == "Health":
                                    target["Health"] += Power_Amount
                                    Player_copy["Health"] -= Power_Amount
                                if stat == "Attack":
                                    target["Attack"] += Power_Amount
                                    Player_copy["Attack"] -= Power_Amount
                                if stat == "Defense":
                                    target["Defense"] += Power_Amount
                                    Player_copy["Defense"] -= Power_Amount
                                if stat == "Accuracy":
                                    target["Accuracy"] += Power_Amount
                                    Player_copy["Accuracy"] -= Power_Amount
                                if stat == "Speed":
                                    target["Speed"] += Power_Amount
                                    Player_copy["Speed"] -= Power_Amount
                                if stat == "Evasion":
                                    target["Evasion"] += Power_Amount
                                    Player_copy["Evasion"] -= Power_Amount
                                if stat == "Mana":
                                    target["Mana"] += Power_Amount
                                    Player_copy["Mana"] -= Power_Amount
                                if stat == "Stamina":
                                    target["Stamina"] += Power_Amount
                                    Player_copy["Stamina"] -= Power_Amount
                                if stat == "Magic Damage":
                                    target["Magic Damage"] += Power_Amount
                                    Player_copy["Magic Damage"] -= Power_Amount
                                if stat == "Magic Density":
                                    target["Magic Density"] += Power_Amount
                                    Player_copy["Magic Density"] -= Power_Amount
                                if stat == "Critical Chance":
                                    target["Critical Chance"] += Power_Amount
                                    Player_copy["Critical Chance"] -= Power_Amount
                                if stat == "Critical Damage":
                                    target["Critical Damage"] += Power_Amount
                                    Player_copy["Critical Damage"] -= Power_Amount
                            else:
                                print("They evaded the attack!")
                        else:
                            print("Not enough Mana...")
                            
                        Turn_Time -= 0.25
                    else:
                        print("Not enough Time...")
                        
                    
                    return Player_copy,target,Turn_Time,Breaker
                
                def Corrupting_Touch(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    if Turn_Time >= 0.5:
                        Player_copy_Critical_Chance = target["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( 25 * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( 25 * Player_copy["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                        choice = "Corrupting Touch"
                        if Mana_Amount < target["Mana"]:
                            target["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Corrupting Touch"

                                Damage = round(Damage)
                                if (Player_copy["Max Health"] * random.uniform(0.05,0.1)) <= Damage:
                                    poison_chance = random.randint(1,5)
                                    if poison_chance == 1:
                                        if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                            Player_copy["Status Effects"]["Status 1"]["Type"] = "Poison"
                                            Player_copy["Status Effects"]["Status 1"]["Duration"] = 2
                                            print("You have been Corrupted")
                                        elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                            Player_copy["Status Effects"]["Status 2"]["Type"] = "Poison"
                                            Player_copy["Status Effects"]["Status 2"]["Duration"] = 2
                                            print("You have been Corrupted")
                                        elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                            Player_copy["Status Effects"]["Status 3"]["Type"] = "Poison"
                                            Player_copy["Status Effects"]["Status 3"]["Duration"] = 2
                                            print("You have been Corrupted")

                                    
                                Damage = Damage / 5
                                Damage = round(Damage)
                                Player_copy["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"They do {Damage} damage")                                
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= 0.5
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Turn_Time

                def Toxin_Spray(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    if Turn_Time >= 0.5:
                        Player_copy_Critical_Chance = target["Critical Chance"] / 100
                        Percentage = random.random()
                        if Percentage <= Player_copy_Critical_Chance:
                            Damage = int( 10 * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                            Damage *= (1 + (Player_copy["Critical Damage"]/100))
                        else:
                            Damage = int( 10 * Player_copy["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                        choice = "Toxin Spray"
                        if Mana_Amount < target["Mana"]:
                            target["Mana"] -= Mana_Amount
                            Evasion_Chance = random.randint(1,100)
                            if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                                Damage += Damage_Amount
                                choice = "Toxin Spray"

                                Damage = round(Damage)
                                if (Player_copy["Max Health"] * random.uniform(0.05,0.1)) <= Damage:
                                    poison_chance = random.randint(1,2)
                                    if poison_chance == 1:
                                        if Player_copy["Status Effects"]["Status 1"]["Type"] == "None":
                                            Player_copy["Status Effects"]["Status 1"]["Type"] = "Poison"
                                            Player_copy["Status Effects"]["Status 1"]["Duration"] = 2
                                            print("You have been Poisoned")
                                        elif Player_copy["Status Effects"]["Status 2"]["Type"] == "None":
                                            Player_copy["Status Effects"]["Status 2"]["Type"] = "Poison"
                                            Player_copy["Status Effects"]["Status 2"]["Duration"] = 2
                                            print("You have been Poisoned")
                                        elif Player_copy["Status Effects"]["Status 3"]["Type"] == "None":
                                            Player_copy["Status Effects"]["Status 3"]["Type"] = "Poison"
                                            Player_copy["Status Effects"]["Status 3"]["Duration"] = 2
                                            print("You have been Poisoned")

                                    

                                Damage = round(Damage)
                                Player_copy["Health"] -= Damage
                                print(f"{choice} is used")
                                print(f"They do {Damage} damage")                                
                            else:
                                print("They avoided the attack!")
                        else:
                            print("It failed because there is not enough mana\n")
                        Turn_Time -= 0.5
                    else:
                        print("\nNot enough Time\n")
                    return Player_copy,target,Turn_Time
                
            class Light:
                def Purify(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    Player_copy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Player_copy_Critical_Chance:
                        Damage = int( 25    * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 25    * Player_copy["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (25 / 50)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Purify"
                    if Mana_Amount < Player_copy["Mana"]:
                        Player_copy["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            choice = "Purify"
                            Damage = round(Damage)

                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(target["Type"],f"does {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time 
        class Mind:
            def Dominate(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    choice = "Dominate"
                    if 50 < target["Mana"]:
                        target["Mana"] -= 50
                        if target["Level"] > Player_copy["Level"]:
                            print(f"\n\n{choice} is used\n")

                            if 25 <= Player_copy["Stamina"]:
                                Percentage = random.random()
                                Enemy_Critical_Chance = Player_copy["Critical Chance"] / 100
                                if Percentage <= Enemy_Critical_Chance:
                                    Damage = int( (10 * Player_copy["Attack"]/  Player_copy["Defense"]))
                                    Damage *= (1 + (Player_copy["Critical Damage"]/100))
                                    print("\n\nCritical Hit!\n")
                                else:
                                    Damage = int( (10 * Player_copy["Attack"]/  Player_copy["Defense"]))
                                Combat_cost = 25 * ( 1 - Player_copy["Magic Density"] /  500 )
                                Player_copy["Stamina"] -= Combat_cost
                                Evasion_Chance = random.randint(1,100)
                                choice = "Straight Punch"
                                Player_copy["Health"] -= Damage
                                print(f"{choice} is used")
                                print(Player_copy["Type"], f" does {Damage} damage to themself")

                            else:
                                print("Not enough Stamina\n")
                        else:
                            print("\nThey resisted!\n")
                    else:
                        print("\nIt failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time
        class Nature:
                def Grappling_Vines(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)

                    choice = "Grappling Vines"
                    if 50 < target["Mana"]:
                        target["Mana"] -= 50
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            chance = random.random()
                            print(f"\n\n{choice} is used\n")
                            if chance > 0.3:
                                Player_Skip = True
                                print("You are immobile!\n\n")
                            else:
                                print("\nIt Failed... \n\n")

                            
                        else:
                            print("\nThey avoided the attack!\n")
                    else:
                        print("\nIt failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time,Player_Skip 
        class Arcane:
            def Mana_Blast(Player_copy,typewriters,**kwargs):
                    global typewriter
                    typewriter = typewriters
                    target = kwargs.get("target",None)
                    Turn_Time = kwargs.get("Turn_Time",None)
                    Enemy1 = kwargs.get("Enemy1",None)
                    Enemy2 = kwargs.get("Enemy2",None)
                    Enemy3 = kwargs.get("Enemy3",None)
                    
                    Player_copy_Critical_Chance = target["Critical Chance"] / 100
                    Percentage = random.random()
                    if Percentage <= Player_copy_Critical_Chance:
                        Damage = int( 10    * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                        Damage *= (1 + (target["Critical Damage"]/100))
                    else:
                        Damage = int( 10   * target["Magic Damage"]    / (Player_copy["Defense"])    * (1 + target["Magic Density"] / 100))
                    while True:
                        try:   
                                Mana_Amount = random.randint(1,target["Mana"])
                                Damage_Amount = Mana_Amount * (10 / 100)
                                Damage_Amount = round(Damage_Amount)
                                Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                Mana_Amount = round(Mana_Amount)
                                if Mana_Amount > 0:
                                    break
                        except Exception as e:
                            print("Error:", e)
                    choice = "Mana Blast"
                    if Mana_Amount < target["Mana"]:
                        target["Mana"] -= Mana_Amount
                        Evasion_Chance = random.randint(1,100)
                        if Evasion_Chance > (min(50,(Player_copy["Evasion"] * (1 - (target["Accuracy"]/100))))):
                            Damage += Damage_Amount
                            Player_copy["Health"] -= Damage
                            print(f"{choice} is used")
                            print(target["Type"],f" does {Damage} damage")
                            
                        else:
                            print("They avoided the attack!")
                    else:
                        print("It failed because there is not enough mana\n")
                    Turn_Time -= 0.5
                    return Player_copy,target,Turn_Time

            def Empower(target,typewriters):
                global typewriter
                typewriter = typewriters
                while True:
                            try:   
                                    Mana_Amount = random.randint(1,target["Mana"])
                                    Power_Amount = Mana_Amount * (10 / 100)
                                    Power_Amount = round(Power_Amount)
                                    Mana_Amount = Mana_Amount * (1 + target["Magic Density"] /  500 )
                                    Mana_Amount = round(Mana_Amount)
                                    if Mana_Amount > 0:
                                        break
                            except Exception as e:
                                print("Error:", e)
                target["Buff"]["Value"] = Power_Amount
                target["Buff"]["Type"] = "Attack"
                target["Buff"]["Duration"] = 3
                target["Attack"] += target["Buff"]["Value"]

                return target
            
        class Support:
            def Heal(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                Turn_Time = kwargs.get("Turn_Time",None)
                target = kwargs.get("target",None)
                while True:
                    try:
                        print("How much mana do you want to use?")
                        Mana_Amount = random.randint(1,target["Mana"])
                        break
                    except Exception as e:
                        print("Error:",e)
                if Mana_Amount < target["Mana"]:
                    Power =  target["Magic Density"] *  (Mana_Amount /100)
                    Power = round(Power)
                    target["Health"] += Power
                    print(f"{Power} Health has been healed")
                else:
                    print("Not Enough Mana")
                Turn_Time -= 0.5
                return target,Turn_Time
            def Summon(target,typewriters):
                global typewriter
                typewriter = typewriters
                T = random.randint(1,3)

                if T == 1:
                    if target["Mana"] >= 70:
                        Ally = copy.deepcopy(Enemy["Tier 1"]["Wolf"])
                        target["Mana"] -= 55
                if T == 2:
                    if target["Mana"] >= 70:
                        Ally = copy.deepcopy(Enemy["Tier 1"]["Goblin"])
                        target["Mana"] -= 50
                if T == 3:
                    if target["Mana"] >= 70:
                        Ally = copy.deepcopy(Enemy["Tier 1"]["Skeleton"])
                        target["Mana"] -= 65
                
                return {"Returning":[target,Ally]}
        class Detection:
            def Analyse(Player_copy,typewriters,**kwargs):
                global typewriter
                typewriter = typewriters
                target = kwargs.get("target",None)
                Turn_Time = kwargs.get("Turn_Time",None)
                choice = "Analyse"
                if 50 < target["Mana"]:
                    target["Mana"] -= 50
                    if target["Level"] > Player_copy["Level"]:
                        print(f"\n\n{choice} is used\n")
                        for key,value in Player_copy.items():
                            print(key,":",value,"\n")
                        back = input("---------------\n\nPress enter to return\n\n")
                    else:
                        print("It Failed...")
                else:
                    print("Not enough Mana")
                Turn_Time -= 0.5
                return target,Turn_Time
            


    class Methods:
        
        def Blood_Offering(target,typewriters):
            global typewriter
            typewriter = typewriters
            health_lost =  random.choice([0.05,0.1,0.15,0.2])

            if health_lost == 0.05:
                target["Health"] -= (target["Max Health"] * health_lost)
                target["Buff"]["Value"] = ( (target["Damage"] * 0.1) + (target["Magic Damage"] * 0.1))  // 2
                target["Buff"]["Type"] = "Attack And Magic Attack"
                target["Buff"]["Duration"] = 3
                print("They offer thier blood to the Gods \n\n gain 10% more attack and magic attack\n\nLose 5% of max health")
            if health_lost == 0.1:
                target["Health"] -= (target["Max Health"] * health_lost)
                target["Buff"]["Value"] = ( (target["Damage"] * 0.25) + (target["Magic Damage"] * 0.25))  // 2
                target["Buff"]["Type"] = "Attack And Magic Attack"
                target["Buff"]["Duration"] = 3
                print("They offer thier blood to the Gods \n\n gain 25% more attack and magic attack\n\nLose 10% of max health")
            if health_lost == 0.15:
                target["Health"] -= (target["Max Health"] * health_lost)
                target["Buff"]["Value"] = ( (target["Damage"] * 0.4) + (target["Magic Damage"] * 0.4))  // 2
                target["Buff"]["Type"] = "Attack And Magic Attack"
                target["Buff"]["Duration"] = 3
                print("They offer thier blood to the Gods \n\n gain 40% more attack and magic attack\n\nLose 15% of max health")
            if health_lost == 0.2:
                target["Health"] -= (target["Max Health"] * health_lost)
                target["Buff"]["Value"] = ( (target["Damage"] * 0.6) + (target["Magic Damage"] * 0.6))  // 2
                target["Buff"]["Type"] = "Attack And Magic Attack"
                target["Buff"]["Duration"] = 3
                print("They offer thier blood to the Gods \n\n gain 60% more attack and magic attack\n\nLose 20% of max health")
            
            return target
        
        def Blood_Frenzy(target,typewriters):
            global typewriter
            typewriter = typewriters
            target["Attack"] += (target["Attack"] * 0.5)
            target["Accuracy"] -= (target["Accuracy"] * 0.5)
            print("\n\nThe berserker starts breathing heavily eminating a dangerous presence\n")
            print("\nTheir physical attack increases by 50%\n")
            print("\nTheir accuracy decreases by 50%\n")
            return target
