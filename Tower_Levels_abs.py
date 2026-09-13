import random
import time
from Text_Writing_Style import TypeWriter as TW
import sys
import builtins
from Level_1 import Level_1 as L1
from Level_2 import Level_2 as L2
from Enemy_Battle_abs import Enemy_Battle as E_Battle
from datetime import datetime
from Player_Moves import Player_Move as PM
from Player_Battle import Player_Battle as PB
tw = TW(delay=0.02, jitter=True)
Player_Battle = PB.Overall_Player_Battle()
typewriter = True
def print(*args, sep=" ", end="\n"):
    if typewriter:
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
    else:
        builtins.print(*args, sep=sep, end=end)
class Tower:
    def Tower(Player,Player_copy,Enemy,Tower_Level_Choice,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,Move_Set,name,Statistics,Game,Body_Condition,Skill_Tree,Chest_items,Skill_Books,Proficiency,Amount_Used,typewriters):
        global typewriter
        typewriter = typewriters
        b = random.randint(1,3)
        Battle_End = False
        battle_choice = ""
        check1 = True
        check2 = True
        check3 = True
        x = 0
        n = 0
        damage = 0
        choice = None
        player_shadows = False
        Player_Skip = False
        Enemy1_Skip = False
        Enemy2_Skip = False
        Enemy3_Skip = False
        lever = False
        Weapon_Held = False
        Metal_Weapon = False
        Evasion1_Stopper = False
        Defense1_Stopper = False
        Evasion2_Stopper = False
        Defense2_Stopper = False
        Evasion3_Stopper = False
        Defense3_Stopper = False
        Outcome = ""
        Enemy1 = None
        Enemy2 = None
        Enemy3 = None
        treasure_chance = 0.1
        Gold_Multiplier = 1
        if Player_copy["Title"] == "Spender":
            treasure_chance = 0.2
        if Player_copy["Title"] == "Big Spender":
            treasure_chance = 0.3
        if Player_copy["Title"] == "High Roller":
            treasure_chance = 0.45
        if Player_copy["Title"] == "Deep Pockets":
            treasure_chance = 0.6
        if Player_copy["Title"] == "Patron Of Treasure":
            treasure_chance = 0.75
        if Player_copy["Title"] == "Penny Pincher":
            Gold_Multiplier = 1.1
        if Player_copy["Title"] == "Hoarder":
            Gold_Multiplier = 1.2
        if Player_copy["Title"] == "Noble":
            Gold_Multiplier = 1.3
        if Player_copy["Title"] == "Tycoon":
            Gold_Multiplier = 1.4
        if Player_copy["Title"] == "Midas":
            Gold_Multiplier = 1.5
        



        def Status_Effect3(Player_copy, Enemy3,n, place,Game):

            if (Enemy3["Status Effects"]["Status 1"]["Type"] == "Burn" or  Enemy3["Status Effects"]["Status 2"]["Type"] == "Burn" or Enemy3["Status Effects"]["Status 3"]["Type"] == "Burn"  ) and Enemy3["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy3["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy3["Status Effects"]["Status 3"]["Duration"] != 0:
                    Enemy3["Health"] -= (Enemy3["Health"] *  0.05)
                    (Enemy3["Health"]) = int(Enemy3["Health"])
                    print(Enemy3["Type"], "takes burn damage")
            if (Enemy3["Status Effects"]["Status 1"]["Type"] == "Poison" or  Enemy3["Status Effects"]["Status 2"]["Type"] == "Poison" or Enemy3["Status Effects"]["Status 3"]["Type"] == "Poison"  ) and Enemy3["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy3["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy3["Status Effects"]["Status 3"]["Duration"] != 0:
                if Enemy3["Attribute"] != "Poison" and Enemy3["Buff"]["Type"] != "Poison Immunity":
                    Enemy3["Health"] -= (Enemy3["Health"] * (random.randint(0.01,0.15)))
                    Enemy3["Health"] = round(Enemy3["Health"])
            if (Enemy3["Status Effects"]["Status 1"]["Type"] == "Bleed" or  Enemy3["Status Effects"]["Status 2"]["Type"] == "Bleed" or Enemy3["Status Effects"]["Status 3"]["Type"] == "Bleed"  ) and Enemy3["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy3["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy3["Status Effects"]["Status 3"]["Duration"] != 0:
                    Enemy3["Health"] -= (Enemy3["Max Health"] * (random.randint(2,5)/ 100))
                    (Enemy3["Health"]) = int(Enemy3["Health"])
                    print(Enemy3["Type"], "takes bleed damage")
            if Game["Current Effect"]["Type"] == "Poison":
                if Enemy3["Buff"]["Type"] != "Poison Immunity":
                        Enemy3["Health"] -= 5
                        print(Enemy3["Type"], "takes poison damage")
            if Game["Current Effect"]["Type"] == "Thundering":
                if Enemy3["Buff"]["Type"] != "Electricity Immunity":
                        chance = random.random()
                        if chance > 0.8:
                            Damage = int((200 / Enemy3["Defense"]))
                            Enemy3["Health"] -= Damage
                            print(Enemy3["Type"], "was struck by lightning!")
            if n == 2 and place == "Shadow Realm Floor":
                    if Enemy3["Status Effects"]["Status 1"]["Type"] == "Shaded":
                        if Enemy3["Status Effects"]["Status 1"]["Duration"] == 0:
                            print(Enemy3["Type"], " steps out of the shadows")
                    if Enemy3["Status Effects"]["Status 2"]["Type"] == "Shaded":
                        if Enemy3["Status Effects"]["Status 2"]["Duration"] == 0:
                            print(Enemy3["Type"], " steps out of the shadows")
                    if Enemy3["Status Effects"]["Status 3"]["Type"] == "Shaded":
                        if Enemy3["Status Effects"]["Status 3"]["Duration"] == 0:
                            print(Enemy3["Type"], " steps out of the shadows")
            if Enemy3["Status Effects"]["Status 1"]["Duration"] != 0:
                Enemy3["Status Effects"]["Status 1"]["Duration"] -= 1
            if Enemy3["Status Effects"]["Status 2"]["Duration"] != 0:
                Enemy3["Status Effects"]["Status 2"]["Duration"] -= 1
            if Enemy3["Status Effects"]["Status 3"]["Duration"] != 0:
                Enemy3["Status Effects"]["Status 3"]["Duration"] -= 1
            if Enemy3["Buff"]["Duration"] != 0:
                Enemy3["Buff"]["Duration"] -= 1
            if Enemy3["Status Effects"]["Status 1"]["Duration"] == 0:
                Enemy3["Status Effects"]["Status 1"]["Type"] = "None"
            if Enemy3["Status Effects"]["Status 2"]["Duration"] == 0:
                Enemy3["Status Effects"]["Status 2"]["Type"] = "None"
            if Enemy3["Status Effects"]["Status 3"]["Duration"] == 0:
                Enemy3["Status Effects"]["Status 3"]["Type"] = "None"
            if Enemy3["Buff"]["Duration"] == 0 and Enemy3["Buff"]["Type"] != "None":
                
                print("\nBuff has wore off\n")
                if Enemy3["Buff"]["Type"] == "Defense":
                    Enemy3["Defense"] -= Enemy3["Buff"]["Value"]
                if Enemy3["Buff"]["Type"] == "Attack":
                    Enemy3["Attack"] -= Enemy3["Buff"]["Value"]
                if Enemy3["Buff"]["Type"] == "Evasion":
                    Enemy3["Evasion"] -= Enemy3["Buff"]["Value"]
                if Enemy3["Buff"]["Type"] == "Attack And Magic Attack":
                    Enemy3["Attack"] -= Enemy3["Buff"]["Value"]
                    Enemy3["Magic Damage"] -= Enemy3["Buff"]["Value"]
                Enemy3["Buff"]["Type"] = "None"
            return Player_copy,Enemy3,n,place,Game

        def Status_Effect2(Player_copy, Enemy2,n, place,Game):

            if (Enemy2["Status Effects"]["Status 1"]["Type"] == "Burn" or  Enemy2["Status Effects"]["Status 2"]["Type"] == "Burn" or Enemy2["Status Effects"]["Status 3"]["Type"] == "Burn"  ) and (Enemy2["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy2["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy2["Status Effects"]["Status 3"]["Duration"] != 0):
                    Enemy2["Health"] -= (Enemy2["Health"] *  0.05)
                    (Enemy2["Health"]) = int(Enemy2["Health"])
                    print(Enemy2["Type"], " takes burn damage")
            if (Enemy2["Status Effects"]["Status 1"]["Type"] == "Poison" or  Enemy2["Status Effects"]["Status 2"]["Type"] == "Poison" or Enemy2["Status Effects"]["Status 3"]["Type"] == "Poison"  ) and Enemy2["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy2["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy2["Status Effects"]["Status 3"]["Duration"] != 0:
                if Enemy2["Attribute"] != "Poison" and Enemy2["Buff"]["Type"] != "Poison Immunity":
                    Enemy2["Health"] -= (Enemy2["Health"] * (random.randint(0.01,0.15)))
                    Enemy2["Health"] = round(Enemy2["Health"])
            if Game["Current Effect"]["Type"] == "Poison":
                if Enemy2["Buff"]["Type"] != "Poison Immunity":
                        Enemy2["Health"] -= 5
                        print(Enemy2["Type"], " takes poison damage")
            if (Enemy2["Status Effects"]["Status 1"]["Type"] == "Bleed" or  Enemy2["Status Effects"]["Status 2"]["Type"] == "Bleed" or Enemy2["Status Effects"]["Status 3"]["Type"] == "Bleed"  ) and Enemy2["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy2["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy2["Status Effects"]["Status 3"]["Duration"] != 0:
                    Enemy2["Health"] -= (Enemy2["Max Health"] * (random.randint(2,5)/ 100))
                    (Enemy2["Health"]) = int(Enemy2["Health"])
                    print(Enemy2["Type"], "takes bleed damage")
                    
            if Game["Current Effect"]["Type"] == "Thundering":
                if Enemy2["Buff"]["Type"] != "Electricity Immunity":
                    chance = random.random()
                    if chance > 0.8:
                        Damage = int((200 / Enemy2["Defense"]))
                        Enemy2["Health"] -= Damage
                        print(Enemy2["Type"], " was struck by lightning!")
            if n == 2 and place == "Shadow Realm Floor":
                    if Enemy2["Status Effects"]["Status 1"]["Type"] == "Shaded":
                        if Enemy2["Status Effects"]["Status 1"]["Duration"] == 0:
                            print(Enemy2["Type"], " steps out of the shadows")
                    if Enemy2["Status Effects"]["Status 2"]["Type"] == "Shaded":
                        if Enemy2["Status Effects"]["Status 2"]["Duration"] == 0:
                            print(Enemy2["Type"], " steps out of the shadows")
                    if Enemy2["Status Effects"]["Status 3"]["Type"] == "Shaded":
                        if Enemy2["Status Effects"]["Status 3"]["Duration"] == 0:
                            print(Enemy2["Type"], " steps out of the shadows")
            if Enemy2["Status Effects"]["Status 1"]["Duration"] != 0:
                Enemy2["Status Effects"]["Status 1"]["Duration"] -= 1
            if Enemy2["Status Effects"]["Status 2"]["Duration"] != 0:
                Enemy2["Status Effects"]["Status 2"]["Duration"] -= 1
            if Enemy2["Status Effects"]["Status 3"]["Duration"] != 0:
                Enemy2["Status Effects"]["Status 3"]["Duration"] -= 1
            if Enemy2["Buff"]["Duration"] != 0:
                Enemy2["Buff"]["Duration"] -= 1
            if Enemy2["Status Effects"]["Status 1"]["Duration"] == 0:
                Enemy2["Status Effects"]["Status 1"]["Type"] = "None"
            if Enemy2["Status Effects"]["Status 2"]["Duration"] == 0:
                Enemy2["Status Effects"]["Status 2"]["Type"] = "None"
            if Enemy2["Status Effects"]["Status 3"]["Duration"] == 0:
                Enemy2["Status Effects"]["Status 3"]["Type"] = "None"
            if Enemy2["Buff"]["Duration"] == 0 and Enemy2["Buff"]["Type"] != "None":
                
                print("\nBuff has wore off\n")
                if Enemy2["Buff"]["Type"] == "Defense":
                    Enemy2["Defense"] -= Enemy2["Buff"]["Value"]
                if Enemy2["Buff"]["Type"] == "Attack":
                    Enemy2["Attack"] -= Enemy2["Buff"]["Value"]
                if Enemy2["Buff"]["Type"] == "Evasion":
                    Enemy2["Evasion"] -= Enemy2["Buff"]["Value"]
                if Enemy2["Buff"]["Type"] == "Attack And Magic Attack":
                    Enemy2["Attack"] -= Enemy2["Buff"]["Value"]
                    Enemy2["Magic Damage"] -= Enemy2["Buff"]["Value"]
                Enemy2["Buff"]["Type"] = "None"
            return Player_copy,Enemy2,n,place,Game
        
        def Status_Effect1(Player_copy, Enemy1,n, place,Game):
            if (Enemy1["Status Effects"]["Status 1"]["Type"] == "Burn" or  Enemy1["Status Effects"]["Status 2"]["Type"] == "Burn" or Enemy1["Status Effects"]["Status 3"]["Type"] == "Burn"  ) and (Enemy1["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy1["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy1["Status Effects"]["Status 3"]["Duration"] != 0):
                    Enemy1["Health"] -= (Enemy1["Health"] *  0.05)
                    (Enemy1["Health"]) = int(Enemy1["Health"])
                    print(Enemy1["Type"], " takes burn damage")
            if (Enemy1["Status Effects"]["Status 1"]["Type"] == "Poison" or  Enemy1["Status Effects"]["Status 2"]["Type"] == "Poison" or Enemy1["Status Effects"]["Status 3"]["Type"] == "Poison"  ) and Enemy1["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy1["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy1["Status Effects"]["Status 3"]["Duration"] != 0:
                if Enemy1["Attribute"] != "Poison" and Enemy1["Buff"]["Type"] != "Poison Immunity":
                    Enemy1["Health"] -= (Enemy1["Health"] * (random.randint(0.01,0.15)))
                    Enemy1["Health"] = round(Enemy1["Health"])
            if Game["Current Effect"]["Type"] == "Poison":
                if Enemy1["Buff"]["Type"] != "Poison Immunity":
                    Enemy1["Health"] -= 5
                    print(Enemy1["Type"], " takes poison damage")
            if (Enemy1["Status Effects"]["Status 1"]["Type"] == "Bleed" or  Enemy1["Status Effects"]["Status 2"]["Type"] == "Bleed" or Enemy1["Status Effects"]["Status 3"]["Type"] == "Bleed"  ) and Enemy1["Status Effects"]["Status 1"]["Duration"] != 0 and Enemy1["Status Effects"]["Status 2"]["Duration"] != 0 and Enemy1["Status Effects"]["Status 3"]["Duration"] != 0:
                    Enemy1["Health"] -= (Enemy1["Max Health"] * (random.randint(2,5)/ 100))
                    (Enemy1["Health"]) = int(Enemy1["Health"])
                    print(Enemy1["Type"], "takes bleed damage")
            if Game["Current Effect"]["Type"] == "Thundering":
                if Enemy1["Buff"]["Type"] != "Electricity Immunity":
                    chance = random.random()
                    if chance > 0.8:
                        Damage = int((200 / Enemy1["Defense"]))
                        Enemy1["Health"] -= Damage
                        print(Enemy1["Type"], " was struck by lightning!")
            if n == 2 and place == "Shadow Realm Floor":
                    if Enemy1["Status Effects"]["Status 1"]["Type"] == "Shaded":
                        if Enemy1["Status Effects"]["Status 1"]["Duration"] == 0:
                            print(Enemy1["Type"], " steps out of the shadows")
                    if Enemy1["Status Effects"]["Status 2"]["Type"] == "Shaded":
                        if Enemy1["Status Effects"]["Status 2"]["Duration"] == 0:
                            print(Enemy1["Type"], " steps out of the shadows")
                    if Enemy1["Status Effects"]["Status 3"]["Type"] == "Shaded":
                        if Enemy1["Status Effects"]["Status 3"]["Duration"] == 0:
                            print(Enemy1["Type"], " steps out of the shadows")
            if Enemy1["Status Effects"]["Status 1"]["Duration"] != 0:
                Enemy1["Status Effects"]["Status 1"]["Duration"] -= 1
            if Enemy1["Status Effects"]["Status 2"]["Duration"] != 0:
                Enemy1["Status Effects"]["Status 2"]["Duration"] -= 1
            if Enemy1["Status Effects"]["Status 3"]["Duration"] != 0:
                Enemy1["Status Effects"]["Status 3"]["Duration"] -= 1
            if Enemy1["Buff"]["Duration"] != 0:
                Enemy1["Buff"]["Duration"] -= 1
            if Enemy1["Status Effects"]["Status 1"]["Duration"] == 0:
                Enemy1["Status Effects"]["Status 1"]["Type"] = "None"
            if Enemy1["Status Effects"]["Status 2"]["Duration"] == 0:
                Enemy1["Status Effects"]["Status 2"]["Type"] = "None"
            if Enemy1["Status Effects"]["Status 3"]["Duration"] == 0:
                Enemy1["Status Effects"]["Status 3"]["Type"] = "None"
            if Enemy1["Buff"]["Duration"] == 0 and Enemy1["Buff"]["Type"] != "None":
                print("\nBuff has wore off\n")
                if Enemy1["Buff"]["Type"] == "Defense":
                    Enemy1["Defense"] -= Enemy1["Buff"]["Value"]
                if Enemy1["Buff"]["Type"] == "Attack":
                    Enemy1["Attack"] -= Enemy1["Buff"]["Value"]
                if Enemy1["Buff"]["Type"] == "Evasion":
                    Enemy1["Evasion"] -= Enemy1["Buff"]["Value"]
                if Enemy1["Buff"]["Type"] == "Attack And Magic Attack":
                    Enemy1["Attack"] -= Enemy1["Buff"]["Value"]
                    Enemy1["Magic Damage"] -= Enemy1["Buff"]["Value"]
                Enemy1["Buff"]["Type"] = "None"
            return Player_copy,Enemy1,n,place,Game

        def Player_Status_Effect(Player_copy,n,Game):
            if (Player_copy["Status Effects"]["Status 1"]["Type"] == "Burn" or  Player_copy["Status Effects"]["Status 2"]["Type"] == "Burn" or Player_copy["Status Effects"]["Status 3"]["Type"] == "Burn"  ) and Player_copy["Status Effect"]["Duration"] != 0:
                    Player_copy["Health"] -= (Player_copy["Health"] *  0.05)
                    (Player_copy["Health"]) = int(Player_copy["Health"])
                    print(f"{name} takes burn damage")
            if (Player_copy["Status Effects"]["Status 1"]["Type"] == "Poison" or  Player_copy["Status Effects"]["Status 2"]["Type"] == "Poison" or Player_copy["Status Effects"]["Status 3"]["Type"] == "Poison"  ) and Player_copy["Status Effects"]["Status 1"]["Duration"] != 0 and Player_copy["Status Effects"]["Status 2"]["Duration"] != 0 and Player_copy["Status Effects"]["Status 3"]["Duration"] != 0:
                if Player_copy["Attribute"] != "Poison" and Player_copy["Buff"]["Type"] != "Poison Immunity":
                    Player_copy["Health"] -= (Player_copy["Health"] * (random.randint(0.01,0.15)))
                    Player_copy["Health"] = round(Player_copy["Health"])
            if Game["Current Effect"]["Type"] == "Poison":
                if Player["Buff"]["Type"] != "Poison Immunity":
                    Player_copy["Health"] -= 5
                    print(f"{name} takes poison damage")
            if (Player_copy["Status Effects"]["Status 1"]["Type"] == "Bleed" or  Player_copy["Status Effects"]["Status 2"]["Type"] == "Bleed" or Player_copy["Status Effects"]["Status 3"]["Type"] == "Bleed"  ) and Player_copy["Status Effects"]["Status 1"]["Duration"] != 0 and Player_copy["Status Effects"]["Status 2"]["Duration"] != 0 and Player_copy["Status Effects"]["Status 3"]["Duration"] != 0:
                    Player_copy["Health"] -= (Player_copy["Max Health"] * (random.randint(2,5)/ 100))
                    (Player_copy["Health"]) = int(Player_copy["Health"])
                    print(f"{name} takes bleed damage")
            if Game["Current Effect"]["Type"] == "Falling Rubble":
                if Player["Buff"]["Type"] != "Under Cover":
                    Player_copy["Health"] -=15
            if Game["Current Effect"]["Duration"] == 0:
                Game["Current Effect"]["Type"] = "None"
                print("Rubble has stopped falling.")
            if Game["Current Effect"]["Type"] == "Thundering":
                if  Player["Buff"]["Type"] != "Electricity Immunity":
                    chance = random.random()
                    if chance > 0.8:
                        Damage = int((200 / Player_copy["Defense"]))
                        Player_copy["Health"] -= Damage
                        print(f"{name} was struck by lightning!")
                    

            if n == 3 and place == "Poison Swamp Chamber":
                Player["Buff"]["Duration"] -= 1
                print("You are no longer immune")
            if n == 3 and place == "Alchemist Lab":
                Game["Current Effect"]["Duration"] -= Game["Current Effect"]["Duration"]
                Player["Buff"]["Duration"] -= 1
            if n == 1 and place == "Collapsing Ruins":
                Player["Buff"]["Duration"] -= 1
                print("You move away from the pillar")
            Game["Current Effect"]["Duration"] -= 1
            if Player_copy["Status Effects"]["Status 1"]["Duration"] != 0:
                Player_copy["Status Effects"]["Status 1"]["Duration"] -= 1
            if Player_copy["Status Effects"]["Status 2"]["Duration"] != 0:
                Player_copy["Status Effects"]["Status 2"]["Duration"] -= 1
            if Player_copy["Status Effects"]["Status 3"]["Duration"] != 0:
                Player_copy["Status Effects"]["Status 3"]["Duration"] -= 1
            if Player_copy["Buff"]["Duration"] != 0:
                Player_copy["Buff"]["Duration"] -= 1
            if Game["Current Effect"]["Duration"] == 0:
                Game["Current Effect"]["Type"] = "None"
            if Player_copy["Status Effects"]["Status 1"]["Duration"] == 0:
                Player_copy["Status Effects"]["Status 1"]["Type"] = "None"
            if Player_copy["Status Effects"]["Status 2"]["Duration"] == 0:
                Player_copy["Status Effects"]["Status 2"]["Type"] = "None"
            if Player_copy["Status Effects"]["Status 3"]["Duration"] == 0:
                Player_copy["Status Effects"]["Status 3"]["Type"] = "None"
            if Player_copy["Buff"]["Duration"] == 0 and Player_copy["Buff"]["Type"] != "None":
                
                print("\nBuff has wore off\n")
                if Player_copy["Buff"]["Type"] == "Defense":
                    Player_copy["Defense"] -= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Attack":
                    Player_copy["Attack"] -= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Evasion":
                    Player_copy["Evasion"] -= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Attack And Magic Attack":
                    Player_copy["Attack"] -= Player_copy["Buff"]["Value"]
                    Player_copy["Magic Damage"] -= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Magic Density":
                    Player_copy["Magic Density"] -= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Defense M":
                    Player_copy["Defense"] /= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Attack M":
                    Player_copy["Attack"] /= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Evasion M":
                    Player_copy["Evasion"] /= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Magic Density M":
                    Player_copy["Defense"] /= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Speed M":
                    Player_copy["Attack"] /= Player_copy["Buff"]["Value"]
                if Player_copy["Buff"]["Type"] == "Accuracy M":
                    Player_copy["Evasion"] /= Player_copy["Buff"]["Value"]
                Player_copy["Buff"]["Type"] = "None"
                
            return Player_copy,n,Game
        def Enemy1_Battle(Enemy1,Player,Player_copy,Evasion1_Stopper,Defense1_Stopper,name,Game,Turn_Time,Enemy1_Skip,Player_Skip,b,typewriter,**kwargs):

            Enemy2 = kwargs.get("Enemy2",None)
            Enemy3 = kwargs.get("Enemy3",None)

            
            if Evasion1_Stopper == True:
                Enemy1["Evasion"] -= 10
                Evasion1_Stopper = False
            if Defense1_Stopper == True:
                Enemy1["Defense"] -= 10
                Defense1_Stopper = False
                          

            if Enemy1_Skip == False and (Enemy1["Status Effects"]["Status 1"]["Type"] != "Freeze" and Enemy1["Status Effects"]["Status 2"]["Type"] != "Freeze" and Enemy1["Status Effects"]["Status 3"]["Type"] != "Freeze"):
                Enemy1,Enemy2,Enemy3,Player_copy,Evasion1_Stopper,Defense1_Stopper,Turn_Time,Player_Skip,Move,b = E_Battle.Enemy1_Battle(Enemy1,b,Player,Player_copy,Evasion1_Stopper,Defense1_Stopper,name,Game,Turn_Time,Player_Skip,typewriter,Enemy2=Enemy2,Enemy3=Enemy3)
                if Move == "Blood Frenzy":
                    Enemy1["Health"] = 0
                
            else:
                print(Enemy1["Type"]," is stunned!")
                Turn_Time = 0
                Enemy1_Skip = False
            

            return  Enemy1,Player_copy,Evasion1_Stopper,Defense1_Stopper,Turn_Time,Enemy1_Skip,Player_Skip,b,Enemy2,Enemy3
        def Enemy2_Battle(Enemy2,Player,Player_copy,Evasion2_Stopper,Defense2_Stopper,name,Game,Turn_Time,Enemy2_Skip,Player_Skip,typewriter):

            if Evasion2_Stopper == True:
                Enemy2["Evasion"] -= 10
                Evasion2_Stopper = False
            if Defense2_Stopper == True:
                Enemy2["Defense"] -= 10
                Defense2_Stopper = False

            if Enemy2_Skip == False and (Enemy2["Status Effects"]["Status 1"]["Type"] != "Freeze" and Enemy2["Status Effects"]["Status 2"]["Type"] != "Freeze" and Enemy2["Status Effects"]["Status 3"]["Type"] != "Freeze"):
                Enemy2,Player_copy,Evasion2_Stopper,Defense2_Stopper,Turn_Time,Player_Skip = E_Battle.Enemy2_Battle(Enemy2,Player,Player_copy,Evasion2_Stopper,Defense2_Stopper,name,Game,Turn_Time,Player_Skip,typewriter,Enemy2=Enemy2)
            else:
                print(Enemy2["Type"]," is stunned!")
                Turn_Time = 0
                Enemy2_Skip = False
            

            return  Enemy2,Player_copy,Evasion2_Stopper,Defense2_Stopper,Turn_Time,Enemy2_Skip,Player_Skip
        def Enemy3_Battle(Enemy3,Player,Player_copy,Evasion3_Stopper,Defense3_Stopper,name,Game,Turn_Time,Enemy3_Skip,Player_Skip,typewriter):

            if Evasion3_Stopper == True:
                Enemy3["Evasion"] -= 10
                Evasion3_Stopper = False
            if Defense3_Stopper == True:
                Enemy3["Defense"] -= 10
                Defense3_Stopper = False

            if Enemy3_Skip == False and (Enemy3["Status Effects"]["Status 1"]["Type"] != "Freeze" and Enemy3["Status Effects"]["Status 2"]["Type"] != "Freeze" and Enemy3["Status Effects"]["Status 3"]["Type"] != "Freeze"):
                Enemy3,Player_copy,Evasion3_Stopper,Defense3_Stopper,Turn_Time,Player_Skip = E_Battle.Enemy3_Battle(Enemy3,Player,Player_copy,Evasion3_Stopper,Defense3_Stopper,name,Game,Turn_Time,Player_Skip,typewriter)
            else:
                print(Enemy3["Type"]," is stunned!")
                Turn_Time = 0
                Enemy3_Skip = False

            return  Enemy3,Player_copy,Evasion3_Stopper,Defense3_Stopper,Turn_Time,Enemy3_Skip,Player_Skip
        

        Battle_End = False
        if Tower_Level_Choice == 1:
            start_hour = 21
            end_hour = 24
            now = datetime.now()
            if start_hour <= now.hour < end_hour:
                place = random.choice(["Burning Armory","Crumbling Bridge","Dark Ritual Room","Poison Swamp Chamber","Collapsing Ruins","Frozen Cavern","Storm Tower Top","Alchemist Lab","Blood Arena","Wilderness","Shadow Realm Floor"])
            else:
                place = random.choice(["Burning Armory","Crumbling Bridge","Dark Ritual Room","Poison Swamp Chamber","Collapsing Ruins","Frozen Cavern","Storm Tower Top","Alchemist Lab","Wilderness","Blood Arena"])
            if b >= 3:
                Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint   = L1.Level_1(Enemy,Player_copy,b,place)
            elif b >= 2:
                Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint   = L1.Level_1(Enemy,Player_copy,b,place)
            elif b >= 1:
                Enemy1,Enemy1_Weakpoint = L1.Level_1(Enemy,Player_copy,b,place)

            print(Enemy1["Type"]," has appeared\n")
            if b >= 2:
                print(Enemy2["Type"]," has appeared\n")
            if b >= 3:
                print(Enemy3["Type"]," has appeared\n")



                        
                    

            print(f"\nYou have entered the {place}\n")
            if place == "Dark Ritual Room":
                print("\nthere is an exorbitant amount of mana eminating from the room \n\n you gain 10% more mana\n")
            if place == "Burning Armory":
                print("\nthe flames burn intensely\n\n")
            if place == "Crumbling Bridge":
                print("\nThe ground feels fragile primed to break at any moment\n\n")
            if place == "Poison Swamp Chamber":
                print("\nYou are knee deep in a concentrated poison\n\n")
            if place == "Collapsing Ruins":
                print("\nDebris falls all around you\n\n")
            if place == "Frozen Cavern":
                print("\nYou drift into a smooth glacial cavern\n\n")
            if place == "Storm Tower Top":
                print("\nThunder resounds through the tower as harsh winds blow\n\n")
            if place == "Alchemist Lab":
                print("\nPotions of various compositions are scattered around the lab \n\n")
            if place == "Blood Arena":
                print("\nRoars of the crowd echo around you\n\n")
            if place == "Wilderness":
                print("\nCritters scamper around in the tall grass\n\n")
            if place == "Shadow Realm Floor":
                print("\nThe atmostphere is heavy with a looming sense of despair enveloping the space\n\n")
            print("\nWoah!...\n")
            time.sleep(2)
            print("Wait Nevermind..")
        
            while Player_copy["Health"] > 0 and Battle_End == False:
                if b >= 3:

                    fighters = [Player_copy, Enemy1, Enemy2, Enemy3]
                    Fastest_Enemy = sorted([Enemy1,Enemy2,Enemy3],key=lambda x: x["Speed"],reverse=True)

                elif b >= 2:

                    fighters = [Player_copy,Enemy1,Enemy2]
                    Fastest_Enemy = sorted([Enemy1,Enemy2],key=lambda x: x["Speed"],reverse=True)

                elif b >= 1:

                    fighters = [Player_copy,Enemy1]
                    Fastest_Enemy = Enemy1

                fighters_sorted = sorted(fighters, key=lambda x: x["Speed"], reverse=True)
                
                for fighter in fighters_sorted:


                    if Player_copy["Health"] <= 0:
                        Outcome = "Enemy Win"
                        continue

                    if x == 1:
                            Outcome = "Fled"
                            continue
                    
                    if b >= 3:
                        if Enemy3["Health"] <= 0 and check3 == True:
                            Enemy3["Health"] = 0
                            xp_gained = Enemy3["XP"] * (Enemy3["Level"] /2)
                            xp_gained = round(xp_gained)
                            Player["XP"] += xp_gained
                            gold_gained = round((random.randint((xp_gained //4),(xp_gained // 2))) * Gold_Multiplier)
                            Player["Gold"] += gold_gained
                            Statistics["Gold Earned"] += gold_gained
                            print(f"\n",Enemy1["Type"],"has been killed\n\n")
                            print(gold_gained ,"Gold has been gained\n\n")
                            percentage = random.random()
                            if percentage >= 0.7:
                                drop = random.choice(Enemy3["Drop"])
                                if drop in inventory:
                                    inventory[drop] += 1
                                else:
                                    inventory[drop] = 1
                                print(f"{drop} was dropped\n\n")
                            print(xp_gained ,"XP has been gained\n")
                            check3 = False
                            Statistics["Enemies Killed"] += 1
                            if Skill_Tree["General"]["Bloodthirsty"]["Status"] == "(Unlocked)":
                                Health_Gained = (round(Player_copy["Health"] * 0.25))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                                print("\n You activate the bloodthirsty skill\n\n You gain 25% of your max health")
                            if Skill_Tree["General"]["Momentum"]["Status"] == "(Unlocked)":
                                Player_copy["Health"] * round(Player_copy["Speed"] * 0.1)
                                print("\n You activate the momentum skill\n\n You gain 10% more speed")

                    if b >= 2:
                        if (Enemy2["Health"] <= 0 and check2 == True) :
                            Enemy2["Health"] = 0
                            xp_gained = Enemy2["XP"] * (Enemy2["Level"] /2)
                            xp_gained = round(xp_gained)
                            gold_gained = round((random.randint((xp_gained //4),(xp_gained // 2))) * Gold_Multiplier)
                            Player["Gold"] += gold_gained
                            Player["XP"] += xp_gained
                            Statistics["Gold Earned"] += gold_gained
                            print(f"\n",Enemy2["Type"]," has been killed\n\n")
                            print(gold_gained ,"Gold has been gained\n\n")
                            percentage = random.random()
                            if percentage >= 0.7:
                                drop = random.choice(Enemy2["Drop"])
                                if drop in inventory:
                                    inventory[drop] += 1
                                else:
                                    inventory[drop] = 1
                                print(f"{drop} was dropped\n\n")
                            print(xp_gained ,"XP has been gained\n")
                            check2 = False
                            Statistics["Enemies Killed"] += 1
                            if Skill_Tree["General"]["Bloodthirsty"]["Status"] == "(Unlocked)":
                                Health_Gained = (round(Player_copy["Health"] * 0.25))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                                print("\n You activate the bloodthirsty skill\n\n You gain 25% of your max health")
                            if Skill_Tree["General"]["Momentum"]["Status"] == "(Unlocked)":
                                Player_copy["Health"] * round(Player_copy["Speed"] * 0.1)
                                print("\n You activate the momentum skill\n\n You gain 10% more speed")

                    if b >= 1:
                        if Enemy1["Health"] <= 0 and check1 == True:
                            Enemy1["Health"] = 0
                            xp_gained = Enemy1["XP"] * (Enemy1["Level"] /2)
                            xp_gained = round(xp_gained)
                            gold_gained = round((random.randint((xp_gained //4),(xp_gained // 2))) * Gold_Multiplier)
                            Player["Gold"] += gold_gained
                            Player["XP"] += xp_gained
                            Statistics["Gold Earned"] += gold_gained
                            print(f"\n",Enemy1["Type"]," has been killed\n\n")
                            print(gold_gained ,"Gold has been gained\n\n")
                            percentage = random.random()
                            if percentage >= 0.7:
                                drop = random.choice(Enemy1["Drop"])
                                if drop in inventory:
                                    inventory[drop] += 1
                                else:
                                    inventory[drop] = 1
                                print(f"{drop} was dropped\n\n")
                            print(xp_gained ,"XP has been gained\n")
                            check1 = False
                            Statistics["Enemies Killed"] += 1
                            if Skill_Tree["General"]["Bloodthirsty"]["Status"] == "(Unlocked)":
                                Health_Gained = (round(Player_copy["Health"] * 0.25))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                                print("\n You activate the bloodthirsty skill\n\n You gain 25% of your max health")
                            if Skill_Tree["General"]["Momentum"]["Status"] == "(Unlocked)":
                                Player_copy["Health"] * round(Player_copy["Speed"] * 0.1)
                                print("\n You activate the momentum skill\n\n You gain 10% more speed")
                        

                        
                    if b == 3:    
                        if (Enemy1["Health"] <= 0) and (Enemy2["Health"] <= 0) and (Enemy3["Health"] <= 0):
                            Battle_End = True
                            Outcome = "Player Win"
                            if Player_Copy["Health"] == Player_copy["Max Health"]:
                                Statistics["Damageless Battles Won"] += 1
                            if "Greatsword" in Gear["Type"]:
                                Amount_Used["Greatsword"] += 1
                                if Amount_Used["Greatsword"] == 100:
                                    Proficiency["Greatsword"] = "Rookie"
                                if Amount_Used["Greatsword"] == 500:
                                    Proficiency["Greatsword"] = "Competent"
                                if Amount_Used["Greatsword"] == 1000:
                                    Proficiency["Greatsword"] = "Proficient"
                                if Amount_Used["Greatsword"] == 2500:
                                    Proficiency["Greatsword"] = "Expert"
                                if Amount_Used["Greatsword"] == 10000:
                                    Proficiency["Greatsword"] = "Master"
                            elif "Sword" in Gear["Type"]:
                                Amount_Used["Sword"] += 1
                                if Amount_Used["Sword"] == 100:
                                    Proficiency["Sword"] = "Rookie"
                                if Amount_Used["Sword"] == 500:
                                    Proficiency["Sword"] = "Competent"
                                if Amount_Used["Sword"] == 1000:
                                    Proficiency["Sword"] = "Proficient"
                                if Amount_Used["Sword"] == 2500:
                                    Proficiency["Sword"] = "Expert"
                                if Amount_Used["Sword"] == 10000:
                                    Proficiency["Sword"] = "Master"
                            elif "Spear" in Gear["Type"]:
                                Amount_Used["Spear"] += 1
                                if Amount_Used["Spear"] == 100:
                                    Proficiency["Spear"] = "Rookie"
                                if Amount_Used["Spear"] == 500:
                                    Proficiency["Spear"] = "Competent"
                                if Amount_Used["Spear"] == 1000:
                                    Proficiency["Spear"] = "Proficient"
                                if Amount_Used["Spear"] == 2500:
                                    Proficiency["Spear"] = "Expert"
                                if Amount_Used["Spear"] == 10000:
                                    Proficiency["Spear"] = "Master"
                            elif "Mace" in Gear["Type"]:
                                Amount_Used["Mace"] += 1
                                if Amount_Used["Mace"] == 100:
                                    Proficiency["Mace"] = "Rookie"
                                if Amount_Used["Mace"] == 500:
                                    Proficiency["Mace"] = "Competent"
                                if Amount_Used["Mace"] == 1000:
                                    Proficiency["Mace"] = "Proficient"
                                if Amount_Used["Mace"] == 2500:
                                    Proficiency["Mace"] = "Expert"
                                if Amount_Used["Mace"] == 10000:
                                    Proficiency["Mace"] = "Master"
                            elif "Dagger" in Gear["Type"]:
                                Amount_Used["Dagger"] += 1
                                if Amount_Used["Dagger"] == 100:
                                    Proficiency["Dagger"] = "Rookie"
                                if Amount_Used["Dagger"] == 500:
                                    Proficiency["Dagger"] = "Competent"
                                if Amount_Used["Dagger"] == 1000:
                                    Proficiency["Dagger"] = "Proficient"
                                if Amount_Used["Dagger"] == 2500:
                                    Proficiency["Dagger"] = "Expert"
                                if Amount_Used["Dagger"] == 10000:
                                    Proficiency["Dagger"] = "Master"
                            elif "Axe" in Gear["Type"]:
                                Amount_Used["Axe"] += 1
                                if Amount_Used["Axe"] == 100:
                                    Proficiency["Axe"] = "Rookie"
                                if Amount_Used["Axe"] == 500:
                                    Proficiency["Axe"] = "Competent"
                                if Amount_Used["Axe"] == 1000:
                                    Proficiency["Axe"] = "Proficient"
                                if Amount_Used["Axe"] == 2500:
                                    Proficiency["Axe"] = "Expert"
                                if Amount_Used["Axe"] == 10000:
                                    Proficiency["Axe"] = "Master"
                            elif "Bow" in Gear["Type"]:
                                Amount_Used["Bow"] += 1
                                if Amount_Used["Bow"] == 100:
                                    Proficiency["Bow"] = "Rookie"
                                if Amount_Used["Bow"] == 500:
                                    Proficiency["Bow"] = "Competent"
                                if Amount_Used["Bow"] == 1000:
                                    Proficiency["Bow"] = "Proficient"
                                if Amount_Used["Bow"] == 2500:
                                    Proficiency["Bow"] = "Expert"
                                if Amount_Used["Bow"] == 10000:
                                    Proficiency["Bow"] = "Master"
                            elif "Wand" in Gear["Type"]:
                                Amount_Used["Wand"] += 1
                                if Amount_Used["Wand"] == 100:
                                    Proficiency["Wand"] = "Rookie"
                                if Amount_Used["Wand"] == 500:
                                    Proficiency["Wand"] = "Competent"
                                if Amount_Used["Wand"] == 1000:
                                    Proficiency["Wand"] = "Proficient"
                                if Amount_Used["Wand"] == 2500:
                                    Proficiency["Wand"] = "Expert"
                                if Amount_Used["Wand"] == 10000:
                                    Proficiency["Wand"] = "Master"
                            elif "Staff" in Gear["Type"]:
                                Amount_Used["Staff"] += 1
                                if Amount_Used["Staff"] == 100:
                                    Proficiency["Staff"] = "Rookie"
                                if Amount_Used["Staff"] == 500:
                                    Proficiency["Staff"] = "Competent"
                                if Amount_Used["Staff"] == 1000:
                                    Proficiency["Staff"] = "Proficient"
                                if Amount_Used["Staff"] == 2500:
                                    Proficiency["Staff"] = "Expert"
                                if Amount_Used["Staff"] == 10000:
                                    Proficiency["Staff"] = "Master"
                            probability = random.random()
                            if probability <= treasure_chance:
                                u = random.random()
                                if u <= 0.1:
                                    award = random.choice(Chest_items["Skill Books"])
                                    if award == "Fireball":
                                        Skill_Books["Fireball"] = True
                                    elif award == "Ice Shard":
                                        Skill_Books["Ice Shard"] = True
                                    elif award == "Shock":
                                        Skill_Books["Shock"] = True
                                    elif award == "Heal":
                                        Skill_Books["Heal"] = True
                                    elif award == "Analysis":
                                        Skill_Books["Analysis"] = True
                                    elif award == "River Fist":
                                        Skill_Books["River Fist"] = True
                                    elif award == "Purify":
                                        Skill_Books["Purify"] = True
                                    elif award == "Grappling Vines":
                                        Skill_Books["Grappling Vines"] = True
                                    elif award == "Domination":
                                        Skill_Books["Domination"] = True
                                    elif award == "Toxin Spray":
                                        Skill_Books["Toxin Spray"] = True
                                    elif award == "Life Drain":
                                        Skill_Books["Life Drain"] = True
                                    elif award == "Devour Essence":
                                        Skill_Books["Devour Essence"] = True
                                    elif award == "Empower":
                                        Skill_Books["Empower"] = True
                                    elif award == "Tremor":
                                        Skill_Books["Tremor"] = True
                                    elif award == "Corrupting Touch":
                                        Skill_Books["Corrupting Touch"] = True
                                    elif award == "Stone Slipstream":
                                        Skill_Books["Stone Slipstream"] = True
                                    elif award == "Mud Shot":
                                        Skill_Books["Mud Shot"] = True
                                    elif award == "Groundbreaker":
                                        Skill_Books["Groundbreaker"] = True
                                    elif award == "Spinning Back Kick":
                                        Skill_Books["Spinning Back Kick"] = True
                                    elif award == "Axe Kick":
                                        Skill_Books["Axe Kick"] = True
                                    elif award == "Headbutt":
                                        Skill_Books["Headbutt"] = True
                                elif u > 0.1 and u <= 0.4:
                                    award = random.choice(["Copper Dagger","Crude Staff","Copper Helmet","Copper Chestplate","Copper Sword","Copper Axe","Copper Mace","Copper Spear","Copper Greatsword","Copper Bow","Copper Shield","Twig Wand","Copper Shoulder Guards","Copper Gardbrace","Copper Greaves","Copper Boots"])
                                    if ("Copper Dagger" not in inventory["Gear"] and award == "Copper Dagger"):
                                        inventory["Gear"].append("Copper Dagger")
                                        print("Copper Dagger Acquired!")
                                    elif ("Crude Staff" not in inventory["Gear"] and award == "Crude Staff"):
                                        inventory["Gear"].append("Crude Staff")
                                        print("Crude Staff Acquired!")
                                    elif ("Copper Helmet" not in inventory["Gear"] and award == "Copper Helmet"):
                                        inventory["Gear"].append("Copper Helmet")
                                        print("Copper Helmet Acquired!")
                                    elif ("Copper Chestplate" not in inventory["Gear"] and award == "Copper Chestplate"):
                                        inventory["Gear"].append("Copper Chestplate")
                                        print("Copper Chestplate Acquired!")
                                    elif ("Copper Sword" not in inventory["Gear"] and award == "Copper Sword"):
                                        inventory["Gear"].append("Copper Sword")
                                        print("Copper Sword Acquired!")
                                    elif ("Copper Axe" not in inventory["Gear"] and award == "Copper Axe"):
                                        inventory["Gear"].append("Copper Axe")
                                        print("Copper Axe Acquired!")
                                    elif ("Copper Mace" not in inventory["Gear"] and award == "Copper Mace"):
                                        inventory["Gear"].append("Copper Mace")
                                        print("Copper Mace Acquired!")
                                    elif ("Copper Spear" not in inventory["Gear"] and award == "Copper Spear"):
                                        inventory["Gear"].append("Copper Spear")
                                        print("Copper Spear Acquired!")
                                    elif ("Copper Greatsword" not in inventory["Gear"] and award == "Copper Greatsword"):
                                        inventory["Gear"].append("Copper Greatsword")
                                        print("Copper Greatsword Acquired!")
                                    elif ("Copper Bow" not in inventory["Gear"] and award == "Copper Bow"):
                                        inventory["Gear"].append("Copper Bow")
                                        print("Copper Bow Acquired!")
                                    elif ("Copper Shield" not in inventory["Gear"] and award == "Copper Shield"):
                                        inventory["Gear"].append("Copper Shield")
                                        print("Copper Shield Acquired!")
                                    elif ("Twig Wand" not in inventory["Gear"] and award == "Twig Wand"):
                                        inventory["Gear"].append("Twig Wand")
                                        print("Twig Wand Acquired!")
                                    elif ("Copper Shoulder Guards" not in inventory["Gear"] and award == "Copper Shoulder Guards"):
                                        inventory["Gear"].append("Copper Shoulder Guards")
                                        print("Copper Shoulder Guards Acquired!")
                                    elif ("Copper Gardbrace" not in inventory["Gear"] and award == "Copper Gardbrace"):
                                        inventory["Gear"].append("Copper Gardbrace")
                                        print("Copper Gardbrace Acquired!")
                                    elif ("Copper Greaves" not in inventory["Gear"] and award == "Copper Greaves"):
                                        inventory["Gear"].append("Copper Greaves")
                                        print("Copper Greaves Acquired!")
                                    elif ("Copper Boots" not in inventory["Gear"] and award == "Copper Boots"):
                                        inventory["Gear"].append("Copper Boots")
                                        print("Copper Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                elif u > 0.4 and u <= 0.7:
                                    award = random.choice(["Bronze Dagger","Carved Staff","Bronze Helmet","Bronze Chestplate","Bronze Sword","Bronze Axe","Bronze Mace","Bronze Spear","Bronze Greatsword","Bronze Bow","Bronze Shield","Carved Wand","Bronze Shoulder Guards","Bronze Gardbrace","Bronze Greaves","Bronze Boots"])
                                    if ("Bronze Dagger" not in inventory["Gear"] and award == "Bronze Dagger"):
                                        inventory["Gear"].append("Bronze Dagger")
                                        print("Bronze Dagger Acquired!")
                                    elif ("Carved Staff" not in inventory["Gear"] and award == "Carved Staff"):
                                        inventory["Gear"].append("Carved Staff")
                                        print("Carved Staff Acquired!")
                                    elif ("Bronze Helmet" not in inventory["Gear"] and award == "Bronze Helmet"):
                                        inventory["Gear"].append("Bronze Helmet")
                                        print("Bronze Helmet Acquired!")
                                    elif ("Bronze Chestplate" not in inventory["Gear"] and award == "Bronze Chestplate"):
                                        inventory["Gear"].append("Bronze Chestplate")
                                        print("Bronze Chestplate Acquired!")
                                    elif ("Bronze Sword" not in inventory["Gear"] and award == "Bronze Sword"):
                                        inventory["Gear"].append("Bronze Sword")
                                        print("Bronze Sword Acquired!")
                                    elif ("Bronze Axe" not in inventory["Gear"] and award == "Bronze Axe"):
                                        inventory["Gear"].append("Bronze Axe")
                                        print("Bronze Axe Acquired!")
                                    elif ("Bronze Mace" not in inventory["Gear"] and award == "Bronze Mace"):
                                        inventory["Gear"].append("Bronze Mace")
                                        print("Bronze Mace Acquired!")
                                    elif ("Bronze Spear" not in inventory["Gear"] and award == "Bronze Spear"):
                                        inventory["Gear"].append("Bronze Spear")
                                        print("Bronze Spear Acquired!")
                                    elif ("Bronze Greatsword" not in inventory["Gear"] and award == "Bronze Greatsword"):
                                        inventory["Gear"].append("Bronze Greatsword")
                                        print("Bronze Greatsword Acquired!")
                                    elif ("Bronze Bow" not in inventory["Gear"] and award == "Bronze Bow"):
                                        inventory["Gear"].append("Bronze Bow")
                                        print("Bronze Bow Acquired!")
                                    elif ("Bronze Shield" not in inventory["Gear"] and award == "Bronze Shield"):
                                        inventory["Gear"].append("Bronze Shield")
                                        print("Bronze Shield Acquired!")
                                    elif ("Carved Wand" not in inventory["Gear"] and award == "Carved Wand"):
                                        inventory["Gear"].append("Carved Wand")
                                        print("Carved Wand Acquired!")
                                    elif ("Bronze Shoulder Guards" not in inventory["Gear"] and award == "Bronze Shoulder Guards"):
                                        inventory["Gear"].append("Bronze Shoulder Guards")
                                        print("Bronze Shoulder Guards Acquired!")
                                    elif ("Bronze Gardbrace" not in inventory["Gear"] and award == "Bronze Gardbrace"):
                                        inventory["Gear"].append("Bronze Gardbrace")
                                        print("Bronze Gardbrace Acquired!")
                                    elif ("Bronze Greaves" not in inventory["Gear"] and award == "Bronze Greaves"):
                                        inventory["Gear"].append("Bronze Greaves")
                                        print("Bronze Greaves Acquired!")
                                    elif ("Bronze Boots" not in inventory["Gear"] and award == "Bronze Boots"):
                                        inventory["Gear"].append("Bronze Boots")
                                        print("Bronze Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                else:
                                    award = random.choice(["Iron Dagger","Runed Staff","Iron Helmet","Iron Chestplate","Iron Sword","Iron Axe","Iron Mace","Iron Spear","Iron Greatsword","Iron Bow","Iron Shield","Crystal Wand","Iron Shoulder Guards","Iron Gardbrace","Iron Greaves","Iron Boots"])
                                    if ("Iron Dagger" not in inventory["Gear"] and award == "Iron Dagger"):
                                        inventory["Gear"].append("Iron Dagger")
                                        print("Iron Dagger Acquired!")
                                    elif ("Runed Staff" not in inventory["Gear"] and award == "Runed Staff"):
                                        inventory["Gear"].append("Runed Staff")
                                        print("Runed Staff Acquired!")
                                    elif ("Iron Helmet" not in inventory["Gear"] and award == "Iron Helmet"):
                                        inventory["Gear"].append("Iron Helmet")
                                        print("Iron Helmet Acquired!")
                                    elif ("Iron Chestplate" not in inventory["Gear"] and award == "Iron Chestplate"):
                                        inventory["Gear"].append("Iron Chestplate")
                                        print("Iron Chestplate Acquired!")
                                    elif ("Iron Sword" not in inventory["Gear"] and award == "Iron Sword"):
                                        inventory["Gear"].append("Iron Sword")
                                        print("Iron Sword Acquired!")
                                    elif ("Iron Axe" not in inventory["Gear"] and award == "Iron Axe"):
                                        inventory["Gear"].append("Iron Axe")
                                        print("Iron Axe Acquired!")
                                    elif ("Iron Mace" not in inventory["Gear"] and award == "Iron Mace"):
                                        inventory["Gear"].append("Iron Mace")
                                        print("Iron Mace Acquired!")
                                    elif ("Iron Spear" not in inventory["Gear"] and award == "Iron Spear"):
                                        inventory["Gear"].append("Iron Spear")
                                        print("Iron Spear Acquired!")
                                    elif ("Iron Greatsword" not in inventory["Gear"] and award == "Iron Greatsword"):
                                        inventory["Gear"].append("Iron Greatsword")
                                        print("Iron Greatsword Acquired!")
                                    elif ("Iron Bow" not in inventory["Gear"] and award == "Iron Bow"):
                                        inventory["Gear"].append("Iron Bow")
                                        print("Iron Bow Acquired!")
                                    elif ("Iron Shield" not in inventory["Gear"] and award == "Iron Shield"):
                                        inventory["Gear"].append("Iron Shield")
                                        print("Iron Shield Acquired!")
                                    elif ("Crystal Wand" not in inventory["Gear"] and award == "Crystal Wand"):
                                        inventory["Gear"].append("Crystal Wand")
                                        print("Crystal Wand Acquired!")
                                    elif ("Iron Shoulder Guards" not in inventory["Gear"] and award == "Iron Shoulder Guards"):
                                        inventory["Gear"].append("Iron Shoulder Guards")
                                        print("Iron Shoulder Guards Acquired!")
                                    elif ("Iron Gardbrace" not in inventory["Gear"] and award == "Iron Gardbrace"):
                                        inventory["Gear"].append("Iron Gardbrace")
                                        print("Iron Gardbrace Acquired!")
                                    elif ("Iron Greaves" not in inventory["Gear"] and award == "Iron Greaves"):
                                        inventory["Gear"].append("Iron Greaves")
                                        print("Iron Greaves Acquired!")
                                    elif ("Iron Boots" not in inventory["Gear"] and award == "Iron Boots"):
                                        inventory["Gear"].append("Iron Boots")
                                        print("Iron Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                            continue
                    elif b == 2:
                        if (Enemy1["Health"] <= 0) and (Enemy2["Health"] <= 0):
                            Battle_End = True
                            Outcome = "Player Win"
                            if Player_Copy["Health"] == Player_copy["Max Health"]:
                                Statistics["Damageless Battles Won"] += 1
                            if "Greatsword" in Gear["Type"]:
                                Amount_Used["Greatsword"] += 1
                                if Amount_Used["Greatsword"] == 100:
                                    Proficiency["Greatsword"] = "Rookie"
                                if Amount_Used["Greatsword"] == 500:
                                    Proficiency["Greatsword"] = "Competent"
                                if Amount_Used["Greatsword"] == 1000:
                                    Proficiency["Greatsword"] = "Proficient"
                                if Amount_Used["Greatsword"] == 2500:
                                    Proficiency["Greatsword"] = "Expert"
                                if Amount_Used["Greatsword"] == 10000:
                                    Proficiency["Greatsword"] = "Master"
                            elif "Sword" in Gear["Type"]:
                                Amount_Used["Sword"] += 1
                                if Amount_Used["Sword"] == 100:
                                    Proficiency["Sword"] = "Rookie"
                                if Amount_Used["Sword"] == 500:
                                    Proficiency["Sword"] = "Competent"
                                if Amount_Used["Sword"] == 1000:
                                    Proficiency["Sword"] = "Proficient"
                                if Amount_Used["Sword"] == 2500:
                                    Proficiency["Sword"] = "Expert"
                                if Amount_Used["Sword"] == 10000:
                                    Proficiency["Sword"] = "Master"
                            elif "Spear" in Gear["Type"]:
                                Amount_Used["Spear"] += 1
                                if Amount_Used["Spear"] == 100:
                                    Proficiency["Spear"] = "Rookie"
                                if Amount_Used["Spear"] == 500:
                                    Proficiency["Spear"] = "Competent"
                                if Amount_Used["Spear"] == 1000:
                                    Proficiency["Spear"] = "Proficient"
                                if Amount_Used["Spear"] == 2500:
                                    Proficiency["Spear"] = "Expert"
                                if Amount_Used["Spear"] == 10000:
                                    Proficiency["Spear"] = "Master"
                            elif "Mace" in Gear["Type"]:
                                Amount_Used["Mace"] += 1
                                if Amount_Used["Mace"] == 100:
                                    Proficiency["Mace"] = "Rookie"
                                if Amount_Used["Mace"] == 500:
                                    Proficiency["Mace"] = "Competent"
                                if Amount_Used["Mace"] == 1000:
                                    Proficiency["Mace"] = "Proficient"
                                if Amount_Used["Mace"] == 2500:
                                    Proficiency["Mace"] = "Expert"
                                if Amount_Used["Mace"] == 10000:
                                    Proficiency["Mace"] = "Master"
                            elif "Dagger" in Gear["Type"]:
                                Amount_Used["Dagger"] += 1
                                if Amount_Used["Dagger"] == 100:
                                    Proficiency["Dagger"] = "Rookie"
                                if Amount_Used["Dagger"] == 500:
                                    Proficiency["Dagger"] = "Competent"
                                if Amount_Used["Dagger"] == 1000:
                                    Proficiency["Dagger"] = "Proficient"
                                if Amount_Used["Dagger"] == 2500:
                                    Proficiency["Dagger"] = "Expert"
                                if Amount_Used["Dagger"] == 10000:
                                    Proficiency["Dagger"] = "Master"
                            elif "Axe" in Gear["Type"]:
                                Amount_Used["Axe"] += 1
                                if Amount_Used["Axe"] == 100:
                                    Proficiency["Axe"] = "Rookie"
                                if Amount_Used["Axe"] == 500:
                                    Proficiency["Axe"] = "Competent"
                                if Amount_Used["Axe"] == 1000:
                                    Proficiency["Axe"] = "Proficient"
                                if Amount_Used["Axe"] == 2500:
                                    Proficiency["Axe"] = "Expert"
                                if Amount_Used["Axe"] == 10000:
                                    Proficiency["Axe"] = "Master"
                            elif "Bow" in Gear["Type"]:
                                Amount_Used["Bow"] += 1
                                if Amount_Used["Bow"] == 100:
                                    Proficiency["Bow"] = "Rookie"
                                if Amount_Used["Bow"] == 500:
                                    Proficiency["Bow"] = "Competent"
                                if Amount_Used["Bow"] == 1000:
                                    Proficiency["Bow"] = "Proficient"
                                if Amount_Used["Bow"] == 2500:
                                    Proficiency["Bow"] = "Expert"
                                if Amount_Used["Bow"] == 10000:
                                    Proficiency["Bow"] = "Master"
                            elif "Wand" in Gear["Type"]:
                                Amount_Used["Wand"] += 1
                                if Amount_Used["Wand"] == 100:
                                    Proficiency["Wand"] = "Rookie"
                                if Amount_Used["Wand"] == 500:
                                    Proficiency["Wand"] = "Competent"
                                if Amount_Used["Wand"] == 1000:
                                    Proficiency["Wand"] = "Proficient"
                                if Amount_Used["Wand"] == 2500:
                                    Proficiency["Wand"] = "Expert"
                                if Amount_Used["Wand"] == 10000:
                                    Proficiency["Wand"] = "Master"
                            elif "Staff" in Gear["Type"]:
                                Amount_Used["Staff"] += 1
                                if Amount_Used["Staff"] == 100:
                                    Proficiency["Staff"] = "Rookie"
                                if Amount_Used["Staff"] == 500:
                                    Proficiency["Staff"] = "Competent"
                                if Amount_Used["Staff"] == 1000:
                                    Proficiency["Staff"] = "Proficient"
                                if Amount_Used["Staff"] == 2500:
                                    Proficiency["Staff"] = "Expert"
                                if Amount_Used["Staff"] == 10000:
                                    Proficiency["Staff"] = "Master"
                            probability = random.random()
                            if probability <= treasure_chance:
                                u = random.random()
                                if u <= 0.1:
                                    award = random.choice(Chest_items["Skill Books"])
                                    if award == "Fireball":
                                        Skill_Books["Fireball"] = True
                                    elif award == "Ice Shard":
                                        Skill_Books["Ice Shard"] = True
                                    elif award == "Shock":
                                        Skill_Books["Shock"] = True
                                    elif award == "Heal":
                                        Skill_Books["Heal"] = True
                                    elif award == "Analysis":
                                        Skill_Books["Analysis"] = True
                                    elif award == "River Fist":
                                        Skill_Books["River Fist"] = True
                                    elif award == "Purify":
                                        Skill_Books["Purify"] = True
                                    elif award == "Grappling Vines":
                                        Skill_Books["Grappling Vines"] = True
                                    elif award == "Domination":
                                        Skill_Books["Domination"] = True
                                    elif award == "Toxin Spray":
                                        Skill_Books["Toxin Spray"] = True
                                    elif award == "Life Drain":
                                        Skill_Books["Life Drain"] = True
                                    elif award == "Devour Essence":
                                        Skill_Books["Devour Essence"] = True
                                    elif award == "Empower":
                                        Skill_Books["Empower"] = True
                                    elif award == "Tremor":
                                        Skill_Books["Tremor"] = True
                                    elif award == "Corrupting Touch":
                                        Skill_Books["Corrupting Touch"] = True
                                    elif award == "Stone Slipstream":
                                        Skill_Books["Stone Slipstream"] = True
                                    elif award == "Mud Shot":
                                        Skill_Books["Mud Shot"] = True
                                    elif award == "Groundbreaker":
                                        Skill_Books["Groundbreaker"] = True
                                    elif award == "Spinning Back Kick":
                                        Skill_Books["Spinning Back Kick"] = True
                                    elif award == "Axe Kick":
                                        Skill_Books["Axe Kick"] = True
                                    elif award == "Headbutt":
                                        Skill_Books["Headbutt"] = True
                                elif u > 0.1 and u <= 0.4:
                                    award = random.choice(["Copper Dagger","Crude Staff","Copper Helmet","Copper Chestplate","Copper Sword","Copper Axe","Copper Mace","Copper Spear","Copper Greatsword","Copper Bow","Copper Shield","Twig Wand","Copper Shoulder Guards","Copper Gardbrace","Copper Greaves","Copper Boots"])
                                    if ("Copper Dagger" not in inventory["Gear"] and award == "Copper Dagger"):
                                        inventory["Gear"].append("Copper Dagger")
                                        print("Copper Dagger Acquired!")
                                    elif ("Crude Staff" not in inventory["Gear"] and award == "Crude Staff"):
                                        inventory["Gear"].append("Crude Staff")
                                        print("Crude Staff Acquired!")
                                    elif ("Copper Helmet" not in inventory["Gear"] and award == "Copper Helmet"):
                                        inventory["Gear"].append("Copper Helmet")
                                        print("Copper Helmet Acquired!")
                                    elif ("Copper Chestplate" not in inventory["Gear"] and award == "Copper Chestplate"):
                                        inventory["Gear"].append("Copper Chestplate")
                                        print("Copper Chestplate Acquired!")
                                    elif ("Copper Sword" not in inventory["Gear"] and award == "Copper Sword"):
                                        inventory["Gear"].append("Copper Sword")
                                        print("Copper Sword Acquired!")
                                    elif ("Copper Axe" not in inventory["Gear"] and award == "Copper Axe"):
                                        inventory["Gear"].append("Copper Axe")
                                        print("Copper Axe Acquired!")
                                    elif ("Copper Mace" not in inventory["Gear"] and award == "Copper Mace"):
                                        inventory["Gear"].append("Copper Mace")
                                        print("Copper Mace Acquired!")
                                    elif ("Copper Spear" not in inventory["Gear"] and award == "Copper Spear"):
                                        inventory["Gear"].append("Copper Spear")
                                        print("Copper Spear Acquired!")
                                    elif ("Copper Greatsword" not in inventory["Gear"] and award == "Copper Greatsword"):
                                        inventory["Gear"].append("Copper Greatsword")
                                        print("Copper Greatsword Acquired!")
                                    elif ("Copper Bow" not in inventory["Gear"] and award == "Copper Bow"):
                                        inventory["Gear"].append("Copper Bow")
                                        print("Copper Bow Acquired!")
                                    elif ("Copper Shield" not in inventory["Gear"] and award == "Copper Shield"):
                                        inventory["Gear"].append("Copper Shield")
                                        print("Copper Shield Acquired!")
                                    elif ("Twig Wand" not in inventory["Gear"] and award == "Twig Wand"):
                                        inventory["Gear"].append("Twig Wand")
                                        print("Twig Wand Acquired!")
                                    elif ("Copper Shoulder Guards" not in inventory["Gear"] and award == "Copper Shoulder Guards"):
                                        inventory["Gear"].append("Copper Shoulder Guards")
                                        print("Copper Shoulder Guards Acquired!")
                                    elif ("Copper Gardbrace" not in inventory["Gear"] and award == "Copper Gardbrace"):
                                        inventory["Gear"].append("Copper Gardbrace")
                                        print("Copper Gardbrace Acquired!")
                                    elif ("Copper Greaves" not in inventory["Gear"] and award == "Copper Greaves"):
                                        inventory["Gear"].append("Copper Greaves")
                                        print("Copper Greaves Acquired!")
                                    elif ("Copper Boots" not in inventory["Gear"] and award == "Copper Boots"):
                                        inventory["Gear"].append("Copper Boots")
                                        print("Copper Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                elif u > 0.4 and u <= 0.7:
                                    award = random.choice(["Bronze Dagger","Carved Staff","Bronze Helmet","Bronze Chestplate","Bronze Sword","Bronze Axe","Bronze Mace","Bronze Spear","Bronze Greatsword","Bronze Bow","Bronze Shield","Carved Wand","Bronze Shoulder Guards","Bronze Gardbrace","Bronze Greaves","Bronze Boots"])
                                    if ("Bronze Dagger" not in inventory["Gear"] and award == "Bronze Dagger"):
                                        inventory["Gear"].append("Bronze Dagger")
                                        print("Bronze Dagger Acquired!")
                                    elif ("Carved Staff" not in inventory["Gear"] and award == "Carved Staff"):
                                        inventory["Gear"].append("Carved Staff")
                                        print("Carved Staff Acquired!")
                                    elif ("Bronze Helmet" not in inventory["Gear"] and award == "Bronze Helmet"):
                                        inventory["Gear"].append("Bronze Helmet")
                                        print("Bronze Helmet Acquired!")
                                    elif ("Bronze Chestplate" not in inventory["Gear"] and award == "Bronze Chestplate"):
                                        inventory["Gear"].append("Bronze Chestplate")
                                        print("Bronze Chestplate Acquired!")
                                    elif ("Bronze Sword" not in inventory["Gear"] and award == "Bronze Sword"):
                                        inventory["Gear"].append("Bronze Sword")
                                        print("Bronze Sword Acquired!")
                                    elif ("Bronze Axe" not in inventory["Gear"] and award == "Bronze Axe"):
                                        inventory["Gear"].append("Bronze Axe")
                                        print("Bronze Axe Acquired!")
                                    elif ("Bronze Mace" not in inventory["Gear"] and award == "Bronze Mace"):
                                        inventory["Gear"].append("Bronze Mace")
                                        print("Bronze Mace Acquired!")
                                    elif ("Bronze Spear" not in inventory["Gear"] and award == "Bronze Spear"):
                                        inventory["Gear"].append("Bronze Spear")
                                        print("Bronze Spear Acquired!")
                                    elif ("Bronze Greatsword" not in inventory["Gear"] and award == "Bronze Greatsword"):
                                        inventory["Gear"].append("Bronze Greatsword")
                                        print("Bronze Greatsword Acquired!")
                                    elif ("Bronze Bow" not in inventory["Gear"] and award == "Bronze Bow"):
                                        inventory["Gear"].append("Bronze Bow")
                                        print("Bronze Bow Acquired!")
                                    elif ("Bronze Shield" not in inventory["Gear"] and award == "Bronze Shield"):
                                        inventory["Gear"].append("Bronze Shield")
                                        print("Bronze Shield Acquired!")
                                    elif ("Carved Wand" not in inventory["Gear"] and award == "Carved Wand"):
                                        inventory["Gear"].append("Carved Wand")
                                        print("Carved Wand Acquired!")
                                    elif ("Bronze Shoulder Guards" not in inventory["Gear"] and award == "Bronze Shoulder Guards"):
                                        inventory["Gear"].append("Bronze Shoulder Guards")
                                        print("Bronze Shoulder Guards Acquired!")
                                    elif ("Bronze Gardbrace" not in inventory["Gear"] and award == "Bronze Gardbrace"):
                                        inventory["Gear"].append("Bronze Gardbrace")
                                        print("Bronze Gardbrace Acquired!")
                                    elif ("Bronze Greaves" not in inventory["Gear"] and award == "Bronze Greaves"):
                                        inventory["Gear"].append("Bronze Greaves")
                                        print("Bronze Greaves Acquired!")
                                    elif ("Bronze Boots" not in inventory["Gear"] and award == "Bronze Boots"):
                                        inventory["Gear"].append("Bronze Boots")
                                        print("Bronze Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                else:
                                    award = random.choice(["Iron Dagger","Runed Staff","Iron Helmet","Iron Chestplate","Iron Sword","Iron Axe","Iron Mace","Iron Spear","Iron Greatsword","Iron Bow","Iron Shield","Crystal Wand","Iron Shoulder Guards","Iron Gardbrace","Iron Greaves","Iron Boots"])
                                    if ("Iron Dagger" not in inventory["Gear"] and award == "Iron Dagger"):
                                        inventory["Gear"].append("Iron Dagger")
                                        print("Iron Dagger Acquired!")
                                    elif ("Runed Staff" not in inventory["Gear"] and award == "Runed Staff"):
                                        inventory["Gear"].append("Runed Staff")
                                        print("Runed Staff Acquired!")
                                    elif ("Iron Helmet" not in inventory["Gear"] and award == "Iron Helmet"):
                                        inventory["Gear"].append("Iron Helmet")
                                        print("Iron Helmet Acquired!")
                                    elif ("Iron Chestplate" not in inventory["Gear"] and award == "Iron Chestplate"):
                                        inventory["Gear"].append("Iron Chestplate")
                                        print("Iron Chestplate Acquired!")
                                    elif ("Iron Sword" not in inventory["Gear"] and award == "Iron Sword"):
                                        inventory["Gear"].append("Iron Sword")
                                        print("Iron Sword Acquired!")
                                    elif ("Iron Axe" not in inventory["Gear"] and award == "Iron Axe"):
                                        inventory["Gear"].append("Iron Axe")
                                        print("Iron Axe Acquired!")
                                    elif ("Iron Mace" not in inventory["Gear"] and award == "Iron Mace"):
                                        inventory["Gear"].append("Iron Mace")
                                        print("Iron Mace Acquired!")
                                    elif ("Iron Spear" not in inventory["Gear"] and award == "Iron Spear"):
                                        inventory["Gear"].append("Iron Spear")
                                        print("Iron Spear Acquired!")
                                    elif ("Iron Greatsword" not in inventory["Gear"] and award == "Iron Greatsword"):
                                        inventory["Gear"].append("Iron Greatsword")
                                        print("Iron Greatsword Acquired!")
                                    elif ("Iron Bow" not in inventory["Gear"] and award == "Iron Bow"):
                                        inventory["Gear"].append("Iron Bow")
                                        print("Iron Bow Acquired!")
                                    elif ("Iron Shield" not in inventory["Gear"] and award == "Iron Shield"):
                                        inventory["Gear"].append("Iron Shield")
                                        print("Iron Shield Acquired!")
                                    elif ("Crystal Wand" not in inventory["Gear"] and award == "Crystal Wand"):
                                        inventory["Gear"].append("Crystal Wand")
                                        print("Crystal Wand Acquired!")
                                    elif ("Iron Shoulder Guards" not in inventory["Gear"] and award == "Iron Shoulder Guards"):
                                        inventory["Gear"].append("Iron Shoulder Guards")
                                        print("Iron Shoulder Guards Acquired!")
                                    elif ("Iron Gardbrace" not in inventory["Gear"] and award == "Iron Gardbrace"):
                                        inventory["Gear"].append("Iron Gardbrace")
                                        print("Iron Gardbrace Acquired!")
                                    elif ("Iron Greaves" not in inventory["Gear"] and award == "Iron Greaves"):
                                        inventory["Gear"].append("Iron Greaves")
                                        print("Iron Greaves Acquired!")
                                    elif ("Iron Boots" not in inventory["Gear"] and award == "Iron Boots"):
                                        inventory["Gear"].append("Iron Boots")
                                        print("Iron Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                            continue

                    elif b == 1:
                        if (Enemy1["Health"] <= 0):
                            Battle_End = True
                            Outcome = "Player Win"
                            if Player_Copy["Health"] == Player_copy["Max Health"]:
                                Statistics["Damageless Battles Won"] += 1
                            if "Greatsword" in Gear["Type"]:
                                Amount_Used["Greatsword"] += 1
                                if Amount_Used["Greatsword"] == 100:
                                    Proficiency["Greatsword"] = "Rookie"
                                if Amount_Used["Greatsword"] == 500:
                                    Proficiency["Greatsword"] = "Competent"
                                if Amount_Used["Greatsword"] == 1000:
                                    Proficiency["Greatsword"] = "Proficient"
                                if Amount_Used["Greatsword"] == 2500:
                                    Proficiency["Greatsword"] = "Expert"
                                if Amount_Used["Greatsword"] == 10000:
                                    Proficiency["Greatsword"] = "Master"
                            elif "Sword" in Gear["Type"]:
                                Amount_Used["Sword"] += 1
                                if Amount_Used["Sword"] == 100:
                                    Proficiency["Sword"] = "Rookie"
                                if Amount_Used["Sword"] == 500:
                                    Proficiency["Sword"] = "Competent"
                                if Amount_Used["Sword"] == 1000:
                                    Proficiency["Sword"] = "Proficient"
                                if Amount_Used["Sword"] == 2500:
                                    Proficiency["Sword"] = "Expert"
                                if Amount_Used["Sword"] == 10000:
                                    Proficiency["Sword"] = "Master"
                            elif "Spear" in Gear["Type"]:
                                Amount_Used["Spear"] += 1
                                if Amount_Used["Spear"] == 100:
                                    Proficiency["Spear"] = "Rookie"
                                if Amount_Used["Spear"] == 500:
                                    Proficiency["Spear"] = "Competent"
                                if Amount_Used["Spear"] == 1000:
                                    Proficiency["Spear"] = "Proficient"
                                if Amount_Used["Spear"] == 2500:
                                    Proficiency["Spear"] = "Expert"
                                if Amount_Used["Spear"] == 10000:
                                    Proficiency["Spear"] = "Master"
                            elif "Mace" in Gear["Type"]:
                                Amount_Used["Mace"] += 1
                                if Amount_Used["Mace"] == 100:
                                    Proficiency["Mace"] = "Rookie"
                                if Amount_Used["Mace"] == 500:
                                    Proficiency["Mace"] = "Competent"
                                if Amount_Used["Mace"] == 1000:
                                    Proficiency["Mace"] = "Proficient"
                                if Amount_Used["Mace"] == 2500:
                                    Proficiency["Mace"] = "Expert"
                                if Amount_Used["Mace"] == 10000:
                                    Proficiency["Mace"] = "Master"
                            elif "Dagger" in Gear["Type"]:
                                Amount_Used["Dagger"] += 1
                                if Amount_Used["Dagger"] == 100:
                                    Proficiency["Dagger"] = "Rookie"
                                if Amount_Used["Dagger"] == 500:
                                    Proficiency["Dagger"] = "Competent"
                                if Amount_Used["Dagger"] == 1000:
                                    Proficiency["Dagger"] = "Proficient"
                                if Amount_Used["Dagger"] == 2500:
                                    Proficiency["Dagger"] = "Expert"
                                if Amount_Used["Dagger"] == 10000:
                                    Proficiency["Dagger"] = "Master"
                            elif "Axe" in Gear["Type"]:
                                Amount_Used["Axe"] += 1
                                if Amount_Used["Axe"] == 100:
                                    Proficiency["Axe"] = "Rookie"
                                if Amount_Used["Axe"] == 500:
                                    Proficiency["Axe"] = "Competent"
                                if Amount_Used["Axe"] == 1000:
                                    Proficiency["Axe"] = "Proficient"
                                if Amount_Used["Axe"] == 2500:
                                    Proficiency["Axe"] = "Expert"
                                if Amount_Used["Axe"] == 10000:
                                    Proficiency["Axe"] = "Master"
                            elif "Bow" in Gear["Type"]:
                                Amount_Used["Bow"] += 1
                                if Amount_Used["Bow"] == 100:
                                    Proficiency["Bow"] = "Rookie"
                                if Amount_Used["Bow"] == 500:
                                    Proficiency["Bow"] = "Competent"
                                if Amount_Used["Bow"] == 1000:
                                    Proficiency["Bow"] = "Proficient"
                                if Amount_Used["Bow"] == 2500:
                                    Proficiency["Bow"] = "Expert"
                                if Amount_Used["Bow"] == 10000:
                                    Proficiency["Bow"] = "Master"
                            elif "Wand" in Gear["Type"]:
                                Amount_Used["Wand"] += 1
                                if Amount_Used["Wand"] == 100:
                                    Proficiency["Wand"] = "Rookie"
                                if Amount_Used["Wand"] == 500:
                                    Proficiency["Wand"] = "Competent"
                                if Amount_Used["Wand"] == 1000:
                                    Proficiency["Wand"] = "Proficient"
                                if Amount_Used["Wand"] == 2500:
                                    Proficiency["Wand"] = "Expert"
                                if Amount_Used["Wand"] == 10000:
                                    Proficiency["Wand"] = "Master"
                            elif "Staff" in Gear["Type"]:
                                Amount_Used["Staff"] += 1
                                if Amount_Used["Staff"] == 100:
                                    Proficiency["Staff"] = "Rookie"
                                if Amount_Used["Staff"] == 500:
                                    Proficiency["Staff"] = "Competent"
                                if Amount_Used["Staff"] == 1000:
                                    Proficiency["Staff"] = "Proficient"
                                if Amount_Used["Staff"] == 2500:
                                    Proficiency["Staff"] = "Expert"
                                if Amount_Used["Staff"] == 10000:
                                    Proficiency["Staff"] = "Master"
                            probability = random.random()
                            if probability <= treasure_chance:
                                u = random.random()
                                if u <= 0.1:
                                    award = random.choice(Chest_items["Skill Books"])
                                    if award == "Fireball":
                                        Skill_Books["Fireball"] = True
                                    elif award == "Ice Shard":
                                        Skill_Books["Ice Shard"] = True
                                    elif award == "Shock":
                                        Skill_Books["Shock"] = True
                                    elif award == "Heal":
                                        Skill_Books["Heal"] = True
                                    elif award == "Analysis":
                                        Skill_Books["Analysis"] = True
                                    elif award == "River Fist":
                                        Skill_Books["River Fist"] = True
                                    elif award == "Purify":
                                        Skill_Books["Purify"] = True
                                    elif award == "Grappling Vines":
                                        Skill_Books["Grappling Vines"] = True
                                    elif award == "Domination":
                                        Skill_Books["Domination"] = True
                                    elif award == "Toxin Spray":
                                        Skill_Books["Toxin Spray"] = True
                                    elif award == "Life Drain":
                                        Skill_Books["Life Drain"] = True
                                    elif award == "Devour Essence":
                                        Skill_Books["Devour Essence"] = True
                                    elif award == "Empower":
                                        Skill_Books["Empower"] = True
                                    elif award == "Tremor":
                                        Skill_Books["Tremor"] = True
                                    elif award == "Corrupting Touch":
                                        Skill_Books["Corrupting Touch"] = True
                                    elif award == "Stone Slipstream":
                                        Skill_Books["Stone Slipstream"] = True
                                    elif award == "Mud Shot":
                                        Skill_Books["Mud Shot"] = True
                                    elif award == "Groundbreaker":
                                        Skill_Books["Groundbreaker"] = True
                                    elif award == "Spinning Back Kick":
                                        Skill_Books["Spinning Back Kick"] = True
                                    elif award == "Axe Kick":
                                        Skill_Books["Axe Kick"] = True
                                    elif award == "Headbutt":
                                        Skill_Books["Headbutt"] = True
                                elif u > 0.1 and u <= 0.4:
                                    award = random.choice(["Copper Dagger","Crude Staff","Copper Helmet","Copper Chestplate","Copper Sword","Copper Axe","Copper Mace","Copper Spear","Copper Greatsword","Copper Bow","Copper Shield","Twig Wand","Copper Shoulder Guards","Copper Gardbrace","Copper Greaves","Copper Boots"])
                                    if ("Copper Dagger" not in inventory["Gear"] and award == "Copper Dagger"):
                                        inventory["Gear"].append("Copper Dagger")
                                        print("Copper Dagger Acquired!")
                                    elif ("Crude Staff" not in inventory["Gear"] and award == "Crude Staff"):
                                        inventory["Gear"].append("Crude Staff")
                                        print("Crude Staff Acquired!")
                                    elif ("Copper Helmet" not in inventory["Gear"] and award == "Copper Helmet"):
                                        inventory["Gear"].append("Copper Helmet")
                                        print("Copper Helmet Acquired!")
                                    elif ("Copper Chestplate" not in inventory["Gear"] and award == "Copper Chestplate"):
                                        inventory["Gear"].append("Copper Chestplate")
                                        print("Copper Chestplate Acquired!")
                                    elif ("Copper Sword" not in inventory["Gear"] and award == "Copper Sword"):
                                        inventory["Gear"].append("Copper Sword")
                                        print("Copper Sword Acquired!")
                                    elif ("Copper Axe" not in inventory["Gear"] and award == "Copper Axe"):
                                        inventory["Gear"].append("Copper Axe")
                                        print("Copper Axe Acquired!")
                                    elif ("Copper Mace" not in inventory["Gear"] and award == "Copper Mace"):
                                        inventory["Gear"].append("Copper Mace")
                                        print("Copper Mace Acquired!")
                                    elif ("Copper Spear" not in inventory["Gear"] and award == "Copper Spear"):
                                        inventory["Gear"].append("Copper Spear")
                                        print("Copper Spear Acquired!")
                                    elif ("Copper Greatsword" not in inventory["Gear"] and award == "Copper Greatsword"):
                                        inventory["Gear"].append("Copper Greatsword")
                                        print("Copper Greatsword Acquired!")
                                    elif ("Copper Bow" not in inventory["Gear"] and award == "Copper Bow"):
                                        inventory["Gear"].append("Copper Bow")
                                        print("Copper Bow Acquired!")
                                    elif ("Copper Shield" not in inventory["Gear"] and award == "Copper Shield"):
                                        inventory["Gear"].append("Copper Shield")
                                        print("Copper Shield Acquired!")
                                    elif ("Twig Wand" not in inventory["Gear"] and award == "Twig Wand"):
                                        inventory["Gear"].append("Twig Wand")
                                        print("Twig Wand Acquired!")
                                    elif ("Copper Shoulder Guards" not in inventory["Gear"] and award == "Copper Shoulder Guards"):
                                        inventory["Gear"].append("Copper Shoulder Guards")
                                        print("Copper Shoulder Guards Acquired!")
                                    elif ("Copper Gardbrace" not in inventory["Gear"] and award == "Copper Gardbrace"):
                                        inventory["Gear"].append("Copper Gardbrace")
                                        print("Copper Gardbrace Acquired!")
                                    elif ("Copper Greaves" not in inventory["Gear"] and award == "Copper Greaves"):
                                        inventory["Gear"].append("Copper Greaves")
                                        print("Copper Greaves Acquired!")
                                    elif ("Copper Boots" not in inventory["Gear"] and award == "Copper Boots"):
                                        inventory["Gear"].append("Copper Boots")
                                        print("Copper Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                elif u > 0.4 and u <= 0.7:
                                    award = random.choice(["Bronze Dagger","Carved Staff","Bronze Helmet","Bronze Chestplate","Bronze Sword","Bronze Axe","Bronze Mace","Bronze Spear","Bronze Greatsword","Bronze Bow","Bronze Shield","Carved Wand","Bronze Shoulder Guards","Bronze Gardbrace","Bronze Greaves","Bronze Boots"])
                                    if ("Bronze Dagger" not in inventory["Gear"] and award == "Bronze Dagger"):
                                        inventory["Gear"].append("Bronze Dagger")
                                        print("Bronze Dagger Acquired!")
                                    elif ("Carved Staff" not in inventory["Gear"] and award == "Carved Staff"):
                                        inventory["Gear"].append("Carved Staff")
                                        print("Carved Staff Acquired!")
                                    elif ("Bronze Helmet" not in inventory["Gear"] and award == "Bronze Helmet"):
                                        inventory["Gear"].append("Bronze Helmet")
                                        print("Bronze Helmet Acquired!")
                                    elif ("Bronze Chestplate" not in inventory["Gear"] and award == "Bronze Chestplate"):
                                        inventory["Gear"].append("Bronze Chestplate")
                                        print("Bronze Chestplate Acquired!")
                                    elif ("Bronze Sword" not in inventory["Gear"] and award == "Bronze Sword"):
                                        inventory["Gear"].append("Bronze Sword")
                                        print("Bronze Sword Acquired!")
                                    elif ("Bronze Axe" not in inventory["Gear"] and award == "Bronze Axe"):
                                        inventory["Gear"].append("Bronze Axe")
                                        print("Bronze Axe Acquired!")
                                    elif ("Bronze Mace" not in inventory["Gear"] and award == "Bronze Mace"):
                                        inventory["Gear"].append("Bronze Mace")
                                        print("Bronze Mace Acquired!")
                                    elif ("Bronze Spear" not in inventory["Gear"] and award == "Bronze Spear"):
                                        inventory["Gear"].append("Bronze Spear")
                                        print("Bronze Spear Acquired!")
                                    elif ("Bronze Greatsword" not in inventory["Gear"] and award == "Bronze Greatsword"):
                                        inventory["Gear"].append("Bronze Greatsword")
                                        print("Bronze Greatsword Acquired!")
                                    elif ("Bronze Bow" not in inventory["Gear"] and award == "Bronze Bow"):
                                        inventory["Gear"].append("Bronze Bow")
                                        print("Bronze Bow Acquired!")
                                    elif ("Bronze Shield" not in inventory["Gear"] and award == "Bronze Shield"):
                                        inventory["Gear"].append("Bronze Shield")
                                        print("Bronze Shield Acquired!")
                                    elif ("Carved Wand" not in inventory["Gear"] and award == "Carved Wand"):
                                        inventory["Gear"].append("Carved Wand")
                                        print("Carved Wand Acquired!")
                                    elif ("Bronze Shoulder Guards" not in inventory["Gear"] and award == "Bronze Shoulder Guards"):
                                        inventory["Gear"].append("Bronze Shoulder Guards")
                                        print("Bronze Shoulder Guards Acquired!")
                                    elif ("Bronze Gardbrace" not in inventory["Gear"] and award == "Bronze Gardbrace"):
                                        inventory["Gear"].append("Bronze Gardbrace")
                                        print("Bronze Gardbrace Acquired!")
                                    elif ("Bronze Greaves" not in inventory["Gear"] and award == "Bronze Greaves"):
                                        inventory["Gear"].append("Bronze Greaves")
                                        print("Bronze Greaves Acquired!")
                                    elif ("Bronze Boots" not in inventory["Gear"] and award == "Bronze Boots"):
                                        inventory["Gear"].append("Bronze Boots")
                                        print("Bronze Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                else:
                                    award = random.choice(["Iron Dagger","Runed Staff","Iron Helmet","Iron Chestplate","Iron Sword","Iron Axe","Iron Mace","Iron Spear","Iron Greatsword","Iron Bow","Iron Shield","Crystal Wand","Iron Shoulder Guards","Iron Gardbrace","Iron Greaves","Iron Boots"])
                                    if ("Iron Dagger" not in inventory["Gear"] and award == "Iron Dagger"):
                                        inventory["Gear"].append("Iron Dagger")
                                        print("Iron Dagger Acquired!")
                                    elif ("Runed Staff" not in inventory["Gear"] and award == "Runed Staff"):
                                        inventory["Gear"].append("Runed Staff")
                                        print("Runed Staff Acquired!")
                                    elif ("Iron Helmet" not in inventory["Gear"] and award == "Iron Helmet"):
                                        inventory["Gear"].append("Iron Helmet")
                                        print("Iron Helmet Acquired!")
                                    elif ("Iron Chestplate" not in inventory["Gear"] and award == "Iron Chestplate"):
                                        inventory["Gear"].append("Iron Chestplate")
                                        print("Iron Chestplate Acquired!")
                                    elif ("Iron Sword" not in inventory["Gear"] and award == "Iron Sword"):
                                        inventory["Gear"].append("Iron Sword")
                                        print("Iron Sword Acquired!")
                                    elif ("Iron Axe" not in inventory["Gear"] and award == "Iron Axe"):
                                        inventory["Gear"].append("Iron Axe")
                                        print("Iron Axe Acquired!")
                                    elif ("Iron Mace" not in inventory["Gear"] and award == "Iron Mace"):
                                        inventory["Gear"].append("Iron Mace")
                                        print("Iron Mace Acquired!")
                                    elif ("Iron Spear" not in inventory["Gear"] and award == "Iron Spear"):
                                        inventory["Gear"].append("Iron Spear")
                                        print("Iron Spear Acquired!")
                                    elif ("Iron Greatsword" not in inventory["Gear"] and award == "Iron Greatsword"):
                                        inventory["Gear"].append("Iron Greatsword")
                                        print("Iron Greatsword Acquired!")
                                    elif ("Iron Bow" not in inventory["Gear"] and award == "Iron Bow"):
                                        inventory["Gear"].append("Iron Bow")
                                        print("Iron Bow Acquired!")
                                    elif ("Iron Shield" not in inventory["Gear"] and award == "Iron Shield"):
                                        inventory["Gear"].append("Iron Shield")
                                        print("Iron Shield Acquired!")
                                    elif ("Crystal Wand" not in inventory["Gear"] and award == "Crystal Wand"):
                                        inventory["Gear"].append("Crystal Wand")
                                        print("Crystal Wand Acquired!")
                                    elif ("Iron Shoulder Guards" not in inventory["Gear"] and award == "Iron Shoulder Guards"):
                                        inventory["Gear"].append("Iron Shoulder Guards")
                                        print("Iron Shoulder Guards Acquired!")
                                    elif ("Iron Gardbrace" not in inventory["Gear"] and award == "Iron Gardbrace"):
                                        inventory["Gear"].append("Iron Gardbrace")
                                        print("Iron Gardbrace Acquired!")
                                    elif ("Iron Greaves" not in inventory["Gear"] and award == "Iron Greaves"):
                                        inventory["Gear"].append("Iron Greaves")
                                        print("Iron Greaves Acquired!")
                                    elif ("Iron Boots" not in inventory["Gear"] and award == "Iron Boots"):
                                        inventory["Gear"].append("Iron Boots")
                                        print("Iron Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                            continue


                    if fighter == Player_copy:
                        if b >= 1:
                            Fastest_Enemy = Enemy1
                        else:
                            Fastest_Enemy = Fastest_Enemy[0]

                        Turn_Time = Player_copy["Speed"] / Fastest_Enemy["Speed"]
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                    
                            if b >= 3:
                                Player,Player_copy, Enemy1, Enemy2, Enemy3,n, place, player_shadows,x,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,Player_Skip,Turn_Time,Statistics  = Player_Battle.Player3_Battle(Player,Player_copy,Enemy,Enemy1,Enemy2,Enemy3,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,Skill_Tree,Statistics,typewriter,Gold_Multiplier)
                            elif b >= 2:
                                Player,Player_copy, Enemy1, Enemy2,n, place,player_shadows,x,Enemy1_Skip,Enemy2_Skip,Player_Skip,Turn_Time,Statistics  = Player_Battle.Player2_Battle(Player,Player_copy,Enemy,Enemy1,Enemy2,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Enemy2_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Enemy2_Skip,Skill_Tree,Statistics,typewriter,Gold_Multiplier)
                            elif b >= 1:
                                Player,Player_copy, Enemy1,n, place,player_shadows,x,Enemy1_Skip,Player_Skip,Turn_Time,Statistics  = Player_Battle.Player1_Battle(Player,Player_copy,Enemy,Enemy1,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Skill_Tree,Statistics,typewriter,Gold_Multiplier)
                        if Skill_Tree["General"]["Fast Recovery"]["Status"] != "(Unlocked)":
                            Player_copy["Stamina"] += (Player["Stamina"] * 0.1)
                        else:
                            Player_copy["Stamina"] += (Player["Stamina"] * 0.25)
                        Player_copy["Stamina"] = round(Player_copy["Stamina"])
                        

                    if fighter == Enemy3:
                        Turn_Time = Enemy3["Speed"] / Player_copy["Speed"]
                        print(f"\n---------------\n",Enemy3["Type"],"turn\n---------------\n")
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                            if Enemy3["Health"] > 0:
                                Enemy3, Player_copy, Evasion3_Stopper, Defense3_Stopper,Turn_Time,Enemy3_Skip,Player_Skip = Enemy3_Battle(Enemy3,Player,Player_copy,Evasion3_Stopper,Defense3_Stopper,name,Game,Turn_Time,Enemy3_Skip,Player_Skip,typewriter)
                        if "Traveler" in Enemy3["Type"]:
                            Enemy3["Stamina"] *= 1.5
                            Enemy3["Stamina"] = round(Enemy3["Stamina"])
                        else:
                            Enemy3["Stamina"] *= 1.1
                            Enemy3["Stamina"] = round(Enemy3["Stamina"])
                        print(f"\n---------------\n Turn End\n---------------\n")

                    if fighter == Enemy2:
                        Turn_Time = Enemy2["Speed"] / Player_copy["Speed"]
                        print(f"\n---------------\n",Enemy2["Type"],"turn\n---------------\n")
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                            if Enemy2["Health"] > 0:
                                Enemy2, Player_copy, Evasion2_Stopper, Defense2_Stopper,Turn_Time,Enemy2_Skip,Player_Skip = Enemy2_Battle(Enemy2,Player,Player_copy,Evasion2_Stopper,Defense2_Stopper,name,Game,Turn_Time,Enemy2_Skip,Player_Skip,typewriter)
                        if "Traveler" in Enemy2["Type"]:
                            Enemy2["Stamina"] *= 1.5
                            Enemy2["Stamina"] = round(Enemy2["Stamina"])
                        else:
                            Enemy2["Stamina"] *= 1.1
                            Enemy2["Stamina"] = round(Enemy2["Stamina"])
                        print(f"\n---------------\n Turn End\n---------------\n")
                        
                    if fighter == Enemy1:
                        Turn_Time = Enemy1["Speed"] / Player_copy["Speed"]
                        print(f"\n---------------\n",Enemy1["Type"],"turn\n---------------\n")
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                            if Enemy1["Health"] > 0:
                                Enemy1,Player_copy, Evasion1_Stopper,Defense1_Stopper,Turn_Time,Enemy1_Skip,Player_Skip,b,Enemy2,Enemy3 = Enemy1_Battle(Enemy1,Player,Player_copy,Evasion1_Stopper,Defense1_Stopper,name,Game,Turn_Time,Enemy1_Skip,Player_Skip,b,typewriter,Enemy2=Enemy2,Enemy3=Enemy3)
                        if "Traveler" in Enemy1["Type"]:
                            Enemy1["Stamina"] *= 1.5
                            Enemy1["Stamina"] = round(Enemy1["Stamina"])
                        else:
                            Enemy1["Stamina"] *= 1.1
                            Enemy1["Stamina"] = round(Enemy1["Stamina"])
                        print(f"\n---------------\n Turn End\n---------------\n")


                    if fighter == fighters_sorted[-1]:
                        if b >= 3:
                            Player_copy, Enemy3,n, place,Game =Status_Effect3(Player_copy, Enemy3,n, place,Game)
                        if b >= 2:
                            Player_copy, Enemy2,n, place,Game = Status_Effect2(Player_copy, Enemy2,n, place,Game)
                        if b >= 1:
                            Player_copy, Enemy1,n, place,Game = Status_Effect1(Player_copy, Enemy1,n, place,Game)

                        Player_copy,n,Game = Player_Status_Effect(Player_copy,n,Game)






        if Tower_Level_Choice == 2:
            start_hour = 21
            end_hour = 24
            now = datetime.now()
            if start_hour <= now.hour < end_hour:
                place = random.choice(["Burning Armory","Crumbling Bridge","Dark Ritual Room","Poison Swamp Chamber","Collapsing Ruins","Frozen Cavern","Storm Tower Top","Alchemist Lab","Blood Arena","Wilderness","Shadow Realm Floor"])
            else:
                place = random.choice(["Burning Armory","Crumbling Bridge","Dark Ritual Room","Poison Swamp Chamber","Collapsing Ruins","Frozen Cavern","Storm Tower Top","Alchemist Lab","Blood Arena","Wilderness"])
            if b >= 3:
                Enemy1,Enemy2,Enemy3,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint, = L2.Level_2(Enemy,Player_copy,b,place)
            elif b >= 2:
                Enemy1,Enemy2,Enemy1_Weakpoint,Enemy2_Weakpoint, = L2.Level_2(Enemy,Player_copy,b,place)
            elif b >= 1:
                Enemy1,Enemy1_Weakpoint = L2.Level_2(Enemy,Player_copy,b,place)

            print(Enemy1["Type"]," has appeared\n")
            if b >= 2:
                print(Enemy2["Type"]," has appeared\n")
            if b >= 3:
                print(Enemy3["Type"]," has appeared\n")



                        
                    

            print(f"\nYou have entered  a {place}\n")
            if place == "Dark Ritual Room":
                print("\nthere is an exorbitant amount of mana eminating from the room \n you gain 10% more mana\n")
            if place == "Burning Armory":
                print("\nthe flames burn intensely\n")
            if place == "Crumbling Bridge":
                print("\nThe ground feels fragile primed to break at any moment\n")
            if place == "Poison Swamp Chamber":
                print("\nYou are knee deep in a concentrated poison\n")
            if place == "Collapsing Ruins":
                print("\nDebris falls all around you\n")
            if place == "Frozen Cavern":
                print("\nYou drift into a smooth glacial cavern\n")
            if place == "Storm Tower Top":
                print("\nThunder resounds through the tower as harsh winds blow\n")
            if place == "Alchemist Lab":
                print("\nPotions of various compositions are scattered around the lab \n")
            if place == "Blood Arena":
                print("\nRoars of the crowd echo around you\n")
            if place == "Wilderness":
                print("\nCritters scamper around in the tall grass\n")
            if place == "Shadow Realm Floor":
                print("\nThe atmostphere is heavy with a looming sense of despair enveloping the space\n")

            print("Woah!...\n")
            time.sleep(2)
            print("Wait Nevermind..")
        
            while Player_copy["Health"] > 0 and Battle_End == False:
                if b >= 3:

                    fighters = [Player_copy, Enemy1, Enemy2, Enemy3]
                    Fastest_Enemy = sorted([Enemy1,Enemy2,Enemy3],key=lambda x: x["Speed"],reverse=True)

                elif b >= 2:

                    fighters = [Player_copy,Enemy1,Enemy2]
                    Fastest_Enemy = sorted([Enemy1,Enemy2],key=lambda x: x["Speed"],reverse=True)

                elif b >= 1:

                    fighters = [Player_copy,Enemy1]
                    Fastest_Enemy = Enemy1

                fighters_sorted = sorted(fighters, key=lambda x: x["Speed"], reverse=True)
                
                for fighter in fighters_sorted:


                    if Player_copy["Health"] <= 0:
                        Outcome = "Enemy Win"
                        continue

                    if x == 1:
                            Outcome = "Fled"
                            continue
                    
                    if b >= 3:
                        if Enemy3["Health"] <= 0 and check3 == True:
                            Enemy3["Health"] = 0
                            xp_gained = Enemy3["XP"] * (Enemy3["Level"] /2)
                            xp_gained = round(xp_gained)
                            gold_gained = round((random.randint((xp_gained //4),(xp_gained // 2))) * Gold_Multiplier)
                            Player["Gold"] += gold_gained
                            Statistics["Gold Earned"] += gold_gained
                            Player["XP"] += xp_gained
                            print(f"\n",Enemy1["Type"],"has been killed\n\n")
                            print(gold_gained ,"Gold has been gained\n\n")
                            percentage = random.random()
                            if percentage >= 0.7:
                                drop = random.choice(Enemy3["Drop"])
                                if drop in inventory:
                                    inventory[drop] += 1
                                else:
                                    inventory[drop] = 1
                                print(f"{drop} was dropped\n\n")
                            print(xp_gained ,"XP has been gained\n")
                            check3 = False
                            Statistics["Enemies Killed"] += 1
                            if Skill_Tree["General"]["Bloodthirsty"]["Status"] == "(Unlocked)":
                                Health_Gained = (round(Player_copy["Health"] * 0.25))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                                print("\n You activate the bloodthirsty skill\n\n You gain 25% of your max health")
                            if Skill_Tree["General"]["Momentum"]["Status"] == "(Unlocked)":
                                Player_copy["Health"] * round(Player_copy["Speed"] * 0.1)
                                print("\n You activate the momentum skill\n\n You gain 10% more speed")
                    

                    if b >= 2:
                        if (Enemy2["Health"] <= 0 and check2 == True) :
                            Enemy2["Health"] = 0
                            xp_gained = Enemy2["XP"] * (Enemy2["Level"] /2)
                            xp_gained = round(xp_gained)
                            gold_gained = round((random.randint((xp_gained //4),(xp_gained // 2))) * Gold_Multiplier)
                            Player["Gold"] += gold_gained
                            Player["XP"] += xp_gained
                            Statistics["Gold Earned"] += gold_gained
                            print(f"\n",Enemy2["Type"]," has been killed\n\n")
                            print(gold_gained ,"Gold has been gained\n\n")
                            percentage = random.random()
                            if percentage >= 0.7:
                                drop = random.choice(Enemy2["Drop"])
                                if drop in inventory:
                                    inventory[drop] += 1
                                else:
                                    inventory[drop] = 1
                                print(f"{drop} was dropped\n\n")
                            print(xp_gained ,"XP has been gained\n")
                            check2 = False
                            Statistics["Enemies Killed"] += 1
                            if Skill_Tree["General"]["Bloodthirsty"]["Status"] == "(Unlocked)":
                                Health_Gained = (round(Player_copy["Health"] * 0.25))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                                print("\n You activate the bloodthirsty skill\n\n You gain 25% of your max health")
                            if Skill_Tree["General"]["Momentum"]["Status"] == "(Unlocked)":
                                Player_copy["Health"] * round(Player_copy["Speed"] * 0.1)
                                print("\n You activate the momentum skill\n\n You gain 10% more speed")


                    if b >= 1:
                        if Enemy1["Health"] <= 0 and check1 == True:
                            Enemy1["Health"] = 0
                            xp_gained = Enemy1["XP"] * (Enemy1["Level"] /2)
                            xp_gained = round(xp_gained)
                            gold_gained = round((random.randint((xp_gained //4),(xp_gained // 2))) * Gold_Multiplier)
                            Player["Gold"] += gold_gained
                            Player["XP"] += xp_gained
                            Statistics["Gold Earned"] += gold_gained
                            print(f"\n",Enemy1["Type"]," has been killed\n\n")
                            print(gold_gained ,"Gold has been gained\n\n")
                            percentage = random.random()
                            if percentage >= 0.7:
                                drop = random.choice(Enemy1["Drop"])
                                if drop in inventory:
                                    inventory[drop] += 1
                                else:
                                    inventory[drop] = 1
                                print(f"{drop} was dropped\n\n")
                            print(xp_gained ,"XP has been gained\n")
                            
                            check1 = False
                            Statistics["Enemies Killed"] += 1
                            if Skill_Tree["General"]["Bloodthirsty"]["Status"] == "(Unlocked)":
                                Health_Gained = (round(Player_copy["Health"] * 0.25))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                                print("\n You activate the bloodthirsty skill\n\n You gain 25% of your max health")
                            if Skill_Tree["General"]["Momentum"]["Status"] == "(Unlocked)":
                                Player_copy["Health"] * round(Player_copy["Speed"] * 0.1)
                                print("\n You activate the momentum skill\n\n You gain 10% more speed")
                        

                        
                    if b == 3:    
                        if (Enemy1["Health"] <= 0) and (Enemy2["Health"] <= 0) and (Enemy3["Health"] <= 0):
                            Battle_End = True
                            Outcome = "Player Win"
                            if Player_Copy["Health"] == Player_copy["Max Health"]:
                                Statistics["Damageless Battles Won"] += 1
                            if "Greatsword" in Gear["Type"]:
                                Amount_Used["Greatsword"] += 1
                                if Amount_Used["Greatsword"] == 100:
                                    Proficiency["Greatsword"] = "Rookie"
                                if Amount_Used["Greatsword"] == 500:
                                    Proficiency["Greatsword"] = "Competent"
                                if Amount_Used["Greatsword"] == 1000:
                                    Proficiency["Greatsword"] = "Proficient"
                                if Amount_Used["Greatsword"] == 2500:
                                    Proficiency["Greatsword"] = "Expert"
                                if Amount_Used["Greatsword"] == 10000:
                                    Proficiency["Greatsword"] = "Master"
                            elif "Sword" in Gear["Type"]:
                                Amount_Used["Sword"] += 1
                                if Amount_Used["Sword"] == 100:
                                    Proficiency["Sword"] = "Rookie"
                                if Amount_Used["Sword"] == 500:
                                    Proficiency["Sword"] = "Competent"
                                if Amount_Used["Sword"] == 1000:
                                    Proficiency["Sword"] = "Proficient"
                                if Amount_Used["Sword"] == 2500:
                                    Proficiency["Sword"] = "Expert"
                                if Amount_Used["Sword"] == 10000:
                                    Proficiency["Sword"] = "Master"
                            elif "Spear" in Gear["Type"]:
                                Amount_Used["Spear"] += 1
                                if Amount_Used["Spear"] == 100:
                                    Proficiency["Spear"] = "Rookie"
                                if Amount_Used["Spear"] == 500:
                                    Proficiency["Spear"] = "Competent"
                                if Amount_Used["Spear"] == 1000:
                                    Proficiency["Spear"] = "Proficient"
                                if Amount_Used["Spear"] == 2500:
                                    Proficiency["Spear"] = "Expert"
                                if Amount_Used["Spear"] == 10000:
                                    Proficiency["Spear"] = "Master"
                            elif "Mace" in Gear["Type"]:
                                Amount_Used["Mace"] += 1
                                if Amount_Used["Mace"] == 100:
                                    Proficiency["Mace"] = "Rookie"
                                if Amount_Used["Mace"] == 500:
                                    Proficiency["Mace"] = "Competent"
                                if Amount_Used["Mace"] == 1000:
                                    Proficiency["Mace"] = "Proficient"
                                if Amount_Used["Mace"] == 2500:
                                    Proficiency["Mace"] = "Expert"
                                if Amount_Used["Mace"] == 10000:
                                    Proficiency["Mace"] = "Master"
                            elif "Dagger" in Gear["Type"]:
                                Amount_Used["Dagger"] += 1
                                if Amount_Used["Dagger"] == 100:
                                    Proficiency["Dagger"] = "Rookie"
                                if Amount_Used["Dagger"] == 500:
                                    Proficiency["Dagger"] = "Competent"
                                if Amount_Used["Dagger"] == 1000:
                                    Proficiency["Dagger"] = "Proficient"
                                if Amount_Used["Dagger"] == 2500:
                                    Proficiency["Dagger"] = "Expert"
                                if Amount_Used["Dagger"] == 10000:
                                    Proficiency["Dagger"] = "Master"
                            elif "Axe" in Gear["Type"]:
                                Amount_Used["Axe"] += 1
                                if Amount_Used["Axe"] == 100:
                                    Proficiency["Axe"] = "Rookie"
                                if Amount_Used["Axe"] == 500:
                                    Proficiency["Axe"] = "Competent"
                                if Amount_Used["Axe"] == 1000:
                                    Proficiency["Axe"] = "Proficient"
                                if Amount_Used["Axe"] == 2500:
                                    Proficiency["Axe"] = "Expert"
                                if Amount_Used["Axe"] == 10000:
                                    Proficiency["Axe"] = "Master"
                            elif "Bow" in Gear["Type"]:
                                Amount_Used["Bow"] += 1
                                if Amount_Used["Bow"] == 100:
                                    Proficiency["Bow"] = "Rookie"
                                if Amount_Used["Bow"] == 500:
                                    Proficiency["Bow"] = "Competent"
                                if Amount_Used["Bow"] == 1000:
                                    Proficiency["Bow"] = "Proficient"
                                if Amount_Used["Bow"] == 2500:
                                    Proficiency["Bow"] = "Expert"
                                if Amount_Used["Bow"] == 10000:
                                    Proficiency["Bow"] = "Master"
                            elif "Wand" in Gear["Type"]:
                                Amount_Used["Wand"] += 1
                                if Amount_Used["Wand"] == 100:
                                    Proficiency["Wand"] = "Rookie"
                                if Amount_Used["Wand"] == 500:
                                    Proficiency["Wand"] = "Competent"
                                if Amount_Used["Wand"] == 1000:
                                    Proficiency["Wand"] = "Proficient"
                                if Amount_Used["Wand"] == 2500:
                                    Proficiency["Wand"] = "Expert"
                                if Amount_Used["Wand"] == 10000:
                                    Proficiency["Wand"] = "Master"
                            elif "Staff" in Gear["Type"]:
                                Amount_Used["Staff"] += 1
                                if Amount_Used["Staff"] == 100:
                                    Proficiency["Staff"] = "Rookie"
                                if Amount_Used["Staff"] == 500:
                                    Proficiency["Staff"] = "Competent"
                                if Amount_Used["Staff"] == 1000:
                                    Proficiency["Staff"] = "Proficient"
                                if Amount_Used["Staff"] == 2500:
                                    Proficiency["Staff"] = "Expert"
                                if Amount_Used["Staff"] == 10000:
                                    Proficiency["Staff"] = "Master"
                            probability = random.random()
                            if probability <= treasure_chance:
                                u = random.random()
                                if u <= 0.1:
                                    award = random.choice(Chest_items["Skill Books"])
                                    if award == "Fireball":
                                        Skill_Books["Fireball"] = True
                                    elif award == "Ice Shard":
                                        Skill_Books["Ice Shard"] = True
                                    elif award == "Shock":
                                        Skill_Books["Shock"] = True
                                    elif award == "Heal":
                                        Skill_Books["Heal"] = True
                                    elif award == "Analysis":
                                        Skill_Books["Analysis"] = True
                                    elif award == "River Fist":
                                        Skill_Books["River Fist"] = True
                                    elif award == "Purify":
                                        Skill_Books["Purify"] = True
                                    elif award == "Grappling Vines":
                                        Skill_Books["Grappling Vines"] = True
                                    elif award == "Domination":
                                        Skill_Books["Domination"] = True
                                    elif award == "Toxin Spray":
                                        Skill_Books["Toxin Spray"] = True
                                    elif award == "Life Drain":
                                        Skill_Books["Life Drain"] = True
                                    elif award == "Devour Essence":
                                        Skill_Books["Devour Essence"] = True
                                    elif award == "Empower":
                                        Skill_Books["Empower"] = True
                                    elif award == "Tremor":
                                        Skill_Books["Tremor"] = True
                                    elif award == "Corrupting Touch":
                                        Skill_Books["Corrupting Touch"] = True
                                    elif award == "Stone Slipstream":
                                        Skill_Books["Stone Slipstream"] = True
                                    elif award == "Mud Shot":
                                        Skill_Books["Mud Shot"] = True
                                    elif award == "Groundbreaker":
                                        Skill_Books["Groundbreaker"] = True
                                    elif award == "Spinning Back Kick":
                                        Skill_Books["Spinning Back Kick"] = True
                                    elif award == "Axe Kick":
                                        Skill_Books["Axe Kick"] = True
                                    elif award == "Headbutt":
                                        Skill_Books["Headbutt"] = True
                                elif u > 0.1 and u <= 0.4:
                                    award = random.choice(["Copper Dagger","Crude Staff","Copper Helmet","Copper Chestplate","Copper Sword","Copper Axe","Copper Mace","Copper Spear","Copper Greatsword","Copper Bow","Copper Shield","Twig Wand","Copper Shoulder Guards","Copper Gardbrace","Copper Greaves","Copper Boots"])
                                    if ("Copper Dagger" not in inventory["Gear"] and award == "Copper Dagger"):
                                        inventory["Gear"].append("Copper Dagger")
                                        print("Copper Dagger Acquired!")
                                    elif ("Crude Staff" not in inventory["Gear"] and award == "Crude Staff"):
                                        inventory["Gear"].append("Crude Staff")
                                        print("Crude Staff Acquired!")
                                    elif ("Copper Helmet" not in inventory["Gear"] and award == "Copper Helmet"):
                                        inventory["Gear"].append("Copper Helmet")
                                        print("Copper Helmet Acquired!")
                                    elif ("Copper Chestplate" not in inventory["Gear"] and award == "Copper Chestplate"):
                                        inventory["Gear"].append("Copper Chestplate")
                                        print("Copper Chestplate Acquired!")
                                    elif ("Copper Sword" not in inventory["Gear"] and award == "Copper Sword"):
                                        inventory["Gear"].append("Copper Sword")
                                        print("Copper Sword Acquired!")
                                    elif ("Copper Axe" not in inventory["Gear"] and award == "Copper Axe"):
                                        inventory["Gear"].append("Copper Axe")
                                        print("Copper Axe Acquired!")
                                    elif ("Copper Mace" not in inventory["Gear"] and award == "Copper Mace"):
                                        inventory["Gear"].append("Copper Mace")
                                        print("Copper Mace Acquired!")
                                    elif ("Copper Spear" not in inventory["Gear"] and award == "Copper Spear"):
                                        inventory["Gear"].append("Copper Spear")
                                        print("Copper Spear Acquired!")
                                    elif ("Copper Greatsword" not in inventory["Gear"] and award == "Copper Greatsword"):
                                        inventory["Gear"].append("Copper Greatsword")
                                        print("Copper Greatsword Acquired!")
                                    elif ("Copper Bow" not in inventory["Gear"] and award == "Copper Bow"):
                                        inventory["Gear"].append("Copper Bow")
                                        print("Copper Bow Acquired!")
                                    elif ("Copper Shield" not in inventory["Gear"] and award == "Copper Shield"):
                                        inventory["Gear"].append("Copper Shield")
                                        print("Copper Shield Acquired!")
                                    elif ("Twig Wand" not in inventory["Gear"] and award == "Twig Wand"):
                                        inventory["Gear"].append("Twig Wand")
                                        print("Twig Wand Acquired!")
                                    elif ("Copper Shoulder Guards" not in inventory["Gear"] and award == "Copper Shoulder Guards"):
                                        inventory["Gear"].append("Copper Shoulder Guards")
                                        print("Copper Shoulder Guards Acquired!")
                                    elif ("Copper Gardbrace" not in inventory["Gear"] and award == "Copper Gardbrace"):
                                        inventory["Gear"].append("Copper Gardbrace")
                                        print("Copper Gardbrace Acquired!")
                                    elif ("Copper Greaves" not in inventory["Gear"] and award == "Copper Greaves"):
                                        inventory["Gear"].append("Copper Greaves")
                                        print("Copper Greaves Acquired!")
                                    elif ("Copper Boots" not in inventory["Gear"] and award == "Copper Boots"):
                                        inventory["Gear"].append("Copper Boots")
                                        print("Copper Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                elif u > 0.4 and u <= 0.7:
                                    award = random.choice(["Bronze Dagger","Carved Staff","Bronze Helmet","Bronze Chestplate","Bronze Sword","Bronze Axe","Bronze Mace","Bronze Spear","Bronze Greatsword","Bronze Bow","Bronze Shield","Carved Wand","Bronze Shoulder Guards","Bronze Gardbrace","Bronze Greaves","Bronze Boots"])
                                    if ("Bronze Dagger" not in inventory["Gear"] and award == "Bronze Dagger"):
                                        inventory["Gear"].append("Bronze Dagger")
                                        print("Bronze Dagger Acquired!")
                                    elif ("Carved Staff" not in inventory["Gear"] and award == "Carved Staff"):
                                        inventory["Gear"].append("Carved Staff")
                                        print("Carved Staff Acquired!")
                                    elif ("Bronze Helmet" not in inventory["Gear"] and award == "Bronze Helmet"):
                                        inventory["Gear"].append("Bronze Helmet")
                                        print("Bronze Helmet Acquired!")
                                    elif ("Bronze Chestplate" not in inventory["Gear"] and award == "Bronze Chestplate"):
                                        inventory["Gear"].append("Bronze Chestplate")
                                        print("Bronze Chestplate Acquired!")
                                    elif ("Bronze Sword" not in inventory["Gear"] and award == "Bronze Sword"):
                                        inventory["Gear"].append("Bronze Sword")
                                        print("Bronze Sword Acquired!")
                                    elif ("Bronze Axe" not in inventory["Gear"] and award == "Bronze Axe"):
                                        inventory["Gear"].append("Bronze Axe")
                                        print("Bronze Axe Acquired!")
                                    elif ("Bronze Mace" not in inventory["Gear"] and award == "Bronze Mace"):
                                        inventory["Gear"].append("Bronze Mace")
                                        print("Bronze Mace Acquired!")
                                    elif ("Bronze Spear" not in inventory["Gear"] and award == "Bronze Spear"):
                                        inventory["Gear"].append("Bronze Spear")
                                        print("Bronze Spear Acquired!")
                                    elif ("Bronze Greatsword" not in inventory["Gear"] and award == "Bronze Greatsword"):
                                        inventory["Gear"].append("Bronze Greatsword")
                                        print("Bronze Greatsword Acquired!")
                                    elif ("Bronze Bow" not in inventory["Gear"] and award == "Bronze Bow"):
                                        inventory["Gear"].append("Bronze Bow")
                                        print("Bronze Bow Acquired!")
                                    elif ("Bronze Shield" not in inventory["Gear"] and award == "Bronze Shield"):
                                        inventory["Gear"].append("Bronze Shield")
                                        print("Bronze Shield Acquired!")
                                    elif ("Carved Wand" not in inventory["Gear"] and award == "Carved Wand"):
                                        inventory["Gear"].append("Carved Wand")
                                        print("Carved Wand Acquired!")
                                    elif ("Bronze Shoulder Guards" not in inventory["Gear"] and award == "Bronze Shoulder Guards"):
                                        inventory["Gear"].append("Bronze Shoulder Guards")
                                        print("Bronze Shoulder Guards Acquired!")
                                    elif ("Bronze Gardbrace" not in inventory["Gear"] and award == "Bronze Gardbrace"):
                                        inventory["Gear"].append("Bronze Gardbrace")
                                        print("Bronze Gardbrace Acquired!")
                                    elif ("Bronze Greaves" not in inventory["Gear"] and award == "Bronze Greaves"):
                                        inventory["Gear"].append("Bronze Greaves")
                                        print("Bronze Greaves Acquired!")
                                    elif ("Bronze Boots" not in inventory["Gear"] and award == "Bronze Boots"):
                                        inventory["Gear"].append("Bronze Boots")
                                        print("Bronze Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                else:
                                    award = random.choice(["Iron Dagger","Runed Staff","Iron Helmet","Iron Chestplate","Iron Sword","Iron Axe","Iron Mace","Iron Spear","Iron Greatsword","Iron Bow","Iron Shield","Crystal Wand","Iron Shoulder Guards","Iron Gardbrace","Iron Greaves","Iron Boots"])
                                    if ("Iron Dagger" not in inventory["Gear"] and award == "Iron Dagger"):
                                        inventory["Gear"].append("Iron Dagger")
                                        print("Iron Dagger Acquired!")
                                    elif ("Runed Staff" not in inventory["Gear"] and award == "Runed Staff"):
                                        inventory["Gear"].append("Runed Staff")
                                        print("Runed Staff Acquired!")
                                    elif ("Iron Helmet" not in inventory["Gear"] and award == "Iron Helmet"):
                                        inventory["Gear"].append("Iron Helmet")
                                        print("Iron Helmet Acquired!")
                                    elif ("Iron Chestplate" not in inventory["Gear"] and award == "Iron Chestplate"):
                                        inventory["Gear"].append("Iron Chestplate")
                                        print("Iron Chestplate Acquired!")
                                    elif ("Iron Sword" not in inventory["Gear"] and award == "Iron Sword"):
                                        inventory["Gear"].append("Iron Sword")
                                        print("Iron Sword Acquired!")
                                    elif ("Iron Axe" not in inventory["Gear"] and award == "Iron Axe"):
                                        inventory["Gear"].append("Iron Axe")
                                        print("Iron Axe Acquired!")
                                    elif ("Iron Mace" not in inventory["Gear"] and award == "Iron Mace"):
                                        inventory["Gear"].append("Iron Mace")
                                        print("Iron Mace Acquired!")
                                    elif ("Iron Spear" not in inventory["Gear"] and award == "Iron Spear"):
                                        inventory["Gear"].append("Iron Spear")
                                        print("Iron Spear Acquired!")
                                    elif ("Iron Greatsword" not in inventory["Gear"] and award == "Iron Greatsword"):
                                        inventory["Gear"].append("Iron Greatsword")
                                        print("Iron Greatsword Acquired!")
                                    elif ("Iron Bow" not in inventory["Gear"] and award == "Iron Bow"):
                                        inventory["Gear"].append("Iron Bow")
                                        print("Iron Bow Acquired!")
                                    elif ("Iron Shield" not in inventory["Gear"] and award == "Iron Shield"):
                                        inventory["Gear"].append("Iron Shield")
                                        print("Iron Shield Acquired!")
                                    elif ("Crystal Wand" not in inventory["Gear"] and award == "Crystal Wand"):
                                        inventory["Gear"].append("Crystal Wand")
                                        print("Crystal Wand Acquired!")
                                    elif ("Iron Shoulder Guards" not in inventory["Gear"] and award == "Iron Shoulder Guards"):
                                        inventory["Gear"].append("Iron Shoulder Guards")
                                        print("Iron Shoulder Guards Acquired!")
                                    elif ("Iron Gardbrace" not in inventory["Gear"] and award == "Iron Gardbrace"):
                                        inventory["Gear"].append("Iron Gardbrace")
                                        print("Iron Gardbrace Acquired!")
                                    elif ("Iron Greaves" not in inventory["Gear"] and award == "Iron Greaves"):
                                        inventory["Gear"].append("Iron Greaves")
                                        print("Iron Greaves Acquired!")
                                    elif ("Iron Boots" not in inventory["Gear"] and award == "Iron Boots"):
                                        inventory["Gear"].append("Iron Boots")
                                        print("Iron Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                            continue
                    elif b == 2:
                        if (Enemy1["Health"] <= 0) and (Enemy2["Health"] <= 0):
                            Battle_End = True
                            Outcome = "Player Win"
                            if Player_Copy["Health"] == Player_copy["Max Health"]:
                                Statistics["Damageless Battles Won"] += 1
                            if "Greatsword" in Gear["Type"]:
                                Amount_Used["Greatsword"] += 1
                                if Amount_Used["Greatsword"] == 100:
                                    Proficiency["Greatsword"] = "Rookie"
                                if Amount_Used["Greatsword"] == 500:
                                    Proficiency["Greatsword"] = "Competent"
                                if Amount_Used["Greatsword"] == 1000:
                                    Proficiency["Greatsword"] = "Proficient"
                                if Amount_Used["Greatsword"] == 2500:
                                    Proficiency["Greatsword"] = "Expert"
                                if Amount_Used["Greatsword"] == 10000:
                                    Proficiency["Greatsword"] = "Master"
                            elif "Sword" in Gear["Type"]:
                                Amount_Used["Sword"] += 1
                                if Amount_Used["Sword"] == 100:
                                    Proficiency["Sword"] = "Rookie"
                                if Amount_Used["Sword"] == 500:
                                    Proficiency["Sword"] = "Competent"
                                if Amount_Used["Sword"] == 1000:
                                    Proficiency["Sword"] = "Proficient"
                                if Amount_Used["Sword"] == 2500:
                                    Proficiency["Sword"] = "Expert"
                                if Amount_Used["Sword"] == 10000:
                                    Proficiency["Sword"] = "Master"
                            elif "Spear" in Gear["Type"]:
                                Amount_Used["Spear"] += 1
                                if Amount_Used["Spear"] == 100:
                                    Proficiency["Spear"] = "Rookie"
                                if Amount_Used["Spear"] == 500:
                                    Proficiency["Spear"] = "Competent"
                                if Amount_Used["Spear"] == 1000:
                                    Proficiency["Spear"] = "Proficient"
                                if Amount_Used["Spear"] == 2500:
                                    Proficiency["Spear"] = "Expert"
                                if Amount_Used["Spear"] == 10000:
                                    Proficiency["Spear"] = "Master"
                            elif "Mace" in Gear["Type"]:
                                Amount_Used["Mace"] += 1
                                if Amount_Used["Mace"] == 100:
                                    Proficiency["Mace"] = "Rookie"
                                if Amount_Used["Mace"] == 500:
                                    Proficiency["Mace"] = "Competent"
                                if Amount_Used["Mace"] == 1000:
                                    Proficiency["Mace"] = "Proficient"
                                if Amount_Used["Mace"] == 2500:
                                    Proficiency["Mace"] = "Expert"
                                if Amount_Used["Mace"] == 10000:
                                    Proficiency["Mace"] = "Master"
                            elif "Dagger" in Gear["Type"]:
                                Amount_Used["Dagger"] += 1
                                if Amount_Used["Dagger"] == 100:
                                    Proficiency["Dagger"] = "Rookie"
                                if Amount_Used["Dagger"] == 500:
                                    Proficiency["Dagger"] = "Competent"
                                if Amount_Used["Dagger"] == 1000:
                                    Proficiency["Dagger"] = "Proficient"
                                if Amount_Used["Dagger"] == 2500:
                                    Proficiency["Dagger"] = "Expert"
                                if Amount_Used["Dagger"] == 10000:
                                    Proficiency["Dagger"] = "Master"
                            elif "Axe" in Gear["Type"]:
                                Amount_Used["Axe"] += 1
                                if Amount_Used["Axe"] == 100:
                                    Proficiency["Axe"] = "Rookie"
                                if Amount_Used["Axe"] == 500:
                                    Proficiency["Axe"] = "Competent"
                                if Amount_Used["Axe"] == 1000:
                                    Proficiency["Axe"] = "Proficient"
                                if Amount_Used["Axe"] == 2500:
                                    Proficiency["Axe"] = "Expert"
                                if Amount_Used["Axe"] == 10000:
                                    Proficiency["Axe"] = "Master"
                            elif "Bow" in Gear["Type"]:
                                Amount_Used["Bow"] += 1
                                if Amount_Used["Bow"] == 100:
                                    Proficiency["Bow"] = "Rookie"
                                if Amount_Used["Bow"] == 500:
                                    Proficiency["Bow"] = "Competent"
                                if Amount_Used["Bow"] == 1000:
                                    Proficiency["Bow"] = "Proficient"
                                if Amount_Used["Bow"] == 2500:
                                    Proficiency["Bow"] = "Expert"
                                if Amount_Used["Bow"] == 10000:
                                    Proficiency["Bow"] = "Master"
                            elif "Wand" in Gear["Type"]:
                                Amount_Used["Wand"] += 1
                                if Amount_Used["Wand"] == 100:
                                    Proficiency["Wand"] = "Rookie"
                                if Amount_Used["Wand"] == 500:
                                    Proficiency["Wand"] = "Competent"
                                if Amount_Used["Wand"] == 1000:
                                    Proficiency["Wand"] = "Proficient"
                                if Amount_Used["Wand"] == 2500:
                                    Proficiency["Wand"] = "Expert"
                                if Amount_Used["Wand"] == 10000:
                                    Proficiency["Wand"] = "Master"
                            elif "Staff" in Gear["Type"]:
                                Amount_Used["Staff"] += 1
                                if Amount_Used["Staff"] == 100:
                                    Proficiency["Staff"] = "Rookie"
                                if Amount_Used["Staff"] == 500:
                                    Proficiency["Staff"] = "Competent"
                                if Amount_Used["Staff"] == 1000:
                                    Proficiency["Staff"] = "Proficient"
                                if Amount_Used["Staff"] == 2500:
                                    Proficiency["Staff"] = "Expert"
                                if Amount_Used["Staff"] == 10000:
                                    Proficiency["Staff"] = "Master"
                            probability = random.random()
                            if probability <= treasure_chance:
                                u = random.random()
                                if u <= 0.1:
                                    award = random.choice(Chest_items["Skill Books"])
                                    if award == "Fireball":
                                        Skill_Books["Fireball"] = True
                                    elif award == "Ice Shard":
                                        Skill_Books["Ice Shard"] = True
                                    elif award == "Shock":
                                        Skill_Books["Shock"] = True
                                    elif award == "Heal":
                                        Skill_Books["Heal"] = True
                                    elif award == "Analysis":
                                        Skill_Books["Analysis"] = True
                                    elif award == "River Fist":
                                        Skill_Books["River Fist"] = True
                                    elif award == "Purify":
                                        Skill_Books["Purify"] = True
                                    elif award == "Grappling Vines":
                                        Skill_Books["Grappling Vines"] = True
                                    elif award == "Domination":
                                        Skill_Books["Domination"] = True
                                    elif award == "Toxin Spray":
                                        Skill_Books["Toxin Spray"] = True
                                    elif award == "Life Drain":
                                        Skill_Books["Life Drain"] = True
                                    elif award == "Devour Essence":
                                        Skill_Books["Devour Essence"] = True
                                    elif award == "Empower":
                                        Skill_Books["Empower"] = True
                                    elif award == "Tremor":
                                        Skill_Books["Tremor"] = True
                                    elif award == "Corrupting Touch":
                                        Skill_Books["Corrupting Touch"] = True
                                    elif award == "Stone Slipstream":
                                        Skill_Books["Stone Slipstream"] = True
                                    elif award == "Mud Shot":
                                        Skill_Books["Mud Shot"] = True
                                    elif award == "Groundbreaker":
                                        Skill_Books["Groundbreaker"] = True
                                    elif award == "Spinning Back Kick":
                                        Skill_Books["Spinning Back Kick"] = True
                                    elif award == "Axe Kick":
                                        Skill_Books["Axe Kick"] = True
                                    elif award == "Headbutt":
                                        Skill_Books["Headbutt"] = True
                                elif u > 0.1 and u <= 0.4:
                                    award = random.choice(["Copper Dagger","Crude Staff","Copper Helmet","Copper Chestplate","Copper Sword","Copper Axe","Copper Mace","Copper Spear","Copper Greatsword","Copper Bow","Copper Shield","Twig Wand","Copper Shoulder Guards","Copper Gardbrace","Copper Greaves","Copper Boots"])
                                    if ("Copper Dagger" not in inventory["Gear"] and award == "Copper Dagger"):
                                        inventory["Gear"].append("Copper Dagger")
                                        print("Copper Dagger Acquired!")
                                    elif ("Crude Staff" not in inventory["Gear"] and award == "Crude Staff"):
                                        inventory["Gear"].append("Crude Staff")
                                        print("Crude Staff Acquired!")
                                    elif ("Copper Helmet" not in inventory["Gear"] and award == "Copper Helmet"):
                                        inventory["Gear"].append("Copper Helmet")
                                        print("Copper Helmet Acquired!")
                                    elif ("Copper Chestplate" not in inventory["Gear"] and award == "Copper Chestplate"):
                                        inventory["Gear"].append("Copper Chestplate")
                                        print("Copper Chestplate Acquired!")
                                    elif ("Copper Sword" not in inventory["Gear"] and award == "Copper Sword"):
                                        inventory["Gear"].append("Copper Sword")
                                        print("Copper Sword Acquired!")
                                    elif ("Copper Axe" not in inventory["Gear"] and award == "Copper Axe"):
                                        inventory["Gear"].append("Copper Axe")
                                        print("Copper Axe Acquired!")
                                    elif ("Copper Mace" not in inventory["Gear"] and award == "Copper Mace"):
                                        inventory["Gear"].append("Copper Mace")
                                        print("Copper Mace Acquired!")
                                    elif ("Copper Spear" not in inventory["Gear"] and award == "Copper Spear"):
                                        inventory["Gear"].append("Copper Spear")
                                        print("Copper Spear Acquired!")
                                    elif ("Copper Greatsword" not in inventory["Gear"] and award == "Copper Greatsword"):
                                        inventory["Gear"].append("Copper Greatsword")
                                        print("Copper Greatsword Acquired!")
                                    elif ("Copper Bow" not in inventory["Gear"] and award == "Copper Bow"):
                                        inventory["Gear"].append("Copper Bow")
                                        print("Copper Bow Acquired!")
                                    elif ("Copper Shield" not in inventory["Gear"] and award == "Copper Shield"):
                                        inventory["Gear"].append("Copper Shield")
                                        print("Copper Shield Acquired!")
                                    elif ("Twig Wand" not in inventory["Gear"] and award == "Twig Wand"):
                                        inventory["Gear"].append("Twig Wand")
                                        print("Twig Wand Acquired!")
                                    elif ("Copper Shoulder Guards" not in inventory["Gear"] and award == "Copper Shoulder Guards"):
                                        inventory["Gear"].append("Copper Shoulder Guards")
                                        print("Copper Shoulder Guards Acquired!")
                                    elif ("Copper Gardbrace" not in inventory["Gear"] and award == "Copper Gardbrace"):
                                        inventory["Gear"].append("Copper Gardbrace")
                                        print("Copper Gardbrace Acquired!")
                                    elif ("Copper Greaves" not in inventory["Gear"] and award == "Copper Greaves"):
                                        inventory["Gear"].append("Copper Greaves")
                                        print("Copper Greaves Acquired!")
                                    elif ("Copper Boots" not in inventory["Gear"] and award == "Copper Boots"):
                                        inventory["Gear"].append("Copper Boots")
                                        print("Copper Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                elif u > 0.4 and u <= 0.7:
                                    award = random.choice(["Bronze Dagger","Carved Staff","Bronze Helmet","Bronze Chestplate","Bronze Sword","Bronze Axe","Bronze Mace","Bronze Spear","Bronze Greatsword","Bronze Bow","Bronze Shield","Carved Wand","Bronze Shoulder Guards","Bronze Gardbrace","Bronze Greaves","Bronze Boots"])
                                    if ("Bronze Dagger" not in inventory["Gear"] and award == "Bronze Dagger"):
                                        inventory["Gear"].append("Bronze Dagger")
                                        print("Bronze Dagger Acquired!")
                                    elif ("Carved Staff" not in inventory["Gear"] and award == "Carved Staff"):
                                        inventory["Gear"].append("Carved Staff")
                                        print("Carved Staff Acquired!")
                                    elif ("Bronze Helmet" not in inventory["Gear"] and award == "Bronze Helmet"):
                                        inventory["Gear"].append("Bronze Helmet")
                                        print("Bronze Helmet Acquired!")
                                    elif ("Bronze Chestplate" not in inventory["Gear"] and award == "Bronze Chestplate"):
                                        inventory["Gear"].append("Bronze Chestplate")
                                        print("Bronze Chestplate Acquired!")
                                    elif ("Bronze Sword" not in inventory["Gear"] and award == "Bronze Sword"):
                                        inventory["Gear"].append("Bronze Sword")
                                        print("Bronze Sword Acquired!")
                                    elif ("Bronze Axe" not in inventory["Gear"] and award == "Bronze Axe"):
                                        inventory["Gear"].append("Bronze Axe")
                                        print("Bronze Axe Acquired!")
                                    elif ("Bronze Mace" not in inventory["Gear"] and award == "Bronze Mace"):
                                        inventory["Gear"].append("Bronze Mace")
                                        print("Bronze Mace Acquired!")
                                    elif ("Bronze Spear" not in inventory["Gear"] and award == "Bronze Spear"):
                                        inventory["Gear"].append("Bronze Spear")
                                        print("Bronze Spear Acquired!")
                                    elif ("Bronze Greatsword" not in inventory["Gear"] and award == "Bronze Greatsword"):
                                        inventory["Gear"].append("Bronze Greatsword")
                                        print("Bronze Greatsword Acquired!")
                                    elif ("Bronze Bow" not in inventory["Gear"] and award == "Bronze Bow"):
                                        inventory["Gear"].append("Bronze Bow")
                                        print("Bronze Bow Acquired!")
                                    elif ("Bronze Shield" not in inventory["Gear"] and award == "Bronze Shield"):
                                        inventory["Gear"].append("Bronze Shield")
                                        print("Bronze Shield Acquired!")
                                    elif ("Carved Wand" not in inventory["Gear"] and award == "Carved Wand"):
                                        inventory["Gear"].append("Carved Wand")
                                        print("Carved Wand Acquired!")
                                    elif ("Bronze Shoulder Guards" not in inventory["Gear"] and award == "Bronze Shoulder Guards"):
                                        inventory["Gear"].append("Bronze Shoulder Guards")
                                        print("Bronze Shoulder Guards Acquired!")
                                    elif ("Bronze Gardbrace" not in inventory["Gear"] and award == "Bronze Gardbrace"):
                                        inventory["Gear"].append("Bronze Gardbrace")
                                        print("Bronze Gardbrace Acquired!")
                                    elif ("Bronze Greaves" not in inventory["Gear"] and award == "Bronze Greaves"):
                                        inventory["Gear"].append("Bronze Greaves")
                                        print("Bronze Greaves Acquired!")
                                    elif ("Bronze Boots" not in inventory["Gear"] and award == "Bronze Boots"):
                                        inventory["Gear"].append("Bronze Boots")
                                        print("Bronze Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                else:
                                    award = random.choice(["Iron Dagger","Runed Staff","Iron Helmet","Iron Chestplate","Iron Sword","Iron Axe","Iron Mace","Iron Spear","Iron Greatsword","Iron Bow","Iron Shield","Crystal Wand","Iron Shoulder Guards","Iron Gardbrace","Iron Greaves","Iron Boots"])
                                    if ("Iron Dagger" not in inventory["Gear"] and award == "Iron Dagger"):
                                        inventory["Gear"].append("Iron Dagger")
                                        print("Iron Dagger Acquired!")
                                    elif ("Runed Staff" not in inventory["Gear"] and award == "Runed Staff"):
                                        inventory["Gear"].append("Runed Staff")
                                        print("Runed Staff Acquired!")
                                    elif ("Iron Helmet" not in inventory["Gear"] and award == "Iron Helmet"):
                                        inventory["Gear"].append("Iron Helmet")
                                        print("Iron Helmet Acquired!")
                                    elif ("Iron Chestplate" not in inventory["Gear"] and award == "Iron Chestplate"):
                                        inventory["Gear"].append("Iron Chestplate")
                                        print("Iron Chestplate Acquired!")
                                    elif ("Iron Sword" not in inventory["Gear"] and award == "Iron Sword"):
                                        inventory["Gear"].append("Iron Sword")
                                        print("Iron Sword Acquired!")
                                    elif ("Iron Axe" not in inventory["Gear"] and award == "Iron Axe"):
                                        inventory["Gear"].append("Iron Axe")
                                        print("Iron Axe Acquired!")
                                    elif ("Iron Mace" not in inventory["Gear"] and award == "Iron Mace"):
                                        inventory["Gear"].append("Iron Mace")
                                        print("Iron Mace Acquired!")
                                    elif ("Iron Spear" not in inventory["Gear"] and award == "Iron Spear"):
                                        inventory["Gear"].append("Iron Spear")
                                        print("Iron Spear Acquired!")
                                    elif ("Iron Greatsword" not in inventory["Gear"] and award == "Iron Greatsword"):
                                        inventory["Gear"].append("Iron Greatsword")
                                        print("Iron Greatsword Acquired!")
                                    elif ("Iron Bow" not in inventory["Gear"] and award == "Iron Bow"):
                                        inventory["Gear"].append("Iron Bow")
                                        print("Iron Bow Acquired!")
                                    elif ("Iron Shield" not in inventory["Gear"] and award == "Iron Shield"):
                                        inventory["Gear"].append("Iron Shield")
                                        print("Iron Shield Acquired!")
                                    elif ("Crystal Wand" not in inventory["Gear"] and award == "Crystal Wand"):
                                        inventory["Gear"].append("Crystal Wand")
                                        print("Crystal Wand Acquired!")
                                    elif ("Iron Shoulder Guards" not in inventory["Gear"] and award == "Iron Shoulder Guards"):
                                        inventory["Gear"].append("Iron Shoulder Guards")
                                        print("Iron Shoulder Guards Acquired!")
                                    elif ("Iron Gardbrace" not in inventory["Gear"] and award == "Iron Gardbrace"):
                                        inventory["Gear"].append("Iron Gardbrace")
                                        print("Iron Gardbrace Acquired!")
                                    elif ("Iron Greaves" not in inventory["Gear"] and award == "Iron Greaves"):
                                        inventory["Gear"].append("Iron Greaves")
                                        print("Iron Greaves Acquired!")
                                    elif ("Iron Boots" not in inventory["Gear"] and award == "Iron Boots"):
                                        inventory["Gear"].append("Iron Boots")
                                        print("Iron Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                            continue

                    elif b == 1:
                        if (Enemy1["Health"] <= 0):
                            Battle_End = True
                            Outcome = "Player Win"
                            if Player_Copy["Health"] == Player_copy["Max Health"]:
                                Statistics["Damageless Battles Won"] += 1
                            if "Greatsword" in Gear["Type"]:
                                Amount_Used["Greatsword"] += 1
                                if Amount_Used["Greatsword"] == 100:
                                    Proficiency["Greatsword"] = "Rookie"
                                if Amount_Used["Greatsword"] == 500:
                                    Proficiency["Greatsword"] = "Competent"
                                if Amount_Used["Greatsword"] == 1000:
                                    Proficiency["Greatsword"] = "Proficient"
                                if Amount_Used["Greatsword"] == 2500:
                                    Proficiency["Greatsword"] = "Expert"
                                if Amount_Used["Greatsword"] == 10000:
                                    Proficiency["Greatsword"] = "Master"
                            elif "Sword" in Gear["Type"]:
                                Amount_Used["Sword"] += 1
                                if Amount_Used["Sword"] == 100:
                                    Proficiency["Sword"] = "Rookie"
                                if Amount_Used["Sword"] == 500:
                                    Proficiency["Sword"] = "Competent"
                                if Amount_Used["Sword"] == 1000:
                                    Proficiency["Sword"] = "Proficient"
                                if Amount_Used["Sword"] == 2500:
                                    Proficiency["Sword"] = "Expert"
                                if Amount_Used["Sword"] == 10000:
                                    Proficiency["Sword"] = "Master"
                            elif "Spear" in Gear["Type"]:
                                Amount_Used["Spear"] += 1
                                if Amount_Used["Spear"] == 100:
                                    Proficiency["Spear"] = "Rookie"
                                if Amount_Used["Spear"] == 500:
                                    Proficiency["Spear"] = "Competent"
                                if Amount_Used["Spear"] == 1000:
                                    Proficiency["Spear"] = "Proficient"
                                if Amount_Used["Spear"] == 2500:
                                    Proficiency["Spear"] = "Expert"
                                if Amount_Used["Spear"] == 10000:
                                    Proficiency["Spear"] = "Master"
                            elif "Mace" in Gear["Type"]:
                                Amount_Used["Mace"] += 1
                                if Amount_Used["Mace"] == 100:
                                    Proficiency["Mace"] = "Rookie"
                                if Amount_Used["Mace"] == 500:
                                    Proficiency["Mace"] = "Competent"
                                if Amount_Used["Mace"] == 1000:
                                    Proficiency["Mace"] = "Proficient"
                                if Amount_Used["Mace"] == 2500:
                                    Proficiency["Mace"] = "Expert"
                                if Amount_Used["Mace"] == 10000:
                                    Proficiency["Mace"] = "Master"
                            elif "Dagger" in Gear["Type"]:
                                Amount_Used["Dagger"] += 1
                                if Amount_Used["Dagger"] == 100:
                                    Proficiency["Dagger"] = "Rookie"
                                if Amount_Used["Dagger"] == 500:
                                    Proficiency["Dagger"] = "Competent"
                                if Amount_Used["Dagger"] == 1000:
                                    Proficiency["Dagger"] = "Proficient"
                                if Amount_Used["Dagger"] == 2500:
                                    Proficiency["Dagger"] = "Expert"
                                if Amount_Used["Dagger"] == 10000:
                                    Proficiency["Dagger"] = "Master"
                            elif "Axe" in Gear["Type"]:
                                Amount_Used["Axe"] += 1
                                if Amount_Used["Axe"] == 100:
                                    Proficiency["Axe"] = "Rookie"
                                if Amount_Used["Axe"] == 500:
                                    Proficiency["Axe"] = "Competent"
                                if Amount_Used["Axe"] == 1000:
                                    Proficiency["Axe"] = "Proficient"
                                if Amount_Used["Axe"] == 2500:
                                    Proficiency["Axe"] = "Expert"
                                if Amount_Used["Axe"] == 10000:
                                    Proficiency["Axe"] = "Master"
                            elif "Bow" in Gear["Type"]:
                                Amount_Used["Bow"] += 1
                                if Amount_Used["Bow"] == 100:
                                    Proficiency["Bow"] = "Rookie"
                                if Amount_Used["Bow"] == 500:
                                    Proficiency["Bow"] = "Competent"
                                if Amount_Used["Bow"] == 1000:
                                    Proficiency["Bow"] = "Proficient"
                                if Amount_Used["Bow"] == 2500:
                                    Proficiency["Bow"] = "Expert"
                                if Amount_Used["Bow"] == 10000:
                                    Proficiency["Bow"] = "Master"
                            elif "Wand" in Gear["Type"]:
                                Amount_Used["Wand"] += 1
                                if Amount_Used["Wand"] == 100:
                                    Proficiency["Wand"] = "Rookie"
                                if Amount_Used["Wand"] == 500:
                                    Proficiency["Wand"] = "Competent"
                                if Amount_Used["Wand"] == 1000:
                                    Proficiency["Wand"] = "Proficient"
                                if Amount_Used["Wand"] == 2500:
                                    Proficiency["Wand"] = "Expert"
                                if Amount_Used["Wand"] == 10000:
                                    Proficiency["Wand"] = "Master"
                            elif "Staff" in Gear["Type"]:
                                Amount_Used["Staff"] += 1
                                if Amount_Used["Staff"] == 100:
                                    Proficiency["Staff"] = "Rookie"
                                if Amount_Used["Staff"] == 500:
                                    Proficiency["Staff"] = "Competent"
                                if Amount_Used["Staff"] == 1000:
                                    Proficiency["Staff"] = "Proficient"
                                if Amount_Used["Staff"] == 2500:
                                    Proficiency["Staff"] = "Expert"
                                if Amount_Used["Staff"] == 10000:
                                    Proficiency["Staff"] = "Master"
                            probability = random.random()
                            if probability <= treasure_chance:
                                u = random.random()
                                if u <= 0.1:
                                    award = random.choice(Chest_items["Skill Books"])
                                    if award == "Fireball":
                                        Skill_Books["Fireball"] = True
                                    elif award == "Ice Shard":
                                        Skill_Books["Ice Shard"] = True
                                    elif award == "Shock":
                                        Skill_Books["Shock"] = True
                                    elif award == "Heal":
                                        Skill_Books["Heal"] = True
                                    elif award == "Analysis":
                                        Skill_Books["Analysis"] = True
                                    elif award == "River Fist":
                                        Skill_Books["River Fist"] = True
                                    elif award == "Purify":
                                        Skill_Books["Purify"] = True
                                    elif award == "Grappling Vines":
                                        Skill_Books["Grappling Vines"] = True
                                    elif award == "Domination":
                                        Skill_Books["Domination"] = True
                                    elif award == "Toxin Spray":
                                        Skill_Books["Toxin Spray"] = True
                                    elif award == "Life Drain":
                                        Skill_Books["Life Drain"] = True
                                    elif award == "Devour Essence":
                                        Skill_Books["Devour Essence"] = True
                                    elif award == "Empower":
                                        Skill_Books["Empower"] = True
                                    elif award == "Tremor":
                                        Skill_Books["Tremor"] = True
                                    elif award == "Corrupting Touch":
                                        Skill_Books["Corrupting Touch"] = True
                                    elif award == "Stone Slipstream":
                                        Skill_Books["Stone Slipstream"] = True
                                    elif award == "Mud Shot":
                                        Skill_Books["Mud Shot"] = True
                                    elif award == "Groundbreaker":
                                        Skill_Books["Groundbreaker"] = True
                                    elif award == "Spinning Back Kick":
                                        Skill_Books["Spinning Back Kick"] = True
                                    elif award == "Axe Kick":
                                        Skill_Books["Axe Kick"] = True
                                    elif award == "Headbutt":
                                        Skill_Books["Headbutt"] = True
                                elif u > 0.1 and u <= 0.4:
                                    award = random.choice(["Copper Dagger","Crude Staff","Copper Helmet","Copper Chestplate","Copper Sword","Copper Axe","Copper Mace","Copper Spear","Copper Greatsword","Copper Bow","Copper Shield","Twig Wand","Copper Shoulder Guards","Copper Gardbrace","Copper Greaves","Copper Boots"])
                                    if ("Copper Dagger" not in inventory["Gear"] and award == "Copper Dagger"):
                                        inventory["Gear"].append("Copper Dagger")
                                        print("Copper Dagger Acquired!")
                                    elif ("Crude Staff" not in inventory["Gear"] and award == "Crude Staff"):
                                        inventory["Gear"].append("Crude Staff")
                                        print("Crude Staff Acquired!")
                                    elif ("Copper Helmet" not in inventory["Gear"] and award == "Copper Helmet"):
                                        inventory["Gear"].append("Copper Helmet")
                                        print("Copper Helmet Acquired!")
                                    elif ("Copper Chestplate" not in inventory["Gear"] and award == "Copper Chestplate"):
                                        inventory["Gear"].append("Copper Chestplate")
                                        print("Copper Chestplate Acquired!")
                                    elif ("Copper Sword" not in inventory["Gear"] and award == "Copper Sword"):
                                        inventory["Gear"].append("Copper Sword")
                                        print("Copper Sword Acquired!")
                                    elif ("Copper Axe" not in inventory["Gear"] and award == "Copper Axe"):
                                        inventory["Gear"].append("Copper Axe")
                                        print("Copper Axe Acquired!")
                                    elif ("Copper Mace" not in inventory["Gear"] and award == "Copper Mace"):
                                        inventory["Gear"].append("Copper Mace")
                                        print("Copper Mace Acquired!")
                                    elif ("Copper Spear" not in inventory["Gear"] and award == "Copper Spear"):
                                        inventory["Gear"].append("Copper Spear")
                                        print("Copper Spear Acquired!")
                                    elif ("Copper Greatsword" not in inventory["Gear"] and award == "Copper Greatsword"):
                                        inventory["Gear"].append("Copper Greatsword")
                                        print("Copper Greatsword Acquired!")
                                    elif ("Copper Bow" not in inventory["Gear"] and award == "Copper Bow"):
                                        inventory["Gear"].append("Copper Bow")
                                        print("Copper Bow Acquired!")
                                    elif ("Copper Shield" not in inventory["Gear"] and award == "Copper Shield"):
                                        inventory["Gear"].append("Copper Shield")
                                        print("Copper Shield Acquired!")
                                    elif ("Twig Wand" not in inventory["Gear"] and award == "Twig Wand"):
                                        inventory["Gear"].append("Twig Wand")
                                        print("Twig Wand Acquired!")
                                    elif ("Copper Shoulder Guards" not in inventory["Gear"] and award == "Copper Shoulder Guards"):
                                        inventory["Gear"].append("Copper Shoulder Guards")
                                        print("Copper Shoulder Guards Acquired!")
                                    elif ("Copper Gardbrace" not in inventory["Gear"] and award == "Copper Gardbrace"):
                                        inventory["Gear"].append("Copper Gardbrace")
                                        print("Copper Gardbrace Acquired!")
                                    elif ("Copper Greaves" not in inventory["Gear"] and award == "Copper Greaves"):
                                        inventory["Gear"].append("Copper Greaves")
                                        print("Copper Greaves Acquired!")
                                    elif ("Copper Boots" not in inventory["Gear"] and award == "Copper Boots"):
                                        inventory["Gear"].append("Copper Boots")
                                        print("Copper Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                elif u > 0.4 and u <= 0.7:
                                    award = random.choice(["Bronze Dagger","Carved Staff","Bronze Helmet","Bronze Chestplate","Bronze Sword","Bronze Axe","Bronze Mace","Bronze Spear","Bronze Greatsword","Bronze Bow","Bronze Shield","Carved Wand","Bronze Shoulder Guards","Bronze Gardbrace","Bronze Greaves","Bronze Boots"])
                                    if ("Bronze Dagger" not in inventory["Gear"] and award == "Bronze Dagger"):
                                        inventory["Gear"].append("Bronze Dagger")
                                        print("Bronze Dagger Acquired!")
                                    elif ("Carved Staff" not in inventory["Gear"] and award == "Carved Staff"):
                                        inventory["Gear"].append("Carved Staff")
                                        print("Carved Staff Acquired!")
                                    elif ("Bronze Helmet" not in inventory["Gear"] and award == "Bronze Helmet"):
                                        inventory["Gear"].append("Bronze Helmet")
                                        print("Bronze Helmet Acquired!")
                                    elif ("Bronze Chestplate" not in inventory["Gear"] and award == "Bronze Chestplate"):
                                        inventory["Gear"].append("Bronze Chestplate")
                                        print("Bronze Chestplate Acquired!")
                                    elif ("Bronze Sword" not in inventory["Gear"] and award == "Bronze Sword"):
                                        inventory["Gear"].append("Bronze Sword")
                                        print("Bronze Sword Acquired!")
                                    elif ("Bronze Axe" not in inventory["Gear"] and award == "Bronze Axe"):
                                        inventory["Gear"].append("Bronze Axe")
                                        print("Bronze Axe Acquired!")
                                    elif ("Bronze Mace" not in inventory["Gear"] and award == "Bronze Mace"):
                                        inventory["Gear"].append("Bronze Mace")
                                        print("Bronze Mace Acquired!")
                                    elif ("Bronze Spear" not in inventory["Gear"] and award == "Bronze Spear"):
                                        inventory["Gear"].append("Bronze Spear")
                                        print("Bronze Spear Acquired!")
                                    elif ("Bronze Greatsword" not in inventory["Gear"] and award == "Bronze Greatsword"):
                                        inventory["Gear"].append("Bronze Greatsword")
                                        print("Bronze Greatsword Acquired!")
                                    elif ("Bronze Bow" not in inventory["Gear"] and award == "Bronze Bow"):
                                        inventory["Gear"].append("Bronze Bow")
                                        print("Bronze Bow Acquired!")
                                    elif ("Bronze Shield" not in inventory["Gear"] and award == "Bronze Shield"):
                                        inventory["Gear"].append("Bronze Shield")
                                        print("Bronze Shield Acquired!")
                                    elif ("Carved Wand" not in inventory["Gear"] and award == "Carved Wand"):
                                        inventory["Gear"].append("Carved Wand")
                                        print("Carved Wand Acquired!")
                                    elif ("Bronze Shoulder Guards" not in inventory["Gear"] and award == "Bronze Shoulder Guards"):
                                        inventory["Gear"].append("Bronze Shoulder Guards")
                                        print("Bronze Shoulder Guards Acquired!")
                                    elif ("Bronze Gardbrace" not in inventory["Gear"] and award == "Bronze Gardbrace"):
                                        inventory["Gear"].append("Bronze Gardbrace")
                                        print("Bronze Gardbrace Acquired!")
                                    elif ("Bronze Greaves" not in inventory["Gear"] and award == "Bronze Greaves"):
                                        inventory["Gear"].append("Bronze Greaves")
                                        print("Bronze Greaves Acquired!")
                                    elif ("Bronze Boots" not in inventory["Gear"] and award == "Bronze Boots"):
                                        inventory["Gear"].append("Bronze Boots")
                                        print("Bronze Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                                else:
                                    award = random.choice(["Iron Dagger","Runed Staff","Iron Helmet","Iron Chestplate","Iron Sword","Iron Axe","Iron Mace","Iron Spear","Iron Greatsword","Iron Bow","Iron Shield","Crystal Wand","Iron Shoulder Guards","Iron Gardbrace","Iron Greaves","Iron Boots"])
                                    if ("Iron Dagger" not in inventory["Gear"] and award == "Iron Dagger"):
                                        inventory["Gear"].append("Iron Dagger")
                                        print("Iron Dagger Acquired!")
                                    elif ("Runed Staff" not in inventory["Gear"] and award == "Runed Staff"):
                                        inventory["Gear"].append("Runed Staff")
                                        print("Runed Staff Acquired!")
                                    elif ("Iron Helmet" not in inventory["Gear"] and award == "Iron Helmet"):
                                        inventory["Gear"].append("Iron Helmet")
                                        print("Iron Helmet Acquired!")
                                    elif ("Iron Chestplate" not in inventory["Gear"] and award == "Iron Chestplate"):
                                        inventory["Gear"].append("Iron Chestplate")
                                        print("Iron Chestplate Acquired!")
                                    elif ("Iron Sword" not in inventory["Gear"] and award == "Iron Sword"):
                                        inventory["Gear"].append("Iron Sword")
                                        print("Iron Sword Acquired!")
                                    elif ("Iron Axe" not in inventory["Gear"] and award == "Iron Axe"):
                                        inventory["Gear"].append("Iron Axe")
                                        print("Iron Axe Acquired!")
                                    elif ("Iron Mace" not in inventory["Gear"] and award == "Iron Mace"):
                                        inventory["Gear"].append("Iron Mace")
                                        print("Iron Mace Acquired!")
                                    elif ("Iron Spear" not in inventory["Gear"] and award == "Iron Spear"):
                                        inventory["Gear"].append("Iron Spear")
                                        print("Iron Spear Acquired!")
                                    elif ("Iron Greatsword" not in inventory["Gear"] and award == "Iron Greatsword"):
                                        inventory["Gear"].append("Iron Greatsword")
                                        print("Iron Greatsword Acquired!")
                                    elif ("Iron Bow" not in inventory["Gear"] and award == "Iron Bow"):
                                        inventory["Gear"].append("Iron Bow")
                                        print("Iron Bow Acquired!")
                                    elif ("Iron Shield" not in inventory["Gear"] and award == "Iron Shield"):
                                        inventory["Gear"].append("Iron Shield")
                                        print("Iron Shield Acquired!")
                                    elif ("Crystal Wand" not in inventory["Gear"] and award == "Crystal Wand"):
                                        inventory["Gear"].append("Crystal Wand")
                                        print("Crystal Wand Acquired!")
                                    elif ("Iron Shoulder Guards" not in inventory["Gear"] and award == "Iron Shoulder Guards"):
                                        inventory["Gear"].append("Iron Shoulder Guards")
                                        print("Iron Shoulder Guards Acquired!")
                                    elif ("Iron Gardbrace" not in inventory["Gear"] and award == "Iron Gardbrace"):
                                        inventory["Gear"].append("Iron Gardbrace")
                                        print("Iron Gardbrace Acquired!")
                                    elif ("Iron Greaves" not in inventory["Gear"] and award == "Iron Greaves"):
                                        inventory["Gear"].append("Iron Greaves")
                                        print("Iron Greaves Acquired!")
                                    elif ("Iron Boots" not in inventory["Gear"] and award == "Iron Boots"):
                                        inventory["Gear"].append("Iron Boots")
                                        print("Iron Boots Acquired!")
                                    else:
                                        print("\n\nItem Already Owned\n")
                            continue


                    if fighter == Player_copy:
                        if b >= 1:
                            Fastest_Enemy = Enemy1
                        else:
                            Fastest_Enemy = Fastest_Enemy[0]
                        Turn_Time = Player_copy["Speed"] / Fastest_Enemy["Speed"]
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                    
                            if b >= 3:
                                Player,Player_copy, Enemy1, Enemy2, Enemy3,n, place, player_shadows,x,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,Player_Skip,Turn_Time,Statistics  = Player_Battle.Player3_Battle(Player,Player_copy,Enemy,Enemy1,Enemy2,Enemy3,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,Skill_Tree,Statistics,typewriter,Gold_Multiplier)
                            elif b >= 2:
                                Player,Player_copy, Enemy1, Enemy2,n, place,player_shadows,x,Enemy1_Skip,Enemy2_Skip,Player_Skip,Turn_Time,Statistics  = Player_Battle.Player2_Battle(Player,Player_copy,Enemy,Enemy1,Enemy2,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Enemy2_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Enemy2_Skip,Skill_Tree,Statistics,typewriter,Gold_Multiplier)
                            elif b >= 1:
                                Player,Player_copy, Enemy1,n, place,player_shadows,x,Enemy1_Skip,Player_Skip,Turn_Time,Statistics  = Player_Battle.Player1_Battle(Player,Player_copy,Enemy,Enemy1,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Skill_Tree,Statistics,typewriter,Gold_Multiplier)
                        if Skill_Tree["General"]["Fast Recovery"]["Status"] != "(Unlocked)":
                            Player_copy["Stamina"] += (Player["Stamina"] * 0.1)
                        else:
                            Player_copy["Stamina"] += (Player["Stamina"] * 0.25)
                        Player_copy["Stamina"] = round(Player_copy["Stamina"])

                    if fighter == Enemy3:
                        Turn_Time = Enemy3["Speed"] / Player_copy["Speed"]
                        print(f"\n---------------\n",Enemy3["Type"],"turn\n---------------\n")
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                            if Enemy3["Health"] > 0:
                                Enemy3, Player_copy, Evasion3_Stopper, Defense3_Stopper,Turn_Time,Player_Skip = Enemy3_Battle(Enemy3,Player,Player_copy,Evasion3_Stopper,Defense3_Stopper,name,Game,Turn_Time,Enemy3_Skip,Player_Skip,typewriter)
                        if "Traveler" in Enemy3["Type"]:
                            Enemy3["Stamina"] *= 1.5
                            Enemy3["Stamina"] = round(Enemy3["Stamina"])
                        else:
                            Enemy3["Stamina"] *= 1.1
                            Enemy3["Stamina"] = round(Enemy3["Stamina"])
                        print(f"\n---------------\n Turn End\n---------------\n")

                    if fighter == Enemy2:
                        Turn_Time = Enemy2["Speed"] / Player_copy["Speed"]
                        print(f"\n---------------\n",Enemy2["Type"],"turn\n---------------\n")
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                            if Enemy2["Health"] > 0:
                                Enemy2, Player_copy, Evasion2_Stopper, Defense2_Stopper,Turn_Time,Player_Skip = Enemy2_Battle(Enemy2,Player,Player_copy,Evasion2_Stopper,Defense2_Stopper,name,Game,Turn_Time,Enemy2_Skip,Player_Skip,typewriter)
                        if "Traveler" in Enemy2["Type"]:
                            Enemy2["Stamina"] *= 1.5
                            Enemy2["Stamina"] = round(Enemy2["Stamina"])
                        else:
                            Enemy2["Stamina"] *= 1.1
                            Enemy2["Stamina"] = round(Enemy2["Stamina"])
                        print(f"\n---------------\n Turn End\n---------------\n")
                        
                    if fighter == Enemy1:
                        Turn_Time = Enemy1["Speed"] / Player_copy["Speed"]
                        print(f"\n---------------\n",Enemy1["Type"],"turn\n---------------\n")
                        while Turn_Time > 0:
                            Turn_Time = round(Turn_Time,2)
                            print(f"\n{Turn_Time}s remaining\n")
                            if Enemy1["Health"] > 0:
                                Enemy1, Player_copy, Evasion1_Stopper, Defense1_Stopper,Turn_Time,Player_Skip,b,Enemy2,Enemy3 = Enemy1_Battle(Enemy1,Player,Player_copy,Evasion1_Stopper,Defense1_Stopper,name,Game,Turn_Time,Enemy2_Skip,Player_Skip,b,typewriter,Enemy2=Enemy2,Enemy3=Enemy3)
                        if "Traveler" in Enemy1["Type"]:
                            Enemy1["Stamina"] *= 1.5
                            Enemy1["Stamina"] = round(Enemy1["Stamina"])
                        else:
                            Enemy1["Stamina"] *= 1.1
                            Enemy1["Stamina"] = round(Enemy1["Stamina"])
                        print(f"\n---------------\n Turn End\n---------------\n")




                    if fighter == fighters_sorted[-1]:
                        if b >= 3:
                            Player_copy, Enemy3,n, place,Game =Status_Effect3(Player_copy, Enemy3,n, place,Game)
                        if b >= 2:
                            Player_copy, Enemy2,n, place,Game = Status_Effect2(Player_copy, Enemy2,n, place,Game)
                        if b >= 1:
                            Player_copy, Enemy1,n, place,Game = Status_Effect1(Player_copy, Enemy1,n, place,Game)

                        Player_copy,n,Game = Player_Status_Effect(Player_copy,n,Game)

        return Outcome,Player["XP"],Statistics,Player["Gold"],Skill_Books,inventory,Amount_Used,Proficiency
            
