import random
import time
from Text_Writing_Style import TypeWriter as TW
import sys
from Enemy_Level_Up_abs import Level_Up_Enemy as L1
from Enemy_Battle_abs import Enemy_Battle as E_Battle
from datetime import datetime
from Player_Moves import Player_Move as PM
import copy
tw = TW(delay=0.02, jitter=True)
def print(*args, sep=" ", end="\n"):
    text = sep.join(str(arg) for arg in args)
    tw.write(text, newline=False)
    sys.stdout.write(end)
Moves = PM()


class Arena:
    def Monster_Arena(Player,Player_copy,Enemy,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,Move_Set,name,Enemies_Killed,Game,Body_Condition):
        Battle_End = False
        Enemy1 = random.choice(["Skeleton" ,"Orc Warrior" ,"Wolf", "Bandit" , "Zombie", "Goblin","Kobold" , "Venom Spider" , "Cultist" ,"Ghost"  ,"Imp"    ,"Eclipsed Artificer",     "Void Spawn", "Flame Warden"  ,      "Ash Soldier"     ,   "Swamp Rat"  ,      "Rot Beast" ,       "Ice Bat"    ,    "Frost Knight"    ,    "Lightning Sprite"    ,    "Storm Knight"  ,    "Shadow Rat"   ,     "Shadow Assassin"      ,  "Gladiator"   ,     "Executioner"     ,   "Alchemical Slime"     ,   "Bridge Troll"    ,    "Fire Imp"     ,   "Scavenger"    ,    "Rust Golem"     ,   "Fire Mage"   ,     "Armory Guard"   ,     "Steel Automaton"   ,     "Flame Warden"   ,     "Ash Soldier"       , "Burning Spirit"     ,   "Flame Wraith"    ,  "Molten Knight"    ,    "Inferno Elemental"   , "Swamp Rat" ,       "Bog Snake"    ,    "Mud Crawler"   ,     "Poison Slime" ,    "Rot Beast"     ,   "Plague Spirit"  , "Disease Demon"     ,   "Shadow Assassin"    ,   "Void Beast"   ,     "Shadow Lord"  ,     "Berserker"     ,   "Mutant Rat"  ,      "Alchemical Horror"  ,      "Homunculus"   ,     "Ancient Guardian"      ,  "Ancient Lich"   ,     "Shadow Beast"   ,     "Night Wolf"     ,   "Goblin Archer"     ,   "Acid Slime"  ,  "Swamp Goblin",  "Bog Serpent"    ,    "Ice Kobold"   ,     "Spearman"   , "Arena Archer"   ,     "Bridge Guard"   ,     "Dark Mage"    ,    "Experiment Soldier"      ,  "Storm Mage"      ,  "Potion Spirit"    , "Summoner"       , "Frozen Skeleton"    ,    "Ritual Knight"     ,   "Shield Fighter"      ,  "Lightning Elemental" ,       "Demon Imp"    ,    "Ice Archer"  ,      "Frost Walker"     ,  "Frost Wolf"     ,   "Ice Slime"     ,   "Ancient Archer"      ,  "Wind Spirit"  ,      "Stone Guardian"   ,     "Tomb Raider" ,   "Thunder Archer"    ,    "Rogue Knight"      ,  "Cursed Blacksmith"  ,   "Phantom Knight"   ,  "Lost Traveler Spirit" ,       "Tempest Lord"   ,     "Failed Experiment"     ,   "Swamp Beast"   ,   "Bone Warrior"  ,      "Acid Beast"   ,   "Ice Golem"    ,    "Ruin Golem"    ,   "Plague Crow"     ,   "Frozen Warrior"     ,   "Mutation Ogre"    ,    "Glacier Beast"      ,  "Summoned Demon"   ,     "Heavy Bandit"     ,   "Living Potion"   ,     "Acid Elemental","Tomb Knight"  ,"Snow Stalker"      ,  "War Hound"     ,   "Tomb Robber"   ,   "Arena Champion"  ,      "Goblin Fighter"    ,    "Dark Acolyte"   ,     "Ritual Guard","Frozen Rat","Ruin Rat","Tower Apprentice", "Shadow Mage", "Bridge Thief","Rogue Archer" ,"Bone Dog" ,"Snow Spider","Storm Spirit","Bone Servant"])
        Enemy1 = Enemy["Tier 1"][Enemy1]
        Enemy1["Level"] = random.randint(Player_copy["Level"],Player_copy["Level"]+ 5)
        Enemy1 = L1.Level_Up_Enemy1(Enemy1,Player_copy)
        while Player_copy["Health"] > 0 and Battle_End == False:
            

            print(Enemy1["Type"]," has appeared")
            Battle_End = False
            battle_choice = ""
            x = 0
            n = 0
            check1 = True
            Player_Skip = False
            Enemy1_Skip = False
            Weapon_Held = False
            Metal_Weapon = False
            if Gear["Type"]["Weapon"]["Presence"] not in ["None"]:
                Weapon_Held = True
                if Gear["Type"]["Weapon"]["Type"] == "Metal":
                    Metal_Weapon = True
            dead_enemy1 = ""


            if Enemy1["Health"] <= 0:
                dead_enemy1 = "(Dead)"

            if Player_Skip == False:
                while True:
                    print("Fight\nAvatar\nRetreat")
                    tw = TW(delay=0.02, jitter=True)
                    battle_choice = input("")
                    battle_choice = battle_choice.lower()
                    if battle_choice not in ["melee","m","1","avatar","a","2","i","interact","3","4","r","retreat"]:
                        continue
                    if battle_choice in ["fight","f","1"]:
                        Breaker = False
                        print("Melee\nSpell")
                        fight_choice = input("")
                        if fight_choice in ["melee","m","1"]:
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

                            print("Choose what move to use.")
                            combat_skill_choice = input("")
                            combat_skill_choice = combat_skill_choice.lower()
                            if combat_skill_choice in ["straight punch","straightpunch"]:
                                Player_copy,target,Breaker  = PM.Melee_Moves.Arms.Straight_Punch(Player_copy,Enemy,Combat_Skill_list,target=target)
                            

                            if combat_skill_choice in ["headbutt"]:
                                Player_copy,target,Breaker  = PM.Melee_Moves.Head.Headbutt(Player_copy,Enemy,Combat_Skill_list,target=target)
                            try:
                                if Evasion_Chance > (target["Evasion"] * (1 - (Player_copy["Accuracy"]/1000))):
                                    print(f"{choice} is used.\n")
                                    print(f"{name} does {Damage} Damage\n")
                            except UnboundLocalError:
                                pass
                        if fight_choice in ["spell","s","2"]:
                            try:
                                for i, item in enumerate(Move_Set, start=1):

                                    if isinstance(item, tuple) and len(item) == 2:
                                        move_name, power = item
                                        print(f"{i}. {move_name} {power}")
                                    else:

                                        print(f"{i}. {item}")
                            except:
                                print("\nNo moves set\n")
                            target = Enemy1
                            print("Choose what move to use.")
                            spell_skill_choice = input("")
                            spell_skill_choice = spell_skill_choice.lower()
                            if spell_skill_choice in ["mana blast","manablast"]:
                                if Spell_list["Mana Blast"]["Cost"] < Player_copy["Mana"]:
                                    Player_copy_Critical_Chance = Player_copy["Critical Chance"] / 100
                                    Percentage = random.random()
                                    if Percentage <= Player_copy_Critical_Chance:
                                        Damage = int( Spell_list["Mana Blast"]["Damage"]    * Player_copy["Magic Damage"]    * (1 / (10 + target["Defense"]))    * (1 + Player_copy["Magic Density"] / 100))
                                        Damage *= (1 + (Player_copy["Critical Damage"]/100))
                                    else:
                                        Damage = int( Spell_list["Mana Blast"]["Damage"]    * Player_copy["Magic Damage"]    * (1 / (10 + target["Defense"]))    * (1 + Player_copy["Magic Density"] / 100))
                                    Mana_cost = Spell_list["Mana Blast"]["Cost"] * (1- Player_copy["Magic Density"] /  500 )
                                    Player_copy["Mana"] -= Mana_cost
                                    Evasion_Chance = random.randint(1,100)
                                    if Evasion_Chance > (target["Evasion"] * (1 - (Player_copy["Accuracy"]/1000))):
                                        target["Health"] -= Damage
                                    else:
                                        print("They avoided the attack!")
                                    choice = "Mana Blast"
                                    Breaker = True
                                else:
                                    print("Not enough mana\n")

                            
                            if spell_skill_choice in ["fireball"]:
                                 Player_copy,target,Breaker  = PM.Spell_Moves.Elemental.Fire.Fireball(Player_copy,Enemy,Spell_list,target=target)
                            try:
                                if Evasion_Chance < target["Evasion"]:
                                    print(f"{choice} is used.\n")
                                    print(f"{name} does {Damage} Damage\n")
                            except UnboundLocalError:
                                pass
                        if Breaker == True:
                            break
                            
                    Breaker = False

                
                    if battle_choice in ["avatar","a","2"]:
                        print("--------------\nGear\n---------------\nHead:",Gear["Type"]["Helmet"],"\nShoulder:",Gear["Type"]["Shoulderwear"],"\nArm:",Gear["Type"]["Armwear"],"\nChest:",Gear["Type"]["Chestplate"],"\nLeg:",Gear["Type"]["Legwear"],"\nFeet:",Gear["Type"]["Footwear"],"\nWeapon:",Gear["Type"]["Weapon"],"\n---------------\n")
                        print("Statistics\n---------------","\nLevel:",Player_copy["Level"],"\nHealth:",Player_copy["Health"],"\nAttack:",Player_copy["Attack"],"\nDefense:",Player_copy["Defense"],"\nSpeed:",Player_copy["Speed"],"\nMagic Density:",Player_copy["Magic Density"],"\nStamina:",Player_copy["Stamina"],"\nCritical Chance:",Player_copy["Critical Chance"],"\nCritical Damage:",Player_copy["Critical Damage"],"\nEvasion:",Player_copy["Evasion"],"\nAccuracy:",Player_copy["Accuracy"],"\nMana:",Player_copy["Mana"],"\nTower Completion:",Player_copy["Tower Level"])
                        print("\n\nInventory\n---------------")
                        for key,value in inventory.items():
                            print(key,":",value,"\n")
                        back = input("---------------\n\nPress enter to return\n\n")
                    if battle_choice in ["retreat","r","3"]:
                        x = random.randint(1,5)
                        if x == 1:
                            print("Escape successful!\n")
                            Battle_End = True
                            continue
                        else:
                            print("It failed...\n")
                            break
            print(f"\n---------------\n",Enemy1["Type"]," turn\n---------------\n")
            if Evasion1_Stopper == False:
                Enemy1["Evasion"] -= 10
            if Defense1_Stopper == False:
                Enemy1["Defense"] -= 10
                              

            if Enemy1_Skip == False:
                Evasion1_Stopper = False
                Defense1_Stopper = False
                Attack_Weight = 0
                Defense_Weight = 0
                Evasion_Weight = 0
                Spell_Caster = False

                
                if Enemy1["Category"] == "Undead":
                    Attack_Weight += 3
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.3):
                        Defense_Weight += 2
                        Evasion_Weight += 2
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                        
                if Enemy1["Category"] == "Humanoid":
                    Attack_Weight += 3
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.5):
                        Defense_Weight += 3
                        Evasion_Weight += 2
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                        
                if Enemy1["Category"] == "Demon":
                    Attack_Weight += 4
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.5):
                        Defense_Weight += 2
                        Evasion_Weight += 2
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                        
                if Enemy1["Category"] == "Beast":
                    Attack_Weight += 3
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.25):
                        Defense_Weight += 2
                        Evasion_Weight += 3
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                        
                if Enemy1["Category"] == "Abberation":
                    Attack_Weight += 2
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.4):
                        Defense_Weight += 3
                        Evasion_Weight += 2
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                if Enemy1["Category"] == "Construct":
                    Attack_Weight += 3
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.6):
                        Defense_Weight += 4
                        Evasion_Weight += 2
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                if Enemy1["Category"] == "Elemental":
                    Attack_Weight += 4
                    if Enemy1["Health"] < (Enemy1["Max Health"] * 0.5):
                        Defense_Weight += 2
                        Evasion_Weight += 2
                    if Enemy1["Stamina"] <= 0:
                        Attack_Weight = -100
                if Enemy1["Behaviour"] == "Aggressive":
                    Attack_Weight += 2
                if Enemy1["Behaviour"] == "Defensive":
                    Defense_Weight +=2
                if Enemy1["Behaviour"] == "Evasive":
                    Evasion_Weight += 3
                if Enemy1["Spell Caster"] == True:
                    Spell_Caster = random.choice([False,True])
                variance = random.choice(["Attack","Defense","Evasion"])
                if variance == "Attack":
                    Attack_Weight += 3
                if variance == "Defense":
                    Defense_Weight +=1
                if variance == "Evasion":
                    Evasion_Weight +=1
                Action = max(Evasion_Weight,Attack_Weight,Defense_Weight)

                if Action == Attack_Weight:
                    if Spell_Caster == True:
                        if Enemy1["Mana"] > 50:
                            Damage = int( 25   * Enemy1["Magic Damage"]    * (1 / (10 + Player_copy["Defense"]))    * (1 + Enemy1["Magic Density"] / 100))
                            Damage = round(Damage)
                            Enemy1["Mana"] -= 50
                            Player_copy["Health"] -= Damage
                            print(f"\n",Enemy1["Type"],f" casts mana blast at  {name}\n")
                            print(f"\n\n",Damage,"Damage done\n")
                        else:
                            print("\nThe enemy does not have enough mana\n")
                    if Enemy1["Spell Caster"] == False:
                        if (Enemy1["Stamina"] > 50 or Enemy1_Category == "Undead"):
                            Damage = int( 25 * Enemy1["Attack"]* (1 / (10 + Player_copy["Defense"])))
                            Damage = round(Damage)
                            Enemy1["Stamina"] -= 50
                            Player_copy["Health"] -= Damage
                            print(f"\n",Enemy1["Type"],f" strikes {name}\n")
                            print(f"\n\n",Damage,"Damage done\n")
                        else:
                            print("\nThe enemy does not have enough stamina\n")
                elif Action == Defense_Weight:
                    if Enemy1["Mana"] > 10:
                        Heal = (1+ (Enemy1["Max Health"]* 0.05))
                        Heal = round(Heal)
                        Enemy1["Mana"] -= 10
                        Enemy1["Health"] += Heal
                        print(f"\n{Enemy1_Type} casts a heal spell\n")
                        print(f"\n+ {Heal} health\n")
                        
                    else:
                        print(f"\n",Enemy1["Type"]," does not have enough mana to cast a heal spell\n")
                        print(f"\n",Enemy1["Type"]," braces to withstand your next attack\n")
                        Enemy1["Defense"] += 10
                        Defense1_Stopper = True
                elif Action == Evasion_Weight:
                    Enemy1["Evasion"] += 10
                    print(f"\n",Enemy1["Type"]," moves away growing wary\n")
                    print("+ 10 Evasion")
                    Evasion1_Stopper = True
            else:
                print(Enemy1["Type"]," is stunned!")
                

            print(f"\n---------------\n Turn End\n---------------\n")
            if Enemy1["Health"] <= 0 and check1 == True:
                Enemy1["Health"] = 0
                xp_gained = Enemy1["XP"] * (Enemy1["Level"] /2)
                xp_gained = round(xp_gained)
                Player["XP"] += xp_gained
                print(f"\n",Enemy3["Type"]," has been killed\n\n")
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
                Enemies_Killed += 1

                
                if (Enemy1["Health"] <= 0):
                    Battle_End = True
                    Outcome = "Player Win"
                    continue
                
                if Player_copy["Health"] <= 0:
                    Outcome = "Enemy Win"
                    continue
        return Outcome,Player["XP"],Enemies_Killed
