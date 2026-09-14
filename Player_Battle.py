import random
import time
from Text_Writing_Style import TypeWriter as TW
import sys
import builtins
from Level_1 import Level_1 as L1
from Enemy_Battle_abs import Enemy_Battle as E_Battle
from datetime import datetime
from Player_Moves import Player_Move as PM
tw = TW(delay=0.02, jitter=True)
typewriter = True
def print(*args, sep=" ", end="\n"):
    if typewriter:
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
    else:
        builtins.print(*args, sep=sep, end=end)
Moves = PM()
class Player_Battle:
    class Overall_Player_Battle:
            def Player3_Battle (self,Player,Player_copy,Enemy,Enemy1,Enemy2,Enemy3,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Enemy2_Weakpoint,Enemy3_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,Skill_Tree,Statistics,typewriters,Gold_Multiplier):
                global typewriter
                typewriter = typewriters
                Battle_End = False
                battle_choice = ""
                x = 0
                n = 0
                turn_over = False 
                lever = False
                Enemy1_Skip = False
                Enemy2_Skip = False
                Enemy3_Skip = False
                Weapon_Held = False
                Metal_Weapon = False
                player_shadows = False
                if Gear["Type"]["Weapon"] not in ["None"]:
                    Weapon_Held = True
                    if "Steel" in Gear["Type"]["Weapon"] or "Iron" in  Gear["Type"]["Weapon"] or "Metal" in Gear["Type"]["Weapon"]:
                        Metal_Weapon = True
                dead_enemy1 = ""
                dead_enemy2 = ""
                dead_enemy3 = ""
                if place == "Poison Swamp Chamber":
                    Game["Current Effect"]["Type"] = "Poison"
                    Game["Current Effect"]["Duration"] = 100
                if place == "Collapsing Ruins":
                    Game["Current Effect"]["Type"] = "Falling Rubble"
                    Game["Current Effect"]["Duration"] = 10
                if place == "Dark Ritual Room":
                    Player_copy["Mana"] *= 1.1
                    Enemy1["Mana"] *= 1.1
                    Enemy2["Mana"] *= 1.1
                    Enemy3["Mana"] *= 1.1
                    Enemy1["Mana"]  = round(Enemy1["Mana"] )
                    Enemy2["Mana"]  = round(Enemy2["Mana"] )
                    Enemy3["Mana"]  = round(Enemy3["Mana"] )
                    Player_copy["Mana"]  = round(Player_copy["Mana"] )
                if place == "Storm Tower Top":
                    Game["Current Effect"]["Type"] = "Thundering"
                    Game["Current Effect"]["Duration"] = 10

                

                    
                if Enemy1["Health"] <= 0:
                    dead_enemy1 = "(Dead)"
                if Enemy2["Health"] <= 0:
                    dead_enemy2 = "(Dead)"
                if Enemy3["Health"] <= 0:
                    dead_enemy3 = "(Dead)"
                if Player_Skip == False:
                    while True:
                        print("Fight\nAvatar\nPotions\nInteract\nWait\nRetreat\n")
                        tw = TW(delay=0.02, jitter=True)
                        battle_choice = input("")
                        battle_choice = battle_choice.lower()
                        if battle_choice not in ["melee","m","1","avatar","a","2","i","interact","3","4","r","retreat","wait","w","5","6","storage","s"]:
                            continue
                        if battle_choice in ["fight","f","1"]:
                            turn_over = True
                            Breaker = False
                            try:
                                for i, item in enumerate(Move_Set, start=1):

                                    if isinstance(item, tuple) and len(item) == 2:
                                        move_name, power = item
                                        print(f"{i}. {move_name} {power}")
                                    else:

                                        print(f"{i}. {item}")
                            except:
                                print("\nNo moves set\n")
                            print("")
                            print("Choose the enemy to attack:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")",dead_enemy1,"\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")",dead_enemy2,"\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],dead_enemy3,")","\n")
                            enemy_choice = input("")
                            enemy_choice = enemy_choice.lower()
                            if enemy_choice in ["1","enemy1","enemy 1"]:
                                    target = Enemy1
                            elif enemy_choice in ["2","enemy2","enemy 2"]:
                                    target = Enemy2
                            elif enemy_choice in ["3","enemy3","enemy 3"]:
                                    target = Enemy3
                            print("Choose what move to use.")
                            skill_choice = input("")
                            skill_choice = skill_choice.lower()
                            skill_choice = "".join(skill_choice.split())
                            
                            if (skill_choice in ["straightpunch"] and "Straight Punch" in Combat_Skill_list):
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI= POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)

                            elif (skill_choice in ["impulsiveswing"] and "Impulsive Swing" in Combat_Skill_list):
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI= POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriter,typewriters,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)

                            if (skill_choice in ["slash"] and "Slash" in Combat_Skill_list):
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI= POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Slash(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)

                        
                            elif (skill_choice in ["jab"] and "Jab" in Combat_Skill_list):
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI= POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Jab(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                        
                                
                            
                            elif skill_choice in ["headbutt"] and "Headbutt" in Combat_Skill_list:
                                POI= "head"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Head.Headbutt(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                                
                            elif skill_choice in ["bite"] and "Bite" in Combat_Skill_list:
                                POI= "head"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Head.Bite(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)

                            elif skill_choice in ["spinningbackkick"] and "Spinning Back Kick" in Combat_Skill_list:
                                POI = "chest"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Legs.Spinning_Back_Kick(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                            
                            elif skill_choice in ["axekick","axe kick"] and "Axe Kick" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Legs.Axe_Kick(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Enemy3=Enemy3,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                                
                            elif skill_choice in ["manablast"] and "Mana Blast" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Arcane.Mana_Blast(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,POI=POI,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
 
                            elif skill_choice in ["fireball"] and "Fireball" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Fire.Fireball(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,POI=POI,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                            elif skill_choice in ["heal"] and "Heal" in Spell_list:
                                Player_copy,Breaker,Turn_Time,Statistics = PM.Spell_Moves.Support.Heal(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Statistics,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                            elif skill_choice in ["analyse"] and "Analyse" in Spell_list:
                                Player_copy,Breaker,Turn_Time = PM.Spell_Moves.Detection.Analyse(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                            elif skill_choice in ["iceshard"] and "Ice Shard" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Ice.Ice_Shard(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)
                            elif skill_choice in ["shock"] and "Shock" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Lightning.Shock(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["riverfist"] and "River Fist" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Water.River_Fist(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["mudshot"] and "Mud Shot" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Earth.Mud_Shot(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["lifedrain"] and "Life Drain" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Dark.Life_Drain(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["purify"] and "Purify" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Light.Purify(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["grapplingvines"] and "Grappling Vines" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Nature.Grappling_Vines(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["domination"] and "Domination" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,target2 = PM.Spell_Moves.Mind.Domination(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["stoneslipstream"] and "Stone Slipstream" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Wind.Stone_Slipstream(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["corruptingtouch"] and "Corrupting Touch" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Dark.Corrupting_Touch(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,Enemy3_Weakpoint=Enemy3_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2, Enemy3 = Enemy3,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip,Enemy3_Skip=Enemy3_Skip)  
                            elif skill_choice in ["bloodoffering"] and "Blood Offering" in Method_list:
                                POI = None
                                Player_copy,Breaker = PM.Methods.Blood_Offering(Player_copy,typewriters)
                            elif skill_choice in ["bloodfrenzy"] and "Blood Frenzy" in Method_list:
                                POI = None
                                Player_copy,Breaker = PM.Methods.Blood_Frenzy(Player_copy,typewriters)
                            elif skill_choice in ["empower"] and "Empower" in Spell_list:
                                POI = None
                                Player_copy,Turn_Time,Breaker = PM.Spell_Moves.Arcane.Empower(Player_copy,Spell_list,typewriter,Turn_Time=Turn_Time)
                            else:
                                print("\n\nThis is not a skill you can use\n\n")
                                
                            if Breaker == True:
                                Breaker = False
                                break
                            
                            

                    
                        if battle_choice in ["avatar","a","2"]:
                            print("--------------\nGear\n---------------\nHead:",Gear["Type"]["Helmet"],"\nShoulder:",Gear["Type"]["Shoulderwear"],"\nArm:",Gear["Type"]["Armwear"],"\nChest:",Gear["Type"]["Chestplate"],"\nLeg:",Gear["Type"]["Legwear"],"\nFeet:",Gear["Type"]["Footwear"],"\nWeapon:",Gear["Type"]["Weapon"],"\n---------------\n")
                            print("Statistics\n---------------","\nLevel:",Player_copy["Level"],"\nHealth:",Player_copy["Health"],"\nAttack:",Player_copy["Attack"],"\nDefense:",Player_copy["Defense"],"\nSpeed:",Player_copy["Speed"],"\nMagic Density:",Player_copy["Magic Density"],"\nStamina:",Player_copy["Stamina"],"\nCritical Chance:",Player_copy["Critical Chance"],"\nCritical Damage:",Player_copy["Critical Damage"],"\nEvasion:",Player_copy["Evasion"],"\nAccuracy:",Player_copy["Accuracy"],"\nMana:",Player_copy["Mana"],"\nTower Completion:",Player_copy["Tower Level"])
                            print("\n\nInventory\n---------------")
                            for key,value in inventory.items():
                                print(key,":",value,"\n")
                            back = input("---------------\n\nPress enter to return\n\n")

                        
                        if battle_choice in ["interact","i","4"]:
                            chance = random.random()
                            Turn_Time -= 1
                            if chance > 0.7:
                                print("Nothing happened...")
                            if chance <= 0.3:
                                o = random.random()
                                if o < 0.3:
                                    item = random.choice(treasure_list)
                                    if item in inventory:
                                        inventory[item] += 1
                                    else:
                                        inventory[item] = 1
                                    print(f"\n{name} found {item}!\n")
                                else:
                                    amount_of_gold = round(random.randint(1,50) * Gold_Multiplier)
                                    print(f"\n{name} found {amount_of_gold} Gold\n")
                                    Player["Gold"] += amount_of_gold
                                    Statistics["Gold Earned"] += amount_of_gold
                            if 0.3 < chance <= 0.7:
                                if place == "Dark Ritual Room":
                                    n = random.randint(1,3)
                                    if n == 1 :
                                        while True:
                                            print("Choose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                if Enemy1["Buff"]["Type"] not in ["None"]:
                                                    Enemy1["Buff"]["Type"] = "None"
                                                    Enemy1["Buff"]["Duration"] = 0
                                                    print(f"{name} disrupted the enemies rune circle")
                                                    break
                                                else:
                                                    print("The enemy has no buff to disrupt")
                                            if Target in ["enemy2","2","enemy 2"]:
                                                if Enemy2["Buff"]["Type"] not in ["None"]:
                                                    Enemy2["Buff"]["Type"] = "None"
                                                    Enemy2["Buff"]["Duration"] = 0
                                                    print(f"{name} disrupted the enemies rune circle")
                                                    break
                                                else:
                                                    print("The enemy has no buff to disrupt")
                                            if Target in ["enemy3","3","enemy 3"]:
                                                if Enemy3["Buff"]["Type"] not in ["None"]:
                                                    Enemy3["Buff"]["Type"] = "None"
                                                    Enemy3["Buff"]["Duration"] = 0
                                                    print(f"{name} disrupted the enemies rune circle")
                                                    break
                                                else:
                                                    print("The enemy has no buff to disrupt")
                                            if Enemy1["Buff"]["Type"] == "None" and Enemy2["Buff"]["Type"] == "None" and Enemy3["Buff"]["Type"] == "None":
                                                print("Nothing to dispel")
                                                break
                                    if n == 2:
                                        l = random.randint(1,2)
                                        print(f"{name}'s surroundings are brimming with magic and you absorb 5% more mana")
                                        if l == 1:
                                            Player_copy["Mana"] += (Player["Mana"] * 0.05)
                                        if l == 2:
                                            Player_copy["Mana"] += (Player["Mana"] * 0.05)
                                            print(f"The mana overwhelms you and you take 10 damage")
                                            Player_copy["Health"] -= 10
                                    if n == 3:
                                        print("{name} smashes a nearby crystal")
                                        Damage = int((100 / Enemy1["Defense"]))
                                        Enemy1["Health"] -= Damage
                                        print(Enemy1["Type"],f" takes {Damage} damage ")
                                                     
                                        Damage = int((100 / Enemy2["Defense"]))
                                        Enemy2["Health"] -= Damage
                                        print(Enemy2["Type"],f" takes {Damage} damage ")
                                                     
                                        Damage = int((100 / Enemy3["Defense"]))
                                        Enemy3["Health"] -= Damage
                                        print(Enemy3["Type"],f" takes {Damage} damage ")
                                if place == "Burning Armory":
                                    n = random.randint(1,4)
                                    if n == 1:
                                        print(f"{name} kicks over a brazier")
                                        l = random.randint(1,3)
                                        if l == 1:
                                            print(Enemy1["Type"]," has been burnt")
                                            if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                            elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                            elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                        if l == 2:
                                            print(Enemy2["Type"]," has been burnt")
                                            if Enemy2["Status Effects"]["Status 1"]["Type"] == "None":
                                                Enemy2["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                Enemy2["Status Effects"]["Status 1"]["Duration"] = 3
                                            elif Enemy2["Status Effects"]["Status 2"]["Type"] == "None":
                                                Enemy2["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                Enemy2["Status Effects"]["Status 2"]["Duration"] = 3
                                            elif Enemy2["Status Effects"]["Status 3"]["Type"] == "None":
                                                Enemy2["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                Enemy2["Status Effects"]["Status 3"]["Duration"] = 3
                                        if l == 3:
                                            print(Enemy3["Type"]," has been burnt")
                                            if Enemy3["Status Effects"]["Status 1"]["Type"] == "None":
                                                Enemy3["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                Enemy3["Status Effects"]["Status 1"]["Duration"] = 3
                                            elif Enemy3["Status Effects"]["Status 2"]["Type"] == "None":
                                                Enemy3["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                Enemy3["Status Effects"]["Status 2"]["Duration"] = 3
                                            elif Enemy3["Status Effects"]["Status 3"]["Type"] == "None":
                                                Enemy3["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                Enemy3["Status Effects"]["Status 3"]["Duration"] = 3
                                    if n == 2:
                                        print(f"{name} ignites an oil spill")
                                        if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                        elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                        elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                        if Enemy2["Status Effects"]["Status 1"]["Type"] == "None":
                                            Enemy2["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            Enemy2["Status Effects"]["Status 1"]["Duration"] = 3
                                        elif Enemy2["Status Effects"]["Status 2"]["Type"] == "None":
                                            Enemy2["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            Enemy2["Status Effects"]["Status 2"]["Duration"] = 3
                                        elif Enemy2["Status Effects"]["Status 3"]["Type"] == "None":
                                            Enemy2["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            Enemy2["Status Effects"]["Status 3"]["Duration"] = 3
                                        if Enemy3["Status Effects"]["Status 1"]["Type"] == "None":
                                            Enemy3["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            Enemy3["Status Effects"]["Status 1"]["Duration"] = 3
                                        elif Enemy3["Status Effects"]["Status 2"]["Type"] == "None":
                                            Enemy3["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            Enemy3["Status Effects"]["Status 2"]["Duration"] = 3
                                        elif Enemy3["Status Effects"]["Status 3"]["Type"] == "None":
                                            Enemy3["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            Enemy3["Status Effects"]["Status 3"]["Duration"] = 3
                                    if n == 3:
                                        print(f"{name} spots a nearby hammer")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((50 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Damage = int((50 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                print(Enemy2["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy3","3","enemy 3"]:
                                                Damage = int((50 / Enemy3["Defense"]))
                                                Enemy3["Health"] -= Damage
                                                print(Enemy3["Type"],f" takes {Damage} damage ")
                                                break
                                    if n == 4:
                                        print(f"{name} hides behind a shield rack")
                                        print("Temporary defense boost")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Defense"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Defense"] += Player_copy["Buff"]["Value"]
                                if place == "Crumbling Bridge":
                                    n = random.randint(1,2)
                                    if n == 1:
                                        print(f"{name} prepares for a shoulder barge")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                print(f"You charge at the", Enemy1["Type"])
                                                percentage = random.random()
                                                if percentage >= (Enemy1["Attack"] / Player_copy["Max Health"]):
                                                    Enemy1["Health"] = 0
                                                    print(Enemy1["Type"]," falls off the bridge")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                print(f"You charge at the {Enemy2_Type}")
                                                percentage = random.random()
                                                if percentage >= (Enemy2["Attack"] / Player_copy["Max Health"]):
                                                    Enemy2["Health"] = 0
                                                    print(Enemy2["Type"]," falls off the bridge")
                                                break
                                            if Target in ["enemy3","3","enemy 3"]:
                                                print(f"You charge at the {Enemy3_Type}")
                                                percentage = random.random()
                                                if percentage >= (Enemy3["Attack"] / Player_copy["Max Health"]):
                                                    Enemy3["Health"] = 0
                                                    print(Enemy3["Type"]," falls off the bridge")
                                                break
                                    if n == 2:
                                        print(f"{name} cuts a support rope")
                                        percentage1 = random.random()
                                        if percentage1 >=0.75:
                                            Enemy1["Health"] = 0
                                            print(Enemy1["Type"]," falls off the bridge")
                                        percentage2 = random.random()
                                        if percentage2 >=0.75:
                                            Enemy2["Health"] = 0
                                            print(Enemy2["Type"]," falls off the bridge")
                                        percentage3 = random.random()
                                        if percentage3 >=0.75:
                                            Enemy3["Health"] = 0
                                            print(Enemy3["Type"]," falls off the bridge")
                                if place == "Poison Swamp Chamber":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        while True:
                                            print("\nChoose the enemy who you want to kick mud at:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Enemy1["Accuracy"] -= 10
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Enemy2["Accuracy"] -= 10
                                                break
                                            if Target in ["enemy3","3","enemy 3"]:
                                                Enemy3["Accuracy"] -= 10
                                                break
                                    if n == 2:
                                        print(f"{name} lures the enemies into a deeper part of the swamp")
                                        Enemy1["Speed"] -= 10
                                        Enemy2["Speed"] -= 10
                                        Enemy3["Speed"] -= 10
                                        print(Enemy1["Type"],Enemy2["Type"] ,"and", Enemy3["Type"]," have their speed decreased")
                                    if n == 3:
                                        print(f"{name} holds their breath")
                                        Player_copy["Buff"]["Type"] = "Poison Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                        print("Poison resistance obtained")
                                if place == "Collapsing Ruins":
                                    if lever == False:
                                        n = random.randint(1,3)
                                    if lever == True:
                                        n = random.randint(1,2)
                                    if n == 3:
                                        while True:
                                            print("\nChoose the enemy who you want to push a pillar on:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy1["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy1["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((150/ Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Damage = int((150 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                print(Enemy2["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy3","3","enemy 3"]:
                                                Damage = int((150 / Enemy3["Defense"]))
                                                Enemy3["Health"] -= Damage
                                                print(Enemy3["Type"],f" takes {Damage} damage ")
                                                break
                                    if n == 1:
                                        print(f"{name} takes cover")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Under Cover"
                                        Player_copy["Buff"]["Duration"] = 3

                                    if n == 2:
                                        while True:
                                            print("\nChoose the enemy who you want to throw rubble at:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((50/ Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Damage = int((50 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                print(Enemy2["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy3","3","enemy 3"]:
                                                Damage = int((50 / Enemy3["Defense"]))
                                                Enemy3["Health"] -= Damage
                                                print(Enemy3["Type"],f" takes {Damage} damage ")
                                                break
                                if place == "Frozen Cavern":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        while True:
                                            print("\nChoose the enemy who you want to push:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            percentage = random.randint(1,2)
                                            if Target in ["enemy1","1","enemy 1"]:
                                                if percentage == 1:
                                                    print("They Slipped!")
                                                    Enemy1_Skip = True
                                                else:
                                                    print("They remain balanced...")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                if percentage == 1:
                                                        print("They Slipped!")
                                                        Enemy2_Skip = True
                                                else:
                                                        print("They remain balanced...")
                                                break

                                            if Target in ["enemy3","3","enemy 3"]:
                                                if percentage ==  1:
                                                        print("They Slipped!")
                                                        Enemy3_Skip = True
                                                else:
                                                        print("They remain balanced...")
                                                break
                                    if n == 2:
                                        print(f"{name} attempts a sliding clothesline")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy1["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 50 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    print(f"{name} slipped!")
                                                    Player_Skip = True
                                                break
                                            if Target in ["enemy2","enemy 2","2"]:
                                                Damage = int((Player_copy["Attack"] * 50 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    print(f"{name} slipped!")
                                                    Player_Skip = True
                                                break
                                            if Target in ["enemy3","enemy 3","3"]:
                                                Damage = int((Player_copy["Attack"] * 50 / Enemy3["Defense"]))
                                                Enemy3["Health"] -= Damage
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    print(f"{name} slipped!")
                                                    Player_Skip = True
                                                break
                                            
                                    if n == 3:
                                        print("An icicle fell")
                                        Target = random.randint(1,3)
                                        if Target == 1:
                                            Damage = int((50/ Enemy1["Defense"]))
                                            Enemy1["Health"] -= Damage
                                            print(Enemy1["Type"],f" takes {Damage} damage ")
                                        if Target == 2:
                                            Damage = int((50 / Enemy2["Defense"]))
                                            Enemy2["Health"] -= Damage
                                            print(Enemy2["Type"],f" takes {Damage} damage ")
                                        if Target == 3:
                                            Damage = int((50 / Enemy3["Defense"]))
                                            Enemy3["Health"] -= Damage
                                            print(Enemy3["Type"],f" takes {Damage} damage ")
                                if place == "Storm Tower Top":
                                    if Weapon_Held == True:
                                        if Metal_Weapon == True:
                                            n= random.randint(1,3)
                                    else:
                                        n = random.randint(1,2)
                                    if n == 3:
                                        if Weapon_Held == True:
                                            if Metal_Weapon == True:
                                                print(f"{name} raises their metal weapon")
                                                while True:
                                                    print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                                    Target = input("")
                                                    if Target in ["enemy1","enemy 1","1"]:
                                                        percentage = random.randint(1,2)
                                                        if percentage == 1:
                                                            Damage = int((Player_copy["Attack"] * 200 / Enemy1["Defense"]))
                                                            Enemy1["Health"] -= Damage
                                                        elif Player_copy["Buff"]["Type"] != "Electrical Immunity":
                                                            print(f"{name} struck yourself with lighting!")
                                                            Damage = int((200 / Player_copy["Defense"]))
                                                            Player_copy["Health"] -= Damage
                                                        break
                                                    if Target in ["enemy2","enemy 2","2"]:
                                                        percentage = random.randint(1,2)
                                                        if percentage == 1:
                                                            Damage = int((Player_copy["Attack"] * 200 / Enemy2["Defense"]))
                                                            Enemy2["Health"] -= Damage
                                                        elif Player_copy["Buff"]["Type"] != "Electrical Immunity":
                                                            print(f"{name} struck themself with lighting!")
                                                            Damage = int((200 / Player_copy["Defense"]))
                                                            Player_copy["Health"] -= Damage
                                                        break

                                                    if Target in ["enemy3","enemy 3","3"]:
                                                        percentage = random.randint(1,2)
                                                        if percentage == 1:
                                                            Damage = int((Player_copy["Attack"] * 200 / Enemy3["Defense"]))
                                                            Enemy1["Health"] -= Damage
                                                        elif Player_copy["Buff"]["Type"] != "Electrical Immunity":
                                                            print(f"{name} struck themself with lighting!")
                                                            Damage = int((200 / Player_copy["Defense"]))
                                                            Player_copy["Health"] -= Damage
                                                        break
                                    if n == 1:
                                        print("a burst of strong wind occurs!")
                                        while True:
                                            print("\nChoose the enemy who you want to try to push:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    Enemy1["Health"] = 0
                                                else:
                                                    print("It failed")
                                                break
                                            if Target in ["enemy2","enemy 2","2"]:
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    Enemy2["Health"] = 0
                                                else:
                                                    print("It failed")
                                                break
                                            if Target in ["enemy3","enemy 3","3"]:
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    Enemy3["Health"] = 0
                                                else:
                                                    print("It failed")
                                                break
                                    if n == 2:
                                        print(f"{name} grounds themself")
                                        Player_copy["Buff"]["Type"] = "Electricity Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                if place == "Alchemist Lab":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} spots an alchemist potion")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 25 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                Enemy1["Defense"] -= 10
                                                break
                                            if Target in ["enemy2","enemy 2","2"]:
                                                Damage = int((Player_copy["Attack"] * 25 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                Enemy2["Defense"] -= 10
                                                break
                                            if Target in ["enemy3","enemy 3","3"]:
                                                Damage = int((Player_copy["Attack"] * 25 / Enemy3["Defense"]))
                                                Enemy3["Health"] -= Damage
                                                Enemy3["Defense"] -= 10
                                                break
                                    if n == 2:
                                        print(f"{name} mixes together a few nearby potions")
                                        potion = random.choice(["Health","Attack","Defense","Speed","Magic Density","Stamina","Critical Chance","Critical Damage","Evasion","Accuracy","Mana"])
                                        print("Do you want to drink it?")
                                        option = input("")
                                        option = option.lower()
                                        if option in ["y","yes","yeah","y"]:
                                            if potion == "Health":
                                                Player_copy["Health"] += 10
                                                potion_type = "Health"
                                            if potion == "Attack":
                                                Player_copy["Attack"] += 10
                                                potion_type = "Attack"
                                            if potion == "Defense":
                                                Player_copy["Defense"] += 10
                                                potion_type = "Defense"
                                            if potion == "Speed":
                                                Player_copy["Speed"] += 10
                                                potion_type = "Speed"
                                            if potion == "Magic Density":
                                                Player_copy["Magic Density"] += 10
                                                potion_type = "Magic Density"
                                            if potion == "Stamina":
                                                Player_copy["Stamina"] += 10
                                                potion_type = "Stamina"
                                            if potion == "Critical Chance":
                                                Player_copy["Critical Chance"] += 10
                                                potion_type = "Critical Chance"
                                            if potion == "Critical Damage":
                                                Player_copy["Critical Damage"] += 10
                                                potion_type = "Critical Damage"
                                            if potion == "Evasion":
                                                Player_copy["Evasion"] += 10
                                                potion_type = "Evasion"
                                            if potion == "Accuracy":
                                                Player_copy["Accuracy"] += 10
                                                potion_type = "Accuracy"
                                            if potion == "Mana":
                                                Player_copy["Mana"] += 10
                                                potion_type = "Mana"
                                            print(f"{potion_type} is increased by 10")
                                        else:
                                            while True:
                                                print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                                Target = input("")
                                                if Target in ["enemy1","enemy 1","1"]:
                                                    if potion == "Health":
                                                        Enemy1["Health"] -= 10
                                                        potion_type = "Health"
                                                    if potion == "Attack":
                                                        Enemy1["Attack"] -= 10
                                                        potion_type = "Attack"
                                                    if potion == "Defense":
                                                        Enemy1["Defense"] -= 10
                                                        potion_type = "Defense"
                                                    if potion == "Speed":
                                                        Enemy1["Speed"] -= 10
                                                        potion_type = "Speed"
                                                    if potion == ["Magic Density"]:
                                                        Enemy1["Magic Density"] -= 10
                                                        potion_type = "Magic Density"
                                                    if potion == ["Stamina"]:
                                                        Enemy1["Stamina"] -= 10
                                                        potion_type = "Stamina"
                                                    if potion == ["Critical Chance"]:
                                                        Enemy1["Critical Chance"] -= 10
                                                        potion_type = "Critical Chance"
                                                    if potion == ["Critical Damage"]:
                                                        Enemy1["Critical Damage"] -= 10
                                                        potion_type = "Critical Damage"
                                                    if potion == ["Evasion"]:
                                                        Enemy1["Evasion"] -= 10
                                                        potion_type = "Evasion"
                                                    if potion == ["Accuracy"]:
                                                        Enemy1["Accuracy"] -= 10
                                                        potion_type = "Accuracy"
                                                    if potion == ["Mana"]:
                                                        Enemy1["Mana"] -= 10
                                                        potion_type = "Mana"
                                                    print(f"{potion_type} is decreased by 10")
                                                    break
                                                    
                                                if Target in ["enemy2","enemy 2","2"]:
                                                    if potion == "Health":
                                                        Enemy2["Health"] -= 10
                                                        potion_type = "Health"
                                                    if potion == "Attack":
                                                        Enemy2["Attack"] -= 10
                                                        potion_type = "Attack"
                                                    if potion == "Defense":
                                                        Enemy1["Defense"] -= 10
                                                        potion_type = "Defense"
                                                    if potion == "Speed":
                                                        Enemy2["Speed"] -= 10
                                                        potion_type = "Speed"
                                                    if potion == "Magic Density":
                                                        Enemy2["Magic Density"] -= 10
                                                        potion_type = "Magic Density"
                                                    if potion == "Stamina":
                                                        Enemy2["Stamina"] -= 10
                                                        potion_type = "Stamina"
                                                    if potion == "Critical Chance":
                                                        Enemy2["Critical Chance"] -= 10
                                                        potion_type = "Critical Chance"
                                                    if potion == "Critical Damage":
                                                        Enemy2["Critical Damage"] -= 10
                                                        potion_type = "Critical Damage"
                                                    if potion == "Evasion":
                                                        Enemy2["Evasion"] -= 10
                                                        potion_type = "Evasion"
                                                    if potion == "Accuracy":
                                                        Enemy2["Accuracy"] -= 10
                                                        potion_type = "Accuracy"
                                                    if potion == "Mana":
                                                        Enemy2["Mana"] -= 10
                                                        potion_type = "Mana"
                                                    print(f"{potion_type} is decreased by 10")
                                                    break

                                                if Target in ["enemy3","enemy 3","3"]:
                                                    if potion == "Health":
                                                        Enemy3["Health"] -= 10
                                                        potion_type = "Health"
                                                    if potion == "Attack":
                                                        Enemy3["Attack"] -= 10
                                                        potion_type = "Health"
                                                    if potion == ["Defense"]:
                                                        Enemy3["Speed"] -= 10
                                                        potion_type = ""
                                                    if potion == "Magic Density":
                                                        Enemy3["Magic Density"] -= 10
                                                        potion_type = "Magic Density"
                                                    if potion == "Stamina":
                                                        Enemy3["Stamina"] -= 10
                                                        potion_type = "Stamina"
                                                    if potion == "Critical Chance":
                                                        Enemy3["Critical Chance"] -= 10
                                                        potion_type = "Critical Chance"
                                                    if potion == "Critical Damage":
                                                        Enemy3["Critical Damage"] -= 10
                                                        potion_type = "Critical Damage"
                                                    if potion == "Evasion":
                                                        Enemy3["Evasion"] -= 10
                                                        potion_type = "Evasion"
                                                    if potion == "Accuracy":
                                                        Enemy3["Accuracy"] -= 10
                                                        potion_type = "Accuracy"
                                                    if potion == "Mana":
                                                        Enemy3["Mana"] -= 10
                                                        potion_type = "Mana"
                                                    print(f"{potion_type} is decreased by 10")
                                                    break
                                        

                                                                                            
                                    if n == 3:
                                        print(f"{name} spills a vial of acid on the ground")
                                        Game["Current Effect"]["Type"] = "Poison"
                                        Game["Current Effect"]["Duration"] = 3
                                        Player_copy["Buff"]["Type"] = "Poison Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                        
                                if place == "Blood Arena":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name}taunts the crowd")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Attack"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Attack"] += Player_copy["Buff"]["Value"]
                                    if n == 2:
                                        print(f"{name} prepares for a flashy attack")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            Player_copy["Critical Chance"] += 10
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 25 / target["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                break

                                            if Target in ["enemy2","enemy 2","2"]:
                                                Damage = int((Player_copy["Attack"] * 25 / target["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                break

                                            if Target in ["enemy3","enemy 3","3"]:
                                                Damage = int((Player_copy["Attack"] * 25 / target["Defense"]))
                                                Enemy3["Health"] -= Damage
                                                break
                                            Player_copy["Critical Chance"] -= 10
                                            

                                    if n == 3:
                                        print(f"{name} intimidate the enemy")
                                        print("Attack reduced by 5")
                                        Enemy1["Attack"] -= 5
                                        Enemy2["Attack"] -= 5
                                        Enemy3["Attack"] -= 5
                                if place == "Shadow Realm Floor":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} steps into the shadows")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Evasion"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Evasion"] += Player_copy["Buff"]["Value"]
                                        
                                    if n == 2:
                                        while True:
                                            print("\nChoose the enemy who you want to pull into the shadows:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n3. ","lvl",Enemy3["Level"],Enemy3["Type"],"( Health:",Enemy3["Health"],")","")
                                            Target = input("")
                                            
                                            if Target in ["enemy1","enemy 1","1"]:
                                                if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 1"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                                elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 2"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                                elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 3"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                                if ((Enemy1["Status Effects"]["Status 1"]["Type"] == "Shaded" and Enemy1["Status Effects"]["Status 1"]["Duration"] != 0) or  (Enemy1["Status Effects"]["Status 2"]["Type"] == "Shaded" and Enemy1["Status Effects"]["Status 2"]["Duration"] != 0 ) or (Enemy1["Status Effects"]["Status 3"]["Type"] == "Shaded"   and Enemy1["Status Effects"]["Status 3"]["Duration"] != 0)):
                                                    Enemy1["Accuracy"] -= 5
                                                    q = 1
                                                elif q == 1:
                                                    Enemy1["Accuracy"] += 5
                                                break

                                            if Target in ["enemy2","enemy 2","2"]:
                                                if Enemy2["Status Effects"]["Status 1"]["Type"] == "None":
                                                    Enemy2["Status Effects"]["Status 1"]["Type"] = "Shaded"
                                                    Enemy2["Status Effects"]["Status 1"]["Duration"] = 3
                                                elif Enemy2["Status Effects"]["Status 2"]["Type"] == "None":
                                                    Enemy2["Status Effects"]["Status 2"]["Type"] = "Shaded"
                                                    Enemy2["Status Effects"]["Status 2"]["Duration"] = 3
                                                elif Enemy2["Status Effects"]["Status 3"]["Type"] == "None":
                                                    Enemy2["Status Effects"]["Status 3"]["Type"] = "Shaded"
                                                    Enemy2["Status Effects"]["Status 3"]["Duration"] = 3
                                                if ((Enemy2["Status Effects"]["Status 1"]["Type"] == "Shaded" and Enemy2["Status Effects"]["Status 1"]["Duration"] != 0) or  (Enemy2["Status Effects"]["Status 2"]["Type"] == "Shaded" and Enemy2["Status Effects"]["Status 2"]["Duration"] != 0 ) or (Enemy2["Status Effects"]["Status 3"]["Type"] == "Shaded"   and Enemy2["Status Effects"]["Status 3"]["Duration"] != 0)):
                                                    Enemy2["Accuracy"] -= 5
                                                    w = 1
                                                elif w == 1:
                                                    Enemy2["Accuracy"] += 5
                                                break

                                            if Target in ["enemy3","enemy 3","3"]:
                                                if Enemy3["Status Effects"]["Status 1"]["Type"] == "None":
                                                    Enemy3["Status Effects"]["Status 1"]["Type"] = "Shaded"
                                                    Enemy3["Status Effects"]["Status 1"]["Duration"] = 3
                                                elif Enemy3["Status Effects"]["Status 2"]["Type"] == "None":
                                                    Enemy3["Status Effects"]["Status 2"]["Type"] = "Shaded"
                                                    Enemy3["Status Effects"]["Status 2"]["Duration"] = 3
                                                elif Enemy3["Status Effects"]["Status 3"]["Type"] == "None":
                                                    Enemy3["Status Effects"]["Status 3"]["Type"] = "Shaded"
                                                    Enemy3["Status Effects"]["Status 3"]["Duration"] = 3
                                                if ((Enemy3["Status Effects"]["Status 1"]["Type"] == "Shaded" and Enemy3["Status Effects"]["Status 1"]["Duration"] != 0) or  (Enemy3["Status Effects"]["Status 2"]["Type"] == "Shaded" and Enemy3["Status Effects"]["Status 2"]["Duration"] != 0 ) or (Enemy3["Status Effects"]["Status 3"]["Type"] == "Shaded"   and Enemy3["Status Effects"]["Status 3"]["Duration"] != 0)):
                                                    Enemy3["Accuracy"] -= 5
                                                    e = 1
                                                elif e == 1:
                                                    Enemy3["Accuracy"] += 5
                                                break
                                            
                                    if player_shadows == False:
                                        if n == 3:
                                           print(f"{name} embraces the shadows")
                                           player_shadows = True
                                           Player_copy["Damage"] += 10
                                           Player_copy["Defense"] -= 5
                                           print("Damage increased by 10")
                                           print("Defense decreased by 5")
                                    else:
                                        print(f"{name} is already in the shadows")
                            
                            Breaker = True
                            if Breaker == True:
                                break

                        if battle_choice in ["retreat","r","6"]:
                            x = random.randint(1,5)
                            Turn_Time -= 1
                            if x == 1:
                                print("Escape successful!\n")
                                Battle_End = True
                                continue
                            else:
                                print("It failed...\n")
                                break
                        if battle_choice in ["wait","w","5"]:
                            Breaker = True
                            if Skill_Tree["General"]["Meditative Mind"]["Status"] == "(Unlocked)":
                                Player_copy["Mana"] += (Turn_Time * 50)
                            Turn_Time -= Turn_Time
                            if Breaker == True:
                                Breaker = False
                                break
                        if battle_choice in ["3","storage","s"]:
                            if inventory["Potions"] != []:
                                for i, potion in enumerate(inventory["Potions"], 1):
                                    if "Power" in potion:
                                        print(f"{i}. {potion['Type']} ( {potion['Power']} )")
                                    else:
                                        print(f"{i}. {potion['Type']}")
                            else:
                                print("\n You have no items to use \n")



                return Player,Player_copy, Enemy1, Enemy2, Enemy3,n, place,player_shadows,x,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,Player_Skip,Turn_Time,Statistics




            def Player2_Battle (self,Player,Player_copy,Enemy,Enemy1,Enemy2,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Enemy2_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Enemy2_Skip,Skill_Tree,Statistics,typewriters,Gold_Multiplier):
                global typewriter
                typewriter = typewriters
                battle_choice = ""
                x = 0
                n = 0
                player_shadows = False
                Player_Skip = False
                Enemy1_Skip = False
                Enemy2_Skip = False
                lever = False
                Weapon_Held = False
                Metal_Weapon = False
                if Gear["Type"]["Weapon"] not in ["None"]:
                    Weapon_Held = True
                    if "Steel" in Gear["Type"]["Weapon"] or "Iron" in  Gear["Type"]["Weapon"] or "Metal" in Gear["Type"]["Weapon"]:
                        Metal_Weapon = True
                dead_enemy1 = ""
                dead_enemy2 = ""
                if place == "Poison Swamp Chamber":
                    Game["Current Effect"]["Type"] = "Poison"
                    Game["Current Effect"]["Duration"] = 100
                if place == "Collapsing Ruins":
                    Game["Current Effect"]["Type"] = "Falling Rubble"
                    Game["Current Effect"]["Duration"] = 10
                if place == "Dark Ritual Room":
                    Player_copy["Mana"] *= 1.1
                    Enemy1["Mana"] *= 1.1
                    Enemy2["Mana"] *= 1.1
                    Enemy1["Mana"]  = round(Enemy1["Mana"] )
                    Enemy2["Mana"]  = round(Enemy2["Mana"] )
                    Player_copy["Mana"]  = round(Player_copy["Mana"] )
                if place == "Storm Tower Top":
                    Game["Current Effect"]["Type"] = "Thundering"
                    Game["Current Effect"]["Duration"] = 10
                

                    
                if Enemy1["Health"] <= 0:
                    dead_enemy1 = "(Dead)"
                if Enemy2["Health"] <= 0:
                    dead_enemy2 = "(Dead)"
                if Player_Skip == False:
                    while True:
                        print("Fight\nAvatar\nPotions\nInteract\nWait\nRetreat")
                        tw = TW(delay=0.02, jitter=True)
                        battle_choice = input("")
                        battle_choice = battle_choice.lower()
                        if battle_choice not in ["melee","m","1","avatar","a","2","i","interact","3","4","r","retreat","wait","w","5","6","s","storage"]:
                            continue
                        if battle_choice in ["fight","f","1"]:
                            turn_over = True
                            Breaker = False
                            try:
                                for i, item in enumerate(Move_Set, start=1):

                                    if isinstance(item, tuple) and len(item) == 2:
                                        move_name, power = item
                                        print(f"{i}. {move_name} {power}")
                                    else:

                                        print(f"{i}. {item}")
                            except:
                                print("\nNo moves set\n")
                            print("")
                            print("Choose the enemy to attack:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")",dead_enemy1,"\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")",dead_enemy2,"\n")
                            enemy_choice = input("")
                            enemy_choice = enemy_choice.lower()
                            if enemy_choice in ["1","enemy1","enemy 1"]:
                                    target = Enemy1
                            elif enemy_choice in ["2","enemy2","enemy 2"]:
                                    target = Enemy2
                            print("Choose what move to use.")
                            skill_choice = input("")
                            skill_choice = skill_choice.lower()
                            skill_choice = "".join(skill_choice.split())
                            
                            if skill_choice in ["straightpunch"] and "Straight Punch" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)

                            
                            if skill_choice in ["slash"] and "Slash" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Slash(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
             
                            
                            elif skill_choice in ["headbutt"] and "Headbutt" in Combat_Skill_list:
                                POI = "head"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Head.Headbutt(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)

                            elif skill_choice in ["bite"] and "Bite" in Combat_Skill_list:
                                POI = "head"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Head.Bite(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)

                            elif skill_choice in ["spinningbackkick"] and "Spinning Back Kick" in Combat_Skill_list:
                                POI = "chest"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Legs.Spinning_Back_Kick(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
  
                        
                            elif skill_choice in ["axekick","axe kick"] and "Axe Kick" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Legs.Axe_Kick(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)


                            elif skill_choice in ["impulsiveswing"] and "Impulsive Swing" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
                            

                            elif skill_choice in ["jab"] and "Jab" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Jab(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Enemy2 = Enemy2,Turn_Time=Turn_Time,Body_Condition=Body_Condition,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
                            

                                
                            elif skill_choice in ["mana blast","manablast"] and "Mana Blast" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Arcane.Mana_Blast(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1=Enemy1,Enemy2=Enemy2,name=name,POI=POI,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)

                            elif skill_choice in ["fireball"] and "Fireball" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Fire.Fireball(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,POI=POI,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
                            elif skill_choice in ["heal"] and "Heal" in Spell_list:
                                Player_copy,Breaker,Turn_Time = PM.Spell_Moves.Support.Heal(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Statistics,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
                            elif skill_choice in ["analyse"] and "Analyse" in Spell_list:
                                Player_copy,Breaker,Turn_Time = PM.Spell_Moves.Detection.Analyse(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)
                            elif skill_choice in ["iceshard"] and "Ice Shard" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Ice.Ice_Shard(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["shock"] and "Shock" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Lightning.Shock(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["riverfist"] and "River Fist" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Water.River_Fist(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["mudshot"] and "Mud Shot" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Earth.Mud_Shot(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["lifedrain"] and "Life Drain" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Dark.Life_Drain(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["purify"] and "Purify" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Light.Purify(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["grapplingvines"] and "Grappling Vines" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Nature.Grappling_Vines(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["domination"] and "Domination" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,target2 = PM.Spell_Moves.Mind.Domination(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["stoneslipstream"] and "Stone Slipstream" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Wind.Stone_Slipstream(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["corruptingtouch"] and "Corrupting Touch" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Dark.Corrupting_Touch(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,Enemy2_Weakpoint=Enemy2_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip,Enemy2_Skip=Enemy2_Skip)  
                            elif skill_choice in ["bloodoffering"] and "Blood Offering" in Method_list:
                                POI = None
                                Player_copy,Breaker = PM.Methods.Blood_Offering(Player_copy)
                            elif skill_choice in ["bloodfrenzy"] and "Blood Frenzy" in Method_list:
                                POI = None
                                Player_copy,Breaker = PM.Methods.Blood_Frenzy(Player_copy,typewriters)
                                
                            elif skill_choice in ["empower"] and "Empower" in Spell_list:
                                POI = None
                                Player_copy,Turn_Time,Breaker = PM.Spell_Moves.Arcane.Empower(Player_copy,Spell_list,typewriter,Turn_Time=Turn_Time)
                            else:
                                print("\nThis is not a skill you can use\n\n")
        
                            if Breaker == True:
                                Breaker = False
                                break
                            

                    
                        if battle_choice in ["avatar","a","2"]:
                            print("--------------\nGear\n---------------\nHead:",Gear["Type"]["Helmet"],"\nShoulder:",Gear["Type"]["Shoulderwear"],"\nArm:",Gear["Type"]["Armwear"],"\nChest:",Gear["Type"]["Chestplate"],"\nLeg:",Gear["Type"]["Legwear"],"\nFeet:",Gear["Type"]["Footwear"],"\nWeapon:",Gear["Type"]["Weapon"],"\n---------------\n")
                            print("Statistics\n---------------","\nLevel:",Player_copy["Level"],"\nHealth:",Player_copy["Health"],"\nAttack:",Player_copy["Attack"],"\nDefense:",Player_copy["Defense"],"\nSpeed:",Player_copy["Speed"],"\nMagic Density:",Player_copy["Magic Density"],"\nStamina:",Player_copy["Stamina"],"\nCritical Chance:",Player_copy["Critical Chance"],"\nCritical Damage:",Player_copy["Critical Damage"],"\nEvasion:",Player_copy["Evasion"],"\nAccuracy:",Player_copy["Accuracy"],"\nMana:",Player_copy["Mana"],"\nTower Completion:",Player_copy["Tower Level"])
                            print("\n\nInventory\n---------------")
                            for key,value in inventory.items():
                                print(key,":",value,"\n")
                            back = input("---------------\n\nPress enter to return\n\n")

                        
                        if battle_choice in ["interact","i","4"]:
                            chance = random.random()
                            Turn_Time -= 1
                            if chance > 0.7:
                                print("Nothing happened...")
                            if chance <= 0.3:
                                o = random.random()
                                if o < 0.3:
                                    item = random.choice(treasure_list)
                                    if item in inventory:
                                        inventory[item] += 1
                                    else:
                                        inventory[item] = 1
                                    print(f"\n{name} found {item}!\n")
                                else:
                                    amount_of_gold = round(random.randint(1,50) * Gold_Multiplier)
                                    print(f"\n{name} found {amount_of_gold} Gold\n")
                                    Player["Gold"] += amount_of_gold
                                    Statistics["Gold Earned"] += amount_of_gold
                            if 0.3 < chance <= 0.7:
                                if place == "Dark Ritual Room":
                                    n = random.randint(1,3)
                                    if n == 1 :
                                        while True:
                                            print("Choose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                if Enemy1["Buff"]["Type"] not in ["None"]:
                                                    Enemy1["Buff"]["Type"] = "None"
                                                    Enemy1["Buff"]["Duration"] = 0
                                                    print(f"{name} disrupted the enemies rune circle")
                                                    break
                                                else:
                                                    print("The enemy has no buff to disrupt")
                                            if Target in ["enemy2","2","enemy 2"]:
                                                if Enemy2["Buff"]["Type"] not in ["None"]:
                                                    Enemy2["Buff"]["Type"] = "None"
                                                    Enemy2["Buff"]["Duration"] = 0
                                                    print(f"{name} disrupted the enemies rune circle")
                                                    break
                                                else:
                                                    print("The enemy has no buff to disrupt")

                                            if Enemy1["Buff"]["Type"] == "None" and Enemy2["Buff"]["Type"] == "None":
                                                print("Nothing to dispel")
                                                break
                                    if n == 2:
                                        l = random.randint(1,2)
                                        print(f"{name}'s surroundings are brimming with magic and you absorb 5% more mana")
                                        if l == 1:
                                            Player_copy["Mana"] += (Player["Mana"] * 0.05)
                                        if l == 2:
                                            Player_copy["Mana"] += (Player["Mana"] * 0.05)
                                            print(f"The mana overwhelms you and you take 10 damage")
                                            Player_copy["Health"] -= 10
                                    if n == 3:
                                        print("You smash a nearby crystal")
                                        Damage = int((100 / Enemy1["Defense"]))
                                        Enemy1["Health"] -= Damage
                                        print(Enemy1["Type"],f" takes {Damage} damage ")
                                                     
                                        Damage = int((100 / Enemy2["Defense"]))
                                        Enemy2["Health"] -= Damage
                                        print(Enemy2["Type"],f" takes {Damage} damage ")
                                                     
                                if place == "Burning Armory":
                                    n = random.randint(1,4)
                                    if n == 1:
                                        print(f"{name} kicks over a brazier")
                                        l = random.randint(1,2)
                                        if l == 1:
                                            print(Enemy1["Type"]," has been burnt")
                                            if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                            elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                            elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                        if l == 2:
                                            print(Enemy2["Type"]," has been burnt")
                                            if Enemy2["Status Effects"]["Status 1"]["Type"] == "None":
                                                Enemy2["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                Enemy2["Status Effects"]["Status 1"]["Duration"] = 3
                                            elif Enemy2["Status Effects"]["Status 2"]["Type"] == "None":
                                                Enemy2["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                Enemy2["Status Effects"]["Status 2"]["Duration"] = 3
                                            elif Enemy2["Status Effects"]["Status 3"]["Type"] == "None":
                                                Enemy2["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                Enemy2["Status Effects"]["Status 3"]["Duration"] = 3

                                    if n == 2:
                                        print(f"{name} ignites an oil spill")
                                        if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                        elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                        elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                        if Enemy2["Status Effects"]["Status 1"]["Type"] == "None":
                                            Enemy2["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            Enemy2["Status Effects"]["Status 1"]["Duration"] = 3
                                        elif Enemy2["Status Effects"]["Status 2"]["Type"] == "None":
                                            Enemy2["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            Enemy2["Status Effects"]["Status 2"]["Duration"] = 3
                                        elif Enemy2["Status Effects"]["Status 3"]["Type"] == "None":
                                            Enemy2["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            Enemy2["Status Effects"]["Status 3"]["Duration"] = 3

                                    if n == 3:
                                        print(f"{name} spots a nearby hammer")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((50 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Damage = int((50 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                print(Enemy2["Type"],f" takes {Damage} damage ")
                                                break
                                    if n == 4:
                                        print(f"{name} hides behind a shield rack")
                                        print("Temporary defense boost")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Defense"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Defense"] += Player_copy["Buff"]["Value"]
                                if place == "Crumbling Bridge":
                                    n = random.randint(1,2)
                                    if n == 1:
                                        print(f"{name} prepares for a shoulder barge")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                print(f"You charge at the", Enemy1["Type"])
                                                percentage = random.random()
                                                if percentage >= (Enemy1["Attack"] / Player_copy["Max Health"]):
                                                    Enemy1["Health"] = 0
                                                    print(Enemy1["Type"]," falls off the bridge")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                print(f"You charge at the {Enemy2_Type}")
                                                percentage = random.random()
                                                if percentage >= (Enemy2["Attack"] / Player_copy["Max Health"]):
                                                    Enemy2["Health"] = 0
                                                    print(Enemy2["Type"]," falls off the bridge")
                                                break

                                    if n == 2:
                                        print(f"{name} cuts a support rope")
                                        percentage1 = random.random()
                                        if percentage1 >=0.75:
                                            Enemy1["Health"] = 0
                                            print(Enemy1["Type"]," falls off the bridge")
                                        percentage2 = random.random()
                                        if percentage2 >=0.75:
                                            Enemy2["Health"] = 0
                                            print(Enemy2["Type"]," falls off the bridge")

                                if place == "Poison Swamp Chamber":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        while True:
                                            print("\nChoose the enemy who you want to kick mud at:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy1["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Enemy1["Accuracy"] -= 10
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Enemy2["Accuracy"] -= 10
                                                break

                                    if n == 2:
                                        print(f"{name} lures the enemies into a deeper part of the swamp")
                                        Enemy1["Speed"] -= 10
                                        Enemy2["Speed"] -= 10
                                        print(Enemy1["Type"]," and",Enemy2["Type"]," have their speed decreased")
                                    if n == 3:
                                        print(f"{name} hold their breath")
                                        Player_copy["Buff"]["Type"] = "Poison Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                        print("Poison resistance obtained")
                                if place == "Collapsing Ruins":
                                    if lever == False:
                                        n = random.randint(1,3)
                                    if lever == True:
                                        n = random.randint(1,2)
                                    if n == 3:
                                        while True:
                                            print("\nChoose the enemy who you want to push a pillar on:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((150/ Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Damage = int((150 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                print(Enemy2["Type"],f" takes {Damage} damage ")
                                                break
                                    if n == 1:
                                        print(f"{name} takes cover")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Under Cover"
                                        Player_copy["Buff"]["Duration"] = 3
                                    if n == 2:
                                        while True:
                                            print("\nChoose the enemy who you want to throw rubble at:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((50/ Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                Damage = int((50 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                print(Enemy2["Type"],f" takes {Damage} damage ")
                                                break

                                if place == "Frozen Cavern":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        while True:
                                            print("\nChoose the enemy who you want to push:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            percentage = random.randint(1,2)
                                            if Target in ["enemy1","1","enemy 1"]:
                                                if percentage == 1:
                                                    print("They Slipped!")
                                                    Enemy1_Skip = True
                                                else:
                                                    print("They remain balanced...")
                                                break
                                            if Target in ["enemy2","2","enemy 2"]:
                                                if percentage == 1:
                                                        print("They Slipped!")
                                                        Enemy2_Skip = True
                                                else:
                                                        print("They remain balanced...")
                                                break
                                    if n == 2:
                                        print(f"{name} attempts a sliding clothesline")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 50 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    print(f"{name} slipped!")
                                                    Player_Skip = True
                                                break
                                            if Target in ["enemy2","enemy 2","2"]:
                                                Damage = int((Player_copy["Attack"] * 50 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    print(f"{name} slipped!")
                                                    Player_Skip = True
                                                break
                                            
                                    if n == 3:
                                        print("An icicle fell")
                                        Target = random.randint(1,2)
                                        if Target == 1:
                                            Damage = int((50/ Enemy1["Defense"]))
                                            Enemy1["Health"] -= Damage
                                            print(Enemy1["Type"],f" takes {Damage} damage ")
                                        if Target == 2:
                                            Damage = int((50 / Enemy2["Defense"]))
                                            Enemy2["Health"] -= Damage
                                            print(Enemy2["Type"],f" takes {Damage} damage ")

                                if place == "Storm Tower Top":
                                    if Weapon_Held == True:
                                        if Metal_Weapon == True:
                                            n= random.randint(1,3)
                                    else:
                                        n = random.randint(1,2)
                                    if n == 3:
                                        if Weapon_Held == True:
                                            if Metal_Weapon == True:
                                                print(f"{name} raise their metal weapon")
                                                while True:
                                                    print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                                    Target = input("")
                                                    if Target in ["enemy1","enemy 1","1"]:
                                                        percentage = random.randint(1,2)
                                                        if percentage == 1:
                                                            Damage = int((Player_copy["Attack"] * 200 / Enemy1["Defense"]))
                                                            Enemy1["Health"] -= Damage
                                                        elif Player_copy["Buff"]["Type"] != "Electrical Immunity":
                                                            print(f"{name} struck themself with lighting!")
                                                            Damage = int((200 / Player_copy["Defense"]))
                                                            Player_copy["Health"] -= Damage
                                                        break
                                                    if Target in ["enemy2","enemy 2","2"]:
                                                        percentage = random.randint(1,2)
                                                        if percentage == 1:
                                                            Damage = int((Player_copy["Attack"] * 200 / Enemy2["Defense"]))
                                                            Enemy2["Health"] -= Damage
                                                        elif Player_copy["Buff"]["Type"] != "Electrical Immunity":
                                                            print(f"{name} struck themself with lighting!")
                                                            Damage = int((200 / Player_copy["Defense"]))
                                                            Player_copy["Health"] -= Damage
                                                        break


                                    if n == 1:
                                        print("a burst of strong wind occurs!")
                                        while True:
                                            print("\nChoose the enemy who you want to try to push:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    Enemy1["Health"] = 0
                                                else:
                                                    print("It failed")
                                                break
                                            if Target in ["enemy2","enemy 2","2"]:
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    Enemy2["Health"] = 0
                                                else:
                                                    print("It failed")
                                                break
                                    if n == 2:
                                        print(f"{name} grounds themselves")
                                        Player_copy["Buff"]["Type"] = "Electrical Immunity"
                                        Player_copy["Buff"]["Duration"]
                                if place == "Alchemist Lab":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} spots an alchemist potion")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 25 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                Enemy1["Defense"] -= 10
                                                break
                                            if Target in ["enemy2","enemy 2","2"]:
                                                Damage = int((Player_copy["Attack"] * 25 / Enemy2["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                Enemy2["Defense"] -= 10
                                                break

                                    if n == 2:
                                        print(f"{name} mixes together a few nearby potions")
                                        potion = random.choice(["Health","Attack","Defense","Speed","Magic Density","Stamina","Critical Chance","Critical Damage","Evasion","Accuracy","Mana"])
                                        print("Do you want to drink it?")
                                        option = input("")
                                        option = option.lower()
                                        if option in ["y","yes","yeah","y"]:
                                            if potion == "Health":
                                                Player_copy["Health"] += 10
                                                potion_type = "Health"
                                            if potion == "Attack":
                                                Player_copy["Attack"] += 10
                                                potion_type = "Attack"
                                            if potion == "Defense":
                                                Player_copy["Defense"] += 10
                                                potion_type = "Defense"
                                            if potion == "Speed":
                                                Player_copy["Speed"] += 10
                                                potion_type = "Speed"
                                            if potion == "Magic Density":
                                                Player_copy["Magic Density"] += 10
                                                potion_type = "Magic Density"
                                            if potion == "Stamina":
                                                Player_copy["Stamina"] += 10
                                                potion_type = "Stamina"
                                            if potion == "Critical Chance":
                                                Player_copy["Critical Chance"] += 10
                                                potion_type = "Critical Chance"
                                            if potion == "Critical Damage":
                                                Player_copy["Critical Damage"] += 10
                                                potion_type = "Critical Damage"
                                            if potion == "Evasion":
                                                Player_copy["Evasion"] += 10
                                                potion_type = "Evasion"
                                            if potion == "Accuracy":
                                                Player_copy["Accuracy"] += 10
                                                potion_type = "Accuracy"
                                            if potion == "Mana":
                                                Player_copy["Mana"] += 10
                                                potion_type = "Mana"
                                            print(f"{potion_type} is increased by 10")
                                        else:
                                            while True:
                                                print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                                Target = input("")
                                                if Target in ["enemy1","enemy 1","1"]:
                                                    if potion == "Health":
                                                        Enemy1["Health"] -= 10
                                                        potion_type = "Health"
                                                    if potion == "Attack":
                                                        Enemy1["Attack"] -= 10
                                                        potion_type = "Attack"
                                                    if potion == "Defense":
                                                        Enemy1["Defense"] -= 10
                                                        potion_type = "Defense"
                                                    if potion == "Speed":
                                                        Enemy1["Speed"] -= 10
                                                        potion_type = "Speed"
                                                    if potion == "Magic Density":
                                                        Enemy1["Magic Density"] -= 10
                                                        potion_type = "Magic Density"
                                                    if potion == "Stamina":
                                                        Enemy1["Stamina"] -= 10
                                                        potion_type = "Stamina"
                                                    if potion == "Critical Chance":
                                                        Enemy1["Critical Chance"] -= 10
                                                        potion_type = "Critical Chance"
                                                    if potion == "Critical Damage":
                                                        Enemy1["Critical Damage"] -= 10
                                                        potion_type = "Critical Damage"
                                                    if potion == "Evasion":
                                                        Enemy1["Evasion"] -= 10
                                                        potion_type = "Evasion"
                                                    if potion == "Accuracy":
                                                        Enemy1["Accuracy"] -= 10
                                                        potion_type = "Accuracy"
                                                    if potion == "Mana":
                                                        Enemy1["Mana"] -= 10
                                                        potion_type = "Mana"
                                                    print(f"{potion_type} is decreased by 10")
                                                    break
                                                    
                                                if Target in ["enemy2","enemy 2","2"]:
                                                    if potion == "Health":
                                                        Enemy2["Health"] -= 10
                                                        potion_type = "Health"
                                                    if potion == "Attack":
                                                        Enemy2["Attack"] -= 10
                                                        potion_type = "Attack"
                                                    if potion == "Defense":
                                                        Enemy2["Defense"] -= 10
                                                        potion_type = "Defense"
                                                    if potion == "Speed":
                                                        Enemy2["Speed"] -= 10
                                                        potion_type = "Speed"
                                                    if potion == "Magic Density":
                                                        Enemy2["Magic Density"] -= 10
                                                        potion_type = "Magic Density"
                                                    if potion == "Stamina":
                                                        Enemy2["Stamina"] -= 10
                                                        potion_type = "Stamina"
                                                    if potion == "Critical Chance":
                                                        Enemy2["Critical Chance"] -= 10
                                                        potion_type = "Critical Chance"
                                                    if potion == "Critical Damage":
                                                        Enemy2["Critical Damage"] -= 10
                                                        potion_type = "Critical Damage"
                                                    if potion == "Evasion":
                                                        Enemy2["Evasion"] -= 10
                                                        potion_type = "Evasion"
                                                    if potion == "Accuracy":
                                                        Enemy2["Accuracy"] -= 10
                                                        potion_type = "Accuracy"
                                                    if potion == "Mana":
                                                        Enemy2["Mana"] -= 10
                                                        potion_type = "Mana"
                                                    print(f"{potion_type} is decreased by 10")
                                                    break                                                                                             
                                    if n == 3:
                                        print(f"{name} spills a vial of acid on the ground")
                                        Game["Current Effect"]["Type"] = "Poison"
                                        Game["Current Effect"]["Duration"] = 3
                                        Player_copy["Buff"]["Type"] = "Poison Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                        
                                if place == "Blood Arena":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} taunts the crowd")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Attack"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Attack"] += Player_copy["Buff"]["Value"]
                                    if n == 2:
                                        print(f"{name} prepares for a flashy attack")
                                        while True:
                                            print("\nChoose the enemy who you want to target:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")","\n")
                                            Target = input("")
                                            Player_copy["Critical Chance"] += 10
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 25 / target["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                break

                                            if Target in ["enemy2","enemy 2","2"]:
                                                Damage = int((Player_copy["Attack"] * 25 / target["Defense"]))
                                                Enemy2["Health"] -= Damage
                                                break

                                            Player_copy["Critical Chance"] -= 10
                                            

                                    if n == 3:
                                        print(f"{name} intimidates the enemy")
                                        print("Attack reduced by 5")
                                        Enemy1["Attack"] -= 5
                                        Enemy2["Attack"] -= 5
                                if place == "Shadow Realm Floor":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} steps into the shadows")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Evasion"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Evasion"] += Player_copy["Buff"]["Value"]
                                        
                                    if n == 2:
                                        while True:
                                            print("\nChoose the enemy who you want to pull into the shadows:\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")","\n2. ","lvl",Enemy2["Level"],Enemy2["Type"],"( Health:",Enemy2["Health"],")\n")
                                            Target = input("")
                                            
                                            if Target in ["enemy1","enemy 1","1"]:
                                                if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 1"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                                elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 2"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                                elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 3"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                                if ((Enemy1["Status Effects"]["Status 1"]["Type"] == "Shaded" and Enemy1["Status Effects"]["Status 1"]["Duration"] != 0) or  (Enemy1["Status Effects"]["Status 2"]["Type"] == "Shaded" and Enemy1["Status Effects"]["Status 2"]["Duration"] != 0 ) or (Enemy1["Status Effects"]["Status 3"]["Type"] == "Shaded"   and Enemy1["Status Effects"]["Status 3"]["Duration"] != 0)):
                                                    Enemy1["Accuracy"] -= 5
                                                    q = 1
                                                elif q == 1:
                                                    Enemy1["Accuracy"] += 5
                                                break

                                            if Target in ["enemy2","enemy 2","2"]:
                                                if Enemy2["Status Effects"]["Status 1"]["Type"] == "None":
                                                    Enemy2["Status Effects"]["Status 1"]["Type"] = "Shaded"
                                                    Enemy2["Status Effects"]["Status 1"]["Duration"] = 3
                                                elif Enemy2["Status Effects"]["Status 2"]["Type"] == "None":
                                                    Enemy2["Status Effects"]["Status 2"]["Type"] = "Shaded"
                                                    Enemy2["Status Effects"]["Status 2"]["Duration"] = 3
                                                elif Enemy2["Status Effects"]["Status 3"]["Type"] == "None":
                                                    Enemy2["Status Effects"]["Status 3"]["Type"] = "Shaded"
                                                if ((Enemy2["Status Effects"]["Status 1"]["Type"] == "Shaded" and Enemy2["Status Effects"]["Status 1"]["Duration"] != 0) or  (Enemy2["Status Effects"]["Status 2"]["Type"] == "Shaded" and Enemy2["Status Effects"]["Status 2"]["Duration"] != 0 ) or (Enemy2["Status Effects"]["Status 3"]["Type"] == "Shaded"   and Enemy2["Status Effects"]["Status 3"]["Duration"] != 0)):
                                                    Enemy2["Accuracy"] -= 5
                                                    w = 1
                                                elif w == 1:
                                                    Enemy2["Accuracy"] += 5
                                                break

                                            
                                    if player_shadows == False:
                                        if n == 3:
                                           print(f"{name} embraces the shadows")
                                           player_shadows = True
                                           Player_copy["Damage"] += 10
                                           Player_copy["Defense"] -= 5
                                           print("Damage increased by 10")
                                           print("Defense decreased by 5")
                                    else:
                                        print(f"{name} is already in the shadows")
                                        
                            Breaker = True
                            if Breaker == True:
                                break      

                        if battle_choice in ["retreat","r","6"]:
                            x = random.randint(1,5)
                            Turn_Time -= 1
                            if x == 1:
                                print(" Escape successful!\n")
                                Battle_End = True
                                continue
                            else:
                                print(" It failed...\n")
                                break

                        if battle_choice in ["wait","w","5"]:
                            Breaker = True
                            if Skill_Tree["General"]["Meditative Mind"]["Status"] == "(Unlocked)":
                                Player_copy["Mana"] += (Turn_Time * 50)
                            Turn_Time -= Turn_Time
                            if Breaker == True:
                                Breaker = False
                                break
                        if battle_choice in ["3","storage","s"]:
                            if inventory["Potions"] != []:
                                for i, potion in enumerate(inventory["Potions"], 1):
                                    if "Power" in potion:
                                        print(f"{i}. {potion['Type']} ( {potion['Power']} )")
                                    else:
                                        print(f"{i}. {potion['Type']}")
                            else:
                                print("\n You have no items to use \n")


                return Player,Player_copy, Enemy1, Enemy2,n, place,player_shadows,x,Enemy1_Skip,Enemy2_Skip,Player_Skip,Turn_Time,Statistics

            def Player1_Battle (self,Player,Player_copy,Enemy,Enemy1,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,place,Player_Skip,Move_Set,b,name,Game,Enemy1_Weakpoint,Body_Condition,Turn_Time,Enemy1_Skip,Skill_Tree,Statistics,typewriters,Gold_Multiplier):
                global typewriter
                typewriter = typewriters
                Battle_End = False
                battle_choice = ""
                x = 0
                n = 0
                player_shadows = False
                Player_Skip = False
                Enemy1_Skip = False
                lever = False
                Weapon_Held = False
                Metal_Weapon = False
                if Gear["Type"]["Weapon"] not in ["None"]:
                    Weapon_Held = True
                    if "Steel" in Gear["Type"]["Weapon"] or "Iron" in  Gear["Type"]["Weapon"] or "Metal" in Gear["Type"]["Weapon"]:
                        Metal_Weapon = True
                dead_enemy1 = ""
                if place == "Poison Swamp Chamber":
                    Game["Current Effect"]["Type"] = "Poison"
                    Game["Current Effect"]["Duration"] = 100
                if place == "Collapsing Ruins":
                    Game["Current Effect"]["Type"] = "Falling Rubble"
                    Game["Current Effect"]["Duration"] = 10
                if place == "Dark Ritual Room":
                    Player_copy["Mana"] *= 1.1
                    Enemy1["Mana"] *= 1.1
                    Enemy1["Mana"]  = round(Enemy1["Mana"] )
                    Player_copy["Mana"]  = round(Player_copy["Mana"] )
                if place == "Storm Tower Top":
                    Game["Current Effect"]["Type"] = "Thundering"
                    Game["Current Effect"]["Duration"] = 10
                

                    
                if Enemy1["Health"] <= 0:
                    dead_enemy1 = "(Dead)"

                if Player_Skip == False:
                    while True:
                        print("Fight\nAvatar\nPotions\nInteract\nWait\nRetreat")
                        tw = TW(delay=0.02, jitter=True)
                        battle_choice = input("")
                        battle_choice = battle_choice.lower()
                        if battle_choice not in ["melee","m","1","avatar","a","2","i","interact","3","4","r","retreat","wait","w","5","6","storage","s"]:
                            continue
                        if battle_choice in ["fight","f","1"]:
                            Breaker = False
                            try:
                                for i, item in enumerate(Move_Set, start=1):

                                    if isinstance(item, tuple) and len(item) == 2:
                                        move_name, power = item
                                        print(f"{i}. {move_name} {power}")
                                    else:

                                        print(f"{i}. {item}")
                            except:
                                print("\nNo moves set\n")
                            print("")
                            target = Enemy1
                            print("\n1. ","lvl",Enemy1["Level"],Enemy1["Type"],"( Health:",Enemy1["Health"],")",dead_enemy1,"\n")
                            print("Choose what move to use.")
                            skill_choice = input("")
                            skill_choice = skill_choice.lower()
                            skill_choice = "".join(skill_choice.split())
                            
                            if skill_choice in ["straight punch","straightpunch"] and "Straight Punch" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time)

                            if skill_choice in ["slash"] and "Slash" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Slash(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time)
                            
                            elif skill_choice in ["headbutt"] and "Headbutt" in Combat_Skill_list:
                                POI = "head"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Head.Headbutt(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)

                            elif skill_choice in ["bite"] and "Bite" in Combat_Skill_list:
                                POI = "head"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Head.Bite(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time)

                            elif skill_choice in ["spinningbackkick"] and "Spinning Back Kick" in Combat_Skill_list:
                                POI = "chest"
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Legs.Spinning_Back_Kick(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)
  
                                
                            elif skill_choice in ["axekick","axe kick"] and "Axe Kick" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Melee_Moves.Legs.Axe_Kick(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)



                            elif skill_choice in ["impulsiveswing"] and "Impulsive Swing" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time)
                            


                            elif skill_choice in ["jab"] and "Jab" in Combat_Skill_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip  = PM.Melee_Moves.Arms.Jab(Player_copy,Enemy,Combat_Skill_list,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,name = name,POI=POI,Enemy1 = Enemy1,Body_Condition=Body_Condition,Turn_Time=Turn_Time)
                            
                                
                            elif skill_choice in ["mana blast","manablast"] and "Mana Blast" in Spell_list:

                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Arcane.Mana_Blast(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,POI=POI,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)

                            elif skill_choice in ["fireball"] and "Fireball" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Fire.Fireball(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,POI=POI,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)
                                 
                            elif skill_choice in ["heal"] and "Heal" in Spell_list:
                                Player_copy,Breaker,Turn_Time = PM.Spell_Moves.Support.Heal(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Statistics,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)
                                
                            elif skill_choice in ["analyse"] and "Analyse" in Spell_list:
                                Player_copy,Breaker,Turn_Time = PM.Spell_Moves.Detection.Analyse(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)
                            elif skill_choice in ["iceshard"] and "Ice Shard" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Ice.Ice_Shard(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,Enemy2 = Enemy2,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  

                            elif skill_choice in ["shock"] and "Shock" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Lightning.Shock(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["riverfist"] and "River Fist" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Water.River_Fist(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["mudshot"] and "Mud Shot" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Earth.Mud_Shot(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["lifedrain"] and "Life Drain" in Spell_list:
                                POI= None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Dark.Life_Drain(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["purify"] and "Purify" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Light.Purify(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["grapplingvines"] and "Grappling Vines" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Nature.Grappling_Vines(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["domination"] and "Domination" in Spell_list:
                                POI = None
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip,target2 = PM.Spell_Moves.Mind.Domination(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["stoneslipstream"] and "Stone Slipstream" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Wind.Stone_Slipstream(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["corruptingtouch"] and "Corrupting Touch" in Spell_list:
                                while True:
                                    print("\nWhere do you want to hit:\n\nHead\n\nLeft Arm\n\nRight Arm\n\nChest\n\nBack\n\nLeft Leg\n\nRight Leg\n")
                                    POI = input("")
                                    POI = POI.lower()
                                    POI = "".join(POI.split())
                                    if POI in["head","leftarm","rightarm","chest","leftleg","rightleg","back"]:
                                        break
                                    else:
                                        print("Not an option.")
                                Player_copy,target,Breaker,Turn_Time,Enemy1_Skip,Enemy2_Skip,Enemy3_Skip = PM.Spell_Moves.Elemental.Dark.Corrupting_Touch(Player_copy,Enemy,Spell_list,Skill_Tree,typewriter,Enemy1_Weakpoint=Enemy1_Weakpoint,target=target,Enemy1 = Enemy1,name = name,Turn_Time=Turn_Time,Enemy1_Skip=Enemy1_Skip)  
                            elif skill_choice in ["bloodoffering"] and "Blood Offering" in Method_list:
                                POI = None
                                Player_copy,Breaker = PM.Methods.Blood_Offering(Player_copy,typewriters)
                            elif skill_choice in ["bloodfrenzy"] and "Blood Frenzy" in Method_list:
                                POI = None
                                Player_copy,Breaker = PM.Methods.Blood_Frenzy(Player_copy,typewriters)
                                
                            elif skill_choice in ["empower"] and "Empower" in Spell_list:
                                POI = None
                                Player_copy,Turn_Time,Breaker = PM.Spell_Moves.Arcane.Empower(Player_copy,Spell_list,typewriter,Turn_Time=Turn_Time)
                            else:
                                print("\nThis is not a skill you can use\n\n")

                            if Breaker == True:
                                Breaker = False
                                break
                            

                    
                        if battle_choice in ["avatar","a","2"]:
                            print("--------------\nGear\n---------------\nHead:",Gear["Type"]["Helmet"],"\nShoulder:",Gear["Type"]["Shoulderwear"],"\nArm:",Gear["Type"]["Armwear"],"\nChest:",Gear["Type"]["Chestplate"],"\nLeg:",Gear["Type"]["Legwear"],"\nFeet:",Gear["Type"]["Footwear"],"\nWeapon:",Gear["Type"]["Weapon"],"\n---------------\n")
                            print("Statistics\n---------------","\nLevel:",Player_copy["Level"],"\nHealth:",Player_copy["Health"],"\nAttack:",Player_copy["Attack"],"\nDefense:",Player_copy["Defense"],"\nSpeed:",Player_copy["Speed"],"\nMagic Density:",Player_copy["Magic Density"],"\nStamina:",Player_copy["Stamina"],"\nCritical Chance:",Player_copy["Critical Chance"],"\nCritical Damage:",Player_copy["Critical Damage"],"\nEvasion:",Player_copy["Evasion"],"\nAccuracy:",Player_copy["Accuracy"],"\nMana:",Player_copy["Mana"],"\nTower Completion:",Player_copy["Tower Level"])
                            print("\n\nInventory\n---------------")
                            for key,value in inventory.items():
                                print(key,":",value,"\n")
                            back = input("---------------\n\nPress enter to return\n\n")

                        
                        if battle_choice in ["interact","i","4"]:
                            Turn_Time -= 1
                            chance = random.random()
                            if chance > 0.7:
                                print("Nothing happened...")
                            if chance <= 0.3:
                                o = random.random()
                                if o < 0.3:
                                    item = random.choice(treasure_list)
                                    if item in inventory:
                                        inventory[item] += 1
                                    else:
                                        inventory[item] = 1
                                    print(f"\n{name} found {item}!\n")
                                else:
                                    amount_of_gold = round(random.randint(1,50) * Gold_Multiplier)
                                    print(f"\n{name} found {amount_of_gold} Gold\n")
                                    Player["Gold"] += amount_of_gold
                                    Statistics["Gold Earned"] += amount_of_gold
                            if 0.3 < chance <= 0.7:
                                if place == "Dark Ritual Room":
                                    n = random.randint(1,3)
                                    if n == 1 :
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","1","enemy 1"]:
                                                if Enemy1["Buff"]["Type"] not in ["None"]:
                                                    Enemy1["Buff"]["Type"] = "None"
                                                    Enemy1["Buff"]["Duration"] = 0
                                                    print(f"{name} disrupted the enemies rune circle")
                                                    break
                                                else:
                                                    print("The enemy has no buff to disrupt")
                                            if Enemy1["Buff"]["Type"] == "None":
                                                print("Nothing to dispel")
                                                break
                                    if n == 2:
                                        l = random.randint(1,2)
                                        print(f"{name}'s surroundings are brimming with magic and you absorb 5% more mana")
                                        if l == 1:
                                            Player_copy["Mana"] += (Player["Mana"] * 0.05)
                                        if l == 2:
                                            Player_copy["Mana"] += (Player["Mana"] * 0.05)
                                            print(f"The mana overwhelms you and you take 10 damage")
                                            Player_copy["Health"] -= 10
                                    if n == 3:
                                        print("You smash a nearby crystal")
                                        Damage = int((100 / Enemy1["Defense"]))
                                        Enemy1["Health"] -= Damage
                                        print(Enemy1["Type"],f" takes {Damage} damage ")
                                if place == "Burning Armory":
                                    n = random.randint(1,4)
                                    if n == 1:
                                        print(f"{name} kick over a brazier")
                                        l = random.randint(1,1)
                                        if l == 1:
                                            print(Enemy1["Type"]," has been burnt")
                                            if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 1"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                            elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 2"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                            elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                                Enemy1["Status Effects"]["Status 3"]["Type"] = "Burn"
                                                Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                    if n == 2:
                                        print(f"{name} ignites an oil spill")
                                        if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 1"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                        elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 2"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                        elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                            Enemy1["Status Effects"]["Status 3"]["Type"] = "Burn"
                                            Enemy1["Status Effects"]["Status 3"]["Duration"] = 3

                                    if n == 3:
                                        print(f"{name} spots a nearby hammer")
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((50 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                    if n == 4:
                                        print("You hide behind a shield rack")
                                        print("Temporary defense boost")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Defense"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Defense"] += Player_copy["Buff"]["Value"]
                                if place == "Crumbling Bridge":
                                    n = random.randint(1,2)
                                    if n == 1:
                                        print(f"{name} prepares for a shoulder barge")
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","1","enemy 1"]:
                                                print(f"You charge at the ",Enemy1["Type"])
                                                percentage = random.random()
                                                if percentage >= (Enemy1["Attack"] / Player_copy["Max Health"]):
                                                    Enemy1["Health"] = 0
                                                    print(Enemy1["Type"]," falls off the bridge")
                                                break
                                    if n == 2:
                                        print(f"{name} cuts a support rope")
                                        percentage1 = random.random()
                                        if percentage1 >=0.75:
                                            Enemy1["Health"] = 0
                                            print(Enemy1["Type"]," falls off the bridge")

                                if place == "Poison Swamp Chamber":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Enemy1["Accuracy"] -= 10
                                                break

                                    if n == 2:
                                        print(f"{name} lures the enemy into a deeper part of the swamp")
                                        Enemy1["Speed"] -= 10
                                        print(Enemy1["Type"]," have their speed decreased")
                                    if n == 3:
                                        print(f"{name} holds your breath")
                                        Player_copy["Buff"]["Type"] = "Poison Immunity"
                                        Player_copt["Buff"]["Duration"] = 3
                                        print("Poison resistance obtained")
                                if place == "Collapsing Ruins":
                                    if lever == False:
                                        n = random.randint(1,3)
                                    if lever == True:
                                        n = random.randint(1,2)
                                    if n == 3:
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((150/ Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
                                    if n == 1:
                                        print(f"{name} takes cover")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Under Cover"
                                        Player_copy["Buff"]["Duration"] = 3
                                    if n == 2:
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","1","enemy 1"]:
                                                Damage = int((50/ Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                print(Enemy1["Type"],f" takes {Damage} damage ")
                                                break
     
                                if place == "Frozen Cavern":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        while True:
                                            Target = "enemy1"
                                            percentage = random.randint(1,2)
                                            if Target in ["enemy1","1","enemy 1"]:
                                                if percentage == 1:
                                                    print("They Slipped!")
                                                    Enemy1_Skip = True
                                                else:
                                                    print("They remain balanced...")
                                                break

                                    if n == 2:
                                        print(f"{name} attempts a sliding clothesline")
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 50 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    print("You slipped!")
                                                    Player_Skip = True
                                                break

                                            
                                    if n == 3:
                                        print("An icicle fell")
                                        Target = random.randint(1,1)
                                        if Target == 1:
                                            Damage = int((50/ Enemy1["Defense"]))
                                            Enemy1["Health"] -= Damage
                                            print(Enemy1["Type"],f" takes {Damage} damage ")
                                if place == "Storm Tower Top":
                                    if Weapon_Held == True:
                                        if Metal_Weapon == True:
                                            n= random.randint(1,3)
                                    else:
                                        n = random.randint(1,2)
                                    if n == 3:
                                        if Weapon_Held == True:
                                            if Metal_Weapon == True:
                                                print(f"{name} raises your metal weapon")
                                                while True:
                                                    Target = "enemy1"
                                                    if Target in ["enemy1","enemy 1","1"]:
                                                        percentage = random.randint(1,2)
                                                        if percentage == 1:
                                                            Damage = int((Player_copy["Attack"] * 200 / Enemy1["Defense"]))
                                                            Enemy1["Health"] -= Damage
                                                        elif Player_copy["Buff"]["Type"] != "Electrical Immunity":
                                                            print(f"{name} strikes themselves with lighting!")
                                                            Damage = int((200 / Player_copy["Defense"]))
                                                            Player_copy["Health"] -= Damage
                                                        break
                                    if n == 1:
                                        print("a burst of strong wind occurs!")
                                        while True:
                                            Target = input("")
                                            if Target in ["enemy1","enemy 1","1"]:
                                                percentage = random.randint(1,2)
                                                if percentage == 1:
                                                    Enemy1["Health"] = 0
                                                else:
                                                    print("It failed")
                                                break
                                    if n == 2:
                                        print("You ground yourself")
                                        Player_copy["Buff"]["Type"] = "Electrical Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                if place == "Alchemist Lab":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} spots an alchemist potion")
                                        while True:
                                            Target = "enemy1"
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 25 / Enemy1["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                Enemy1["Defense"] -= 10
                                                break
                                    if n == 2:
                                        print(f"{name} mixes together a few nearby potions")
                                        potion = random.choice(["Health","Attack","Defense","Speed","Magic Density","Stamina","Critical Chance","Critical Damage","Evasion","Accuracy","Mana"])
                                        print("Do you want to drink it?")
                                        option = input("")
                                        option = option.lower()
                                        if option in ["y","yes","yeah","y"]:
                                            if potion == "Health":
                                                Player_copy["Health"] += 10
                                                potion_type = "Health"
                                            if potion == "Attack":
                                                Player_copy["Attack"] += 10
                                                potion_type = "Attack"
                                            if potion == "Defense":
                                                Player_copy["Defense"] += 10
                                                potion_type = "Defense"
                                            if potion == "Speed":
                                                Player_copy["Speed"] += 10
                                                potion_type = "Speed"
                                            if potion == "Magic Density":
                                                Player_copy["Magic Density"] += 10
                                                potion_type = "Magic Density"
                                            if potion == "Stamina":
                                                Player_copy["Stamina"] += 10
                                                potion_type = "Stamina"
                                            if potion == "Critical Chance":
                                                Player_copy["Critical Chance"] += 10
                                                potion_type = "Critical Chance"
                                            if potion == "Critical Damage":
                                                Player_copy["Critical Damage"] += 10
                                                potion_type = "Critical Damage"
                                            if potion == "Evasion":
                                                Player_copy["Evasion"] += 10
                                                potion_type = "Evasion"
                                            if potion == "Accuracy":
                                                Player_copy["Accuracy"] += 10
                                                potion_type = "Accuracy"
                                            if potion == "Mana":
                                                Player_copy["Mana"] += 10
                                                potion_type = "Mana"
                                            print(f"{potion_type} is increased by 10")
                                        else:
                                            while True:
                                                Target = "enemy1"
                                                if Target in ["enemy1","enemy 1","1"]:
                                                    if potion == "Health":
                                                        Enemy1["Health"] -= 10
                                                        potion_type = "Health"
                                                    if potion == "Attack":
                                                        Enemy1["Attack"] -= 10
                                                        potion_type = "Attack"
                                                    if potion == "Defense":
                                                        Enemy1["Defense"] -= 10
                                                        potion_type = "Defense"
                                                    if potion == "Speed":
                                                        Enemy1["Speed"] -= 10
                                                        potion_type = "Speed"
                                                    if potion == "Magic Density":
                                                        Enemy1["Magic Density"] -= 10
                                                        potion_type = "Magic Density"
                                                    if potion == "Stamina":
                                                        Enemy1["Stamina"] -= 10
                                                        potion_type = "Stamina"
                                                    if potion == "Critical Chance":
                                                        Enemy1["Critical Chance"] -= 10
                                                        potion_type = "Critical Chance"
                                                    if potion == "Critical Damage":
                                                        Enemy1["Critical Damage"] -= 10
                                                        potion_type = "Critical Damage"
                                                    if potion == "Evasion":
                                                        Enemy1["Evasion"] -= 10
                                                        potion_type = "Evasion"
                                                    if potion == "Accuracy":
                                                        Enemy1["Accuracy"] -= 10
                                                        potion_type = "Accuracy"
                                                    if potion == "Mana":
                                                        Enemy1["Mana"] -= 10
                                                        potion_type = "Mana"
                                                    print(f"{potion_type} is decreased by 10")
                                                    break
                                                                                            
                                    if n == 3:
                                        print(f"{name} spills a vial of acid on the ground")
                                        Game["Current Effect"]["Type"] = "Poison"
                                        Game["Current Effect"]["Duration"] = 3
                                        Player_copy["Buff"]["Type"] = "Poison Immunity"
                                        Player_copy["Buff"]["Duration"] = 3
                                        
                                if place == "Blood Arena":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} taunt the crowd")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Attack"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Attack"] += Player_copy["Buff"]["Value"]
                                    if n == 2:
                                        print(f"{name} prepares for a flashy attack")
                                        while True:
                                            Target = "enemy1"
                                            Player_copy["Critical Chance"] += 10
                                            if Target in ["enemy1","enemy 1","1"]:
                                                Damage = int((Player_copy["Attack"] * 25 / target["Defense"]))
                                                Enemy1["Health"] -= Damage
                                                break

                                            Player_copy["Critical Chance"] -= 10
                                            

                                    if n == 3:
                                        print(f"{name} intimidates the enemy")
                                        print("Attack reduced by 5")
                                        Enemy1["Attack"] -= 5

                                if place == "Shadow Realm Floor":
                                    n = random.randint(1,3)
                                    if n == 1:
                                        print(f"{name} steps into the shadows")
                                        Player_copy["Buff"]["Value"] = 5
                                        Player_copy["Buff"]["Type"] = "Evasion"
                                        Player_copy["Buff"]["Duration"] = 3
                                        Player_copy["Evasion"] += Player_copy["Buff"]["Value"]
                                        
                                    if n == 2:
                                        while True:
                                            Target = "enemy1"
                                            
                                            if Target in ["enemy1","enemy 1","1"]:
                                                if Enemy1["Status Effects"]["Status 1"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 1"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 1"]["Duration"] = 3
                                                elif Enemy1["Status Effects"]["Status 2"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 2"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 2"]["Duration"] = 3
                                                elif Enemy1["Status Effects"]["Status 3"]["Type"] == "None":
                                                    Enemy1["Status Effects"]["Status 3"]["Type"] = "Shaded"
                                                    Enemy1["Status Effects"]["Status 3"]["Duration"] = 3
                                                if ((Enemy1["Status Effects"]["Status 1"]["Type"] == "Shaded" and Enemy1["Status Effects"]["Status 1"]["Duration"] != 0) or  (Enemy1["Status Effects"]["Status 2"]["Type"] == "Shaded" and Enemy1["Status Effects"]["Status 2"]["Duration"] != 0 ) or (Enemy1["Status Effects"]["Status 3"]["Type"] == "Shaded"   and Enemy1["Status Effects"]["Status 3"]["Duration"] != 0)):
                                                    Enemy1["Accuracy"] -= 5
                                                    q = 1
                                                elif q == 1:
                                                    Enemy1["Accuracy"] += 5
                                                break


                                            
                                    if player_shadows == False:
                                        if n == 3:
                                           print(f"{name} embraces the shadows")
                                           player_shadows = True
                                           Player_copy["Damage"] += 10
                                           Player_copy["Defense"] -= 5
                                           print("Damage increased by 10")
                                           print("Defense decreased by 5")
                                    else:
                                        print(f"{name} are already in the shadows")


                            Breaker = True
                            if Breaker == True:
                                break
                                    

                        if battle_choice in ["retreat","r","6"]:
                            Turn_Time -= 1
                            x = random.randint(1,5)
                            if x == 1:
                                print("Escape successful!\n")
                                Battle_End = True
                                continue
                            else:
                                print("It failed...\n")
                                break

                        if battle_choice in ["wait","w","5"]:
                            Breaker= True
                            if Skill_Tree["General"]["Meditative Mind"]["Status"] == "(Unlocked)":
                                Player_copy["Mana"] += (Turn_Time * 50)
                            Turn_Time -= Turn_Time
                            if Breaker == True:
                                Breaker = False
                                break
                        if battle_choice in ["3","potions","p"]:
                            print("\n\n\n")
                            if inventory["Potions"] != []:
                                for i, potion in enumerate(inventory["Potions"], 1):
                                    if "Power" in potion:
                                        print(f"{i}. {potion['Type']} ( {potion['Power']} )")
                                    else:
                                        print(f"{i}. {potion['Type']}")
                            else:
                                print("\n You have no items to use \n")
                            while True:
                                try:
                                    choice = int(input("\nChoose a potion: "))

                                    if 1 <= choice <= len(inventory["Potions"]):
                                        potion = inventory["Potions"][choice - 1]
                                        break
                                    else:
                                        print("Invalid choice.")

                                except ValueError:
                                    print("Please enter a number.")
                            potion = inventory["Potions"][choice - 1]
                            if potion["Type"] == "Health Potion":
                                Health_Gained = (round(Player_copy["Health"] * potion["Power"]))
                                Player_copy["Health"] += Health_Gained
                                if Player_copy["Max Health"] < Player_copy["Health"]:
                                    Player_copy["Health"] = Player_copy["Max Health"]
                                Statistics["Health Healed"] += Health_Gained
                            elif potion["Type"] == "Mana Potion":
                                Player_copy["Mana"] *= potion["Power"]
                                Player_copy["Mana"] = round(Player_copy["Mana"])
                            elif potion["Type"] == "Defense Potion":
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                Player_copy["Buff"]["Type"] = "Defense M"
                                Player_copy["Buff"]["Duration"] = 3
                                Player_copy["Defense"] *= Player_copy["Buff"]["Value"]
                                Player_copy["Defense"] = round(Player_copy["Defense"])
                            elif potion["Type"] == "Stamina Potion":
                                Player_copy["Stamina"] *= potion["Power"]
                                Player_copy["Stamina"] = round(Player_copy["Stamina"])
                            elif potion["Type"] == "Holy Potion":
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                Player_copy["Buff"]["Type"] = "Boost Holy"
                                Player_copy["Buff"]["Duration"] = 3
                            elif potion["Type"] == "Spell Potion":
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                Player_copy["Buff"]["Type"] = "Spell"
                                Player_copy["Buff"]["Duration"] = 3
                            elif potion["Type"] == "Dense Potion":
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                Player_copy["Buff"]["Type"] = "Magic Density M"
                                Player_copy["Buff"]["Duration"] = 3
                                Player_copy["Magic Density"] *= Player_copy["Buff"]["Value"]
                                Player_copy["Magic Density"] = round(Player_copy["Magic Density"])
                            elif potion["Type"] == "Hasty Potion":
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                Player_copy["Buff"]["Type"] = "Speed M"
                                Player_copy["Buff"]["Duration"] = 3
                                Player_copy["Speed"] *= Player_copy["Buff"]["Value"]
                                Player_copy["Speed"] = round(Player_copy["Speed"])
                            elif potion["Type"] == "Battle Potion":
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                Player_copy["Buff"]["Type"] = "Attack M"
                                Player_copy["Buff"]["Duration"] = 3
                                Player_copy["Attack"] *= Player_copy["Buff"]["Value"]
                                Player_copy["Attack"] = round(Player_copy["Attack"])
                            elif potion["Type"] == "Evasion Potion":
                                if Player_copy["Buff"]["Type"] == "Evasion M":
                                    pass
                                else:     
                                    Player_copy["Buff"]["Duration"] = 0
                                Player_copy["Buff"]["Value"] = potion["Power"]
                                if Player_copy["Buff"]["Type"] == "Defense":
                                    Player_copy["Defense"] -= Player_copy["Buff"]["Value"]
                                if Player_copy["Buff"]["Type"] == "Attack":
                                    Player_copy["Attack"] -= Player_copy["Buff"]["Value"]
                                if Player_copy["Buff"]["Type"] == "Evasion":
                                    Player_copy["Buff"]["Duration"] += 3
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
                                    Player_copy["Accuracy"] /= Player_copy["Buff"]["Value"]
                                Player_copy["Buff"]["Type"] = "Evasion M"
                                Player_copy["Buff"]["Duration"] += 3
                                Player_copy["Evasion"] *= Player_copy["Buff"]["Value"]
                                Player_copy["Evasion"] = round(Player_copy["Evasion"])
                            elif potion["Type"] == "Focus Potion":
                                if Player_copy["Buff"]["Type"] == "Accuracy M":
                                    pass
                                else:     
                                    Player_copy["Buff"]["Duration"] = 0
                                Player_copy["Buff"]["Value"] = potion["Power"]
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
                                    Player_copy["Buff"]["Duration"] += 3 
                                Player_copy["Buff"]["Type"] = "Accuracy M"
                                Player_copy["Buff"]["Duration"] += 3
                                Player_copy["Accuracy"] *= Player_copy["Buff"]["Value"]
                                Player_copy["Accuracy"] = round(Player_copy["Accuracy"])
                                
                            inventory["Potions"].remove(potion)


                return Player,Player_copy, Enemy1,n, place, player_shadows,x,Enemy1_Skip,Player_Skip,Turn_Time,Statistics
