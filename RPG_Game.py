import json
import random
import time
from Text_Writing_Style import TypeWriter as TW
from Tower_Levels_abs import Tower as T
from Arena import Arena as A
import sys
import copy
import builtins
tw = TW(delay=0.02, jitter=True)
leave = False
skill_points = 2
typewriter = False

def print(*args, sep=" ", end="\n"):
    if typewriter:
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
    else:
        builtins.print(*args, sep=sep, end=end)
        

Player = {"XP":0,"XP Needed":100,"Max Health":100,"Health":100,"Attack":10,"Defense":10,"Speed":10,"Magic Density":10,"Magic Damage":10,"Level":1,"Stamina":500,"Critical Chance":5,"Critical Damage":125,"Evasion":2,"Accuracy":75,"Mana":0,"Tower Level":1,"Buff":{"Type":"None","Value":5,"Duration":3},"Title":"None","Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0} },"Gold":0,"Title":"None"}
    

Game = {"Current Effect":{"Type":"None","Value":5,"Duration":3}}

Gear = {"Type":{"Helmet":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Shoulderwear":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Armwear":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Chestplate":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Legwear":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Footwear":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Weapon":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}},"Offhand":{"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}}}
Spell_list = {"Mana Blast":{"Damage": 20,"Cost":35,"Level":"Starter","Weight":"Medium","Time":0.5}}
Skills = {"Mana Blast":{"Damage":20,"Cost":35,"Level":"Starter","Weight":"Medium","Time":0.5},"Fireball":{"Damage":55,"Cost":70,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Straight Punch":{"Damage":20,"Cost":25,"Level":"Starter","Weight":"Medium","Time":0.5},"Headbutt":{"Damage":75,"Cost":60,"Level":"Not Learned","Weight":"Heavy","Time":1},"Axe Kick":{"Damage":90,"Cost":75,"Level":"Not Learned","Weight":"Heavy","Time":1},"Analyse":{"Power":30,"Cost":40,"Level":"Not Learned","Time":0.5},"Heal":{"Power":45,"Cost":80,"Level":"Not Learned","Time":0.5},"Spinning Back Kick":{"Damage":110,"Cost":90,"Level":"Not Learned","Weight":"Heavy","Time":1},"Ice Shard":{"Damage":50,"Cost":65,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Shock":{"Damage":45,"Cost":55,"Level":"Not Learned","Weight":"Medium","Time":0.5},"River Fist":{"Damage":60,"Cost":60,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Mud Shot":{"Damage":40,"Cost":45,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Life Drain":{"Damage":45,"Cost":75,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Purify":{"Damage":35,"Cost":50,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Domination":{"Power": 0,"Cost": 120,"Level":"Not Learned","Weight":"Heavy","Time":1},"Grappling Vines":{"Damage":0,"Cost":75,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Stone Slipstream":{"Damage":70,"Cost":80,"Level":"Not Learned","Weight":"Heavy","Time":1},"Corrupting Touch":{"Damage":65,"Cost":90,"Level":"Not Learned","Weight":"Medium","Time":0.5},"Impulsive Swing":{"Damage":120,"Cost":100,"Level":"Starter","Weight":"Heavy","Time":1},"Jab":{"Damage":18,"Cost":5,"Level":"Not Learned","Weight":"Light","Time":0.1},"Bite":{"Damage":40,"Cost":20,"Level":"Starter","Weight":"Medium","Time":0.5},"Devour Essence":{"Power":80,"Cost":120,"Level":"Not Learned","Weight":"Heavy","Time":0.5},"Front Kick":{"Damage":35,"Cost":20,"Level":"Starter","Weight":"Heavy","Time":0.5},"Aimed Shot":{"Damage":40,"Cost":25,"Level":"Starter","Weight":"Heavy","Time":0.5},"Tackle":{"Damage":35,"Cost":25,"Level":"Starter","Weight":"Heavy","Time":0.5},"Tackle":{"Damage":35,"Cost":25,"Level":"Starter","Weight":"Heavy","Time":0.5},"Toxin Spray":{"Damage":30,"Cost":45,"Level":"Not Learned","Weight":"Heavy","Time":0.5},"Tackle":{"Damage":35,"Cost":25,"Level":"Starter","Weight":"Heavy","Time":0.5},"Groundbreaker":{"Damage":75,"Cost":80,"Level":"Not Learned","Weight":"Heavy","Time":1},"Groundbreaker":{"Damage":75,"Cost":80,"Level":"Not Learned","Weight":"Heavy","Time":1},"Tremor":{"Damage":75,"Cost":80,"Level":"Not Learned","Weight":"Heavy","Time":1},"Empower":{"Power":45,"Cost":80,"Level":"Starter","Time":0.5}}
Combat_Skill_list = {"Straight Punch":{"Damage":20,"Cost":25,"Level":"Starter","Weight":"Medium","Time":0.5},"Bite":{"Damage":40,"Cost":20,"Level":"Starter","Weight":"Medium","Time":0.5},"Quick Stab":{"Damage":45,"Cost":40,"Level":"Starter","Weight":"Heavy","Time":0.5},"Slash":{"Damage":60,"Cost":55,"Level":"Starter","Weight":"Heavy","Time":1},"Front Kick":{"Damage":35,"Cost":20,"Level":"Starter","Weight":"Heavy","Time":0.5},"Aimed Shot":{"Damage":25,"Cost":50,"Level":"Starter","Weight":"Heavy","Time":0.5},"Tackle":{"Damage":25,"Cost":50,"Level":"Tackle","Weight":"Medium","Time":0.5},"Impulsive Swing":{"Damage":120,"Cost":100,"Level":"Starter","Weight":"Heavy","Time":1}}
Body_Condition = {"Biceps":{"Strength":5},"Triceps":{"Strength":5},"Hands":{"Strength":5},"Shoulders":{"Strength":5},"Chest":{"Strength":5},"Trapezius":{"Strength":5},"Abdomen":{"Strength":5},"Back":{"Strength":5},"Legs":{"Strength":5},"Head":{"Strength":5}}
Base_Stats = {"XP":0,"XP Needed":100,"Max Health":100,"Health":100,"Attack":10,"Defense":10,"Speed":10,"Magic Density":10,"Magic Damage":10,"Level":1,"Stamina":500,"Critical Chance":5,"Critical Damage":125,"Evasion":2,"Accuracy":75,"Mana":0,"Tower Level":1,"Buff":{"Type":"None","Value":5,"Duration":3}}
treasure_list = ["Wood","Stone","Cloth","Glass","Spirit Essence","String","Healing Herb","Mana Herb","Bitter Herb","Coal"]
inventory = {"Orc Tusk":5,"Galvano Flower":5,"Gear":["Copper Dagger"],"Potions":[]}
Skill_Tree = {"General": {"Advanced Mind":{"Status":"(Locked)"},"Bloodthirsty":{"Status":"(Locked)"},"Momentum":{"Status":"(Locked)"},"Arcane Echo":{"Status":"(Locked)"},"Fast Recovery":{"Status":"(Locked)"},"Meditative Mind":{"Status":"(Locked)"},"Strong Body":{"Status":"(Locked)"}},"Training": { "Lock": "(Locked)","Lightweight": {"Status": "(Locked)"},"Running": {"Status": "(Locked)"}, "Sword Swing": {"Status": "(Locked)"}, "Weight Carry": {"Status": "(Locked)"}, "Dead Hang": {"Status": "(Locked)"}, "Neck Bridge": {"Status": "(Locked)"}, "Push Up": {"Status": "(Locked)"}} ,"Smithing": { "Lock": "(Locked)","Apprenticeship": {"Status": "(Locked)"},"Hit em": {"Status": "(Locked)"}, "Skill 3": {"Status": "(Locked)"}} ,"Alchemy": { "Lock": "(Locked)","Scientific Cooking": {"Status": "(Locked)"},"Skill 2": {"Status": "(Locked)"}, "Skill 3": {"Status": "(Locked)"}}}
Unlocked_Functions = {"Training":{"Status": "(Locked)"},"Smithing":{"Status":"(Locked)"},"Alchemy":{"Status":"(Locked)"}}
name = "player"
Move_Set = ()
Memory = 4
Chest_items = {"Skill Books":["Fireball","Headbutt","Axe Kick","Analysis","Heal","Grappling Vines","River Fist","Shock","Life Drain","Devour Essence","Purify","Spinning Back Kick","Ice Shard","Mud Shot","Tremor","Groundbreaker","Jab","Stone Slipstream","Domination","Corrupting Touch","Toxin Spray","Empower"],"Gear":{"Common":[""],"Uncommon":[""]}}
Say = True
Max_Limit = 25
Weapon_Name = ""
Helmet_Name = ""
Shoulderwear_Name = ""
Armwear_Name = ""
Chestplate_Name = ""
Legwear_Name = ""
Footwear_Name = ""
Skill_Books = {"Fireball":False,"Headbutt":False,"Axe Kick":False,"Analysis":False,"Heal":False,"Grappling Vines":False,"River Fist":False,"Shock":False,"Life Drain":False,"Devour Essence":False,"Purify":False,"Spinning Back Kick":False,"Ice Shard":False,"Mud Shot":False,"Tremor":False,"Groundbreaker":False,"Jab":False,"Stone Slipstream":False,"Domination":False,"Corrupting Touch":False,"Toxin Spray":False,"Empower":False}
Statistics = {"Battles Fought": 0,"Battles Won":0,"Battles Lost":0,"Enemies Killed":0,"Damageless Battles Won":0,"Bosses Killed":0,"Training Sessions":0,"Gold Earned":0,"Gold Spent":0,"Health Healed":0,"Gear Forged":0,"Potions Brewed":0}
Amount_Practiced = {"Fireball":0,"Headbutt":0,"Axe Kick":0,"Analysis":0,"Heal":0,"Grappling Vines":0,"River Fist":0,"Shock":0,"Life Drain":0,"Devour Essence":0,"Purify":0,"Spinning Back Kick":0,"Ice Shard":0,"Mud Shot":0,"Tremor":0,"Groundbreaker":0,"Jab":0,"Stone Slipstream":0,"Domination":0,"Corrupting Touch":0,"Toxin Spray":0,"Empower":0,"Straight Punch":0,"Front Kick":0,"Bite":0,"Aimed Shot":0,"Slash":0,"Quick Stab":0,"Tackle":0,"Mana Blast":0}
Proficiency = {"Sword":"Starter","Greatsword":"Starter","Dagger":"Starter","Spear":"Starter","Staff":"Starter","Wand":"Starter","Axe":"Starter","Mace":"Starter","Bow":"Starter"}
Amount_Used = {"Sword":0,"Greatsword":0,"Dagger":0,"Spear":0,"Staff":0,"Wand":0,"Axe":0,"Mace":0,"Bow":0}
Quests = {"Novice Slayer":"(Incomplete)","Veteran Slayer":"(Incomplete)","Legendary Slayer":"(Incomplete)","Well Built":"(Incomplete)","Peak Physique":"(Incomplete)","Recruit":"(Incomplete)","Fighter":"(Incomplete)","Veteran":"(Incomplete)","Battle-Hardened":"(Incomplete)","Seasoned Warrior":"(Incomplete)","Elite Combatant":"(Incomplete)","Champion":"(Incomplete)","Warlord":"(Incomplete)","Conqueror":"(Incomplete)","Living Legend":"(Incomplete)","Eternal Warrior":"(Incomplete)","Winner":"(Incomplete)","The Professional":"(Incomplete)","Indomitable":"(Incomplete)","Unstoppable Force":"(Incomplete)","The One Above All":"(Incomplete)","Loser":"(Incomplete)","Scarred":"(Incomplete)","Tenacious":"(Incomplete)","The Immovable":"(Incomplete)","The Ever Enduring":"(Incomplete)","Unscathed":"(Incomplete)","Flawless Victor":"(Incomplete)","Phantom Menace":"(Incomplete)","Untouchable Duelist":"(Incomplete)","The Peerless Champion":"(Incomplete)","Boss Demolisher":"(Incomplete)","Giant Annihilator":"(Incomplete)","The Bane Of Titans":"(Incomplete)","Legend Hunter":"(Incomplete)","One Of The Greats":"(Incomplete)","Penny Pincher":"(Incomplete)","Hoarder":"(Incomplete)","Noble":"(Incomplete)","Tycoon":"(Incomplete)","Midas":"(Incomplete)","Spender":"(Incomplete)","Big Spender":"(Incomplete)","High Roller":"(Incomplete)","Deep Pockets":"(Incomplete)","Patron Of Treasure":"(Incomplete)","Trainee":"(Incomplete","Dedicated":"(Incomplete)","Fanatic Trainer":"(Incomplete)","Tireless":"(Incomplete)","Pillar Of Discipline":"(Incomplete)","Virile":"(Incomplete)","Hearty":"(Incomplete)","Bulky":"(Incomplete)","Behemoth":"(Incomplete)","The Jade Emperor":"(Incomplete)","Forgehand":"(Incomplete)","Skilled Blacksmith":"(Incomplete)","Elite Craftsmen":"(Incomplete)","Master Of Metal":"(Incomplete)","Artificer Of Legend":"(Incomplete)","Herbalist":"(Incomplete)","Elixir Maker":"(Incomplete)","Skilled Alchemist":"(Incomplete)","Grandmaster Brewer":"(Incomplete)","The One Who Knocks":"(Incomplete)"}
Titles = []

def save_game(Say):

    data = {
    "Player": Player,
    "Base_Stats": Base_Stats,
    "Body_Condition": Body_Condition,
    "Gear": Gear,
    "Inventory": inventory,
    "Skill_Tree": Skill_Tree,
    "Unlocked_Functions": Unlocked_Functions,
    "Skill_Points": skill_points,
    "Name":name,
    "Skills":Skills,
    "Spell List":Spell_list,
    "Combat Skill List":Combat_Skill_list,
    "Move Set":Move_Set,
    "Memory":Memory,
    "Max Limit":Max_Limit,
    "Statistics":Statistics,
    "Skill Books": Skill_Books,
    "Amount Practiced": Amount_Practiced,
    "Weapon Name": Weapon_Name,
    "Helmet Name": Helmet_Name,
    "Shoulderwear Name":Shoulderwear_Name,
    "Armwear Name": Armwear_Name,
    "Chestplate Name":Chestplate_Name,
    "Legwear Name":Legwear_Name,
    "Footwear Name": Footwear_Name,
    "Proficiency": Proficiency,
    "Amount Used": Amount_Used,
    "Quests": Quests,
    "Titles": Titles,
    "Typewriter": typewriter
    
    
}

    with open("SaveGame.json", "w") as file:
        json.dump(data, file, indent=4)

    if Say == True:
        print("\nGame saved.\n")

def load_game():

    global name, Skills, Spell_list, Combat_Skill_list,Base_Stats,Body_Condition,Gear
    global Move_Set, Memory, Max_Limit, Statistics,skill_points,inventory,Skill_Tree,Unlocked_Functions

    try:
        with open("SaveGame.json", "r") as file:
            data = json.load(file)

        Player = data["Player"]
        Base_Stats = data["Base_Stats"]
        Body_Condition = data["Body_Condition"]
        Gear = data["Gear"]
        inventory = data["Inventory"]
        Skill_Tree = data["Skill_Tree"]
        Unlocked_Functions = data["Unlocked_Functions"]
        skill_points = data["Skill_Points"]
        name = data["Name"]
        Skills = data["Skills"]
        Spell_list = data["Spell List"]
        Combat_Skill_list = data["Combat Skill List"]
        Move_Set = data["Move Set"]
        Memory = data["Memory"]
        Max_Limit = data["Max Limit"]
        Statistics = data["Statistics"]
        Skill_Books = data["Skill Books"]
        Amount_Practiced = data["Amount Practiced"]
        Weapon_Name = data["Weapon Name"]
        Helmet_Name = data["Helmet Name"]
        Shoulderwear_Name = data["Shoulderwear Name"]
        Armwear_Name = data["Armwear Name"]
        Chestplate_Name = data["Chestplate Name"]
        Legwear_Name = data["Legwear Name"]
        Footwear_Name = data["Footwear Name"]
        Proficency = data["Proficiency"]
        Amount_Used = data["Amount Used"]
        Quests = data["Quests"]
        Titles = data["Titles"]
        typewriter = data["Typewriter"]
        
        print("\nGame loaded.\n")

    except FileNotFoundError:
        print("\nNo save file found.\n")

while leave == False:
    if name != "player":
        Say = True
        save_game(Say)
    Enemy = {
        "Tier 1":{

            "Skeleton":{"XP":20,"Max Health":random.randint(75,90),"Health":80,"Attack":random.randint(11,15),"Defense":random.randint(8,10),"Speed":random.randint(8,10),"Magic Density":random.randint(10,11),"Magic Damage":random.randint(8,10),"Level":1,"Stamina":random.randint(400,500),"Critical Chance":random.randint(4,5),"Critical Damage":random.randint(120,130),"Evasion":random.randint(3,5),"Accuracy":random.randint(80,85),"Mana":random.randint(10,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Bones"],"Category":"Undead","Behaviour":"Defender","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Skeleton","Ability":"None","Attribute":"None"},
            "Orc Warrior":{"XP":100,"Max Health":random.randint(130,160),"Health":150,"Attack":random.randint(18,21),"Defense":random.randint(12,16),"Speed":random.randint(7,8),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(500,750),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,145),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(0,5),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Orc Tusk"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Orc Warrior","Ability":"None","Attribute":"None"},
            "Wolf":{"XP":35,"Max Health":random.randint(65,80),"Health":70,"Attack":random.randint(13,15),"Defense":random.randint(8,10),"Speed":random.randint(12,14),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(400,700),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(85,90),"Mana":random.randint(0,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Wolf Pelt"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Wolf","Ability":"None","Attribute":"None"},
            "Bandit":{"XP":40,"Max Health":random.randint(80,100),"Health":85,"Attack":random.randint(13,15),"Defense":random.randint(6,10),"Speed":random.randint(10,12),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(10,12),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(4,7),"Accuracy":random.randint(80,90),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Cape Cloth"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bandit","Ability":"None","Attribute":"None"},
            "Zombie":{"XP":55,"Max Health":random.randint(130,155),"Health":140,"Attack":random.randint(14,16),"Defense":random.randint(14,16),"Speed":random.randint(7,8),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(750,775),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,135),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(0,10),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rotting Flesh"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Zombie","Ability":"None","Attribute":"None"},
            "Goblin":{"XP":25,"Max Health":random.randint(60,80),"Health":65,"Attack":random.randint(13,16),"Defense":random.randint(9,12),"Speed":random.randint(12,15),"Magic Density":random.randint(7,11),"Magic Damage":random.randint(7,14),"Level":1,"Stamina":random.randint(400,650),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(140,155),"Evasion":random.randint(6,7),"Accuracy":random.randint(80,90),"Mana":random.randint(20,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Goblin Ear"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Goblin","Ability":"None","Attribute":"None"},
            "Kobold":{"XP":15,"Max Health":random.randint(60,80),"Health":70,"Attack":random.randint(10,15),"Defense":random.randint(7,10),"Speed":random.randint(15,16),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,10),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(80,90),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Kobold Fang"],"Category":"Humanoid","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Kobold","Ability":"None","Attribute":"None"},
            "Cultist":{"XP":60,"Max Health":random.randint(70,85),"Health":75,"Attack":random.randint(11,15),"Defense":random.randint(7,12),"Speed":random.randint(11,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,450),"Critical Chance":random.randint(3,8),"Critical Damage":random.randint(120,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,85),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dark Robe Fabric"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Cultist","Ability":"None","Attribute":"None"},
            "Ghost":{"XP":75,"Max Health":random.randint(60,80),"Health":75,"Attack":random.randint(1,5),"Defense":random.randint(10,12),"Speed":random.randint(12,16),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(325,375),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(120,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(80,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Souls"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ghost","Ability":"None","Attribute":"None"},
            "Imp":{"XP":40,"Max Health":random.randint(60,80),"Health":65,"Attack":random.randint(10,16),"Defense":random.randint(8,11),"Speed":random.randint(14,17),"Magic Density":random.randint(12,16),"Magic Damage":random.randint(14,16),"Level":1,"Stamina":random.randint(550,750),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(75,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Demon Ash"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Imp","Ability":"None","Attribute":"None"},
            "Gladiator":{"XP":110,"Max Health":random.randint(110,140),"Health":130,"Attack":random.randint(16,19),"Defense":random.randint(12,16),"Speed":random.randint(11,15),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,11),"Level":1,"Stamina":random.randint(700,750),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(130,140),"Evasion":random.randint(5,6),"Accuracy":random.randint(80,90),"Mana":random.randint(20,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Arena Blade"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Gladiator","Ability":"None","Attribute":"None"},
            "Executioner":{"XP":65,"Max Health":random.randint(90,120),"Health":160,"Attack":random.randint(15,17),"Defense":random.randint(10,13),"Speed":random.randint(8,10),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(7,10),"Level":1,"Stamina":random.randint(400,600),"Critical Chance":random.randint(10,12),"Critical Damage":random.randint(140,155),"Evasion":random.randint(2,4),"Accuracy":random.randint(88,90),"Mana":random.randint(1,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Execution Axe"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Executioner","Ability":"None","Attribute":"None"},
            "Scavenger":{"XP":20,"Max Health":random.randint(70,90),"Health":85,"Attack":random.randint(10,12),"Defense":random.randint(8,11),"Speed":random.randint(12,15),"Magic Density":random.randint(8,10),"Magic Damage":random.randint(8,10),"Level":1,"Stamina":random.randint(500,600),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(80,90),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Scrap"],"Category":"Human","Behaviour":"Opportunist","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Scavenger","Ability":"None","Attribute":"None"},
            "Berserker":{"XP":90,"Max Health":random.randint(140,155),"Health":160,"Attack":random.randint(15,18),"Defense":random.randint(15,19),"Speed":random.randint(8,10),"Magic Density":random.randint(7,11),"Magic Damage":random.randint(7,11),"Level":1,"Stamina":random.randint(550,600),"Critical Chance":random.randint(2,4),"Critical Damage":random.randint(120,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(10,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Berserker Claw"],"Category":"Human","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Berserker","Ability":"None","Attribute":"None"},
            "Homunculus":{"XP":60,"Max Health":random.randint(65,155),"Health":150,"Attack":random.randint(10,17),"Defense":random.randint(7,16),"Speed":random.randint(7,16),"Magic Density":random.randint(7,16),"Magic Damage":random.randint(7,16),"Level":1,"Stamina":random.randint(325,775),"Critical Chance":random.randint(3,8),"Critical Damage":random.randint(120,155),"Evasion":random.randint(2,8),"Accuracy":random.randint(75,90),"Mana":random.randint(0,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Homunculus Core"],"Category":"Experiment","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Homunculus","Ability":"None","Attribute":"None"},
            "Goblin Archer": {"XP": 35, "Max Health": random.randint(65,90), "Health": 55, "Attack": random.randint(14,17), "Defense": random.randint(12,15), "Speed": random.randint(14,17), "Magic Density": random.randint(7,11), "Magic Damage": random.randint(7,11), "Level": 1, "Stamina": random.randint(500,600), "Critical Chance": random.randint(6,8), "Critical Damage": random.randint(140,155), "Evasion": random.randint(7,8), "Accuracy": random.randint(80,85), "Mana": random.randint(0,25), "Buff": {"Type": "None", "Value": 0, "Duration": 0}, "Drop": ["Goblin Bow", "Arrow Bundle"], "Category": "Humanoid", "Behaviour": "Evasive", "Spell Caster": False, "Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Goblin Archer","Ability":"None","Attribute":"None"},
            "Spearman":{"XP":50,"Max Health":random.randint(100,120),"Health":85,"Attack":random.randint(15,18),"Defense":random.randint(10,13),"Speed":random.randint(13,16),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(7,10),"Level":1,"Stamina":random.randint(650,750),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(130,145),"Evasion":random.randint(5,6),"Accuracy":random.randint(80,90),"Mana":random.randint(0,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Iron Spear"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Spearman","Ability":"None","Attribute":"None"},
            "Lost Traveler Spirit":{"XP":80,"Max Health":random.randint(60,100),"Health":80,"Attack":random.randint(1,5),"Defense":random.randint(10,15),"Speed":random.randint(12,18),"Magic Density":random.randint(12,16),"Magic Damage":random.randint(12,16),"Level":1,"Stamina":random.randint(350,500),"Critical Chance":random.randint(4,8),"Critical Damage":random.randint(130,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(75,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Traveler's Remains","Ethereal Dust"],"Category":"Spirit","Behaviour":"Wanderer","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Lost Traveler Spirit","Ability":"None","Attribute":"None"},
            "Summoner":{"XP":65,"Max Health":random.randint(100,125),"Health":90,"Attack":random.randint(11,14),"Defense":random.randint(10,15),"Speed":random.randint(8,11),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(14,16),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(130,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Summoning Tome","Mana Crystal"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Summoner","Ability":"None","Attribute":"None"},
            "Summoned Demon":{"XP":145,"Max Health":random.randint(130,140),"Health":200,"Attack":random.randint(16,18),"Defense":random.randint(14,16),"Speed":random.randint(10,15),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(400,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(80,90),"Mana":random.randint(30,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Demon Essence","Summoning Sigil"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Summoned Demon","Ability":"None","Attribute":"None"},
            "War Hound":{"XP":55,"Max Health":random.randint(90,110),"Health":95,"Attack":random.randint(15,18),"Defense":random.randint(8,10),"Speed":random.randint(12,14),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(130,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(80,85),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Hound Fang","Hound Fur"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"War Hound","Ability":"None","Attribute":"None"},
            "Goblin Fighter":{"XP":35,"Max Health":random.randint(70,90),"Health":75,"Attack":random.randint(15,17),"Defense":random.randint(9,12),"Speed":random.randint(16,17),"Magic Density":random.randint(6,7),"Magic Damage":random.randint(6,7),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(150,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(85,90),"Mana":random.randint(15,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Goblin Ear","Rusty Dagger"],"Category":"Goblin","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Goblin Fighter","Ability":"None","Attribute":"None"},
            "Tower Apprentice":{"XP":40,"Max Health":random.randint(70,90),"Health":80,"Attack":random.randint(10,12),"Defense":random.randint(7,11),"Speed":random.randint(10,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(130,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(87,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Apprentice Robe","Mana Crystal"],"Category":"Mage","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Tower Apprentice","Ability":"None","Attribute":"None"},
            "Ambush Rogue":{"XP":55,"Max Health":random.randint(75,85),"Health":72,"Attack":random.randint(18,20),"Defense":random.randint(10,12),"Speed":random.randint(15,16),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(600,750),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(88,90),"Mana":random.randint(10,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dagger","Smoke Bomb"],"Category":"Humanoid","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ambush Rogue","Ability":"None","Attribute":"None"},
            "Blood Knight":{"XP":220,"Max Health":random.randint(130,155),"Health":220,"Attack":random.randint(11,18),"Defense":random.randint(15,17),"Speed":random.randint(7,10),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(9,13),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,155),"Evasion":random.randint(3,4),"Accuracy":random.randint(75,90),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Blood Sword","Knights Emblem"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Blood Knight","Ability":"None","Attribute":"None"},
            "Duelist":{"XP":200,"Max Health":random.randint(110,130),"Health":170,"Attack":random.randint(15,18),"Defense":random.randint(12,15),"Speed":random.randint(10,15),"Magic Density":random.randint(8,9),"Magic Damage":random.randint(8,10),"Level":1,"Stamina":random.randint(600,755),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(130,145),"Evasion":random.randint(5,7),"Accuracy":random.randint(80,83),"Mana":random.randint(23,41),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rapier","Duelist Emblem"],"Category":"Human","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Duelist","Ability":"None","Attribute":"None"},
            "War Beast":{"XP":180,"Max Health":random.randint(120,130),"Health":280,"Attack":random.randint(15,19),"Defense":random.randint(7,9),"Speed":random.randint(9,11),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(25,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["War Beast Fang","Beast Hide"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"War Beast","Ability":"None","Attribute":"None"},
            "Blood Mage":{"XP":120,"Max Health":random.randint(75,95),"Health":170,"Attack":random.randint(10,14),"Defense":random.randint(8,12),"Speed":random.randint(10,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(350,450),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(85,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Blood Tome","Crimson Crystal"],"Category":"Human","Behaviour":"Tactical","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Blood Mage","Ability":"None","Attribute":"None"},
            "Slime":{"XP":25,"Max Health":random.randint(65,155),"Health":120,"Attack":random.randint(10,12),"Defense":random.randint(7,9),"Speed":random.randint(7,10),"Magic Density":random.randint(10,13),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(500,669),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,125),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(30,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Slime Gel","Sticky Residue"],"Category":"Beast","Behaviour":"Erratic","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Slime","Ability":"None","Attribute":"None"},
            "Arena Trainee":{"XP":120,"Max Health":random.randint(110,120),"Health":140,"Attack":random.randint(15,17),"Defense":random.randint(10,16),"Speed":random.randint(12,15),"Magic Density":random.randint(10,15),"Magic Damage":random.randint(10,15),"Level":1,"Stamina":random.randint(350,400),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(135,155),"Evasion":random.randint(3,6),"Accuracy":random.randint(80,90),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Training Token","Worn Gloves"],"Category":"Human","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Arena Trainee","Ability":"None","Attribute":"None"},
            "Traveler Bandit":{"XP":75,"Max Health":random.randint(90,120),"Health":45,"Attack":random.randint(13,16),"Defense":random.randint(8,10),"Speed":random.randint(11,13),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(7,10),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(130,150),"Evasion":random.randint(3,8),"Accuracy":random.randint(80,90),"Mana":random.randint(20,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Coin Pouch","Rusty Dagger","Traveler Cloak"],"Category":"Human","Behaviour":"Hunter","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Traveler Bandit","Ability":"None","Attribute":"None"},
            "Pit Dog":{"XP":110,"Max Health":random.randint(70,100),"Health":170,"Attack":random.randint(12,15),"Defense":random.randint(9,13),"Speed":random.randint(14,17),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(450,700),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,160),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,85),"Mana":random.randint(10,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dog Fang","Torn Hide"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Pit Dog","Ability":"None","Attribute":"None"},
            "Initiate Mage":{"XP":160,"Max Health":random.randint(90,105),"Health":120,"Attack":random.randint(10,14),"Defense":random.randint(11,15),"Speed":random.randint(9,14),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,650),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(120,155),"Evasion":random.randint(3,8),"Accuracy":random.randint(85,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Magic Tome","Apprentice Robe"],"Category":"Humanoid","Behaviour":"Caster","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Initiate Mage","Ability":"None","Attribute":"None"},
            "Eclipsed Artificer":{"Max Health":random.randint(140,155),"Health":210,"Attack":random.randint(16,19),"Defense":random.randint(12,16),"Speed":random.randint(12,14),"Magic Density":random.randint(16,17),"Magic Damage":random.randint(16,17),"Level":1,"Stamina":random.randint(450,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(88,90),"Mana":random.randint(45,50),"XP":120,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Broken Arcane Core"],"Category":"Construct","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Eclipsed Artificer","Ability":"None","Attribute":"None"},
            "Rogue Knight":{"XP":210,"Max Health":random.randint(110,150),"Health":140,"Attack":random.randint(15,19),"Defense":random.randint(12,13),"Speed":random.randint(11,15),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(600,800),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(3,8),"Accuracy":random.randint(85,90),"Mana":random.randint(0,10),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rogue Sword","Rusty Armor Fragment"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Rogue Knight","Ability":"None","Attribute":"None"},
            "Rogue Archer":{"XP":85,"Max Health":random.randint(75,90),"Health":75,"Attack":random.randint(16,19),"Defense":random.randint(7,10),"Speed":random.randint(15,16),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(89,90),"Mana":random.randint(0,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rogue Arrow","Light Bow"],"Category":"Humanoid","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Rogue Archer","Ability":"None","Attribute":"None"},
            "Rogue Fighter":{"XP":75,"Max Health":random.randint(100,110),"Health":120,"Attack":random.randint(15,18),"Defense":random.randint(10,11),"Speed":random.randint(12,14),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(550,775),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(140,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(85,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Steel Dagger","Light Armor","Rogue Emblem"],"Category":"Human","Behaviour":"Hunter","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Rogue Fighter","Ability":"None","Attribute":"None"},
            "Wind Spirit":{"XP":55,"Max Health":random.randint(70,100),"Health":90,"Attack":random.randint(12,15),"Defense":random.randint(10,13),"Speed":random.randint(16,20),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(400,600),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(88,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Wind Essence"],"Category":"Elemental","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Wind Spirit","Ability":"None","Attribute":"None"},
            "Dust Spirit":{"XP":60,"Max Health":random.randint(70,100),"Health":95,"Attack":random.randint(12,15),"Defense":random.randint(11,15),"Speed":random.randint(15,19),"Magic Density":random.randint(12,16),"Magic Damage":random.randint(12,16),"Level":1,"Stamina":random.randint(400,600),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(135,145),"Evasion":random.randint(5,7),"Accuracy":random.randint(85,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ritual Bone","Beast Heart"],"Category":"Beast","Behaviour":"Ritualistic","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Dust Spirit","Ability":"None","Attribute":"None"},
            "Broken Knight":{"XP":180,"Max Health":random.randint(140,155),"Health":1000,"Attack":random.randint(11,14),"Defense":random.randint(7,9),"Speed":random.randint(7,9),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(7,10),"Level":1,"Stamina":random.randint(325,450),"Critical Chance":random.randint(4,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(0,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Broken Sword","Broken Helmet"],"Category":"Humanoid","Behaviour":"Motionless","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Broken Knight","Ability":"None","Attribute":"None"},

           
            "Venom Spider":{"XP":25,"Max Health":random.randint(55,70),"Health":65,"Attack":random.randint(12,16),"Defense":random.randint(7,9),"Speed":random.randint(16,17),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(550,600),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(130,145),"Evasion":random.randint(5,8),"Accuracy":random.randint(85,90),"Mana":random.randint(10,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Venom Silk"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Venom Spider","Ability":"None","Attribute":"None"},
            "Swamp Rat":{"XP":20,"Max Health":random.randint(40,60),"Health":50,"Attack":random.randint(12,14),"Defense":random.randint(7,9),"Speed":random.randint(11,13),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(130,140),"Evasion":random.randint(6,8),"Accuracy":random.randint(82,85),"Mana":random.randint(20,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rat Tail"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Swamp Rat","Ability":"None","Attribute":"None"},
            "Bog Snake":{"XP":35,"Max Health":random.randint(70,90),"Health":85,"Attack":random.randint(12,16),"Defense":random.randint(8,10),"Speed":random.randint(10,15),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(85,90),"Mana":random.randint(15,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Snake Venom"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bog Snake","Ability":"None","Attribute":"None"},
            "Mud Crawler":{"XP":40,"Max Health":random.randint(80,110),"Health":95,"Attack":random.randint(11,14),"Defense":random.randint(10,15),"Speed":random.randint(7,8),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(550,750),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,3),"Accuracy":random.randint(80,85),"Mana":random.randint(10,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Mud Core"],"Category":"Beast","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Mud Crawler","Ability":"None","Attribute":"None"},
            "Poison Slime":{"XP":30,"Max Health":random.randint(65,155),"Health":110,"Attack":random.randint(10,12),"Defense":random.randint(7,9),"Speed":random.randint(7,10),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(9,13),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,145),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Slime Core"],"Category":"Slime","Behaviour":"Passive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Poison Slime","Ability":"None","Attribute":"None"},
            "Acid Slime":{"XP":30,"Max Health":random.randint(65,155),"Health":110,"Attack":random.randint(10,12),"Defense":random.randint(7,9),"Speed":random.randint(7,10),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(9,13),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,145),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Slime Core"],"Category":"Slime","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Acid Slime","Ability":"None","Attribute":"None"},
            "Swamp Goblin":{"XP":25,"Max Health":random.randint(65,80),"Health":60,"Attack":random.randint(13,16),"Defense":random.randint(9,14),"Speed":random.randint(11,14),"Magic Density":random.randint(9,14),"Magic Damage":random.randint(9,14),"Level":1,"Stamina":random.randint(500,600),"Critical Chance":random.randint(5,6),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,85),"Mana":random.randint(20,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Goblin Fang"],"Category":"Humanoid","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Swamp Goblin"},
            "Bog Serpent":{"XP":30,"Max Health":random.randint(55,70),"Health":60,"Attack":random.randint(14,16),"Defense":random.randint(9,11),"Speed":random.randint(14,17),"Magic Density":random.randint(9,12),"Magic Damage":random.randint(9,12),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,150),"Evasion":random.randint(6,8),"Accuracy":random.randint(85,90),"Mana":random.randint(15,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Serpent Fang"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bog Serpent","Ability":"None","Attribute":"None"},
            "Swamp Beast":{"XP":50,"Max Health":random.randint(110,130),"Health":120,"Attack":random.randint(15,19),"Defense":random.randint(14,16),"Speed":random.randint(8,11),"Magic Density":random.randint(8,11),"Magic Damage":random.randint(8,11),"Level":1,"Stamina":random.randint(650,700),"Critical Chance":random.randint(2,4),"Critical Damage":random.randint(130,150),"Evasion":random.randint(3,4),"Accuracy":random.randint(77,85),"Mana":random.randint(20,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Swamp Hide"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Swamp Beast","Ability":"None","Attribute":"None"},
            "Acid Beast":{"XP":60,"Max Health":random.randint(110,130),"Health":140,"Attack":random.randint(15,19),"Defense":random.randint(14,16),"Speed":random.randint(8,11),"Magic Density":random.randint(8,11),"Magic Damage":random.randint(8,11),"Level":1,"Stamina":random.randint(650,700),"Critical Chance":random.randint(2,4),"Critical Damage":random.randint(130,150),"Evasion":random.randint(3,4),"Accuracy":random.randint(77,85),"Mana":random.randint(20,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Acid Core","Corrosive Slime"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Acid Beast","Ability":"None","Attribute":"None"},
            "Toxic Elemental":{"XP":85,"Max Health":random.randint(90,125),"Health":180,"Attack":random.randint(13,15),"Defense":random.randint(12,14),"Speed":random.randint(12,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(14,16),"Level":1,"Stamina":random.randint(350,500),"Critical Chance":random.randint(3,7),"Critical Damage":random.randint(135,150),"Evasion":random.randint(6,8),"Accuracy":random.randint(80,87),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Toxic Core","Elemental Residue"],"Category":"Elemental","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Toxic Elemental","Ability":"None","Attribute":"None"},
            "Toxic Horror":{"XP":100,"Max Health":random.randint(120,145),"Health":190,"Attack":random.randint(16,20),"Defense":random.randint(14,16),"Speed":random.randint(8,10),"Magic Density":random.randint(10,13),"Magic Damage":random.randint(10,13),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(80,85),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Night Fang","Shadow Hide"],"Category":"Beast","Behaviour":"Hunter","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Toxic Horror","Ability":"None","Attribute":"None"},
            "Swamp Horror":{"XP":110,"Max Health":random.randint(120,145),"Health":190,"Attack":random.randint(16,20),"Defense":random.randint(14,16),"Speed":random.randint(8,10),"Magic Density":random.randint(10,13),"Magic Damage":random.randint(10,13),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(80,85),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Night Fang","Shadow Hide"],"Category":"Beast","Behaviour":"Hunter","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Swamp Horror","Ability":"None","Attribute":"None"},
            "Venom Wraith":{"XP":80,"Max Health":random.randint(110,125),"Health":180,"Attack":random.randint(8,11),"Defense":random.randint(11,14),"Speed":random.randint(13,15),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(500,650),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(88,90),"Mana":random.randint(20,45),"Buff":{"Type":"Magic Damage","Value":5,"Duration":2},"Drop":["Wraith Flame"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Venom Wraith","Ability":"None","Attribute":"None"},

            
            "Rot Beast":{"XP":55,"Max Health":random.randint(100,120),"Health":135,"Attack":random.randint(13,17),"Defense":random.randint(12,14),"Speed":random.randint(6,9),"Magic Density":random.randint(9,12),"Magic Damage":random.randint(9,12),"Level":1,"Stamina":random.randint(650,700),"Critical Chance":random.randint(4,5),"Critical Damage":random.randint(130,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rot Core"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Rot Beast","Ability":"None","Attribute":"None"},
            "Plague Spirit":{"XP":75,"Max Health":random.randint(90,110),"Health":100,"Attack":random.randint(11,14),"Defense":random.randint(13,14),"Speed":random.randint(7,8),"Magic Density":random.randint(11,15),"Magic Damage":random.randint(11,15),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(130,135),"Evasion":random.randint(5,7),"Accuracy":random.randint(80,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Plague Essence"],"Category":"Spirit","Behaviour":"Caster","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Plague Spirit","Ability":"None","Attribute":"None"},
            "Disease Demon":{"XP":85,"Max Health":random.randint(120,140),"Health":200,"Attack":random.randint(14,16),"Defense":random.randint(13,16),"Speed":random.randint(8,13),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(14,16),"Level":1,"Stamina":random.randint(400,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(80,90),"Mana":random.randint(30,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Demon Core"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Disease Demon","Ability":"None","Attribute":"None"},
            "Ruin Golem":{"XP":90,"Max Health":random.randint(140,145),"Health":240,"Attack":random.randint(15,19),"Defense":random.randint(14,15),"Speed":random.randint(7,8),"Magic Density":random.randint(11,15),"Magic Damage":random.randint(11,15),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ruin Core","Shattered Metal"],"Category":"Construct","Behaviour":"Defender","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ruin Golem","Ability":"None","Attribute":"None"},
            "Plague Crow":{"XP":35,"Max Health":random.randint(80,100),"Health":80,"Attack":random.randint(12,14),"Defense":random.randint(9,11),"Speed":random.randint(12,15),"Magic Density":random.randint(10,12),"Magic Damage":random.randint(10,12),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(6,7),"Critical Damage":random.randint(145,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(85,90),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Plague Feather"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Plague Crow","Ability":"None","Attribute":"None"},
            "Rot Walker":{"XP":40,"Max Health":random.randint(100,130),"Health":120,"Attack":random.randint(12,14),"Defense":random.randint(10,12),"Speed":random.randint(11,13),"Magic Density":random.randint(11,13),"Magic Damage":random.randint(11,13),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(130,140),"Evasion":random.randint(3,5),"Accuracy":random.randint(80,85),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rot Bone"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Rot Walker","Ability":"None","Attribute":"None"},
            "Ruin Rat":{"XP":25,"Max Health":random.randint(40,60),"Health":60,"Attack":random.randint(12,14),"Defense":random.randint(7,9),"Speed":random.randint(11,13),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(120,140),"Evasion":random.randint(6,8),"Accuracy":random.randint(82,85),"Mana":random.randint(20,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ruin Tail"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ruin Rat","Ability":"None","Attribute":"None"},
            "Ruin Wraith":{"XP":85,"Max Health":random.randint(110,130),"Health":230,"Attack":random.randint(8,9),"Defense":random.randint(13,15),"Speed":random.randint(13,16),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(130,140),"Evasion":random.randint(6,7),"Accuracy":random.randint(85,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ruin Essence","Broken Relic"],"Category":"Spirit","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ruin Wraith","Ability":"None","Attribute":"None"},
            "Bone Warrior":{"XP":60,"Max Health":random.randint(120,130),"Health":130,"Attack":random.randint(15,18),"Defense":random.randint(11,13),"Speed":random.randint(10,15),"Magic Density":random.randint(10,13),"Magic Damage":random.randint(10,13),"Level":1,"Stamina":random.randint(400,600),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(140,150),"Evasion":random.randint(4,6),"Accuracy":random.randint(85,90),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Bone Sword","Bone Shield"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bone Warrior","Ability":"None","Attribute":"None"},
            "Bone Dog":{"XP":35,"Max Health":random.randint(70,100),"Health":170,"Attack":random.randint(12,15),"Defense":random.randint(9,13),"Speed":random.randint(14,17),"Magic Density":random.randint(7,8),"Magic Damage":random.randint(7,8),"Level":1,"Stamina":random.randint(450,700),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,160),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,85),"Mana":random.randint(10,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Bone Fang","Bone Fragment"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bone Dog","Ability":"None","Attribute":"None"},
            "Bone Servant":{"XP":26,"Max Health":random.randint(60,80),"Health":70,"Attack":random.randint(10,12),"Defense":random.randint(7,10),"Speed":random.randint(8,11),"Magic Density":random.randint(8,11),"Magic Damage":random.randint(8,11),"Level":1,"Stamina":random.randint(350,500),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,85),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Bone Fragment","Old Cloth"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bone Servant","Ability":"None","Attribute":"None"},
            "Bone Golem":{"XP":95,"Max Health":random.randint(140,145),"Health":240,"Attack":random.randint(15,19),"Defense":random.randint(14,15),"Speed":random.randint(7,8),"Magic Density":random.randint(11,15),"Magic Damage":random.randint(11,15),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Bone Fragment","Golem Core"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bone Golem","Ability":"None","Attribute":"None"},
            
            "Ice Bat":{"XP":22,"Max Health":random.randint(45,65),"Health":55,"Attack":random.randint(12,14),"Defense":random.randint(7,8),"Speed":random.randint(13,15),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(350,550),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(140,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(85,90),"Mana":random.randint(30,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frozen Wing"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ice Bat","Ability":"None","Attribute":"None"},      
            "Frost Knight":{"XP":85,"Max Health":random.randint(125,140),"Health":140,"Attack":random.randint(16,19),"Defense":random.randint(13,15),"Speed":random.randint(8,9),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,5),"Accuracy":random.randint(86,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frost Blade"],"Category":"Undead","Behaviour":"Defender","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Frost Knight","Ability":"None","Attribute":"None"},
            "Ice Kobold":{"XP":15,"Max Health":random.randint(70,85),"Health":75,"Attack":random.randint(11,15),"Defense":random.randint(7,12),"Speed":random.randint(11,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,450),"Critical Chance":random.randint(3,8),"Critical Damage":random.randint(120,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,85),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ice Shard"],"Category":"Humanoid","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ice Kobold","Ability":"None","Attribute":"None"},
            "Frozen Skeleton":{"XP":35,"Max Health":random.randint(75,90),"Health":85,"Attack":random.randint(12,14),"Defense":random.randint(9,11),"Speed":random.randint(7,9),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(13,17),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(130,155),"Evasion":random.randint(2,6),"Accuracy":random.randint(75,90),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frozen Bone"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Frozen Skeleton","Ability":"None","Attribute":"None"},
            "Ice Archer":{"XP":50,"Max Health":random.randint(65,100),"Health":60,"Attack":random.randint(14,17),"Defense":random.randint(7,10),"Speed":random.randint(9,13),"Magic Density":random.randint(10,13),"Magic Damage":random.randint(10,13),"Level":1,"Stamina":random.randint(450,650),"Critical Chance":random.randint(3,8),"Critical Damage":random.randint(120,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,90),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ice Arrow"],"Category":"Elemental","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ice Archer","Ability":"None","Attribute":"None"},
            "Frost Walker":{"XP":45,"Max Health":random.randint(90,110),"Health":80,"Attack":random.randint(13,16),"Defense":random.randint(8,11),"Speed":random.randint(9,12),"Magic Density":random.randint(11,14),"Magic Damage":random.randint(11,14),"Level":1,"Stamina":random.randint(550,750),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,135),"Evasion":random.randint(2,5),"Accuracy":random.randint(80,86),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frost Core"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Frost Walker","Ability":"None","Attribute":"None"},
            "Frost Wolf":{"XP":30,"Max Health":random.randint(65,80),"Health":75,"Attack":random.randint(14,16),"Defense":random.randint(8,11),"Speed":random.randint(14,16),"Magic Density":random.randint(10,14),"Magic Damage":random.randint(10,14),"Level":1,"Stamina":random.randint(450,650),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(135,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(85,90),"Mana":random.randint(25,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frost Fang"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Frost Wolf","Ability":"None","Attribute":"None"},
            "Ice Slime":{"XP":25,"Max Health":random.randint(65,75),"Health":60,"Attack":random.randint(10,12),"Defense":random.randint(7,9),"Speed":random.randint(7,9),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(350,450),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frozen Slime Gel"],"Category":"Slime","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ice Slime","Ability":"None","Attribute":"None"},
            "Ice Golem":{"XP":80,"Max Health":random.randint(140,155),"Health":220,"Attack":random.randint(17,23),"Defense":random.randint(14,16),"Speed":random.randint(7,9),"Magic Density":random.randint(11,15),"Magic Damage":random.randint(11,15),"Level":1,"Stamina":random.randint(550,775),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,125),"Evasion":random.randint(2,3),"Accuracy":random.randint(80,90),"Mana":random.randint(20,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ice Core","Frozen Shard"],"Category":"Construct","Behaviour":"Defender","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ice Golem","Ability":"None","Attribute":"None"},
            "Frozen Warrior":{"XP":60,"Max Health":random.randint(125,145),"Health":140,"Attack":random.randint(17,19),"Defense":random.randint(12,14),"Speed":random.randint(11,13),"Magic Density":random.randint(11,15),"Magic Damage":random.randint(11,15),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(140,155),"Evasion":random.randint(5,6),"Accuracy":random.randint(88,90),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frozen Armor","Ice Blade"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Frozen Warrior","Ability":"None","Attribute":"None"},
            "Snow Stalker":{"XP":50,"Max Health":random.randint(110,125),"Health":110,"Attack":random.randint(12,15),"Defense":random.randint(9,12),"Speed":random.randint(13,16),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(145,155),"Evasion":random.randint(8,10),"Accuracy":random.randint(87,90),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frost Claw","Snow Pelt"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Snow Stalker","Ability":"None","Attribute":"None"},
            "Frozen Rat":{"XP":30,"Max Health":random.randint(40,60),"Health":60,"Attack":random.randint(12,14),"Defense":random.randint(7,9),"Speed":random.randint(11,13),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(120,140),"Evasion":random.randint(6,8),"Accuracy":random.randint(82,85),"Mana":random.randint(20,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frozen Tail"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Frozen Rat","Ability":"None","Attribute":"None"},
            "Snow Spider":{"XP":35,"Max Health":random.randint(80,105),"Health":65,"Attack":random.randint(11,15),"Defense":random.randint(7,10),"Speed":random.randint(11,14),"Magic Density":random.randint(10,15),"Magic Damage":random.randint(10,15),"Level":1,"Stamina":random.randint(350,400),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(7,8),"Accuracy":random.randint(85,90),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Frozen Silk","Ice Venom"],"Category":"Beast","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Snow Spider","Ability":"None","Attribute":"None"},

            "Lightning Phantom":{"XP":28,"Max Health":random.randint(75,90),"Health":60,"Attack":random.randint(12,15),"Defense":random.randint(9,12),"Speed":random.randint(13,15),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(4,9),"Critical Damage":random.randint(135,155),"Evasion":random.randint(4,7),"Accuracy":random.randint(88,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Spark Core"],"Category":"Elemental","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Lightning Phantom","Ability":"None","Attribute":"None"},     
            "Lightning Sprite":{"XP":28,"Max Health":random.randint(65,75),"Health":60,"Attack":random.randint(12,15),"Defense":random.randint(8,10),"Speed":random.randint(13,15),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,7),"Accuracy":random.randint(82,90),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Spark Core"],"Category":"Elemental","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Lightning Sprite","Ability":"None","Attribute":"None"},
            "Storm Knight":{"XP":95,"Max Health":random.randint(125,145),"Health":150,"Attack":random.randint(18,21),"Defense":random.randint(12,13),"Speed":random.randint(13,14),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(450,650),"Critical Chance":random.randint(4,8),"Critical Damage":random.randint(135,155),"Evasion":random.randint(2,8),"Accuracy":random.randint(85,90),"Mana":random.randint(30,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Storm Blade"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Storm Knight","Ability":"None","Attribute":"None"},
            "Storm Mage":{"XP":65,"Max Health":random.randint(75,100),"Health":85,"Attack":random.randint(8,12),"Defense":random.randint(8,12),"Speed":random.randint(10,14),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(130,155),"Evasion":random.randint(4,7),"Accuracy":random.randint(87,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Storm Tome","Lightning Crystal"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Storm Mage","Ability":"None","Attribute":"None"},
            "Lightning Elemental":{"XP":60,"Max Health":random.randint(100,110),"Health":120,"Attack":random.randint(11,14),"Defense":random.randint(13,15),"Speed":random.randint(15,16),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(145,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(88,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Lightning Core"],"Category":"Elemental","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Lightning Elemental","Ability":"None","Attribute":"None"},
            "Thunder Archer":{"XP":95,"Max Health":random.randint(95,110),"Health":100,"Attack":random.randint(12,16),"Defense":random.randint(13,15),"Speed":random.randint(13,16),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(400,600),"Critical Chance":random.randint(4,8),"Critical Damage":random.randint(145,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(89,90),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Thunder Bow"],"Category":"Elemental","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Thunder Archer","Ability":"None","Attribute":"None"},
            "Tempest Lord":{"XP":120,"Max Health":random.randint(120,135),"Health":200,"Attack":random.randint(17,19),"Defense":random.randint(13,15),"Speed":random.randint(13,15),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(85,90),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Tempest Blade","Storm Core"],"Category":"Elemental","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Tempest Lord","Ability":"None","Attribute":"None"},
            "Thunder Beast":{"XP":115,"Max Health":random.randint(135,150),"Health":180,"Attack":random.randint(17,21),"Defense":random.randint(10,11),"Speed":random.randint(10,13),"Magic Density":random.randint(12,16),"Magic Damage":random.randint(12,16),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(140,155),"Evasion":random.randint(5,7),"Accuracy":random.randint(83,90),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Thunder Fang","Storm Core"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Thunder Beast","Ability":"None","Attribute":"None"},
            "Storm Spirit":{"XP":65,"Max Health":random.randint(90,120),"Health":85,"Attack":random.randint(10,14),"Defense":random.randint(7,14),"Speed":random.randint(14,16),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(14,16),"Level":2,"Stamina":random.randint(440,550),"Critical Chance":random.randint(3,7),"Critical Damage":random.randint(145,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(86,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Storm Essence"],"Category":"Elemental","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3},"Type":"Storm Spirit","Ability":"None","Attribute":"None"},
            "Charged Golem":{"XP":125,"Max Health":random.randint(120,155),"Health":240,"Attack":random.randint(18,22),"Defense":random.randint(12,15),"Speed":random.randint(12,14),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(450,560),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(145,155),"Evasion":random.randint(2,4),"Accuracy":random.randint(78,84),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Charged Core","Golem Stone"],"Category":"Construct","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Charged Golem","Ability":"None","Attribute":"None"},
            "Thunder Wraith":{"XP":85,"Max Health":random.randint(90,110),"Health":200,"Attack":random.randint(10,13),"Defense":random.randint(13,15),"Speed":random.randint(14,16),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(14,16),"Level":1,"Stamina":random.randint(450,500),"Critical Chance":random.randint(4,5),"Critical Damage":random.randint(145,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(88,90),"Mana":random.randint(25,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Thunder Essence","Charged Core"],"Category":"Spirit","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Thunder Wraith","Ability":"None","Attribute":"None"},
            "Storm Crow":{"XP":35,"Max Health":random.randint(70,90),"Health":130,"Attack":random.randint(14,17),"Defense":random.randint(7,10),"Speed":random.randint(12,14),"Magic Density":random.randint(14,15),"Magic Damage":random.randint(14,15),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(135,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(77,88),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Storm Feather","Crow Beak"],"Category":"Beast","Behaviour":"Hunter","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Storm Crow","Ability":"None","Attribute":"None"},
            
            "Shadow Rat":{"XP":20,"Max Health":random.randint(65,75),"Health":55,"Attack":random.randint(12,15),"Defense":random.randint(7,9),"Speed":random.randint(13,15),"Magic Density":random.randint(11,13),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(6,7),"Critical Damage":random.randint(125,140),"Evasion":random.randint(4,7),"Accuracy":random.randint(81,88),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shadow Tail"],"Category":"Abberation","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shadow Rat","Ability":"None","Attribute":"None"},
            "Shadow Assassin":{"XP":65,"Max Health":random.randint(100,120),"Health":95,"Attack":random.randint(18,21),"Defense":random.randint(7,11),"Speed":random.randint(14,16),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(500,666),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(156,175),"Evasion":random.randint(6,8),"Accuracy":random.randint(88,90),"Mana":random.randint(35,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shadow Blade"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shadow Assassin","Ability":"None","Attribute":"None"},
            "Void Beast":{"XP":95,"Max Health":random.randint(135,155),"Health":150,"Attack":random.randint(15,19),"Defense":random.randint(12,15),"Speed":random.randint(8,11),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(11,14),"Level":1,"Stamina":random.randint(400,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(125,135),"Evasion":random.randint(6,8),"Accuracy":random.randint(80,90),"Mana":random.randint(15,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Void Core"],"Category":"Void","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Void Beast","Ability":"None","Attribute":"None"},
            "Shadow Lord":{"XP":160,"Max Health":random.randint(120,135),"Health":200,"Attack":random.randint(17,19),"Defense":random.randint(13,15),"Speed":random.randint(13,15),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(85,90),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shadow Core"],"Category":"Boss","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shadow Lord","Ability":"None","Attribute":"None"},
            "Void Spawn":{"Max Health":random.randint(90,110),"Health":95,"Attack":random.randint(15,18),"Defense":random.randint(10,12),"Speed":random.randint(14,16),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(4,5),"Critical Damage":random.randint(130,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(80,90),"Mana":random.randint(20,35),"XP":12,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Void Fragment"],"Category":"Abberation","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Void Spawn","Ability":"None","Attribute":"None"},
            "Shadow Beast":{"XP":85,"Max Health":random.randint(135,155),"Health":150,"Attack":random.randint(15,19),"Defense":random.randint(12,15),"Speed":random.randint(8,11),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(11,14),"Level":1,"Stamina":random.randint(400,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(125,135),"Evasion":random.randint(6,8),"Accuracy":random.randint(80,90),"Mana":random.randint(15,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shadow Fang"],"Category":"Shadow","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shadow Beast","Ability":"None","Attribute":"None"},
            "Night Wolf":{"XP":65,"Max Health":random.randint(80,100),"Health":70,"Attack":random.randint(17,20),"Defense":random.randint(11,13),"Speed":random.randint(12,14),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(400,700),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(86,90),"Mana":random.randint(10,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Night Fur"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Night Wolf","Ability":"None","Attribute":"None"},
            "Dark Mage":{"XP":45,"Max Health":random.randint(90,105),"Health":120,"Attack":random.randint(10,14),"Defense":random.randint(11,15),"Speed":random.randint(9,14),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,650),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(120,155),"Evasion":random.randint(3,8),"Accuracy":random.randint(85,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dark Tome","Mana Crystal"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Dark Mage","Ability":"None","Attribute":"None"},
            "Phantom Knight":{"XP":105,"Max Health":random.randint(120,140),"Health":140,"Attack":random.randint(17,21),"Defense":random.randint(12,14),"Speed":random.randint(13,15),"Magic Density":random.randint(11,14),"Magic Damage":random.randint(11,14),"Level":1,"Stamina":random.randint(450,775),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(134,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(81,90),"Mana":random.randint(25,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Phantom Sword","Ectoplasm Shard"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Phantom Knight","Ability":"None","Attribute":"None"},
            "Dark Acolyte":{"XP":42,"Max Health":random.randint(90,110),"Health":85,"Attack":random.randint(12,16),"Defense":random.randint(10,12),"Speed":random.randint(11,13),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(120,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(88,90),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dark Robe","Mana Crystal"],"Category":"Cultist","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Dark Acolyte","Ability":"None","Attribute":"None"},
            "Shadow Mage":{"XP":55,"Max Health":random.randint(90,105),"Health":95,"Attack":random.randint(10,14),"Defense":random.randint(10,14),"Speed":random.randint(9,14),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(400,600),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(120,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(81,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shadow Tome","Dark Crystal"],"Category":"Mage","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shadow Mage","Ability":"None","Attribute":"None"},
            "Lich Servant":{"XP":58,"Max Health":random.randint(90,120),"Health":95,"Attack":random.randint(12,14),"Defense":random.randint(7,10),"Speed":random.randint(10,13),"Magic Density":random.randint(13,14),"Magic Damage":random.randint(14,15),"Level":1,"Stamina":random.randint(500,650),"Critical Chance":random.randint(2,4),"Critical Damage":random.randint(125,145),"Evasion":random.randint(3,5),"Accuracy":random.randint(75,80),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dark Essence","Bone Staff"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Lich Servant","Ability":"None","Attribute":"None"},
            "Abyss Walker":{"XP":110,"Max Health":random.randint(85,95),"Health":350,"Attack":random.randint(16,20),"Defense":random.randint(11,12),"Speed":random.randint(14,16),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(5,6),"Critical Damage":random.randint(140,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(88,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Abyss Core","Abyss Blade"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Abyss Walker","Ability":"None","Attribute":"None"},
            "Nightmare Beast":{"XP":130,"Max Health":random.randint(145,155),"Health":300,"Attack":random.randint(21,23),"Defense":random.randint(14,16),"Speed":random.randint(7,9),"Magic Density":random.randint(10,12),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(400,550),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(20,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Nightmare Fang","Shadow Essence"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Nightmare Beast","Ability":"None","Attribute":"None"},
            "Void Wraith":{"XP":85,"Max Health":random.randint(110,125),"Health":180,"Attack":random.randint(8,11),"Defense":random.randint(11,14),"Speed":random.randint(13,15),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(500,650),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(88,90),"Mana":random.randint(20,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Void Essence","Wraith Core"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Void Wraith","Ability":"None","Attribute":"None"},
            "Demon Lord Servant":{"XP":125,"Max Health":random.randint(125,145),"Health":260,"Attack":random.randint(18,20),"Defense":random.randint(12,15),"Speed":random.randint(12,15),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(12,16),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(5,6),"Evasion":random.randint(6,7),"Accuracy":random.randint(84,90),"Mana":random.randint(45,55),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Demon Core","Cursed Armor Fragment"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Demon Lord Servant","Ability":"None","Attribute":"None"},
            "Shadow Demon":{"XP":145,"Max Health":random.randint(130,145),"Health":210,"Attack":random.randint(17,20),"Defense":random.randint(11,13),"Speed":random.randint(13,15),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(12,16),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(125,155),"Evasion":random.randint(5,7),"Accuracy":random.randint(82,88),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shadow Core","Demon Claw"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shadow Demon","Ability":"None","Attribute":"None"},
            "Abyss Summoner":{"XP":85,"Max Health":random.randint(110,125),"Health":220,"Attack":random.randint(11,14),"Defense":random.randint(12,13),"Speed":random.randint(12,13),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(13,16),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(125,145),"Evasion":random.randint(3,5),"Accuracy":random.randint(84,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Abyss Orb","Summoner's Robe"],"Category":"Demon","Behaviour":"Tactical","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Abyss Summoner","Ability":"None","Attribute":"None"},
            "Night Stalker":{"XP":95,"Max Health":random.randint(100,135),"Health":135,"Attack":random.randint(15,17),"Defense":random.randint(8,10),"Speed":random.randint(13,15),"Magic Density":random.randint(12,13),"Magic Damage":random.randint(13,14),"Level":1,"Stamina":random.randint(550,750),"Critical Chance":random.randint(6,9),"Critical Damage":random.randint(140,160),"Evasion":random.randint(7,8),"Accuracy":random.randint(89,90),"Mana":random.randint(20,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Night Fang","Shadow Hide"],"Category":"Beast","Behaviour":"Hunter","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Night Stalker","Ability":"None","Attribute":"None"},
            "Cursed Blacksmith":{"XP":70,"Max Health":random.randint(125,135),"Health":150,"Attack":random.randint(17,20),"Defense":random.randint(14,16),"Speed":random.randint(11,13),"Magic Density":random.randint(13,14),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(450,755),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,5),"Accuracy":random.randint(84,90),"Mana":random.randint(11,33),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Blacksmith Hammer","Cursed Metal Shard"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Cursed Blacksmith","Ability":"None","Attribute":"None"},
            "Curse Spirit":{"XP":76,"Max Health":random.randint(110,135),"Health":180,"Attack":random.randint(12,14),"Defense":random.randint(12,15),"Speed":random.randint(15,16),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(450,750),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(88,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Cursed Essence","Spirit Shard"],"Category":"Spirit","Behaviour":"Tactical","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Curse Spirit","Ability":"None","Attribute":"None"},
            
            "Alchemical Slime":{"XP":30,"Max Health":random.randint(65,155),"Health":110,"Attack":random.randint(10,12),"Defense":random.randint(7,9),"Speed":random.randint(7,10),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(9,13),"Level":1,"Stamina":random.randint(450,600),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,145),"Evasion":random.randint(2,4),"Accuracy":random.randint(75,80),"Mana":random.randint(30,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Slime Core"],"Category":"Elemental","Behaviour":"Defensive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Alchemical Slime","Ability":"None","Attribute":"None"},
            "Mutant Rat":{"XP":40,"Max Health":random.randint(70,100),"Health":90,"Attack":random.randint(13,15),"Defense":random.randint(8,12),"Speed":random.randint(14,16),"Magic Density":random.randint(8,10),"Magic Damage":random.randint(8,10),"Level":1,"Stamina":random.randint(500,650),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,8),"Accuracy":random.randint(75,90),"Mana":random.randint(5,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Mutant Flesh"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Mutant Rat","Ability":"None","Attribute":"None"},
            "Alchemical Horror":{"XP":100,"Max Health":random.randint(120,145),"Health":190,"Attack":random.randint(16,20),"Defense":random.randint(14,16),"Speed":random.randint(8,10),"Magic Density":random.randint(10,13),"Magic Damage":random.randint(10,13),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(120,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(80,85),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Alchemical Core"],"Category":"Experiment","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Alchemical Horror","Ability":"None","Attribute":"None"},
            "Experiment Soldier":{"XP":55,"Max Health":random.randint(130,140),"Health":130,"Attack":random.randint(17,21),"Defense":random.randint(14,15),"Speed":random.randint(12,15),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,90),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Experiment Core","Broken Blade"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Experiment Soldier","Ability":"None","Attribute":"None"},
            "Potion Spirit":{"XP":38,"Max Health":random.randint(100,125),"Health":180,"Attack":random.randint(12,14),"Defense":random.randint(12,15),"Speed":random.randint(12,14),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(450,750),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(88,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Spirit Essence","Potion Residue"],"Category":"Spirit","Behaviour":"Defensive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Potion Spirit","Ability":"None","Attribute":"None"},
            "Failed Experiment":{"XP":90,"Max Health":random.randint(85,100),"Health":160,"Attack":random.randint(13,16),"Defense":random.randint(8,10),"Speed":random.randint(8,11),"Magic Density":random.randint(11,13),"Magic Damage":random.randint(11,14),"Level":1,"Stamina":random.randint(555,666),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(125,140),"Evasion":random.randint(3,4),"Accuracy":random.randint(80,85),"Mana":random.randint(15,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Experiment Core","Mutated Tissue"],"Category":"Experiment","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Failed Experiment","Ability":"None","Attribute":"None"},
            "Mutation Ogre":{"XP":120,"Max Health":random.randint(145,155),"Health":250,"Attack":random.randint(20,22),"Defense":random.randint(15,16),"Speed":random.randint(11,14),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(145,155),"Evasion":random.randint(4,6),"Accuracy":random.randint(81,86),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ogre Core","Mutated Claw"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Mutation Ogre","Ability":"None","Attribute":"None"},
            "Living Potion":{"XP":35,"Max Health":random.randint(70,85),"Health":80,"Attack":random.randint(12,14),"Defense":random.randint(10,12),"Speed":random.randint(8,12),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(12,13),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(125,140),"Evasion":random.randint(3,5),"Accuracy":random.randint(80,85),"Mana":random.randint(20,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Potion Residue","Living Essence"],"Category":"Slime","Behaviour":"Defensive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Living Potion","Ability":"None","Attribute":"None"},
            "Mad Alchemist Spirit":{"XP":111,"Max Health":random.randint(110,135),"Health":180,"Attack":random.randint(12,14),"Defense":random.randint(12,15),"Speed":random.randint(15,16),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(450,750),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(88,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Alchemical Essence","Spirit Flask"],"Category":"Spirit","Behaviour":"Erratic","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Mad Alchemist Spirit","Ability":"None","Attribute":"None"},
            "Tiny Ooze":{"XP":40,"Max Health":random.randint(65,70),"Health":60,"Attack":random.randint(7,9),"Defense":random.randint(7,8),"Speed":random.randint(7,8),"Magic Density":random.randint(11,14),"Magic Damage":random.randint(7,12),"Level":1,"Stamina":random.randint(350,500),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,5),"Accuracy":random.randint(75,80),"Mana":random.randint(10,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ooze Droplet","Sticky Gel"],"Category":"Beast","Behaviour":"Erratic","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Tiny Ooze","Ability":"None","Attribute":"None"},
            "Chemical Spider":{"XP":35,"Max Health":random.randint(80,105),"Health":65,"Attack":random.randint(11,15),"Defense":random.randint(7,10),"Speed":random.randint(11,14),"Magic Density":random.randint(10,15),"Magic Damage":random.randint(10,15),"Level":1,"Stamina":random.randint(350,450),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(7,8),"Accuracy":random.randint(85,90),"Mana":random.randint(15,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Acid Sac","Spider Silk","Chemical Fang"],"Category":"Beast","Behaviour":"Hunter","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Chemical Spider","Ability":"None","Attribute":"None"},
            "Plague Experiment":{"XP":85,"Max Health":random.randint(100,110),"Health":165,"Attack":random.randint(14,17),"Defense":random.randint(11,13),"Speed":random.randint(9,12),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(125,145),"Evasion":random.randint(2,4),"Accuracy":random.randint(81,90),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Plague Core","Toxic Flesh"],"Category":"Experiment","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Plague Experiment","Ability":"None","Attribute":"None"},
            
         
            "Fire Imp":{"XP":45,"Max Health":random.randint(60,80),"Health":65,"Attack":random.randint(10,16),"Defense":random.randint(8,11),"Speed":random.randint(14,17),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(14,16),"Level":1,"Stamina":random.randint(550,750),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(75,90),"Mana":random.randint(40,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Imp Ash"],"Category":"Fire","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Fire Imp","Ability":"None","Attribute":"None"},
            "Fire Mage":{"XP":60,"Max Health":random.randint(75,95),"Health":170,"Attack":random.randint(10,14),"Defense":random.randint(8,12),"Speed":random.randint(10,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(350,450),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(140,155),"Evasion":random.randint(5,8),"Accuracy":random.randint(85,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Mage Robe"],"Category":"Fire","Behaviour":"Caster","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Fire Mage","Ability":"None","Attribute":"None"},
            "Flame Warden":{"XP":70,"Max Health":random.randint(120,135),"Health":130,"Attack":random.randint(17,19),"Defense":random.randint(12,14),"Speed":random.randint(10,14),"Magic Density":random.randint(14,16),"Magic Damage":random.randint(12,16),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(135,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(84,88),"Mana":random.randint(25,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Flame Core"],"Category":"Fire","Behaviour":"Balanced","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Flame Warden","Ability":"None","Attribute":"None"},
            "Burning Spirit":{"XP":60,"Max Health":random.randint(110,135),"Health":180,"Attack":random.randint(12,14),"Defense":random.randint(12,15),"Speed":random.randint(15,16),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(450,750),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(130,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(88,90),"Mana":random.randint(35,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Spirit Essence"],"Category":"Spirit","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Burning Spirit","Ability":"None","Attribute":"None"},
            "Flame Wraith":{"XP":75,"Max Health":random.randint(110,125),"Health":180,"Attack":random.randint(8,11),"Defense":random.randint(11,14),"Speed":random.randint(13,15),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(500,650),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(88,90),"Mana":random.randint(20,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Wraith Flame"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Flame Wraith","Ability":"None","Attribute":"None"},
            "Molten Knight":{"XP":90,"Max Health":random.randint(120,135),"Health":170,"Attack":random.randint(18,21),"Defense":random.randint(13,16),"Speed":random.randint(8,11),"Magic Density":random.randint(11,16),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(550,675),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(125,155),"Evasion":random.randint(2,4),"Accuracy":random.randint(85,90),"Mana":random.randint(15,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Molten Armor"],"Category":"Fire","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Molten Knight","Ability":"None","Attribute":"None"},
            "Inferno Elemental":{"XP":100,"Max Health":random.randint(100,115),"Health":160,"Attack":random.randint(10,14),"Defense":random.randint(12,14),"Speed":random.randint(11,15),"Magic Density":random.randint(13,16),"Magic Damage":random.randint(12,15),"Level":1,"Stamina":random.randint(450,567),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(125,155),"Evasion":random.randint(3,6),"Accuracy":random.randint(75,83),"Mana":random.randint(30,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Inferno Core"],"Category":"Elemental","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Inferno Elemental","Ability":"None","Attribute":"None"},
            "Demon Imp":{"XP":45,"Max Health":random.randint(70,90),"Health":75,"Attack":random.randint(12,18),"Defense":random.randint(9,13),"Speed":random.randint(16,17),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(600,775),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(145,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(82,90),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Imp Core"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Demon Imp","Ability":"None","Attribute":"None"},
            "Demon Warrior":{"XP":90,"Max Health":random.randint(120,135),"Health":210,"Attack":random.randint(18,20),"Defense":random.randint(11,14),"Speed":random.randint(11,15),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(150,165),"Evasion":random.randint(3,7),"Accuracy":random.randint(85,90),"Mana":random.randint(30,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Demon Blade","Burning Core"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Demon Warrior","Ability":"None","Attribute":"None"},
            "Ash Soldier":{"XP":55,"Max Health":random.randint(130,140),"Health":130,"Attack":random.randint(17,21),"Defense":random.randint(14,15),"Speed":random.randint(12,15),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(80,90),"Mana":random.randint(35,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Experiment Core","Broken Blade"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ash Soldier","Ability":"None","Attribute":"None"},

            
            "Armory Guard":{"XP":50,"Max Health":random.randint(100,125),"Health":120,"Attack":random.randint(13,17),"Defense":random.randint(14,16),"Speed":random.randint(10,13),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(125,155),"Evasion":random.randint(2,5),"Accuracy":random.randint(82,88),"Mana":random.randint(10,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Guard Armor"],"Category":"Human","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Armory Guard","Ability":"None","Attribute":"None"},
            "Tomb Raider":{"XP":65,"Max Health":random.randint(85,110),"Health":180,"Attack":random.randint(11,18),"Defense":random.randint(9,12),"Speed":random.randint(14,16),"Magic Density":random.randint(10,12),"Magic Damage":random.randint(8,11),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(2,4),"Critical Damage":random.randint(130,140),"Evasion":random.randint(7,8),"Accuracy":random.randint(88,90),"Mana":random.randint(10,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ancient Relic"],"Category":"Human","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Tomb Raider","Ability":"None","Attribute":"None"},
            "Tomb Knight":{"XP":90,"Max Health":random.randint(125,145),"Health":140,"Attack":random.randint(14,17),"Defense":random.randint(12,16),"Speed":random.randint(10,13),"Magic Density":random.randint(9,12),"Magic Damage":random.randint(8,10),"Level":1,"Stamina":random.randint(550,755),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(135,145),"Evasion":random.randint(2,4),"Accuracy":random.randint(85,90),"Mana":random.randint(20,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Tomb Sword","Ancient Shield"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Tomb Knight","Ability":"None","Attribute":"None"},
            "Tomb Robber":{"XP":65,"Max Health":random.randint(90,115),"Health": 110,"Attack":random.randint(12,16),"Defense":random.randint(10,13),"Speed":random.randint(13,16),"Magic Density" :random.randint(9,12),"Magic Damage":random.randint(8,10),"Level":1,"Stamina": random.randint(550,650),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(135,145),"Evasion":random.randint(7,8),"Accuracy":random.randint(88,90),"Mana":random.randint(15,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Golden Bar","Golden Goblet"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Tomb Robber","Ability":"None","Attribute":"None"},
            "Bridge Troll":{"XP":80,"Max Health":random.randint(145,155),"Health":200,"Attack":random.randint(18,21),"Defense":random.randint(14,16),"Speed":random.randint(7,10),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(2,3),"Critical Damage":random.randint(125,135),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(15,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Troll Hide"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bridge Troll","Ability":"None","Attribute":"None"},
            "Bridge Guard":{"XP":40,"Max Health":random.randint(105,115),"Health":110,"Attack":random.randint(11,15),"Defense":random.randint(12,14),"Speed":random.randint(11,14),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(600,750),"Critical Chance":random.randint(4,7),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(83,89),"Mana":random.randint(10,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":[{"Iron Sword":"Weapon"},"Guard Shield"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bridge Guard","Ability":"None","Attribute":"None"},
            "Bridge Thief":{"XP":32,"Max Health":random.randint(85,100),"Health":70,"Attack":random.randint(12,14),"Defense":random.randint(9,11),"Speed":random.randint(14,16),"Magic Density":random.randint(9,13),"Magic Damage":random.randint(9,11),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(145,155),"Evasion":random.randint(7,8),"Accuracy":random.randint(89,90),"Mana":random.randint(10,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Stolen Coin","Rusty Knife"],"Category":"Humanoid","Behaviour":"Evasive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bridge Thief","Ability":"None","Attribute":"None"},
            "Bridge Wraith":{"XP":95,"Max Health":random.randint(110,125),"Health":180,"Attack":random.randint(8,11),"Defense":random.randint(11,14),"Speed":random.randint(13,15),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(500,650),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(135,145),"Evasion":random.randint(3,6),"Accuracy":random.randint(88,90),"Mana":random.randint(20,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Wraith Essence","Ethereal Cloth"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Bridge Wraith","Ability":"None","Attribute":"None"},
           "Ancient Guardian":{"XP":110,"Max Health":random.randint(145,155),"Health":190,"Attack":random.randint(20,23),"Defense":random.randint(14,16),"Speed":random.randint(7,8),"Magic Density":random.randint(8,11),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(650,755),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(135,150),"Evasion":random.randint(2,4),"Accuracy":random.randint(81,84),"Mana":random.randint(10,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ancient Core"],"Category":"Construct","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ancient Guardian","Ability":"None","Attribute":"None"},
            "Ancient Lich":{"XP":150,"Max Health":random.randint(85,110),"Health":160,"Attack":random.randint(10,12),"Defense":random.randint(13,15),"Speed":random.randint(8,11),"Magic Density":random.randint(15,16),"Magic Damage":random.randint(15,16),"Level":1,"Stamina":random.randint(450,500),"Critical Chance":random.randint(3,6),"Critical Damage":random.randint(135,150),"Evasion":random.randint(3,5),"Accuracy":random.randint(85,90),"Mana":random.randint(45,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ancient Staff"],"Category":"Undead","Behaviour":"Caster","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ancient Lich","Ability":"None","Attribute":"None"},
            "Ancient Archer":{"XP":60,"Max Health":random.randint(85,100),"Health":120,"Attack":random.randint(15,18),"Defense":random.randint(9,12),"Speed":random.randint(13,15),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(9,12),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(7,8),"Critical Damage":random.randint(145,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(86,90),"Mana":random.randint(10,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ancient Arrow"],"Category":"Undead","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ancient Archer","Ability":"None","Attribute":"None"}, 
            "Arena Archer":{"XP":32,"Max Health":random.randint(85,95),"Health":70,"Attack":random.randint(14,19),"Defense":random.randint(8,11),"Speed":random.randint(14,16),"Magic Density":random.randint(7,10),"Magic Damage":random.randint(8,14),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(5,8),"Critical Damage":random.randint(150,155),"Evasion":random.randint(6,8),"Accuracy":random.randint(89,90),"Mana":random.randint(15,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":[{"Iron Spear":"Weapon"}],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Arena Archer","Ability":"None","Attribute":"None"},
            "Arena Champion":{"XP":120,"Max Health":random.randint(135,145),"Health":220,"Attack":random.randint(19,22),"Defense":random.randint(14,16),"Speed":random.randint(12,14),"Magic Density":random.randint(12,15),"Magic Damage":random.randint(7,14),"Level":1,"Stamina":random.randint(650,800),"Critical Chance":random.randint(6,8),"Critical Damage":random.randint(145,160),"Evasion":random.randint(5,7),"Accuracy":random.randint(87,90),"Mana":random.randint(5,45),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Champion Blade","Arena Medal"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Arena Champion","Ability":"None","Attribute":"None"},
            "Ritual Knight":{"XP":60,"Max Health":random.randint(135,150),"Health":140,"Attack":random.randint(16,19),"Defense":random.randint(12,14),"Speed":random.randint(10,12),"Magic Density":random.randint(11,13),"Magic Damage":random.randint(13,14),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(4,6),"Critical Damage":random.randint(135,150),"Evasion":random.randint(2,4),"Accuracy":random.randint(85,90),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":[{"Ritual Sword":"Weapon"},"Dark Armor Fragment"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ritual Knight","Ability":"None","Attribute":"None"},
            "Ritual Guard":{"XP":58,"Max Health":random.randint(85,95),"Health":135,"Attack":random.randint(11,14),"Defense":random.randint(11,14),"Speed":random.randint(11,14),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(450,550),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(135,145),"Evasion":random.randint(4,6),"Accuracy":random.randint(84,87),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ritual Spear","Guard Armor Fragment"],"Category":"Cultist","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ritual Guard","Ability":"None","Attribute":"None"},
            "Ritual Demon":{"XP":145,"Max Health":random.randint(110,135),"Health":180,"Attack":random.randint(16,19),"Defense":random.randint(12,15),"Speed":random.randint(12,14),"Magic Density":random.randint(13,15),"Magic Damage":random.randint(13,15),"Level":1,"Stamina":random.randint(550,750),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(135,145),"Evasion":random.randint(4,7),"Accuracy":random.randint(85,90),"Mana":random.randint(25,50),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Demonic Sigil","Ritual Core"],"Category":"Demon","Behaviour":"Caster","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ritual Demon","Ability":"None","Attribute":"None"},
            "Ritual Beast":{"XP":115,"Max Health":random.randint(120,155),"Health":260,"Attack":random.randint(19,21),"Defense":random.randint(13,15),"Speed":random.randint(7,9),"Magic Density":random.randint(12,14),"Magic Damage":random.randint(12,14),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,130),"Evasion":random.randint(2,3),"Accuracy":random.randint(75,80),"Mana":random.randint(25,35),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ritual Bone","Beast Heart"],"Category":"Beast","Behaviour":"Ritualistic","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Ritual Beast","Ability":"None","Attribute":"None"},

            "Shield Fighter":{"XP":45,"Max Health":random.randint(130,145),"Health":130,"Attack":random.randint(13,16),"Defense":random.randint(14,15),"Speed":random.randint(7,9),"Magic Density":random.randint(8,11),"Magic Damage":random.randint(8,10),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(120,135),"Evasion":random.randint(2,5),"Accuracy":random.randint(79,85),"Mana":random.randint(5,30),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Shield Fragment"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Shield Fighter","Ability":"None","Attribute":"None"},
            "Stone Guardian":{"XP":110,"Max Health":random.randint(145,155),"Health":250,"Attack":random.randint(16,19),"Defense":random.randint(12,14),"Speed":random.randint(7,8),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(135,140),"Evasion":random.randint(2,4),"Accuracy":random.randint(81,86),"Mana":random.randint(10,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Stone Core"],"Category":"Construct","Behaviour":"Defender","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Stone Guardian","Ability":"None","Attribute":"None"},
            "Heavy Bandit":{"XP":40,"Max Health":random.randint(110,125),"Health":100,"Attack":random.randint(15,22),"Defense":random.randint(13,14),"Speed":random.randint(9,11),"Magic Density":random.randint(7,9),"Magic Damage":random.randint(7,9),"Level":1,"Stamina":random.randint(550,700),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(130,135),"Evasion":random.randint(4,5),"Accuracy":random.randint(84,88),"Mana":random.randint(5,20),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Heavy Dagger","Bandit Armor"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Heavy Bandit","Ability":"None","Attribute":"None"},
            "Heavy Knight":{"XP":135,"Max Health":random.randint(145,155),"Health":400,"Attack":random.randint(16,20),"Defense":random.randint(15,16),"Speed":random.randint(8,11),"Magic Density":random.randint(7,11),"Magic Damage":random.randint(7,11),"Level":1,"Stamina":random.randint(650,775),"Critical Chance":random.randint(5,7),"Critical Damage":random.randint(125,145),"Evasion":random.randint(3,5),"Accuracy":random.randint(82,88),"Mana":random.randint(25,40),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Knight Armor","Greatsword"],"Category":"Humanoid","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Heavy Knight","Ability":"None","Attribute":"None"},
            "Stone Golem":{"XP":75,"Max Health":random.randint(140,155),"Health":180,"Attack":random.randint(15,23),"Defense":random.randint(13,15),"Speed":random.randint(8,11),"Magic Density":random.randint(11,14),"Magic Damage":random.randint(9,12),"Level":1,"Stamina":random.randint(550,650),"Critical Chance":random.randint(3,4),"Critical Damage":random.randint(120,135),"Evasion":random.randint(2,4),"Accuracy":random.randint(81,84),"Mana":random.randint(20,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Golem Core"],"Category":"Construct","Behaviour":"Defender","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3},"Type":"Stone Golem","Ability":"None","Attribute":"None"},
            "Rust Golem":{"XP":65,"Max Health":random.randint(125,145),"Health":180,"Attack":random.randint(14,22),"Defense":random.randint(12,14),"Speed":random.randint(7,10),"Magic Density":random.randint(11,14),"Magic Damage":random.randint(9,11),"Level":1,"Stamina":random.randint(500,600),"Critical Chance":random.randint(2,3),"Critical Damage":random.randint(110,125),"Evasion":random.randint(1,3),"Accuracy":random.randint(75,79),"Mana":random.randint(15,25),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Rust Core"],"Category":"Construct","Behaviour":"Defensive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Rust Golem","Ability":"None","Attribute":"None"},
            "Steel Automaton":{"XP":65,"Max Health":random.randint(135,155),"Health":150,"Attack":random.randint(16,19),"Defense":random.randint(13,15),"Speed":random.randint(7,9),"Magic Density":random.randint(7,11),"Magic Damage":random.randint(7,11),"Level":1,"Stamina":random.randint(450,750),"Critical Chance":random.randint(3,5),"Critical Damage":random.randint(125,130),"Evasion":random.randint(2,4),"Accuracy":random.randint(80,84),"Mana":random.randint(15,15),"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Steel Core"],"Category":"Construct","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Type":"Steel Automation","Ability":"None","Attribute":"None"},


     
          
    },


        

    "Tier 2":{

                    "Skeleton Knight":{"XP":50,"Max Health":110,"Health":110,"Attack":18,"Defense":14,"Speed":11,"Magic Density":6,"Magic Damage":6,"Level":2,"Stamina":800,"Critical Chance":6,"Critical Damage":140,"Evasion":4,"Accuracy":90,"Mana":30,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Ancient Bones"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Dire Wolf":{"XP":45,"Max Health":100,"Health":100,"Attack":19,"Defense":9,"Speed":18,"Magic Density":3,"Magic Damage":3,"Level":2,"Stamina":700,"Critical Chance":13,"Critical Damage":145,"Evasion":12,"Accuracy":94,"Mana":0,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Dire Pelt"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Mercenary":{"XP":50,"Max Health":120,"Health":120,"Attack":20,"Defense":15,"Speed":12,"Magic Density":4,"Magic Damage":4,"Level":2,"Stamina":800,"Critical Chance":9,"Critical Damage":150,"Evasion":6,"Accuracy":92,"Mana":25,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Steel  Chain"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Rotting Zombie":{"XP":55,"Max Health":180,"Health":180,"Attack":16,"Defense":18,"Speed":5,"Magic Density":1,"Magic Damage":1,"Level":2,"Stamina":1000,"Critical Chance":3,"Critical Damage":125,"Evasion":1,"Accuracy":82,"Mana":0,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Putrid Core"],"Category":"Undead","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Hobgoblin":{"XP":40,"Max Health":95,"Health":95,"Attack":18,"Defense":10,"Speed":15,"Magic Density":5,"Magic Damage":5,"Level":2,"Stamina":700,"Critical Chance":10,"Critical Damage":145,"Evasion":10,"Accuracy":92,"Mana":30,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["War Banner Scrap"],"Category":"Humanoid","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Dire Bear":{"XP":60,"Max Health":170,"Health":170,"Attack":19,"Defense":16,"Speed":6,"Magic Density":0,"Magic Damage":0,"Level":2,"Stamina":1000,"Critical Chance":6,"Critical Damage":150,"Evasion":2,"Accuracy":88,"Mana":0,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Thick Bear Hide"],"Category":"Beast","Behaviour":"Aggressive","Spell Caster":False,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Hellhound":{"XP":55,"Max Health":120,"Health":120,"Attack":20,"Defense":12,"Speed":14,"Magic Density":8,"Magic Damage":10,"Level":2,"Stamina":800,"Critical Chance":10,"Critical Damage":155,"Evasion":8,"Accuracy":92,"Mana":40,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Hellfire Ember"],"Category":"Demon","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Animated Armor":{"XP":55,"Max Health":130,"Health":130,"Attack":18,"Defense":18,"Speed":8,"Magic Density":3,"Magic Damage":3,"Level":2,"Stamina":900,"Critical Chance":5,"Critical Damage":140,"Evasion":2,"Accuracy":90,"Mana":10,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Enchanted Plate"],"Category":"Construct","Behaviour":"Defender","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Fire Elemental":{"XP":60,"Max Health":95,"Health":95,"Attack":16,"Defense":8,"Speed":14,"Magic Density":18,"Magic Damage":20,"Level":2,"Stamina":650,"Critical Chance":8,"Critical Damage":150,"Evasion":10,"Accuracy":92,"Mana":120,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Flame Core"],"Category":"Elemental","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Void Leech":{"XP":50,"Max Health":90,"Health":90,"Attack":16,"Defense":9,"Speed":15,"Magic Density":12,"Magic Damage":14,"Level":2,"Stamina":700,"Critical Chance":7,"Critical Damage":145,"Evasion":9,"Accuracy":90,"Mana":60,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Void Blood"],"Category":"Abberation","Behaviour":"Evasive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}},

                    "Eldritch Horror":{"XP":120,"Max Health":220,"Health":220,"Attack":22,"Defense":18,"Speed":10,"Magic Density":25,"Magic Damage":24,"Level":3,"Stamina":1200,"Critical Chance":10,"Critical Damage":170,"Evasion":6,"Accuracy":95,"Mana":200,"Buff":{"Type":"None","Value":0,"Duration":0},"Drop":["Eldritch Eye"],"Category":"Abberation","Behaviour":"Aggressive","Spell Caster":True,"Status Effects":{"Status 1":{"Type":"None","Value":0,"Duration":0} ,"Status 2":{"Type":"None","Value":0,"Duration":0},"Status 3":{"Type":"None","Value":0,"Duration":0}},"Buff":{"Type":"None","Value":5,"Duration":3}}

    }}

    print("\n---------------\n\n""     Menu\n\n""---------------\n"f"Adventure\n""---------------\n"f"Character\n""---------------\nFacilities""\n---------------\nSystem\n---------------\n")
    if Player["XP Needed"] <= Player["XP"]:
        Player["XP"] = Player["XP"] - Player["XP Needed"]
        Player["XP Needed"] = Player["XP Needed"] * 2
        Player["XP Needed"] = round(Player["XP Needed"])
        skill_points += 1
        Player["Level"] += 1
        Base_Stats["Level"] += 1
        print("\nYou Leveled Up!\n\n")
        print("You gain +1 skill point")
        
    Attack_Bonus = (Body_Condition["Biceps"]["Strength"]* 1.2) + (Body_Condition["Triceps"]["Strength"] * 0.8) + (Body_Condition["Shoulders"]["Strength"]* 0.5)
    Defense_Bonus = (Body_Condition["Back"]["Strength"]) + (Body_Condition["Shoulders"]["Strength"]* 0.4) + (Body_Condition["Chest"]["Strength"]* 0.6)
    Max_Health_Bonus = (Body_Condition["Chest"]["Strength"] *  6) + (Body_Condition["Back"]["Strength"] * 3) + (Body_Condition["Abdomen"]["Strength"]* 4)
    Stamina_Bonus = (Body_Condition["Legs"]["Strength"] * 5) + (Body_Condition["Abdomen"]["Strength"] * 3)
    Speed_Bonus = (Body_Condition["Legs"]["Strength"]* 0.8) + (Body_Condition["Trapezius"]["Strength"]*0.4)
    Accuracy_Bonus = (Body_Condition["Hands"]["Strength"]*0.7) + (Body_Condition["Shoulders"]["Strength"]* 0.3)
    Critical_Chance_Bonus = (Body_Condition["Hands"]["Strength"]*0.3) + (Body_Condition["Trapezius"]["Strength"]*0.2)
    Critical_Damage_Bonus = (Body_Condition["Hands"]["Strength"]*0.3) + (Body_Condition["Trapezius"]["Strength"]*0.2)
    Magic_Density_Bonus = (Body_Condition["Biceps"]["Strength"]* 1.2) + (Body_Condition["Triceps"]["Strength"] * 0.8) + (Body_Condition["Shoulders"]["Strength"]* 0.5)
    Magic_Damage_Bonus = (Body_Condition["Chest"]["Strength"]* 1.2) + (Body_Condition["Abdomen"]["Strength"] * 0.8) + (Body_Condition["Back"]["Strength"]* 0.5)
    Evasion_Bonus =  (Body_Condition["Abdomen"]["Strength"] * 0.8) + (Body_Condition["Legs"]["Strength"]* 0.5)
    Mana_Bonus = (Body_Condition["Head"]["Strength"] * 5) + (Body_Condition["Chest"]["Strength"] * 3) + (Body_Condition["Back"]["Strength"] * 4)
    Attack_Bonus = round(Attack_Bonus )
    Defense_Bonus = round(Defense_Bonus )
    Max_Health_Bonus = round(Max_Health_Bonus )
    Stamina_Bonus = round(Stamina_Bonus )
    Speed_Bonus = round(Speed_Bonus )
    Accuracy_Bonus = round(Accuracy_Bonus )
    Critical_Chance_Bonus = round(Critical_Chance_Bonus)
    Magic_Density_Bonus = round(Magic_Density_Bonus )
    Magic_Damage_Bonus = round(Magic_Damage_Bonus)
    Critical_Damage_Bonus = round(Critical_Damage_Bonus)
    Evasion_Bonus = round(Evasion_Bonus)
    Mana_Bonus = round(Mana_Bonus)
    Level_Scaling = (Base_Stats["Level"] * 0.04 ) + 1 
    Player["Attack"] = round((Base_Stats["Attack"] * Level_Scaling)+ Attack_Bonus )
    Player["Defense"] = round((Base_Stats["Defense"] * Level_Scaling) + Defense_Bonus)
    Player["Max Health"] = round((Base_Stats["Max Health"] * Level_Scaling) + Max_Health_Bonus)
    Player["Health"] = copy.deepcopy(Player["Max Health"])
    Player["Stamina"] = round((Base_Stats["Stamina"] * Level_Scaling) + Stamina_Bonus)
    Player["Speed"] = round((Base_Stats["Speed"] * Level_Scaling) + Speed_Bonus)
    Player["Accuracy"] = round((Base_Stats["Accuracy"] * Level_Scaling) + Accuracy_Bonus)
    Player["Critical Chance"] = round((Base_Stats["Critical Chance"] * Level_Scaling) + Critical_Chance_Bonus)
    Player["Magic Density"] = round((Base_Stats["Magic Density"] * Level_Scaling) + Magic_Density_Bonus)
    Player["Magic Damage"] = round((Base_Stats["Magic Damage"] * Level_Scaling) + Magic_Damage_Bonus)
    Player["Critical Damage"] = round((Base_Stats["Critical Damage"] * Level_Scaling) + Critical_Damage_Bonus)
    Player["Evasion"] = round((Base_Stats["Evasion"] * Level_Scaling) + Evasion_Bonus)
    Player["Mana"] = round((Base_Stats["Mana"] * Level_Scaling) + Mana_Bonus)
    if Player["Title"] == "Novice Slayer":
        Player["Attack"] *= 1.05
        Player["Attack"] = round(Player["Attack"])
        Player["Magic Damage"] *= 1.05
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Veteran Slayer":
        Player["Attack"] *= 1.1
        Player["Attack"] = round(Player["Attack"])
        Player["Magic Damage"] *= 1.1
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Legendary Slayer":
        Player["Attack"] *= 1.15
        Player["Attack"] = round(Player["Attack"])
        Player["Magic Damage"] *= 1.15
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Peak Physique":
        Player["Stamina"] *= 1.02
        Player["Stamina"] = round(Player["Stamina"])
    if Player["Title"] == "Recruit":
        Player["Attack"] *= 1.01
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.01
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.01
        Player["Speed"] = round(Player["Speed"])
    if Player["Title"] == "Fighter":
        Player["Attack"] *= 1.05
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.05
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.05
        Player["Speed"] = round(Player["Speed"])
    if Player["Title"] == "Veteran":
        Player["Attack"] *= 1.05
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.05
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.05
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.05
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.05
        Player["Mana"] = round(Player["Mana"])
    if Player["Title"] == "Battle-Hardened":
        Player["Attack"] *= 1.05
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.05
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.05
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.05
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.05
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.05
        Player["Magic Density"] = round(Player["Magic Density"])
    if Player["Title"] == "Seasoned Warrior":
        Player["Attack"] *= 1.05
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.05
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.05
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.05
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.05
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.05
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.05
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Elite Combatant":
        Player["Attack"] *= 1.075
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.075
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.075
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.075
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.075
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.075
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.075
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Champion":
        Player["Attack"] *= 1.1
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.1
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.1
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.1
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.1
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.1
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.1
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Warlord":
        Player["Attack"] *= 1.15
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.15
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.15
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.15
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.15
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.15
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.15
        Player["Magic Damage"] = round(Player["Magic Damage"])
    if Player["Title"] == "Conqueror":
        Player["Attack"] *= 1.15
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.15
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.15
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.15
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.15
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.15
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.15
        Player["Magic Damage"] = round(Player["Magic Damage"])
        Player["Critical Chance"] *= 1.05
        Player["Critical Chance"] = round(Player["Critical Chance"])
        Player["Critical Damage"] *= 1.1
        Player["Critical Damage"] = round(Player["Critical Damage"])
    if Player["Title"] == "Living Legend":
        Player["Attack"] *= 1.2
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.2
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.2
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.2
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.2
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.2
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.2
        Player["Magic Damage"] = round(Player["Magic Damage"])
        Player["Critical Chance"] *= 1.1
        Player["Critical Chance"] = round(Player["Critical Chance"])
        Player["Critical Damage"] *= 1.15
        Player["Critical Damage"] = round(Player["Critical Damage"])
    if Player["Title"] == "Eternal Warrior":
        Player["Attack"] *= 1.3
        Player["Attack"] = round(Player["Attack"])
        Player["Defense"] *= 1.3
        Player["Defense"] = round(Player["Defense"])
        Player["Speed"] *= 1.3
        Player["Speed"] = round(Player["Speed"])
        Player["Stamina"] *= 1.3
        Player["Stamina"] = round(Player["Stamina"])
        Player["Mana"] *= 1.3
        Player["Mana"] = round(Player["Mana"])
        Player["Magic Density"] *= 1.3
        Player["Magic Density"] = round(Player["Magic Density"])
        Player["Magic Damage"] *= 1.3
        Player["Magic Damage"] = round(Player["Magic Damage"])
        Player["Critical Chance"] *= 1.2
        Player["Critical Chance"] = round(Player["Critical Chance"])
        Player["Critical Damage"] *= 1.25
        Player["Critical Damage"] = round(Player["Critical Damage"])
        if Player["Title"] == "Winner":
            Player["Attack"] *= 1.1
            Player["Attack"] = round(Player["Attack"])
            Player["Magic Damage"] *= 1.1
        Player["Magic Damage"] = round(Player["Magic Damage"])
        if Player["Title"] == "The Professional":
            Player["Attack"] *= 1.15
            Player["Attack"] = round(Player["Attack"])
            Player["Magic Damage"] *= 1.15
        Player["Magic Damage"] = round(Player["Magic Damage"])
        if Player["Title"] == "Indomitable":
            Player["Attack"] *= 1.25
            Player["Attack"] = round(Player["Attack"])
            Player["Magic Damage"] *= 1.25
            Player["Magic Damage"] = round(Player["Magic Damage"])
        if Player["Title"] == "Unstoppable Force":
            Player["Attack"] *= 1.4
            Player["Attack"] = round(Player["Attack"])
            Player["Magic Damage"] *= 1.4
            Player["Magic Damage"] = round(Player["Magic Damage"])
        if Player["Title"] == "The One Above All":
            Player["Attack"] *= 1.5
            Player["Attack"] = round(Player["Attack"])
            Player["Magic Damage"] *= 1.5
            Player["Magic Damage"] = round(Player["Magic Damage"])
        if Player["Title"] == "Loser":
            Player["Defense"] *= 1.1
            Player["Defense"] = round(Player["Defense"])
        if Player["Title"] == "Scarred":
            Player["Defense"] *= 1.15
            Player["Defense"] = round(Player["Defense"])
        if Player["Title"] == "Tenacious":
            Player["Defense"] *= 1.25
            Player["Defense"] = round(Player["Defense"])
        if Player["Title"] == "The Immovable":
            Player["Defense"] *= 1.4
            Player["Defense"] = round(Player["Defense"])
        if Player["Title"] == "The Ever Enduring":
            Player["Defense"] *= 1.5
            Player["Defense"] = round(Player["Defense"])
        if Player["Title"] == "Unscathed":
            Player["Speed"] *= 1.05
            Player["Speed"] = round(Player["Speed"])
            Player["Evasion"] *= 1.05
            Player["Evasion"] = round(Player["Evasion"])
        if Player["Title"] == "Flawless Victor":
            Player["Speed"] *= 1.075
            Player["Speed"] = round(Player["Speed"])
            Player["Evasion"] *= 1.075
            Player["Evasion"] = round(Player["Evasion"])
        if Player["Title"] == "Phantom Menace":
            Player["Speed"] *= 1.125
            Player["Speed"] = round(Player["Speed"])
            Player["Evasion"] *= 1.125
            Player["Evasion"] = round(Player["Evasion"])
        if Player["Title"] == "Untouchable Duelist":
            Player["Speed"] *= 1.2
            Player["Speed"] = round(Player["Speed"])
            Player["Evasion"] *= 1.2
            Player["Evasion"] = round(Player["Evasion"])
        if Player["Title"] == "The Peerless Champion":
            Player["Speed"] *= 1.25
            Player["Speed"] = round(Player["Speed"])
            Player["Evasion"] *= 1.25
            Player["Evasion"] = round(Player["Evasion"])
        if Player["Title"] == "Trainee":
            Player["Stamina"] *= 1.05
            Player["Stamina"] = round(Player["Stamina"])
            Player["Mana"] *= 1.05
            Player["Mana"] = round(Player["Mana"])
        if Player["Title"] == "Dedicated":
            Player["Stamina"] *= 1.075
            Player["Stamina"] = round(Player["Stamina"])
            Player["Mana"] *= 1.075
            Player["Mana"] = round(Player["Mana"])
        if Player["Title"] == "Fanatic Trainer":
            Player["Stamina"] *= 1.125
            Player["Stamina"] = round(Player["Stamina"])
            Player["Mana"] *= 1.125
            Player["Mana"] = round(Player["Mana"])
        if Player["Title"] == "Tireless":
            Player["Stamina"] *= 1.2
            Player["Stamina"] = round(Player["Stamina"])
            Player["Mana"] *= 1.2
            Player["Mana"] = round(Player["Mana"])
        if Player["Title"] == "Pillar Of Discipline":
            Player["Stamina"] *= 1.25
            Player["Stamina"] = round(Player["Stamina"])
            Player["Mana"] *= 1.25
            Player["Mana"] = round(Player["Mana"])
        if Player["Title"] == "Virile":
            Player["Max Health"] *= 1.1
            Player["Max Health"] = round(Player["Max Health"])
            Player["Health"] = copy.deepcopy(Player["Max Health"])
        if Player["Title"] == "Hearty":
            Player["Max Health"] *= 1.15
            Player["Max Health"] = round(Player["Max Health"])
            Player["Health"] = copy.deepcopy(Player["Max Health"])
        if Player["Title"] == "Bulky":
            Player["Max Health"] *= 1.25
            Player["Max Health"] = round(Player["Max Health"])
            Player["Health"] = copy.deepcopy(Player["Max Health"])
        if Player["Title"] == "Behemoth":
            Player["Max Health"] *= 1.4
            Player["Max Health"] = round(Player["Max Health"])
            Player["Health"] = copy.deepcopy(Player["Max Health"])
        if Player["Title"] == "The Jade Emperor":
            Player["Max Health"] *= 1.5
            Player["Max Health"] = round(Player["Max Health"])
            Player["Health"] = copy.deepcopy(Player["Max Health"])

       
    Choice = input("")
    Choice = Choice.lower()
    Choice = "".join(Choice.split())

    if Choice in ["adventure","a","1"]:

        print("\n""---------------\n"f"Climb The Tower\n""---------------\n"f"Arena\n""---------------\n"f"Quests\n""---------------\n")
        Choice = (input(""))
            
        if Choice in ["t","tower","ctt","play","p","1","climbthetower"]:
            while True:
                try:
                    print("What Floor do you want to go to?")
                    Tower_Level_Choice = int(input(""))
                    if 0 < Tower_Level_Choice <= 100:
                        if Tower_Level_Choice > Player["Tower Level"]:
                            print("You have not reached this floor before")
                        else:
                            break
                    else:
                        print("Enter a number between 1 and and 100")
                except ValueError:
                    print("Not a Number between 1 and 100")
            Player_copy = copy.deepcopy(Player)

            result = T.Tower(Player,Player_copy,Enemy,Tower_Level_Choice,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,Move_Set,name,Statistics,Game,Body_Condition,Skill_Tree,Chest_items,Skill_Books,Proficiency,Amount_Used,typewriter)
            Outcome = result[0]
            Player["XP"] = result[1]
            Statistics = result[2]
            Player["Gold"] = result[3]
            Skill_Books = result[4]
            inventory = result[5]
            Amount_Used = result[6]
            Proficiency = result[7]
            Statistics["Battles Fought"] += 1
            if Outcome == "Enemy Win":
                print("\nYou lost... \n")
                Statistics["Battles Lost"] += 1
            if Outcome == "Player Win":
                if Tower_Level_Choice == Player["Tower Level"]:
                    Player["Tower Level"] += 1
                    print("\nYou unlocked the next floor\n")
                    Statistics["Battles Won"] += 1
                    
        elif Choice in ["arena","a","2"]:
            print("Do you want to fight a Monster or a Player?")
            decision = input("")
            if decision in ["1","monster","m"]:
                Player_copy = copy.deepcopy(Player)
                results = A.Monster_Arena(Player,Player_copy,Enemy,Combat_Skill_list,Spell_list,Gear,inventory,treasure_list,Move_Set,name,Statistics,Game,Body_Condition)
                Outcome = result[0]
                Player["XP"] = result[1]
                Statistics = result[2] 
                Statistics["Battles Fought"] += 1
                if Outcome == "Enemy Win":
                    print("\nYou lost... \n")
                    Statistics["Battles Lost"]  += 1
                if Outcome == "Player Win":
                    if Tower_Level_Choice == Player["Tower Level"]:
                        Player["Tower Level"] += 1
                        print("\nYou unlocked the next floor\n")
                        Statistics["Battles Won"] += 1
            elif decision in ["2","player","p"]:
                print("Not Finished :(\n\n Go away")
            else:
                print("Then go away!")
        elif Choice in ["quests","quest","q","3"]:
            print("----------------------------------------\n"f"                  Quests\n""----------------------------------------\n")
            decide = input("What method would you prefer?\n\n\n1. Show All\n\n2. Choose Specific Quest Categories\n").lower()
            decide = "".join(decide.split())
            if decide in ["1","showall","sa","s"]:
                print("\nNovice Slayer: [ Kill 100 Enemies ] ",Quests["Novice Slayer"],"\n")
                print("\nVeteran Slayer: [ Kill 1,000 Enemies ] ",Quests["Veteran Slayer"],"\n")
                print("\nLegendary Slayer: [ Kill 10,000 Enemies ] ",Quests["Legendary Slayer"],"\n")
                print("\nWell Built: [ Reach 1,000 Overall Body Condition ] ",Quests["Well Built"],"\n")
                print("\nPeak Physique: [ Reach 5,000 Overall Body Condition ] ",Quests["Peak Physique"],"\n")
                print("\nTrainee: [ Train 50 Times ] ",Quests["Trainee"],"\n")
                print("\nDedicated: [ Train 250 Times ] ",Quests["Dedicated"],"\n")
                print("\nFanatic Trainer: [ Train 1,000 Times ] ",Quests["Fanatic Trainer"],"\n")
                print("\nTireless: [ Train 5,000 Times ] ",Quests["Living Legend"],"\n")
                print("\nPillar Of Discipline: [ Train 10,000 Times ] ",Quests["Pillar Of Discipline"],"\n")
                print("\nForgehand: [ Forge 50 Gear ] ",Quests["Forgehand"],"\n")
                print("\nSkilled Blacksmith: [ Forge 250 Gear ] ",Quests["Skilled Blacksmith"],"\n")
                print("\nElite Craftsmen: [ Forge 1,000 Gear ] ",Quests["Elite Craftsmen"],"\n")
                print("\nMaster Of Metal: [ Forge 5,000 Gear ] ",Quests["Master Of Metal"],"\n")
                print("\nArtificer Of Legend: [ Forge 10,000 Gear ] ",Quests["Artificer Of Legend"],"\n")
                print("\nHerbalist: [ Brew 50 Potions ] ",Quests["Herbalist"],"\n")
                print("\nElixir Maker: [ Brew 250 Potions ] ",Quests["Elixir Maker"],"\n")
                print("\nSkilled Alchemist: [ Brew 1,000 Potions ] ",Quests["Skilled Alchemist"],"\n")
                print("\nGrandmaster Brewer: [ Brew 5,000 Potions ] ",Quests["Grandmaster Brewer"],"\n")
                print("\nThe One Who Knocks: [ Brew 10,000 Potions ] ",Quests["The One Who Knocks"],"\n")
                print("\nRecruit: [ Fight 25 Battles ] ",Quests["Recruit"],"\n")
                print("\nFighter: [ Fight 100 Battles ] ",Quests["Fighter"],"\n")
                print("\nVeteran: [ Fight 250 Battles ] ",Quests["Veteran"],"\n")
                print("\nBattle-Hardened: [ Fight 500 Battles ] ",Quests["Battle-Hardened"],"\n")
                print("\nSeasoned Warrior: [ Fight 1,000 Battles ] ",Quests["Seasoned Warrior"],"\n")
                print("\nElite Combatant: [ Fight 2,500 Battles ] ",Quests["Elite Combatant"],"\n")
                print("\nChampion: [ Fight 5,000 Battles ] ",Quests["Champion"],"\n")
                print("\nWarlord: [ Fight 10,000 Battles ] ",Quests["Warlord"],"\n")
                print("\nConqueror: [ Fight 25,000 Battles ] ",Quests["Conqueror"],"\n")
                print("\nLiving Legend: [ Fight 50,000 Battles ] ",Quests["Living Legend"],"\n")
                print("\nEternal Warrior: [ Fight 100,000 Battles ] ",Quests["Eternal Warrior"],"\n")
                print("\nWinner: [ Win 50 Battles ] ",Quests["Winner"],"\n")
                print("\nThe Professional: [ Win 500 Battles ] ",Quests["The Professional"],"\n")
                print("\nIndomitable: [ Win 2,500 Battles ] ",Quests["Indomitable"],"\n")
                print("\nUnstoppable Force: [ Win 10,000 Battles ] ",Quests["Unstoppable Force"],"\n")
                print("\nThe One Above All: [ Win 25,000 Battles ] ",Quests["The One Above All"],"\n")
                print("\nLoser: [ Lose 50 Battles ] ",Quests["Loser"],"\n")
                print("\nScarred: [ Lose 500 Battles ] ",Quests["Scarred"],"\n")
                print("\nTenacious: [ Lose 2,500 Battles ] ",Quests["Tenacious"],"\n")
                print("\nThe Immovable: [ Lose 100,00 Battles ] ",Quests["The Immovable"],"\n")
                print("\nThe Ever Enduring: [ Lose 250,00 Battles ] ",Quests["The Ever Enduring"],"\n")
                print("\nUnscathed: [ Win 10 Damageless Battles ] ",Quests["Unscathed"],"\n")
                print("\nFlawless Victor: [ Win 50 Damageless Battles ] ",Quests["Flawless Victor"],"\n")
                print("\nPhantom Menace: [ Win 250 Damageless Battles ] ",Quests["Phantom Menace"],"\n")
                print("\nUntouchable Duelist: [ Win 1,000 Damageless Battles ] ",Quests["Untouchable Duelist"],"\n")
                print("\nThe Peerless Champion: [ Win 5,000 Damageless Battles ] ",Quests["The Peerless Champion"],"\n")
                print("\nBoss Demolisher: [ Kill 5 Bosses ] ",Quests["Boss Demolisher"],"\n")
                print("\nGiant Annihilator: [ Kill 50 Bosses ] ",Quests["Giant Annihilator"],"\n")
                print("\nThe Bane Of Titans: [ Kill 250 Bosses ] ",Quests["The Bane Of Titans"],"\n")
                print("\nLegend Hunter: [ Kill 1,000 Bosses ] ",Quests["Legend Hunter"],"\n")
                print("\nOne Of The Greats: [ Kill 2,500 Bosses ] ",Quests["One Of The Greats"],"\n")
                print("\nPenny Pincher: [ Earn 1,000 Gold ] ",Quests["Penny Pincher"],"\n")
                print("\nHoarder: [ Earn 10,000 Gold ] ",Quests["Hoarder"],"\n")
                print("\nNoble: [ Earn 100,000 Gold ] ",Quests["Noble"],"\n")
                print("\nTycoon: [ Earn 1,000,000 Gold ] ",Quests["Tycoon"],"\n")
                print("\nMidas: [ Earn 10,000,000 Gold ] ",Quests["Midas"],"\n")
                print("\nSpender: [ Spend 1,000 Gold ] ",Quests["Spender"],"\n")
                print("\nBig Spender: [ Spend 10,000 Gold ] ",Quests["Big Spender"],"\n")
                print("\nHigh Roller: [ Spend 100,000 Gold ] ",Quests["High Roller"],"\n")
                print("\nDeep Pockets: [ Spend 1,000,000 Gold ] ",Quests["Deep Pockets"],"\n")
                print("\nPatron Of Treasure: [ Spend 10,000,000 Gold ] ",Quests["Patron Of Treasure"],"\n")
                print("\nVirile: [ Heal 1,000 Health ] ",Quests["Virile"],"\n")
                print("\nHearty: [ Heal 10,000 Health ] ",Quests["Hearty"],"\n")
                print("\nBulky: [ Heal 50,000 Health ] ",Quests["Bulky"],"\n")
                print("\nBehemoth: [ Heal 250,000 Health ] ",Quests["Behemoth"],"\n")
                print("\nThe Jade Emperor: [ Heal 1,000,000 Health ] ",Quests["The Jade Emperor"],"\n")
                
            if decide in ["2","choosespecificquestcategories","csqc","c"]:
                decide = input("Choose the category of quest you would like to look at\n\n1. Enemies Killed\n2. Training\n3. Battles Fought\n4. Battles Won\n5. Battles Lost\n6. Damageless Battles Won\n7. Bosses Killed\n8. Gold Earned\n9. Gold Spent\n10. Health Healed\n\n").lower()
                decide = "".join(decide.split())
                if decide in ["1","enemieskilled","ek"]:
                    print("\nNovice Slayer: [ Kill 100 Enemies ] ",Quests["Novice Slayer"],"\n")
                    print("\nVeteran Slayer: [ Kill 1,000 Enemies ] ",Quests["Veteran Slayer"],"\n")
                    print("\nLegendary Slayer: [ Kill 10,000 Enemies ] ",Quests["Legendary Slayer"],"\n")
                if decide in ["2","training","t"]:
                    print("\nWell Built: [ Reach 1,000 Overall Body Condition ] ",Quests["Well Built"],"\n")
                    print("\nPeak Physique: [ Reach 5,000 Overall Body Condition ] ",Quests["Peak Physique"],"\n")
                    print("\nTrainee: [ Train 50 Times ] ",Quests["Trainee"],"\n")
                    print("\nDedicated: [ Train 250 Times ] ",Quests["Dedicated"],"\n")
                    print("\nFanatic Trainer: [ Train 1,000 Times ] ",Quests["Fanatic Trainer"],"\n")
                    print("\nTireless: [ Train 5,000 Times ] ",Quests["Living Legend"],"\n")
                    print("\nPillar Of Discipline: [ Train 10,000 Times ] ",Quests["Pillar Of Discipline"],"\n")
                if decide in ["3","battlesfought","bf"]:
                    print("\nRecruit: [ Fight 25 Battles ] ",Quests["Recruit"],"\n")
                    print("\nFighter: [ Fight 100 Battles ] ",Quests["Fighter"],"\n")
                    print("\nVeteran: [ Fight 250 Battles ] ",Quests["Veteran"],"\n")
                    print("\nBattle-Hardened: [ Fight 500 Battles ] ",Quests["Battle-Hardened"],"\n")
                    print("\nSeasoned Warrior: [ Fight 1,000 Battles ] ",Quests["Seasoned Warrior"],"\n")
                    print("\nElite Combatant: [ Fight 2,500 Battles ] ",Quests["Elite Combatant"],"\n")
                    print("\nChampion: [ Fight 5,000 Battles ] ",Quests["Champion"],"\n")
                    print("\nWarlord: [ Fight 10,000 Battles ] ",Quests["Warlord"],"\n")
                    print("\nConqueror: [ Fight 25,000 Battles ] ",Quests["Conqueror"],"\n")
                    print("\nLiving Legend: [ Fight 50,000 Battles ] ",Quests["Living Legend"],"\n")
                    print("\nEternal Warrior: [ Fight 100,000 Battles ] ",Quests["Eternal Warrior"],"\n")
                if decide in ["4","battleswon","bw"]:
                    print("\nWinner: [ Win 50 Battles ] ",Quests["Winner"],"\n")
                    print("\nThe Professional: [ Win 500 Battles ] ",Quests["The Professional"],"\n")
                    print("\nIndomitable: [ Win 2,500 Battles ] ",Quests["Indomitable"],"\n")
                    print("\nUnstoppable Force: [ Win 10,000 Battles ] ",Quests["Unstoppable Force"],"\n")
                    print("\nThe One Above All: [ Win 25,000 Battles ] ",Quests["The One Above All"],"\n")
                if decide in ["5","battleslost","bw"]:
                    print("\nLoser: [ Lose 50 Battles ] ",Quests["Loser"],"\n")
                    print("\nScarred: [ Lose 500 Battles ] ",Quests["Scarred"],"\n")
                    print("\nTenacious: [ Lose 2,500 Battles ] ",Quests["Tenacious"],"\n")
                    print("\nThe Immovable: [ Lose 10,000 Battles ] ",Quests["The Immovable"],"\n")
                    print("\nThe Ever Enduring: [ Lose 25,000 Battles ] ",Quests["The Ever Enduring"],"\n")
                if decide in ["6","damagelessbattleswon","dbw"]:
                    print("\nUnscathed: [ Win 10 Damageless Battles ] ",Quests["Unscathed"],"\n")
                    print("\nFlawless Victor: [ Win 50 Damageless Battles ] ",Quests["Flawless Victor"],"\n")
                    print("\nPhantom Menace: [ Win 250 Damageless Battles ] ",Quests["Phantom Menace"],"\n")
                    print("\nUntouchable Duelist: [ Win 1,000 Damageless Battles ] ",Quests["Untouchable Duelist"],"\n")
                    print("\nThe Peerless Champion: [ Win 5,000 Damageless Battles ] ",Quests["The Peerless Champion"],"\n")
                if decide in ["7","bosseskilled","bk"]:
                    print("\nBoss Demolisher: [ Kill 5 Bosses ] ",Quests["Boss Demolisher"],"\n")
                    print("\nGiant Annihilator: [ Kill 50 Bosses ] ",Quests["Giant Annihilator"],"\n")
                    print("\nThe Bane Of Titans: [ Kill 250 Bosses ] ",Quests["The Bane Of Titans"],"\n")
                    print("\nLegend Hunter: [ Kill 1,000 Bosses ] ",Quests["Legend Hunter"],"\n")
                    print("\nOne Of The Greats: [ Kill 2,500 Bosses ] ",Quests["One Of The Greats"],"\n")
                if decide in ["8","goldearned","ge"]:
                    print("\nPenny Pincher: [ Earn 1,000 Gold ] ",Quests["Penny Pincher"],"\n")
                    print("\nHoarder: [ Earn 10,000 Gold ] ",Quests["Hoarder"],"\n")
                    print("\nNoble: [ Earn 100,000 Gold ] ",Quests["Noble"],"\n")
                    print("\nTycoon: [ Earn 1,000,000 Gold ] ",Quests["Tycoon"],"\n")
                    print("\nMidas: [ Earn 10,000,000 Gold ] ",Quests["Midas"],"\n")
                if decide in ["9","goldspent","gp"]:
                    print("\nSpender: [ Spend 1,000 Gold ] ",Quests["Spender"],"\n")
                    print("\nBig Spender: [ Spend 10,000 Gold ] ",Quests["Big Spender"],"\n")
                    print("\nHigh Roller: [ Spend 100,000 Gold ] ",Quests["High Roller"],"\n")
                    print("\nDeep Pockets: [ Spend 1,000,000 Gold ] ",Quests["Deep Pockets"],"\n")
                    print("\nPatron Of Treasure: [ Spend 10,000,000 Gold ] ",Quests["Patron Of Treasure"],"\n")
                if decide in ["10","healthhealed","h","hh"]:
                    print("\nVirile: [ Heal 1,000 Health ] ",Quests["Virile"],"\n")
                    print("\nHearty: [ Heal 10,000 Health ] ",Quests["Hearty"],"\n")
                    print("\nBulky: [ Heal 50,000 Health ] ",Quests["Bulky"],"\n")
                    print("\nBehemoth: [ Heal 250,000 Health ] ",Quests["Behemoth"],"\n")
                    print("\nThe Jade Emperor: [ Heal 1,000,000 Health ] ",Quests["The Jade Emperor"],"\n")
            time.sleep(2)
            print("\n\n\n")
            if Statistics["Enemies Killed"] >= 1000 and "Novice Slayer" not in Titles:
                print("\n\nYou unlocked the title of Novice Slayer!\n\n  [ gain 5% more Attack ]\n\n [ gain 5% more Magic Damage ]")
                Titles.append("Novice Slayer")
                Quests["Novice Slayer"] = "(Completed) [ gain 5% more Attack ] [ gain 5% more Magic Damage ]"
            if Statistics["Enemies Killed"] >= 10000 and "Veteran Slayer" not in Titles:
                print("\n\nYou unlocked the title of Veteran Slayer!\n\n  [ gain 10% more Attack ]\n\n [ gain 10% more Magic Damage ]")
                Titles.append("Veteran Slayer")
                Quests["Veteran Slayer"] = "(Completed) [ gain 10% more Attack ] [ gain 10% more Magic Damage ]"
            if Statistics["Enemies Killed"] >= 100000 and "Legendary Slayer" not in Titles:
                print("\n\nYou unlocked the title of Legendary Slayer!\n\n  [ gain 15% more Attack ]\n\n [ gain 10% more Magic Damage ]")
                Titles.append("Legendary Slayer")
                Quests["Legendary Slayer"] = "(Completed) [ gain 15% more Attack ] [ gain 10% more Magic Damage ]"
            if (Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"] + Body_Condition["Shoulders"]["Strength"] + Body_Condition["Chest"]["Strength"] + Body_Condition["Trapezius"]["Strength"] + Body_Condition["Abdomen"]["Strength"] + Body_Condition["Back"]["Strength"] + Body_Condition["Legs"]["Strength"]) >= 1000 and "Well Built" not in Titles:
                print("\n\nYou unlocked the title of Well Built!\n\n  [ gain 25 more body condition capacity ]")
                Titles.append("Well Built")
                Quests["Well Built"] = "(Completed) [ gain 25 more body condition capacity ]"
            if (Body_Condition["Biceps"]["Strength"] + Body_Condition["Triceps"]["Strength"] + Body_Condition["Hands"]["Strength"] + Body_Condition["Shoulders"]["Strength"] + Body_Condition["Chest"]["Strength"] + Body_Condition["Trapezius"]["Strength"] + Body_Condition["Abdomen"]["Strength"] + Body_Condition["Back"]["Strength"] + Body_Condition["Legs"]["Strength"]) >= 5000 and "Peak Physique" not in Titles:
                print("\n\nYou unlocked the title of Peak Physique!\n\n  [ gain 50 more body condition capacity ]\n\n  [ gain 2% more stamina ]")
                Titles.append("Peak Physique")
                Quests["Peak Physique"] = "(Completed) [ gain 50 more body condition capacity ]  [ gain 2% more stamina ]"
            if Statistics["Battles Fought"] >= 25 and "Recruit" not in Titles:
                print("\n\nYou unlocked the title of Recruit!\n\n  [ gain 1% more Attack ]\n\n [ gain 1% more Speed ]\n\n [ gain 1% more Defense ]")
                Titles.append("Recruit")
                Quests["Recruit"] = "(Completed) [ gain 1% more Attack ] [ gain 1% more Speed ] [ gain 1% more Defense ]"
            if Statistics["Battles Fought"] >= 100 and "Fighter" not in Titles:
                print("\n\nYou unlocked the title of Fighter!\n\n  [ gain 5% more Attack ]\n\n [ gain 5% more Speed ]\n\n [ gain 5% more Defense ]")
                Titles.append("Fighter")
                Quests["Fighter"] = "(Completed) [ gain 5% more Attack ] [ gain 5% more Speed ] [ gain 5% more Defense ]"
            if Statistics["Battles Fought"] >= 250 and "Veteran" not in Titles:
                print("\n\nYou unlocked the title of Veteran!\n\n  [ gain 5% more Attack ]\n\n [ gain 5% more Speed ]\n\n [ gain 5% more Defense ]\n\n [ gain 5% more Stamina ]\n\n [ gain 5% more Mana ]")
                Titles.append("Veteran")
                Quests["Veteran"] = "(Completed) [ gain 5% more Attack ] [ gain 5% more Speed ] [ gain 5% more Defense ] [ gain 5% more Stamina ] [ gain 5% more Mana ]"
            if Statistics["Battles Fought"] >= 500 and "Battle-Hardened" not in Titles:
                print("\n\nYou unlocked the title of Battle-Hardened!\n\n  [ gain 5% more Attack ]\n\n [ gain 5% more Speed ]\n\n [ gain 5% more Defense ]\n\n [ gain 5% more Stamina ]\n\n [ gain 5% more Mana ]\n\n [ gain 5% more Magic Density ]")
                Titles.append("Battle-Hardened")
                Quests["Battle-Hardened"] = "(Completed) [ gain 5% more Attack ] [ gain 5% more Speed ] [ gain 5% more Defense ] [ gain 5% more Stamina ] [ gain 5% more Mana ] [ gain 5% more Magic Density ]"
            if Statistics["Battles Fought"] >= 1000 and "Seasoned Warrior" not in Titles:
                print("\n\nYou unlocked the title of Seasoned Warrior!\n\n  [ gain 5% more Attack ]\n\n [ gain 5% more Speed ]\n\n [ gain 5% more Defense ]\n\n [ gain 5% more Stamina ]\n\n [ gain 5% more Mana ]\n\n [ gain 5% more Magic Density ]\n\n [ gain 5% more Magic Damage ]")
                Titles.append("Seasoned Warrior")
                Quests["Seasoned Warrior"] = "(Completed) [ gain 5% more Attack ] [ gain 5% more Speed ] [ gain 5% more Defense ] [ gain 5% more Stamina ] [ gain 5% more Mana ] [ gain 5% more Magic Density ] [ gain 5% more Magic Damage ]"
            if Statistics["Battles Fought"] >= 2500 and "Elite Combatant" not in Titles:
                print("\n\nYou unlocked the title of Elite Combatant!\n\n  [ gain 7.5% more Attack ]\n\n [ gain 7.5% more Speed ]\n\n [ gain 7.5% more Defense ]\n\n [ gain 7.5% more Stamina ]\n\n [ gain 7.5% more Mana ]\n\n [ gain 7.5% more Magic Density ]\n\n [ gain 7.5% more Magic Damage ]")
                Titles.append("Elite Combatant")
                Quests["Elite Combatant"] = "(Completed) [ gain 7.5% more Attack ] [ gain 7.5% more Speed ] [ gain 7.5% more Defense ] [ gain 7.5% more Stamina ] [ gain 7.5% more Mana ] [ gain 7.5% more Magic Density ] [ gain 7.5% more Magic Damage ]"
            if Statistics["Battles Fought"] >= 5000 and "Champion" not in Titles:
                print("\n\nYou unlocked the title of Champion!\n\n  [ gain 10% more Attack ]\n\n [ gain 10% more Speed ]\n\n [ gain 10% more Defense ]\n\n [ gain 10% more Stamina ]\n\n [ gain 10% more Mana ]\n\n [ gain 10% more Magic Density ]\n\n [ gain 10% more Magic Damage ]")
                Titles.append("Champion")
                Quests["Champion"] = "(Completed) [ gain 10% more Attack ] [ gain 10% more Speed ] [ gain 10% more Defense ] [ gain 10% more Stamina ] [ gain 10% more Mana ] [ gain 10% more Magic Density ] [ gain 10% more Magic Damage ]"
            if Statistics["Battles Fought"] >= 10000 and "Warlord" not in Titles:
                print("\n\nYou unlocked the title of Warlord!\n\n  [ gain 15% more Attack ]\n\n [ gain 15% more Speed ]\n\n [ gain 15% more Defense ]\n\n [ gain 15% more Stamina ]\n\n [ gain 15% more Mana ]\n\n [ gain 15% more Magic Density ]\n\n [ gain 15% more Magic Damage ]")
                Titles.append("Warlord")
                Quests["Warlord"] = "(Completed) [ gain 15% more Attack ] [ gain 15% more Speed ] [ gain 15% more Defense ] [ gain 15% more Stamina ] [ gain 15% more Mana ] [ gain 15% more Magic Density ] [ gain 15% more Magic Damage ]"
            if Statistics["Battles Fought"] >= 25000 and "Conqueror" not in Titles:
                print("\n\nYou unlocked the title of Conqueror!\n\n  [ gain 15% more Attack ]\n\n [ gain 15% more Speed ]\n\n [ gain 15% more Defense ]\n\n [ gain 15% more Stamina ]\n\n [ gain 15% more Mana ]\n\n [ gain 15% more Magic Density ]\n\n [ gain 15% more Magic Damage ]\n\n [ gain 10% more Critical Damage ]\n\n [ gain 5% more Critical Chance ]")
                Titles.append("Conqueror")
                Quests["Conqueror"] = "(Completed) [ gain 15% more Attack ] [ gain 15% more Speed ] [ gain 15% more Defense ] [ gain 15% more Stamina ] [ gain 15% more Mana ] [ gain 15% more Magic Density ] [ gain 15% more Magic Damage ] [ gain 10% more Critical Damage ] [ gain 5% more Critical Chance ]"
            if Statistics["Battles Fought"] >= 50000 and "Living Legend" not in Titles:
                print("\n\nYou unlocked the title of Living Legend!\n\n  [ gain 20% more Attack ]\n\n [ gain 20% more Speed ]\n\n [ gain 20% more Defense ]\n\n [ gain 20% more Stamina ]\n\n [ gain 20% more Mana ]\n\n [ gain 20% more Magic Density ]\n\n [ gain 20% more Magic Damage ]\n\n [ gain 15% more Critical Damage ]\n\n [ gain 10% more Critical Chance ]")
                Titles.append("Living Legend")
                Quests["Living Legend"] = "(Completed) [ gain 20% more Attack ] [ gain 20% more Speed ] [ gain 20% more Defense ] [ gain 20% more Stamina ] [ gain 20% more Mana ] [ gain 20% more Magic Density ] [ gain 20% more Magic Damage ] [ gain 15% more Critical Damage ] [ gain 10% more Critical Chance ]"
            if Statistics["Battles Fought"] >= 100000 and "Eternal Warrior" not in Titles:
                print("\n\nYou unlocked the title of Eternal Warrior!\n\n  [ gain 30% more Attack ]\n\n [ gain 30% more Speed ]\n\n [ gain 30% more Defense ]\n\n [ gain 30% more Stamina ]\n\n [ gain 30% more Mana ]\n\n [ gain 30% more Magic Density ]\n\n [ gain 30% more Magic Damage ]\n\n [ gain 25% more Critical Damage ]\n\n [ gain 20% more Critical Chance ]")
                Titles.append("Eternal Warrior")
                Quests["Eternal Warrior"] = "(Completed) [ gain 30% more Attack ] [ gain 30% more Speed ] [ gain 30% more Defense ] [ gain 30% more Stamina ] [ gain 30% more Mana ] [ gain 30% more Magic Density ] [ gain 30% more Magic Damage ] [ gain 25% more Critical Damage ] [ gain 20% more Critical Chance ]"
            if Statistics["Battles Won"] >= 50 and "Winner" not in Titles:
                print("\n\nYou unlocked the title of Winner!\n\n [ gain 10% more Attack ]\n\n [ gain 10% more Magic Damage ]")
                Titles.append("Winner")
                Quests["Winner"] = "(Completed) [ gain 10% more Attack ] [ gain 10% more Magic Damage ]"
            if Statistics["Battles Won"] >= 500 and "The Professional" not in Titles:
                print("\n\nYou unlocked the title of The Professional!\n\n [ gain 15% more Attack ]\n\n [ gain 15% more Magic Damage ]")
                Titles.append("The Professional")
                Quests["The Professional"] = "(Completed) [ gain 15% more Attack ] [ gain 15% more Magic Damage ]"
            if Statistics["Battles Won"] >= 2500 and "Indomitable" not in Titles:
                print("\n\nYou unlocked the title of Indomitable!\n\n [ gain 25% more Attack ]\n\n [ gain 25% more Magic Damage ]")
                Titles.append("Indomitable")
                Quests["Indomitable"] = "(Completed) [ gain 25% more Attack ] [ gain 25% more Magic Damage ]"
            if Statistics["Battles Won"] >= 10000 and "Unstoppable Force" not in Titles:
                print("\n\nYou unlocked the title of Unstoppable Force!\n\n [ gain 40% more Attack ]\n\n [ gain 40% more Magic Damage ]")
                Titles.append("Unstoppable Force")
                Quests["Unstoppable Force"] = "(Completed) [ gain 40% more Attack ] [ gain 40% more Magic Damage ]"
            if Statistics["Battles Won"] >= 25000 and "The One Above All" not in Titles:
                print("\n\nYou unlocked the title of The One Above All!\n\n [ gain 50% more Attack ]\n\n [ gain 50% more Magic Damage ]")
                Titles.append("The One Above All")
                Quests["The One Above All"] = "(Completed) [ gain 50% more Attack ]\n\n [ gain 50% more Magic Damage ]"
            if Statistics["Battles Lost"] >= 50 and "Loser" not in Titles:
                print("\n\nYou unlocked the title of Loser!\n\n [ gain 10% more Defense ]")
                Titles.append("Loser")
                Quests["Loser"] = "(Completed) [ gain 10% more Defense ]"
            if Statistics["Battles Lost"] >= 500 and "Scarred" not in Titles:
                print("\n\nYou unlocked the title of Scarred!\n\n [ gain 15% more Defense ]")
                Titles.append("Scarred")
                Quests["Scarred"] = "(Completed) [ gain 15% more Defense ]"
            if Statistics["Battles Lost"] >= 2500 and "Tenacious" not in Titles:
                print("\n\nYou unlocked the title of Tenacious!\n\n [ gain 25% more Defense ]")
                Titles.append("Tenacious")
                Quests["Tenacious"] = "(Completed) [ gain 25% more Defense ]"
            if Statistics["Battles Lost"] >= 10000 and "The Immovable" not in Titles:
                print("\n\nYou unlocked the title of The Immovable!\n\n [ gain 40% more Defense ]")
                Titles.append("The Immovable")
                Quests["The Immovable"] = "(Completed) [ gain 40% more Defense ]"
            if Statistics["Battles Lost"] >= 25000 and "The Ever Enduring" not in Titles:
                print("\n\nYou unlocked the title of The Ever Enduring!\n\n [ gain 50% more Defense ]")
                Titles.append("The Ever Enduring")
                Quests["The Ever Enduring"] = "(Completed) [ gain 50% more Defense ]"
            if Statistics["Damageless Battles Won"] >= 10 and "Unscathed" not in Titles:
                print("\n\nYou unlocked the title of Unscathed!\n\n [ gain 5% more Speed ]\n\n [ gain 5% more Evasion ]")
                Titles.append("Unscathed")
                Quests["Unscathed"] = "(Completed) [ gain 5% more Speed ] [ gain 5% more Evasion ]"
            if Statistics["Damageless Battles Won"] >= 50 and "Flawless Victor" not in Titles:
                print("\n\nYou unlocked the title of Flawless Victor!\n\n [ gain 7.5% more Speed ]\n\n [ gain 7.5% more Evasion ]")
                Titles.append("Flawless Victor")
                Quests["Flawless Victor"] = "(Completed) [ gain 7.5% more Speed ] [ gain 7.5% more Evasion ]"
            if Statistics["Damageless Battles Won"] >= 250 and "Phantom Menace" not in Titles:
                print("\n\nYou unlocked the title of Phantom Menace!\n\n [ gain 12.5% more Speed ]\n\n [ gain 12.5% more Evasion ]")
                Titles.append("Phantom Menace")
                Quests["Phantom Menace"] = "(Completed) [ gain 12.5% more Speed ] [ gain 12.5% more Evasion ]"
            if Statistics["Damageless Battles Won"] >= 1000 and "Untouchable Duelist" not in Titles:
                print("\n\nYou unlocked the title of Untouchable Duelist!\n\n [ gain 20% more Speed ]\n\n [ gain 20% more Evasion ]")
                Titles.append("Untouchable Duelist")
                Quests["Untouchable Duelist"] = "(Completed) [ gain 20% more Speed ] [ gain 20% more Evasion ]"
            if Statistics["Damageless Battles Won"] >= 5000 and "The Peerless Champion" not in Titles:
                print("\n\nYou unlocked the title of The Peerless Champion!\n\n [ gain 25% more Speed ]\n\n [ gain 25% more Evasion ]")
                Titles.append("The Peerless Champion")
                Quests["The Peerless Champion"] = "(Completed) [ gain 25% more Speed ] [ gain 25% more Evasion ]"
            if Statistics["Bosses Killed"] >= 50 and "Boss Demolisher" not in Titles:
                print("\n\nYou unlocked the title of Boss Demolisher!\n\n [ gain 20% more Attack to Bosses ]\n\n [ gain 20% more Magic Damage to Bosses ]")
                Titles.append("Boss Demolisher")
                Quests["Boss Demolisher"] = "(Completed) [ gain 20% more Attack to Bosses ] [ gain 20% more Magic Damage to Bosses ]"
            if Statistics["Bosses Killed"] >= 500 and "Giant Annihilator" not in Titles:
                print("\n\nYou unlocked the title of Giant Annihilator!\n\n [ gain 30% more Attack to Bosses ]\n\n [ gain 30% more Magic Damage to Bosses ]")
                Titles.append("Giant Annihilator")
                Quests["Giant Annihilator"] = "(Completed) [ gain 30% more Attack to Bosses ] [ gain 30% more Magic Damage to Bosses ]"
            if Statistics["Bosses Killed"] >= 2500 and "The Bane Of Titans" not in Titles:
                print("\n\nYou unlocked the title of The Bane Of Titans!\n\n [ gain 50% more Attack to Bosses ]\n\n [ gain 50% more Magic Damage to Bosses ]")
                Titles.append("The Bane Of Titans")
                Quests["The Bane Of Titans"] = "(Completed) [ gain 50% more Attack to Bosses ] [ gain 50% more Magic Damage to Bosses ]"
            if Statistics["Bosses Killed"] >= 10000 and "Legend Hunter" not in Titles:
                print("\n\nYou unlocked the title of Legend Hunter!\n\n [ gain 80% more Attack to Bosses ]\n\n [ gain 80% more Magic Damage to Bosses ]")
                Titles.append("Legend Hunter")
                Quests["Legend Hunter"] = "(Completed) [ gain 80% more Attack to Bosses ] [ gain 80% more Magic Damage to Bosses ]"
            if Statistics["Bosses Killed"] >= 25000 and "One Of The Greats" not in Titles:
                print("\n\nYou unlocked the title of One Of The Greats!\n\n [ gain 100% more Attack to Bosses ]\n\n [ gain 100% more Magic Damage to Bosses ]")
                Titles.append("One Of The Greats")
                Quests["One Of The Greats"] = "(Completed) [ gain 100% more Attack to Bosses ]\n\n [ gain 100% more Magic Damage to Bosses ]"
            if Statistics["Gold Earned"] >= 1000 and "Penny Pincher" not in Titles:
                print("\n\nYou unlocked the title of Penny Pincher!\n\n [ gain 10% more Gold ]")
                Titles.append("Penny Pincher")
                Quests["Penny Pincher"] = "(Completed) [ gain 10% more Gold ]"
            if Statistics["Gold Earned"] >= 10000 and "Hoarder" not in Titles:
                print("\n\nYou unlocked the title of Hoarder!\n\n [ gain 20% more Gold ]")
                Titles.append("Hoarder")
                Quests["Hoarder"] = "(Completed) [ gain 20% more Gold ]"
            if Statistics["Gold Earned"] >= 100000 and "Noble" not in Titles:
                print("\n\nYou unlocked the title of Noble!\n\n [ gain 30% more Gold ]")
                Titles.append("Noble")
                Quests["Noble"] = "(Completed) [ gain 30% more Gold ]"
            if Statistics["Gold Earned"] >= 1000000 and "Tycoon" not in Titles:
                print("\n\nYou unlocked the title of Tycoon!\n\n [ gain 40% more Gold ]")
                Titles.append("Tycoon")
                Quests["Tycoon"] = "(Completed) [ gain 40% more Gold ]"
            if Statistics["Gold Earned"] >= 10000000 and "Midas" not in Titles:
                print("\n\nYou unlocked the title of Midas!\n\n [ gain 50% more Gold ]")
                Titles.append("Midas")
                Quests["Midas"] = "(Completed) [ gain 50% more Gold ]"
            if Statistics["Gold Spent"] >= 1000 and "Spender" not in Titles:
                print("\n\nYou unlocked the title of Spender!\n\n [ 20% treasure chance ]")
                Titles.append("Spender")
                Quests["Spender"] = "(Completed) [ 20% treasure chance ]"
            if Statistics["Gold Spent"] >= 10000 and "Big Spender" not in Titles:
                print("\n\nYou unlocked the title of Big Spender!\n\n [ 30% treasure chance ]")
                Titles.append("Big Spender")
                Quests["Big Spender"] = "(Completed) [ 30% treasure chance ]"
            if Statistics["Gold Spent"] >= 100000 and "High Roller" not in Titles:
                print("\n\nYou unlocked the title of High Roller!\n\n [ 45% treasure chance ]")
                Titles.append("High Roller")
                Quests["High Roller"] = "(Completed) [ 45% treasure chance ]"
            if Statistics["Gold Earned"] >= 1000000 and "Deep Pockets" not in Titles:
                print("\n\nYou unlocked the title of Deep Pockets!\n\n [ 60% treasure chance ]")
                Titles.append("Deep Pockets")
                Quests["Deep Pockets"] = "(Completed) [ 60% treasure chance ]"
            if Statistics["Gold Earned"] >= 10000000 and "Patron Of Treasure" not in Titles:
                print("\n\nYou unlocked the title of Patron Of Treasure!\n\n [ 75% treasure chance ]")
                Titles.append("Patron Of Treasure")
                Quests["Patron Of Treasure"] = "(Completed) [ 75% treasure chance ]"
            if Statistics["Training Sessions"] >= 50 and "Trainee" not in Titles:
                print("\n\nYou unlocked the title of Trainee!\n\n [ 5% more Stamina ]\n\n [ 5% more Mana ]")
                Titles.append("Trainee")
                Quests["Trainee"] = "(Completed) [ 5% more Stamina ]\n\n [ 5% more Stamina ]"
            if Statistics["Training Sessions"] >= 250 and "Dedicated" not in Titles:
                print("\n\nYou unlocked the title of Dedicated!\n\n [ 7.5% more Stamina ]\n\n [ 7.5% more Mana ]")
                Titles.append("Dedicated")
                Quests["Dedicated"] = "(Completed) [ 7.5% more Stamina ]\n\n [ 7.5% more Mana ]"
            if Statistics["Training Sessions"] >= 1000 and "Fanatic Trainer" not in Titles:
                print("\n\nYou unlocked the title of Fanatic Trainer!\n\n [ 12.5% more Stamina ]\n\n [ 12.5% more Mana ]")
                Titles.append("Fanatic Trainer")
                Quests["Fanatic Trainer"] = "(Completed) [ 12.5% more Stamina ]\n\n [ 12.5% more Mana ]"
            if Statistics["Training Sessions"] >= 5000 and "Tireless" not in Titles:
                print("\n\nYou unlocked the title of Tireless!\n\n [ 20% more Stamina ]\n\n [ 20% more Mana ]")
                Titles.append("Tireless")
                Quests["Tireless"] = "(Completed) [ 20% more Stamina ]\n\n [ 20% more Mana ]"
            if Statistics["Training Sessions"] >= 10000 and "Pillar Of Discipline" not in Titles:
                print("\n\nYou unlocked the title of Pillar Of Discipline!\n\n [ 25% more Stamina ]\n\n [ 25% more Mana ]")
                Titles.append("Pillar Of Discipline")
                Quests["Pillar Of Discipline"] = "(Completed) [ 25% more Stamina ]\n\n [ 25% more Mana ]"
            if Statistics["Gold Earned"] >= 1000 and "Virile" not in Titles:
                print("\n\nYou unlocked the title of Virile!\n\n [ gain 10% more Max Health ]")
                Titles.append("Virile")
                Quests["Virile"] = "(Completed) [ gain 10% more Max Health ]"
            if Statistics["Gold Earned"] >= 10000 and "Hearty" not in Titles:
                print("\n\nYou unlocked the title of Hearty!\n\n [ gain 15% more Max Health ]")
                Titles.append("Hearty")
                Quests["Hearty"] = "(Completed) [ gain 15% more Max Health ]"
            if Statistics["Gold Earned"] >= 50000 and "Bulky" not in Titles:
                print("\n\nYou unlocked the title of Bulky!\n\n [ gain 25% more Max Health ]")
                Titles.append("Bulky")
                Quests["Bulky"] = "(Completed) [ gain 25% more Max Health ]"
            if Statistics["Gold Earned"] >= 250000 and "Behemoth" not in Titles:
                print("\n\nYou unlocked the title of Behemoth!\n\n [ gain 40% more Max Health ]")
                Titles.append("Behemoth")
                Quests["Behemoth"] = "(Completed) [ gain 40% more Max Health ]"
            if Statistics["Gold Earned"] >= 1000000 and "The Jade Emperor" not in Titles:
                print("\n\nYou unlocked the title of The Jade Emperor!\n\n [ gain 50% more Max Health ]")
                Titles.append("The Jade Emperor")
                Quests["The Jade Emperor"] = "(Completed) [ gain 50% more Max Health ]"
            back = input("\n\nPress enter to go back")






        
    elif Choice in ["Character","2","c"]:
        print("\n---------------\n"f"Avatar\n""---------------\n"f"Skill Tree""\n---------------\n"f"Combatives\n---------------\n"f"Move Memory\n---------------\nUse Skill Book\n---------------\nTitles\n---------------\n\n")
        Choice = input("")
        if Choice in ["avatar","a","1"]:


        
            print(f"--------------\n\n   Name\n\n--------------\n   {name}\n--------------\nGear\n---------------\nHead:",Gear["Type"]["Helmet"],"\nShoulder:",Gear["Type"]["Shoulderwear"],"\nArm:",Gear["Type"]["Armwear"],"\nChest:",Gear["Type"]["Chestplate"],"\nLeg:",Gear["Type"]["Legwear"],"\nFeet:",Gear["Type"]["Footwear"],"\n---------------")
            if Gear["Type"]["Weapon"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                print("Weapon:", Gear["Type"]["Weapon"])
                print("---------------")
            if any(Gear.values()) or (inventory.get("Gear") and len(inventory["Gear"]) > 0):
                print("\nDo you want to equip or unequip  something?\n")
                confirmation = input("")
                confirmation = confirmation.lower()
                if "ye" in confirmation:
                    def normalize_input(text):
                        return "".join(text.lower().split())


                    def display_gear():
                        print("--------------\nGear\n---------------\nHead:",Gear["Type"]["Helmet"],"\nShoulder:",Gear["Type"]["Shoulderwear"],"\nArm:",Gear["Type"]["Armwear"],"\nChest:",Gear["Type"]["Chestplate"],"\nLeg:",Gear["Type"]["Legwear"],"\nFeet:",Gear["Type"]["Footwear"],"\n---------------")
                        if Gear["Type"]["Weapon"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                            print("Weapon:", Gear["Type"]["Weapon"])
                            print("---------------")
                        print("\n\nInventory\n---------------")
                        for key,value in inventory.items():
                            print(key,":",value,"\n")
                        print("---------------")
                        
                        


                    def gear_menu():
                        while True:
                            print("\n1. Equip\n2. Unequip\n3. Show Gear\n4. Exit")
                            choice = input("Choose: ").strip()

                            if choice == "1":
                                print("What Item do you want to equip?")
                                option = input("").lower()
                                option = "".join(option.split())
                                print("\n\n")
                                if Gear["Type"]["Weapon"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    if "Copper Dagger" in inventory["Gear"] and option == "copperdagger":
                                        Gear["Type"]["Weapon"] = {"Copper Dagger":{"Attack":3,"Magic Damage":0,"Critical Chance":0,"Speed":2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Dagger"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Dagger":{"Attack":4,"Magic Damage":0,"Critical Chance":5,"Speed":3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Dagger"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Dagger":{"Attack":6,"Magic Damage":0,"Critical Chance":15,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Dagger"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Dagger":{"Attack":8,"Magic Damage":0,"Critical Chance":25,"Speed":8,"Defense":0,"Max Health":0}}
                                        if Proficiency["Dagger"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Dagger":{"Attack":10,"Magic Damage":0,"Critical Chance":30,"Speed":10,"Defense":0,"Max Health":0}}
                                        if Proficiency["Dagger"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Dagger":{"Attack":12,"Magic Damage":0,"Critical Chance":40,"Speed":15,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Dagger"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Dagger"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Dagger"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Dagger"]["Critical Chance"]
                                        Weapon_Name = "Copper Dagger"
                                    elif "Crude Staff" in inventory["Gear"] and option == "crudestaff":
                                        Gear["Type"]["Weapon"] = {"Crude Staff":{"Attack":0,"Magic Damage":4,"Critical Chance":5,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Crude Staff":{"Attack":0,"Magic Damage":6,"Critical Chance":10,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Crude Staff":{"Attack":0,"Magic Damage":8,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Crude Staff":{"Attack":0,"Magic Damage":12,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Crude Staff":{"Attack":0,"Magic Damage":16,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Crude Staff":{"Attack":0,"Magic Damage":20,"Critical Chance":40,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Crude Staff"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Crude Staff"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Crude Staff"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Crude Staff"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Crude Staff"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Crude Staff"]["Max Health"] 
                                        Weapon_Name = "Crude Staff"
                                    elif "Copper Helmet" in inventory["Gear"] and option == "copperhelmet":
                                        Gear["Type"]["Helmet"] = {"Copper Helmet":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":3,"Max Health":20}}
                                        Base_Stats["Attack"] += Gear["Type"]["Helmet"]["Copper Helmet"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Helmet"]["Copper Helmet"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Helmet"]["Copper Helmet"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Helmet"]["Copper Helmet"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Helmet"]["Copper Helmet"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Helmet"]["Copper Helmet"]["Max Health"] 
                                        Helmet_Name = "Copper Helmet"
                                    elif "Copper Chestplate" in inventory["Gear"] and option == "copperchestplate":
                                        Gear["Type"]["Chestplate"] = {"Copper Chestplate":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":4,"Max Health":10}}
                                        Base_Stats["Attack"] += Gear["Type"]["Chestplate"]["Copper Chestplate"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Chestplate"]["Copper Chestplate"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Chestplate"]["Copper Chestplate"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Chestplate"]["Copper Chestplate"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Chestplate"]["Copper Chestplate"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Chestplate"]["Copper Chestplate"]["Max Health"] 
                                        Chestplate_Name = "Copper Chestplate"
                                    elif "Copper Sword" in inventory["Gear"] and option == "coppersword":
                                        Gear["Type"]["Weapon"] = {"Copper Sword":{"Attack":3,"Magic Damage":0,"Critical Chance":10,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Sword":{"Attack":4,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Sword":{"Attack":6,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Sword":{"Attack":10,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Sword":{"Attack":15,"Magic Damage":0,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Sword":{"Attack":20,"Magic Damage":0,"Critical Chance":40,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Sword"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Sword"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Sword"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Sword"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Copper Sword"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Copper Sword"]["Max Health"] 
                                        Chestplate_Name = "Copper Sword"
                                    elif "Copper Axe" in inventory["Gear"] and option == "copperaxe":
                                        Gear["Type"]["Weapon"] = {"Copper Axe":{"Attack":2,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Axe":{"Attack":3,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Axe":{"Attack":5,"Magic Damage":0,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Axe":{"Attack":7,"Magic Damage":0,"Critical Chance":40,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Axe":{"Attack":10,"Magic Damage":0,"Critical Chance":55,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Axe":{"Attack":15,"Magic Damage":0,"Critical Chance":70,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Axe"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Axe"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Axe"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Axe"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Copper Axe"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Copper Axe"]["Max Health"] 
                                        Chestplate_Name = "Copper Axe"
                                    elif "Copper Mace" in inventory["Gear"] and option == "coppermace":
                                        Gear["Type"]["Weapon"] = {"Copper Mace":{"Attack":3,"Magic Damage":0,"Critical Chance":5,"Speed":0,"Defense":1,"Max Health":0}}
                                        if Proficiency["Mace"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Mace":{"Attack":4,"Magic Damage":0,"Critical Chance":10,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Mace":{"Attack":6,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Mace":{"Attack":9,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Mace":{"Attack":12,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Mace":{"Attack":15,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Mace"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Mace"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Mace"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Mace"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Copper Mace"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Copper Mace"]["Max Health"] 
                                        Chestplate_Name = "Copper Mace"
                                    elif "Copper Spear" in inventory["Gear"] and option == "copperspear":
                                        Gear["Type"]["Weapon"] = {"Copper Spear":{"Attack":3,"Magic Damage":0,"Critical Chance":10,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Spear"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Spear":{"Attack":4,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Spear"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Spear":{"Attack":6,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Spear"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Spear":{"Attack":10,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Spear"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Spear":{"Attack":15,"Magic Damage":0,"Critical Chance":45,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Spear"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Spear":{"Attack":20,"Magic Damage":0,"Critical Chance":60,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Spear"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Spear"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Spear"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Spear"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Copper Spear"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Copper Spear"]["Max Health"] 
                                        Chestplate_Name = "Copper Spear"
                                    elif "Copper Greatsword" in inventory["Gear"] and option == "coppergreatsword":
                                        Gear["Type"]["Weapon"] = {"Copper Greatsword":{"Attack":5,"Magic Damage":0,"Critical Chance":0,"Speed":-1,"Defense":1,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Greatsword":{"Attack":8,"Magic Damage":0,"Critical Chance":5,"Speed":-1,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Greatsword":{"Attack":12,"Magic Damage":0,"Critical Chance":10,"Speed":-1,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Greatsword":{"Attack":16,"Magic Damage":0,"Critical Chance":15,"Speed":-1,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Greatsword":{"Attack":25,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Greatsword":{"Attack":35,"Magic Damage":0,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Greatsword"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Greatsword"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Greatsword"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Greatsword"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Copper Greatsword"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Copper Greatsword"]["Max Health"] 
                                        Chestplate_Name = "Copper Greatsword"
                                    elif "Copper Bow" in inventory["Gear"] and option == "copperbow":
                                        Gear["Type"]["Weapon"] = {"Copper Bow":{"Attack":2,"Magic Damage":0,"Critical Chance":5,"Speed":2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Copper Bow":{"Attack":3,"Magic Damage":0,"Critical Chance":15,"Speed":3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Copper Bow":{"Attack":5,"Magic Damage":0,"Critical Chance":20,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Copper Bow":{"Attack":9,"Magic Damage":0,"Critical Chance":25,"Speed":8,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Copper Bow":{"Attack":14,"Magic Damage":0,"Critical Chance":30,"Speed":12,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Copper Bow":{"Attack":18,"Magic Damage":0,"Critical Chance":40,"Speed":16,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Copper Bow"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Copper Bow"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Copper Bow"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Copper Bow"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Copper Bow"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Copper Bow"]["Max Health"] 
                                        Chestplate_Name = "Copper Bow"
                                    elif "Copper Shield" in inventory["Gear"] and option == "coppershield":
                                        Gear["Type"]["Offhand"] = {"Copper Shield":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":5,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Offhand"]["Copper Shield"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Offhand"]["Copper Shield"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Offhand"]["Copper Shield"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Offhand"]["Copper Shield"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Offhand"]["Copper Shield"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Offhand"]["Copper Shield"]["Max Health"] 
                                        Chestplate_Name = "Copper Shield"
                                    elif "Twig Wand" in inventory["Gear"] and option == "twigwand":
                                        Gear["Type"]["Weapon"] = {"Twig Wand":{"Attack":0,"Magic Damage":3,"Critical Chance":5,"Speed":1,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Twig Wand":{"Attack":0,"Magic Damage":5,"Critical Chance":10,"Speed":2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Twig Wand":{"Attack":0,"Magic Damage":8,"Critical Chance":15,"Speed":3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Twig Wand":{"Attack":0,"Magic Damage":12,"Critical Chance":22,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Twig Wand":{"Attack":0,"Magic Damage":16,"Critical Chance":30,"Speed":7,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Twig Wand":{"Attack":0,"Magic Damage":22,"Critical Chance":40,"Speed":11,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Twig Wand"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Twig Wand"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Twig Wand"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Twig Wand"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Twig Wand"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Twig Wand"]["Max Health"] 
                                        Chestplate_Name = "Twig Wand"
                                    elif "Copper Shoulder Guards" in inventory["Gear"] and option == "coppershoulderguards":
                                        Gear["Type"]["Shoulderwear"] = {"Copper Shoulder Guards":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":2,"Max Health":30}}
                                        Base_Stats["Attack"] += Gear["Type"]["Shoulderwear"]["Copper Shoulder Guards"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Shoulderwear"]["Copper Shoulder Guards"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Shoulderwear"]["Copper Shoulder Guards"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Shoulderwear"]["Copper Shoulder Guards"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Shoulderwear"]["Copper Shoulder Guards"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Shoulderwear"]["Copper Shoulder Guards"]["Max Health"] 
                                        Chestplate_Name = "Copper Shoulder Guards"
                                    elif "Copper Gardbrace" in inventory["Gear"] and option == "coppergardbrace":
                                        Gear["Type"]["Armwear"] = {"Copper Gardbrace":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":3,"Max Health":20}}
                                        Base_Stats["Attack"] += Gear["Type"]["Armwear"]["Copper Gardbrace"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Armwear"]["Copper Gardbrace"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Armwear"]["Copper Gardbrace"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Armwear"]["Copper Gardbrace"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Armwear"]["Copper Gardbrace"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Armwear"]["Copper Gardbrace"]["Max Health"] 
                                        Chestplate_Name = "Copper Gardbrace"
                                    elif "Copper Greaves" in inventory["Gear"] and option == "coppergreaves":
                                        Gear["Type"]["Legwear"] = {"Copper Greaves":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":2,"Max Health":30}}
                                        Base_Stats["Attack"] += Gear["Type"]["Legwear"]["Copper Greaves"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Legwear"]["Copper Greaves"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Legwear"]["Copper Greaves"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Legwear"]["Copper Greaves"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Legwear"]["Copper Greaves"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Legwear"]["Copper Greaves"]["Max Health"] 
                                        Chestplate_Name = "Copper Greaves"
                                    elif "Copper Boots" in inventory["Gear"] and option == "copperboots":
                                        Gear["Type"]["Footwear"] = {"Copper Boots":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":2,"Defense":2,"Max Health":10}}
                                        Base_Stats["Attack"] += Gear["Type"]["Footwear"]["Copper Boots"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Footwear"]["Copper Boots"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Footwear"]["Copper Boots"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Footwear"]["Copper Boots"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Footwear"]["Copper Boots"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Footwear"]["Copper Boots"]["Max Health"] 
                                        Chestplate_Name = "Copper Boots"
                                    elif "Bronze Dagger" in inventory["Gear"] and option == "bronzedagger":
                                        Gear["Type"]["Weapon"] = {"Bronze Dagger":{"Attack":5,"Magic Damage":0,"Critical Chance":0,"Speed":3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Dagger":{"Attack":8,"Magic Damage":0,"Critical Chance":5,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Dagger":{"Attack":11,"Magic Damage":0,"Critical Chance":10,"Speed":8,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Dagger":{"Attack":14,"Magic Damage":0,"Critical Chance":20,"Speed":10,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Dagger":{"Attack":18,"Magic Damage":0,"Critical Chance":30,"Speed":15,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Dagger":{"Attack":24,"Magic Damage":0,"Critical Chance":45,"Speed":22,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Dagger"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Dagger"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Dagger"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Dagger"]["Critical Chance"]
                                        Weapon_Name = "Bronze Dagger"
                                    elif "Carved Staff" in inventory["Gear"] and option == "carvedstaff":
                                        Gear["Type"]["Weapon"] = {"Carved Staff":{"Attack":0,"Magic Damage":5,"Critical Chance":5,"Speed":1,"Defense":0,"Max Health":10}}
                                        if Proficiency["Staff"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Carved Staff":{"Attack":0,"Magic Damage":8,"Critical Chance":10,"Speed":2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Carved Staff":{"Attack":0,"Magic Damage":14,"Critical Chance":15,"Speed":4,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Carved Staff":{"Attack":0,"Magic Damage":20,"Critical Chance":25,"Speed":7,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Carved Staff":{"Attack":0,"Magic Damage":30,"Critical Chance":30,"Speed":10,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Carved Staff":{"Attack":0,"Magic Damage":45,"Critical Chance":40,"Speed":15,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Carved Staff"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Carved Staff"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Carved Staff"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Carved Staff"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Carved Staff"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Carved Staff"]["Max Health"] 
                                        Weapon_Name = "Carved Staff"
                                    elif "Bronze Helmet" in inventory["Gear"] and option == "bronzehelmet":
                                        Gear["Type"]["Helmet"] = {"Bronze Helmet":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":5,"Max Health":30}}
                                        Base_Stats["Attack"] += Gear["Type"]["Helmet"]["Bronze Helmet"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Helmet"]["Bronze Helmet"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Helmet"]["Bronze Helmet"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Helmet"]["Bronze Helmet"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Helmet"]["Bronze Helmet"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Helmet"]["Bronze Helmet"]["Max Health"] 
                                        Helmet_Name = "Bronze Helmet"
                                    elif "Bronze Chestplate" in inventory["Gear"] and option == "bronzechestplate":
                                        Gear["Type"]["Chestplate"] = {"Bronze Chestplate":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":6,"Max Health":20}}
                                        Base_Stats["Attack"] += Gear["Type"]["Chestplate"]["Bronze Chestplate"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Chestplate"]["Bronze Chestplate"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Chestplate"]["Bronze Chestplate"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Chestplate"]["Bronze Chestplate"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Chestplate"]["Bronze Chestplate"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Chestplate"]["Bronze Chestplate"]["Max Health"] 
                                        Chestplate_Name = "Bronze Chestplate"
                                    elif "Bronze Sword" in inventory["Gear"] and option == "bronzesword":
                                        Gear["Type"]["Weapon"] = {"Bronze Sword":{"Attack":5,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Sword":{"Attack":9,"Magic Damage":0,"Critical Chance":22,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Sword":{"Attack":14,"Magic Damage":0,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Sword":{"Attack":20,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Sword":{"Attack":27,"Magic Damage":0,"Critical Chance":44,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Sword":{"Attack":33,"Magic Damage":0,"Critical Chance":56,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Sword"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Sword"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Sword"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Sword"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Bronze Sword"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Bronze Sword"]["Max Health"] 
                                        Chestplate_Name = "Bronze Sword"
                                    elif "Bronze Axe" in inventory["Gear"] and option == "bronzeaxe":
                                        Gear["Type"]["Weapon"] = {"Bronze Axe":{"Attack":4,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Axe":{"Attack":7,"Magic Damage":0,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Axe":{"Attack":11,"Magic Damage":0,"Critical Chance":43,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Axe":{"Attack":15,"Magic Damage":0,"Critical Chance":55,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Axe":{"Attack":20,"Magic Damage":0,"Critical Chance":65,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Axe":{"Attack":27,"Magic Damage":0,"Critical Chance":75,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Axe"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Axe"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Axe"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Axe"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Bronze Axe"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Bronze Axe"]["Max Health"] 
                                        Chestplate_Name = "Bronze Axe"
                                    elif "Bronze Mace" in inventory["Gear"] and option == "bronzemace":
                                        Gear["Type"]["Weapon"] = {"Bronze Mace":{"Attack":4,"Magic Damage":0,"Critical Chance":10,"Speed":0,"Defense":2,"Max Health":0}}
                                        if Proficiency["Mace"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Mace":{"Attack":7,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":3,"Max Health":0}}
                                        if Proficiency["Mace"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Mace":{"Attack":11,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":5,"Max Health":0}}
                                        if Proficiency["Mace"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Mace":{"Attack":15,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":8,"Max Health":0}}
                                        if Proficiency["Mace"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Mace":{"Attack":20,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":12,"Max Health":0}}
                                        if Proficiency["Mace"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Mace":{"Attack":27,"Magic Damage":0,"Critical Chance":45,"Speed":0,"Defense":16,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Mace"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Mace"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Mace"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Mace"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Bronze Mace"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Bronze Mace"]["Max Health"] 
                                        Chestplate_Name = "Bronze Mace"
                                    elif "Bronze Spear" in inventory["Gear"] and option == "bronzespear":
                                        Gear["Type"]["Weapon"] = {"Bronze Spear":{"Attack":4,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Spear":{"Attack":7,"Magic Damage":0,"Critical Chance":30,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Spear":{"Attack":11,"Magic Damage":0,"Critical Chance":43,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Spear":{"Attack":15,"Magic Damage":0,"Critical Chance":55,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Spear":{"Attack":20,"Magic Damage":0,"Critical Chance":65,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Spear":{"Attack":27,"Magic Damage":0,"Critical Chance":75,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Spear"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Spear"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Spear"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Spear"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Bronze Spear"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Bronze Spear"]["Max Health"] 
                                        Chestplate_Name = "Bronze Spear"
                                    elif "Bronze Greatsword" in inventory["Gear"] and option == "bronzegreatsword":
                                        Gear["Type"]["Weapon"] = {"Bronze Greatsword":{"Attack":7,"Magic Damage":0,"Critical Chance":0,"Speed":-3,"Defense":2,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Greatsword":{"Attack":12,"Magic Damage":0,"Critical Chance":5,"Speed":-2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Greatsword":{"Attack":18,"Magic Damage":0,"Critical Chance":8,"Speed":-2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Greatsword":{"Attack":25,"Magic Damage":0,"Critical Chance":12,"Speed":-1,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Greatsword":{"Attack":38,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Greatsword":{"Attack":50,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Greatsword"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Greatsword"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Greatsword"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Greatsword"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Bronze Greatsword"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Bronze Greatsword"]["Max Health"] 
                                        Chestplate_Name = "Bronze Greatsword"
                                    elif "Bronze Bow" in inventory["Gear"] and option == "bronzebow":
                                        Gear["Type"]["Weapon"] = {"Bronze Bow":{"Attack":3,"Magic Damage":0,"Critical Chance":10,"Speed":3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Bronze Bow":{"Attack":5,"Magic Damage":0,"Critical Chance":20,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Bronze Bow":{"Attack":8,"Magic Damage":0,"Critical Chance":25,"Speed":8,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Bronze Bow":{"Attack":12,"Magic Damage":0,"Critical Chance":35,"Speed":12,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Bronze Bow":{"Attack":18,"Magic Damage":0,"Critical Chance":45,"Speed":16,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Bronze Bow":{"Attack":25,"Magic Damage":0,"Critical Chance":60,"Speed":22,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Bronze Bow"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Bronze Bow"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Bronze Bow"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Bronze Bow"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Bronze Bow"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Bronze Bow"]["Max Health"] 
                                        Chestplate_Name = "Bronze Bow"
                                    elif "Bronze Shield" in inventory["Gear"] and option == "bronzeshield":
                                        Gear["Type"]["Offhand"] = {"Bronze Shield":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":8,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Offhand"]["Bronze Shield"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Offhand"]["Bronze Shield"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Offhand"]["Bronze Shield"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Offhand"]["Bronze Shield"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Offhand"]["Bronze Shield"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Offhand"]["Bronze Shield"]["Max Health"] 
                                        Chestplate_Name = "Bronze Shield"
                                    elif "Carved Wand" in inventory["Gear"] and option == "carvedwand":
                                        Gear["Type"]["Weapon"] = {"Carved Wand":{"Attack":0,"Magic Damage":4,"Critical Chance":5,"Speed":3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Carved Wand":{"Attack":0,"Magic Damage":7,"Critical Chance":15,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Carved Wand":{"Attack":0,"Magic Damage":11,"Critical Chance":22,"Speed":8,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Carved Wand":{"Attack":0,"Magic Damage":16,"Critical Chance":30,"Speed":12,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Carved Wand":{"Attack":0,"Magic Damage":22,"Critical Chance":40,"Speed":17,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Carved Wand":{"Attack":0,"Magic Damage":30,"Critical Chance":55,"Speed":23,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Carved Wand"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Carved Wand"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Carved Wand"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Carved Wand"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Carved Wand"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Carved Wand"]["Max Health"] 
                                        Chestplate_Name = "Twig Wand"
                                    elif "Bronze Shoulder Guards" in inventory["Gear"] and option == "bronzeshoulderguards":
                                        Gear["Type"]["Shoulderwear"] = {"Bronze Shoulder Guards":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":3,"Max Health":50}}
                                        Base_Stats["Attack"] += Gear["Type"]["Shoulderwear"]["Bronze Shoulder Guards"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Shoulderwear"]["Bronze Shoulder Guards"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Shoulderwear"]["Bronze Shoulder Guards"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Shoulderwear"]["Bronze Shoulder Guards"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Shoulderwear"]["Bronze Shoulder Guards"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Shoulderwear"]["Bronze Shoulder Guards"]["Max Health"] 
                                        Chestplate_Name = "Bronze Shoulder Guards"
                                    elif "Bronze Gardbrace" in inventory["Gear"] and option == "bronzegardbrace":
                                        Gear["Type"]["Armwear"] = {"Bronze Gardbrace":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":5,"Max Health":30}}
                                        Base_Stats["Attack"] += Gear["Type"]["Armwear"]["Bronze Gardbrace"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Armwear"]["Bronze Gardbrace"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Armwear"]["Bronze Gardbrace"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Armwear"]["Bronze Gardbrace"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Armwear"]["Bronze Gardbrace"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Armwear"]["Bronze Gardbrace"]["Max Health"] 
                                        Chestplate_Name = "Bronze Gardbrace"
                                    elif "Bronze Greaves" in inventory["Gear"] and option == "bronzegreaves":
                                        Gear["Type"]["Legwear"] = {"Bronze Greaves":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":1,"Defense":3,"Max Health":40}}
                                        Base_Stats["Attack"] += Gear["Type"]["Legwear"]["Bronze Greaves"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Legwear"]["Bronze Greaves"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Legwear"]["Bronze Greaves"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Legwear"]["Bronze Greaves"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Legwear"]["Bronze Greaves"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Legwear"]["Bronze Greaves"]["Max Health"] 
                                        Chestplate_Name = "Bronze Greaves"
                                    elif "Bronze Boots" in inventory["Gear"] and option == "bronzeboots":
                                        Gear["Type"]["Footwear"] = {"Bronze Boots":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":3,"Defense":3,"Max Health":20}}
                                        Base_Stats["Attack"] += Gear["Type"]["Footwear"]["Bronze Boots"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Footwear"]["Bronze Boots"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Footwear"]["Bronze Boots"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Footwear"]["Bronze Boots"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Footwear"]["Bronze Boots"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Footwear"]["Bronze Boots"]["Max Health"] 
                                        Chestplate_Name = "Bronze Boots"
                                    elif "Iron Dagger" in inventory["Gear"] and option == "irondagger":
                                        Gear["Type"]["Weapon"] = {"Iron Dagger":{"Attack":10,"Magic Damage":0,"Critical Chance":0,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Dagger":{"Attack":14,"Magic Damage":0,"Critical Chance":5,"Speed":5,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Dagger":{"Attack":19,"Magic Damage":0,"Critical Chance":10,"Speed":8,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Dagger":{"Attack":24,"Magic Damage":0,"Critical Chance":20,"Speed":10,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Dagger":{"Attack":30,"Magic Damage":0,"Critical Chance":30,"Speed":15,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Dagger":{"Attack":40,"Magic Damage":0,"Critical Chance":45,"Speed":22,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Dagger"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Dagger"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Dagger"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Dagger"]["Critical Chance"]
                                        Weapon_Name = "Iron Dagger"
                                    elif "Runed Staff" in inventory["Gear"] and option == "runedstaff":
                                        Gear["Type"]["Weapon"] = {"Runed Staff":{"Attack":0,"Magic Damage":7,"Critical Chance":5,"Speed":2,"Defense":0,"Max Health":20}}
                                        if Proficiency["Staff"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Runed Staff":{"Attack":0,"Magic Damage":10,"Critical Chance":10,"Speed":4,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Runed Staff":{"Attack":0,"Magic Damage":14,"Critical Chance":15,"Speed":7,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Runed Staff":{"Attack":0,"Magic Damage":24,"Critical Chance":25,"Speed":10,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Runed Staff":{"Attack":0,"Magic Damage":30,"Critical Chance":30,"Speed":15,"Defense":0,"Max Health":0}}
                                        if Proficiency["Staff"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Runed Staff":{"Attack":0,"Magic Damage":45,"Critical Chance":40,"Speed":25,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Runed Staff"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Runed Staff"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Runed Staff"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Runed Staff"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Runed Staff"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Runed Staff"]["Max Health"] 
                                        Weapon_Name = "Carved Staff"
                                    elif "Iron Helmet" in inventory["Gear"] and option == "ironhelmet":
                                        Gear["Type"]["Helmet"] = {"Iron Helmet":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":7,"Max Health":50}}
                                        Base_Stats["Attack"] += Gear["Type"]["Helmet"]["Iron Helmet"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Helmet"]["Iron Helmet"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Helmet"]["Iron Helmet"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Helmet"]["Iron Helmet"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Helmet"]["Iron Helmet"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Helmet"]["Iron Helmet"]["Max Health"] 
                                        Helmet_Name = "Iron Helmet"
                                    elif "Iron Chestplate" in inventory["Gear"] and option == "ironchestplate":
                                        Gear["Type"]["Chestplate"] = {"Iron Chestplate":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":9,"Max Health":30}}
                                        Base_Stats["Attack"] += Gear["Type"]["Chestplate"]["Iron Chestplate"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Chestplate"]["Iron Chestplate"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Chestplate"]["Iron Chestplate"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Chestplate"]["Iron Chestplate"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Chestplate"]["Iron Chestplate"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Chestplate"]["Iron Chestplate"]["Max Health"] 
                                        Chestplate_Name = "Iron Chestplate"
                                    elif "Iron Sword" in inventory["Gear"] and option == "ironsword":
                                        Gear["Type"]["Weapon"] = {"Iron Sword":{"Attack":8,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Sword":{"Attack":13,"Magic Damage":0,"Critical Chance":36,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Sword":{"Attack":18,"Magic Damage":0,"Critical Chance":47,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Sword":{"Attack":26,"Magic Damage":0,"Critical Chance":59,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Sword":{"Attack":35,"Magic Damage":0,"Critical Chance":70,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Sword"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Sword":{"Attack":45,"Magic Damage":0,"Critical Chance":80,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Sword"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Sword"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Sword"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Sword"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Iron Sword"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Iron Sword"]["Max Health"] 
                                        Chestplate_Name = "Iron Sword"
                                    elif "Iron Axe" in inventory["Gear"] and option == "ironaxe":
                                        Gear["Type"]["Weapon"] = {"Iron Axe":{"Attack":6,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Axe":{"Attack":10,"Magic Damage":0,"Critical Chance":45,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Axe":{"Attack":15,"Magic Damage":0,"Critical Chance":51,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Axe":{"Attack":20,"Magic Damage":0,"Critical Chance":58,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Axe":{"Attack":30,"Magic Damage":0,"Critical Chance":67,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Axe"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Axe":{"Attack":45,"Magic Damage":0,"Critical Chance":80,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Axe"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Axe"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Axe"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Axe"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Iron Axe"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Iron Axe"]["Max Health"] 
                                        Chestplate_Name = "Iron Axe"
                                    elif "Iron Mace" in inventory["Gear"] and option == "ironmace":
                                        Gear["Type"]["Weapon"] = {"Iron Mace":{"Attack":6,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":3,"Max Health":0}}
                                        if Proficiency["Mace"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Mace":{"Attack":10,"Magic Damage":0,"Critical Chance":20,"Speed":0,"Defense":5,"Max Health":0}}
                                        if Proficiency["Mace"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Mace":{"Attack":15,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":8,"Max Health":0}}
                                        if Proficiency["Mace"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Mace":{"Attack":20,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":12,"Max Health":0}}
                                        if Proficiency["Mace"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Mace":{"Attack":27,"Magic Damage":0,"Critical Chance":45,"Speed":0,"Defense":16,"Max Health":0}}
                                        if Proficiency["Mace"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Mace":{"Attack":39,"Magic Damage":0,"Critical Chance":60,"Speed":0,"Defense":22,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Mace"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Mace"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Mace"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Mace"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Iron Mace"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Iron Mace"]["Max Health"] 
                                        Chestplate_Name = "Iron Mace"
                                    elif "Iron Spear" in inventory["Gear"] and option == "ironspear":
                                        Gear["Type"]["Weapon"] = {"Iron Spear":{"Attack":7,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Spear":{"Attack":11,"Magic Damage":0,"Critical Chance":35,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Spear":{"Attack":15,"Magic Damage":0,"Critical Chance":45,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Spear":{"Attack":20,"Magic Damage":0,"Critical Chance":60,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Spear":{"Attack":30,"Magic Damage":0,"Critical Chance":70,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Mace"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Spear":{"Attack":45,"Magic Damage":0,"Critical Chance":85,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Spear"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Spear"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Spear"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Spear"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Iron Spear"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Iron Spear"]["Max Health"] 
                                        Chestplate_Name = "Iron Spear"
                                    elif "Iron Greatsword" in inventory["Gear"] and option == "irongreatsword":
                                        Gear["Type"]["Weapon"] = {"Iron Greatsword":{"Attack":9,"Magic Damage":0,"Critical Chance":0,"Speed":-5,"Defense":4,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Greatsword":{"Attack":15,"Magic Damage":0,"Critical Chance":5,"Speed":-3,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Greatsword":{"Attack":22,"Magic Damage":0,"Critical Chance":8,"Speed":-2,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Greatsword":{"Attack":30,"Magic Damage":0,"Critical Chance":12,"Speed":-1,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Greatsword":{"Attack":40,"Magic Damage":0,"Critical Chance":15,"Speed":0,"Defense":0,"Max Health":0}}
                                        if Proficiency["Greatsword"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Greatsword":{"Attack":60,"Magic Damage":0,"Critical Chance":25,"Speed":0,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Greatsword"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Greatsword"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Greatsword"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Greatsword"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Iron Greatsword"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Iron Greatsword"]["Max Health"] 
                                        Chestplate_Name = "Iron Greatsword"
                                    elif "Iron Bow" in inventory["Gear"] and option == "ironbow":
                                        Gear["Type"]["Weapon"] = {"Iron Bow":{"Attack":5,"Magic Damage":0,"Critical Chance":15,"Speed":4,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Iron Bow":{"Attack":8,"Magic Damage":0,"Critical Chance":20,"Speed":7,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Iron Bow":{"Attack":12,"Magic Damage":0,"Critical Chance":25,"Speed":12,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Iron Bow":{"Attack":18,"Magic Damage":0,"Critical Chance":35,"Speed":16,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Iron Bow":{"Attack":25,"Magic Damage":0,"Critical Chance":45,"Speed":22,"Defense":0,"Max Health":0}}
                                        if Proficiency["Bow"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Iron Bow":{"Attack":40,"Magic Damage":0,"Critical Chance":60,"Speed":30,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Iron Bow"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Iron Bow"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Iron Bow"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Iron Bow"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Iron Bow"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Iron Bow"]["Max Health"] 
                                        Chestplate_Name = "Iron Bow"
                                    elif "Iron Shield" in inventory["Gear"] and option == "ironshield":
                                        Gear["Type"]["Offhand"] = {"Iron Shield":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":12,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Offhand"]["Iron Shield"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Offhand"]["Iron Shield"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Offhand"]["Iron Shield"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Offhand"]["Iron Shield"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Offhand"]["Iron Shield"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Offhand"]["Iron Shield"]["Max Health"] 
                                        Chestplate_Name = "Iron Shield"
                                    elif "Crystal Wand" in inventory["Gear"] and option == "crystalwand":
                                        Gear["Type"]["Weapon"] = {"Crystal Wand":{"Attack":0,"Magic Damage":6,"Critical Chance":10,"Speed":4,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Rookie":
                                            Gear["Type"]["Weapon"] = {"Crystal Wand":{"Attack":0,"Magic Damage":10,"Critical Chance":15,"Speed":7,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Competent":
                                            Gear["Type"]["Weapon"] = {"Crystal Wand":{"Attack":0,"Magic Damage":16,"Critical Chance":22,"Speed":12,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Proficient":
                                            Gear["Type"]["Weapon"] = {"Crystal Wand":{"Attack":0,"Magic Damage":22,"Critical Chance":30,"Speed":17,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Expert":
                                            Gear["Type"]["Weapon"] = {"Crystal Wand":{"Attack":0,"Magic Damage":32,"Critical Chance":40,"Speed":23,"Defense":0,"Max Health":0}}
                                        if Proficiency["Wand"] == "Master":
                                            Gear["Type"]["Weapon"] = {"Crystal Wand":{"Attack":0,"Magic Damage":43,"Critical Chance":55,"Speed":30,"Defense":0,"Max Health":0}}
                                        Base_Stats["Attack"] += Gear["Type"]["Weapon"]["Crystal Wand"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Weapon"]["Crystal Wand"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Weapon"]["Crystal Wand"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Weapon"]["Crystal Wand"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Weapon"]["Crystal Wand"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Weapon"]["Crystal Wand"]["Max Health"] 
                                        Chestplate_Name = "Twig Wand"
                                    elif "Iron Shoulder Guards" in inventory["Gear"] and option == "ironshoulderguards":
                                        Gear["Type"]["Shoulderwear"] = {"Iron Shoulder Guards":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":5,"Max Health":70}}
                                        Base_Stats["Attack"] += Gear["Type"]["Shoulderwear"]["Iron Shoulder Guards"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Shoulderwear"]["Iron Shoulder Guards"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Shoulderwear"]["Iron Shoulder Guards"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Shoulderwear"]["Iron Shoulder Guards"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Shoulderwear"]["Iron Shoulder Guards"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Shoulderwear"]["Iron Shoulder Guards"]["Max Health"] 
                                        Chestplate_Name = "Iron Shoulder Guards"
                                    elif "Iron Gardbrace" in inventory["Gear"] and option == "irongardbrace":
                                        Gear["Type"]["Armwear"] = {"Iron Gardbrace":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":7,"Max Health":50}}
                                        Base_Stats["Attack"] += Gear["Type"]["Armwear"]["Iron Gardbrace"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Armwear"]["Iron Gardbrace"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Armwear"]["Iron Gardbrace"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Armwear"]["Iron Gardbrace"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Armwear"]["Iron Gardbrace"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Armwear"]["Iron Gardbrace"]["Max Health"] 
                                        Chestplate_Name = "Iron Gardbrace"
                                    elif "Iron Greaves" in inventory["Gear"] and option == "irongreaves":
                                        Gear["Type"]["Legwear"] = {"Iron Greaves":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":3,"Defense":4,"Max Health":50}}
                                        Base_Stats["Attack"] += Gear["Type"]["Legwear"]["Iron Greaves"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Legwear"]["Iron Greaves"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Legwear"]["Iron Greaves"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Legwear"]["Iron Greaves"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Legwear"]["Iron Greaves"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Legwear"]["Iron Greaves"]["Max Health"] 
                                        Chestplate_Name = "Iron Greaves"
                                    elif "Iron Boots" in inventory["Gear"] and option == "ironboots":
                                        Gear["Type"]["Footwear"] = {"Iron Boots":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":4,"Defense":5,"Max Health":30}}
                                        Base_Stats["Attack"] += Gear["Type"]["Footwear"]["Iron Boots"]["Attack"] 
                                        Base_Stats["Speed"] += Gear["Type"]["Footwear"]["Iron Boots"]["Speed"] 
                                        Base_Stats["Magic Damage"] += Gear["Type"]["Footwear"]["Iron Boots"]["Magic Damage"] 
                                        Base_Stats["Critical Chance"] += Gear["Type"]["Footwear"]["Iron Boots"]["Critical Chance"]
                                        Base_Stats["Defense"] += Gear["Type"]["Footwear"]["Iron Boots"]["Defense"]
                                        Base_Stats["Max Health"] += Gear["Type"]["Footwear"]["Iron Boots"]["Max Health"] 
                                        Chestplate_Name = "Iron Boots"
                                    else:
                                        print("\nYou do not have this gear piece\n")

                                    if Gear["Type"]["Weapon"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                        print(Gear["Type"]["Weapon"],"Equipped.\n")
                            elif choice == "2":
                                print("What type of gear do you want to unequip?\n\n Helmet\n\n Shoulderwear\n\n Armwear\n\n Chestplate\n\n Legwear\n\n Footwear\n\n Weapon")
                                option = input("").lower()
                                option = "".join(option.split())
                                print("\n\n")
                                if option == "weapon" and Gear["Type"]["Weapon"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    Base_Stats["Attack"] -= Gear["Type"]["Weapon"][Weapon_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Weapon"][Weapon_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Weapon"][Weapon_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Weapon"][Weapon_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Weapon"][Weapon_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Weapon"][Weapon_Name]["Max Health"] 
                                    Gear["Type"]["Weapon"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Weapon_Name} unequipped")
                                elif option == "helmet"  and Gear["Type"]["Helmet"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:     
                                    Base_Stats["Attack"] -= Gear["Type"]["Helmet"][Helmet_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Helmet"][Helmet_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Helmet"][Helmet_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Helmet"][Helmet_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Helmet"][Helmet_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Helmet"][Helmet_Name]["Max Health"] 
                                    Gear["Type"]["Helmet"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Helmet_Name} unequipped")
                                elif option == "chestplate"  and Gear["Type"]["Chestplate"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    Base_Stats["Attack"] -= Gear["Type"]["Chestplate"][Chestplate_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Chestplate"][Chestplate_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Chestplate"][Chestplate_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Chestplate"][Chestplate_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Chestplate"][Chestplate_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Chestplate"][Chestplate_Name]["Max Health"] 
                                    Gear["Type"]["Chestplate"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Chestplate_Name} unequipped")
                                elif option == "shoulderwear" and Gear["Type"]["Shoulderwear"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    Base_Stats["Attack"] -= Gear["Type"]["Shoulderwear"][Shoulderwear_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Shoulderwear"][Shoulderwear_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Shoulderwear"][Shoulderwear_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Shoulderwear"][Shoulderwear_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Shoulderwear"][Shoulderwear_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Shoulderwear"][Shoulderwear_Name]["Max Health"] 
                                    Gear["Type"]["Shoulderwear"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Shoulderwear_Name} unequipped")
                                elif option == "armwear"  and Gear["Type"]["Armwear"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    Base_Stats["Attack"] -= Gear["Type"]["Armwear"][Armwear_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Armwear"][Armwear_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Armwear"][Armwear_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Armwear"][Armwear_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Armwear"][Armwear_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Armwear"][Armwear_Name]["Max Health"] 
                                    Gear["Type"]["Armwear"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Armwear_Name} unequipped")
                                elif option == "legwear"  and Gear["Type"]["Legwear"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    Base_Stats["Attack"] -= Gear["Type"]["Legwear"][Legwear_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Legwear"][Legwear_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Legwear"][Legwear_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Legwear"][Legwear_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Legwear"][Legwear_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Legwear"][Legwear_Name]["Max Health"] 
                                    Gear["Type"]["Legwear"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Legwear_Name} unequipped")
                                elif option == "footwear"  and Gear["Type"]["Footwear"] != {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}:
                                    Gear["Type"]["Footwear"] = "None"
                                    Base_Stats["Attack"] -= Gear["Type"]["Footwear"][Footwear_Name]["Attack"] 
                                    Base_Stats["Speed"] -= Gear["Type"]["Footwear"][Footwear_Name]["Speed"] 
                                    Base_Stats["Magic Damage"] -= Gear["Type"]["Footwear"][Footwear_Name]["Magic Damage"] 
                                    Base_Stats["Critical Chance"] -= Gear["Type"]["Footwear"][Footwear_Name]["Critical Chance"]
                                    Base_Stats["Defense"] -= Gear["Type"]["Footwear"][Footwear_Name]["Defense"]
                                    Base_Stats["Max Health"] -= Gear["Type"]["Footwear"][Footwear_Name]["Max Health"] 
                                    Gear["Type"]["Footwear"] = {"None":{"Attack":0,"Magic Damage":0,"Critical Chance":0,"Speed":0,"Defense":0,"Max Health":0}}
                                    print(f"{Footwear_Name} unequipped")
                                else:
                                    print("\nThat is not equipped\n")
                            elif choice == "3":
                                display_gear()
                            elif choice == "4":
                                break
                            else:
                                print("Invalid choice.")

                    gear_menu()
                                
            print("Attributes\n---------------","\nLevel:",Player["Level"],"\nXP:(",Player["XP"],"/",Player["XP Needed"],")","\nHealth:",Player["Health"],"\nAttack:",Player["Attack"],"\nDefense:",Player["Defense"],"\nSpeed:",Player["Speed"],"\nMagic Density:",Player["Magic Density"],"\nStamina:",Player["Stamina"],"\nCritical Chance:",Player["Critical Chance"],"\nCritical Damage:",Player["Critical Damage"],"\nEvasion:",Player["Evasion"],"\nAccuracy:",Player["Accuracy"],"\nMana:",Player["Mana"],"\nTower Completion:",Player["Tower Level"])
            print("\n\nInventory\n---------------")
            for key,value in inventory.items():
                print(key,":",value,"\n")
            print("---------------")
            print("\n\nBody Condition\n---------------")
            for key,value in Body_Condition.items():
                print(key,":",value)
            print("\n\nTitle\n---------------")
            print(Player["Title"])
            back = input("---------------\n\nPress enter to return\n\n")

                
        elif Choice in ["skilltree","st","skill","tree","2"]:
            while skill_points > 0:



                print("\nType the name of the skill you want to unlock.\n")
                print("Skill Points:",skill_points,"\n\nPress enter to return\n\n\n---------------\nGeneral\n---------------")
                print(f"Advanced Mind: {Skill_Tree['General']['Advanced Mind']['Status']}     [ Memory Capacity becomes 8 ]")
                print(f"Bloodthirsty: {Skill_Tree['General']['Bloodthirsty']['Status']}      [ 25% of Max Health gained each kill ]")
                print(f"Momentum: {Skill_Tree['General']['Momentum']['Status']}          [ 10% Speed gained each kill ]")
                print(f"Arcane Echo: {Skill_Tree['General']['Arcane Echo']['Status']}       [ 10% chance to repeat a spell ]")
                print(f"Fast Recovery: {Skill_Tree['General']['Fast Recovery']['Status']}     [ 25% Stamina recovered each turn instead of 10% ]")
                print(f"Meditative Mind: {Skill_Tree['General']['Meditative Mind']['Status']}   [ Waiting restores Mana ]")
                print(f"Strong Body: {Skill_Tree['General']['Strong Body']['Status']}       [ Max Limit for body upgrades to 50 ]")
                print(f"\n---------------\nTraining\n---------------\nLightweight: {Skill_Tree['Training']['Lightweight']['Status']}")
                if Skill_Tree["Training"]["Lock"] == "(Unlocked)":
                    print(f"Run! : {Skill_Tree['Training']['Running']['Status']}")
                    print(f"Sword Swing: {Skill_Tree['Training']['Sword Swing']['Status']}")
                    print(f"Weight Carry: {Skill_Tree['Training']['Weight Carry']['Status']}")
                    print(f"Dead Hang: {Skill_Tree['Training']['Dead Hang']['Status']}")
                    print(f"Neck Bridge: {Skill_Tree['Training']['Neck Bridge']['Status']}")
                    print(f"Push Up: {Skill_Tree['Training']['Push Up']['Status']}")

                print("\n---------------\nSmithing\n---------------")
                print(f"Apprenticeship: {Skill_Tree['Smithing']['Apprenticeship']['Status']}")
                if Skill_Tree["Smithing"]["Lock"] == "(Unlocked)":
                    print(f"Hit em! :{Skill_Tree['Smithing']['Hit em']['Status']}")

                print("\n---------------\nAlchemy\n---------------")
                print(f"Scientific Cooking: {Skill_Tree['Alchemy']['Scientific Cooking']['Status']}")
                if Skill_Tree["Alchemy"]["Lock"] == "(Unlocked)":
                    print(f"Skill 2: {Skill_Tree['Alchemy']['Skill 2']['Status']}")
                Target = input("")
                Target = Target.lower()
                Target = "".join(Target.split())
                if (Target == "lightweight" and skill_points > 0) and Skill_Tree["Training"]["Lock"] != "(Unlocked)" :
                    Skill_Tree["Training"]["Lock"] = "(Unlocked)"
                    Skill_Tree["Training"]["Lightweight"]["Status"] = "(Unlocked)"
                    Unlocked_Functions["Training"]["Status"] = "(Unlocked)"
                    print("\nPurchase Complete!\n")
                    skill_points -= 1
                elif (Target == "apprenticeship" and skill_points > 0) and Skill_Tree["Smithing"]["Lock"] != "(Unlocked)" :
                    Skill_Tree["Smithing"]["Lock"] = "(Unlocked)"
                    Skill_Tree["Smithing"]["Apprenticeship"]["Status"] = "(Unlocked)"
                    Unlocked_Functions["Smithing"]["Status"] = "(Unlocked)"
                    print("\nPurchase Complete!\n")
                    skill_points -= 1
                elif (Target == "scientificcooking" and skill_points > 0) and Skill_Tree["Alchemy"]["Lock"] != "(Unlocked)" :
                    Skill_Tree["Alchemy"]["Lock"] = "(Unlocked)"
                    Skill_Tree["Alchemy"]["Scientific Cooking"]["Status"] = "(Unlocked)"
                    Unlocked_Functions["Alchemy"]["Status"] = "(Unlocked)"
                    print("\nPurchase Complete!\n")
                    skill_points -= 1
                
                elif Skill_Tree["Training"]["Lock"] == "(Unlocked)" and Skill_Tree["Training"]["Running"]["Status"] != "(Unlocked)":
                    if (Target == "run" and skill_points > 0):
                        Skill_Tree["Training"]["Running"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "swordswing" and skill_points > 0) and Skill_Tree["Training"]["Sword Swing"]["Status"] != "(Unlocked)":
                        Skill_Tree["Training"]["Sword Swing"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "weightcarry" and skill_points > 0) and Skill_Tree["Training"]["Weight Carry"]["Status"] != "(Unlocked)":
                        Skill_Tree["Training"]["Weight Carry"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "deadhang" and skill_points > 0) and Skill_Tree["Training"]["Dead Hang"]["Status"] != "(Unlocked)":
                        Skill_Tree["Training"]["Dead Hang"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "neckbridge" and skill_points > 0) and Skill_Tree["Training"]["Neck Bridge"]["Status"] != "(Unlocked)":
                        Skill_Tree["Training"]["Neck Bridge"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "pushup" and skill_points > 0):
                        Skill_Tree["Training"]["Push Up"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "advancedmind" and skill_points > 0) and Skill_Tree["General"]["Advanced Mind"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Advanced Mind"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                        Memory = 8
                    elif (Target == "bloodthirsty" and skill_points > 0) and Skill_Tree["General"]["Bloodthirsty"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Bloodthirsty"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "momentum" and skill_points > 0) and Skill_Tree["General"]["Momentum"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Momentum"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "arcaneecho" and skill_points > 0) and Skill_Tree["General"]["Arcane Echo"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Arcane Echo"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "fastrecovery" and skill_points > 0) and Skill_Tree["General"]["Fast Recovery"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Fast Recovery"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "meditativemind" and skill_points > 0) and Skill_Tree["General"]["Meditative Mind"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Meditative Mind"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                    elif (Target == "strongbody" and skill_points > 0) and Skill_Tree["General"]["Strong Body"]["Status"] != "(Unlocked)":
                        Skill_Tree["General"]["Strong Body"]["Status"] = "(Unlocked)"
                        print("\nPurchase Complete!\n")
                        skill_points -= 1
                        Max_Limit = 50
                    else:
                        print("Not enough Skill Points or already unlocked")
                    
                elif Target == "":
                    break
                else:
                    print("Not enough Skill Points or already unlocked")

        elif Choice in ["combatives","c","3"]:
            Choice = ""
            method = input("\nWhat do you want to do?\n1. Search for a specific move\n\n2. Show all\n\n")
            method = method.lower()
            method = "".join(method.split())
            
            if method in ["2","showall"]:
                print("\n\nSpells\n---------------")
                for key,value in Spell_list.items():
                    print(key,":",value)
                print("\n\nCombat Moves\n---------------")
                for key,value in Combat_Skill_list.items():
                    print(key,":",value)
                back = input("\n---------------\n\nPress enter to return\n\n")
            elif method in ["1","search"]:
                choice = input("\n Enter the name of the move\n")
                choice = choice.lower()
                choice = "".join(choice.split())
                if choice in ["fireball"] and Skills["Fireball"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Fireball"],"\n")
                elif choice in ["manablast"] and Skills["Mana Blast"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Mana Blast"],"\n")
                elif choice in ["straightpunch"] and Skills["Straight Punch"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Straight Punch"],"\n")
                elif choice in ["shock"] and Skills["Shock"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Shock"],"\n")
                elif choice in ["mudshot"] and Skills["Mud Shot"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Mud Shot"],"\n")
                elif choice in ["riverfist"] and Skills["River Fist"]["Level"] != "Not Learned":
                    print("\n",Spell_list["River Fist"],"\n")
                elif choice in ["purify"] and Skills["Purify"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Purify"],"\n")
                elif choice in ["tremor"] and Skills["Tremor"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Tremor"],"\n")
                elif choice in ["iceshard"] and Skills["Ice Shard"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Ice Shard"],"\n")
                elif choice in ["stoneslipstream"] and Skills["Stone Slipstream"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Stone Slipstream"],"\n")
                elif choice in ["lifedrain"] and Skills["Life Drain"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Life Drain"],"\n")
                elif choice in ["devouressence"] and Skills["Devour Essence"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Devour Essence"],"\n")
                elif choice in ["corruptingtouch"] and Skills["Corrupting Touch"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Corrupting Touch"],"\n")
                elif choice in ["toxinspray"] and Skills["Toxin Spray"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Toxin Spray"],"\n")
                elif choice in ["dominate"] and Skills["Dominate"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Dominate"],"\n")
                elif choice in ["grapplingvines"] and Skills["Grappling Vines"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Grappling Vines"],"\n")
                elif choice in ["empower"] and Skills["Empower"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Empower"],"\n")
                elif choice in ["heal"] and Skills["Heal"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Heal"],"\n")
                elif choice in ["analyse"] and Skills["Analyse"]["Level"] != "Not Learned":
                    print("\n",Spell_list["Analyse"],"\n")
                elif choice in ["headbutt"] and Skills["Headbutt"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Headbutt"],"\n")
                elif choice in ["bite"] and Skills["Bite"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Bite"],"\n")
                elif choice in ["frontkick"] and Skills["Front Kick"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Front Kick"],"\n")
                elif choice in ["axekick"] and Skills["Axe Kick"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Axe Kick"],"\n")
                elif choice in ["spinningbackkick"] and Skills["Spinning Back Kick"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Spinning Back Kick"],"\n")
                elif choice in ["groundbreaker"] and Skills["Groundbreaker"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Groundbreaker"],"\n")
                elif choice in ["aimedshot"] and Skills["Aimed Shot"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Aimed Shot"],"\n")
                elif choice in ["tackle"] and Skills["Tackle"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Tackle"],"\n")
                elif choice in ["slash"] and Skills["Slash"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Slash"],"\n")
                elif choice in ["quickstab"] and Skills["Quick Stab"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Quick Stab"],"\n")
                elif choice in ["impulsiveswing"] and Skills["Impulsive Swing"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Impulsive Swing"],"\n")
                elif choice in ["jab"] and Skills["Jab"]["Level"] != "Not Learned":
                    print("\n",Combat_Skill_list["Jab"],"\n")
        elif Choice in  ["movememory","m","mm","4"]:
            Choice = ""
            Move_Set = []
            print("You have 15 characters per slot")
            while len(Move_Set) != Memory:
                print("Input the move you want to store in your memory")
                mind = input("")
                if len(mind) <= 15: 
                    print(f"{mind} has been stored")
                    Move_Set.append(mind)
                else:
                    print("Don't try to put several moves inside one slot")


        elif Choice in ["5","use skill book","useskillbook","usb","u"]:
            print("\nChoose one of the following:\n")
            if Skill_Books["Fireball"] == True:
               print("\nLearn Fireball\n")
            if Skill_Books["Headbutt"] == True:
               print("\nLearn Headbutt\n")
            if Skill_Books["Axe Kick"] == True:
               print("\nLearn Axe Kick\n")
            if Skill_Books["Analysis"] == True:
               print("\nLearn Analysis\n")
            if Skill_Books["Heal"] == True:
               print("\nLearn Heal\n")
            if Skill_Books["Grappling Vines"] == True:
               print("\nLearn Grappling Vines\n")
            if Skill_Books["River Fist"] == True:
               print("\nLearn River Fist\n")
            if Skill_Books["Shock"] == True:
               print("\nLearn Shock\n")
            if Skill_Books["Life Drain"] == True:
               print("\nLearn Life Drain\n")
            if Skill_Books["Devour Essence"] == True:
               print("\nLearn Devour Essence\n")
            if Skill_Books["Purify"] == True:
               print("\nLearn Purify\n")
            if Skill_Books["Spinning Back Kick"] == True:
               print("\nLearn Spinning Back Kick\n")
            if Skill_Books["Ice Shard"] == True:
               print("\nLearn Ice Shard\n")
            if Skill_Books["Mud Shot"] == True:
               print("\nLearn Mud Shot\n")
            if Skill_Books["Tremor"] == True:
               print("\nLearn Tremor\n")
            if Skill_Books["Groundbreaker"] == True:
               print("\nLearn Groundbreaker\n")
            if Skill_Books["Jab"] == True:
               print("\nLearn Jab\n")
            if Skill_Books["Stone Slipstream"] == True:
               print("\nLearn Stone Slipstream\n")
            if Skill_Books["Domination"] == True:
               print("\nLearn Domination\n")
            if Skill_Books["Corrupting Touch"] == True:
               print("\nLearn Corrupting Touch\n")
            if Skill_Books["Toxin Spray"] == True:
               print("\nLearn Toxin Spray\n")
            if Skill_Books["Empower"] == True:
               print("\nLearn Empower\n")

            chosen = input("")
            chosen = chosen.lower()
            chosen = "".join(chosen.split())
            if chosen in ["fireball"] and Skill_Books["Fireball"] == True:
                Spell_list["Fireball"] = {"Damage":55,"Cost":70,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Fireball"]["Level"] = "Starter"
                
            elif chosen in ["headbutt"] and Skill_Books["Headbutt"] == True:
                Spell_list["Headbutt"] = {"Damage":25,"Cost":50,"Level":"Starter","Weight":"Heavy","Time":1}
                Skills["Headbutt"]["Level"] = "Starter"
                
            elif chosen in ["axekick"] and Skill_Books["Axe Kick"] == True:
                Spell_list["Axe Kick"] = {"Damage":90,"Cost":75,"Level":"Starter","Weight":"Heavy","Time":1}
                Skills["Axe Kick"]["Level"] = "Starter"
                
            elif chosen in ["analysis"] and Skill_Books["Analysis"] == True:
                Spell_list["Analysis"] = {"Power":30,"Cost":40,"Level":"Starter","Time":0.5}
                Skills["Analysis"]["Level"] = "Starter"
                
            elif chosen in ["heal"] and Skill_Books["Heal"] == True:
                Spell_list["Heal"] = {"Power":45,"Cost":80,"Level":"Starter","Time":0.5}
                Skills["Heal"]["Level"] = "Starter"
                
            elif chosen in ["grapplingvines"] and Skill_Books["Grappling Vines"] == True:
                Spell_list["Grappling Vines"] = {"Damage":0,"Cost":75,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Grappling Vines"]["Level"] = "Starter"
                
            elif chosen in ["riverfist"] and Skill_Books["River Fist"] == True:
                Spell_list["River Fist"] = {"Damage":60,"Cost":60,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["River Fist"]["Level"] = "Starter"
                
            elif chosen in ["shock"] and Skill_Books["Shock"] == True:
                Spell_list["Shock"] = {"Damage":45,"Cost":55,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Shock"]["Level"] = "Starter"
                
            elif chosen in ["lifedrain"] and Skill_Books["Life Drain"] == True:
                Spell_list["Life Drain"] = {"Damage":45,"Cost":75,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Life Drain"]["Level"] = "Starter"
                
            elif chosen in ["devouressence"] and Skill_Books["Devour Essence"] == True:
                Spell_list["Devour Essence"] = {"Power":80,"Cost":120,"Level":"Starter","Weight":"Heavy","Time":0.5}
                Skills["Devour Essence"]["Level"] = "Starter"
                
            elif chosen in ["purify"] and Skill_Books["Purify"] == True:
                Spell_list["Purify"] = {"Damage":35,"Cost":50,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Purify"]["Level"] = "Starter"
                
            elif chosen in ["spinningbackkick"] and Skill_Books["Spinning Back Kick"] == True:
                Spell_list["Spinning Back Kick"] = {"Damage":110,"Cost":90,"Level":"Starter","Weight":"Heavy","Time":1}
                Skills["Spinning Back Kick"]["Level"] = "Starter"

            elif chosen in ["iceshard"] and Skill_Books["Ice Shard"] == True:
                Spell_list["Ice Shard"] = {"Damage":50,"Cost":65,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Ice Shard"]["Level"] = "Starter"

            elif chosen in ["mudshot"] and Skill_Books["Mud Shot"] == True:
                Spell_list["Mud Shot"] = {"Damage":40,"Cost":45,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Mud Shot"]["Level"] = "Starter"

            elif chosen in ["tremor"] and Skill_Books["Tremor"] == True:
                Spell_list["Tremor"] = {"Damage":75,"Cost":80,"Level":"Starter","Weight":"Heavy","Time":1}
                Skills["Tremor"]["Level"] = "Starter"

            elif chosen in ["groundbreaker"] and Skill_Books["Groundbreaker"] == True:
                Spell_list["Groundbreaker"] = {"Damage":75,"Cost":80,"Level":"Starter","Weight":"Medium","Time":1}
                Skills["Groundbreaker"]["Level"] = "Starter"

            elif chosen in ["jab"] and Skill_Books["Jab"] == True:
                Spell_list["Jab"] = {"Damage":8,"Cost":5,"Level":"Starter","Weight":"Light","Time":0.1}
                Skills["Jab"]["Level"] = "Starter"

            elif chosen in ["stoneslipstream"] and Skill_Books["Stone Slipstream"] == True:
                Spell_list["Stone Slipstream"] = {"Damage":55,"Cost":60,"Level":"Starter","Weight":"Heavy","Time":1}
                Skills["Stone Slipstream"]["Level"] = "Starter"

            elif chosen in ["domination"] and Skill_Books["Domination"] == True:
                Spell_list["Domination"] = {"Power": 0,"Cost": 120,"Level":"Not Learned","Weight":"Heavy","Time":1}
                Skills["Domination"]["Level"] = "Starter"

            elif chosen in ["corruptingtouch"] and Skill_Books["Corrupting Touch"] == True:
                Spell_list["Corrupting Touch"] = {"Damage":45,"Cost":70,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Corrupting Touch"]["Level"] = "Starter"

            elif chosen in ["toxinspray"] and Skill_Books["Toxin Spray"] == True:
                Spell_list["Toxin Spray"] = {"Damage":30,"Cost":45,"Level":"Starter","Weight":"Medium","Time":0.5}
                Skills["Toxin Spray"]["Level"] = "Starter"

            elif chosen in ["empower"] and Skill_Books["Empower"] == True:
                Spell_list["Empower"] = {"Power":45,"Cost":80,"Level":"Starter","Time":0.5}
                Skills["Empower"]["Level"] = "Starter"

        elif Choice in ["6","titles","title","t"]:
            print("\nCurrent Title: ",Player["Title"],"\n\n---------------")
            for x in Titles:
                print(x)
            if Titles == []:
                print("\nYou have no titles\n")
            print("---------------\n\n")
            if Titles != []:
                print("What Title you would you like to equip?")
                equipped = input("")
                equipped = equipped.lower()
                equipped = "".join(equipped.split())
                if equipped in ["noviceslayer"] and "Novice Slayer" in Titles:
                    Player["Title"] = "Novice Slayer"
                    print("\nTitle Equipped\n")
                if equipped in ["veteranslayer"] and "Veteran Slayer" in Titles:
                    Player["Title"] = "Veteran Slayer"
                    print("\nTitle Equipped\n")
                if equipped in ["legendaryslayer"] and "Legendary Slayer" in Titles:
                    Player["Title"] = "Legendary Slayer"
                    print("\nTitle Equipped\n")
                if equipped in ["wellbuilt"] and "Well Built" in Titles:
                    Player["Title"] = "Well Built"
                    print("\nTitle Equipped\n")
                if equipped in ["peakphysique"] and "Peak Physique" in Titles:
                    Player["Title"] = "Peak Physique"
                    print("\nTitle Equipped\n")
                if equipped in ["recruit"] and "Recruit" in Titles:
                    Player["Title"] = "Recruit"
                    print("\nTitle Equipped\n")
                if equipped in ["fighter"] and "Fighter" in Titles:
                    Player["Title"] = "Fighter"
                    print("\nTitle Equipped\n")
                if equipped in ["veteran"] and "Veteran" in Titles:
                    Player["Title"] = "Veteran"
                    print("\nTitle Equipped\n")
                if equipped in ["battlehardened","battle-hardened"] and "Battle-Hardened" in Titles:
                    Player["Title"] = "Battle-Hardened"
                    print("\nTitle Equipped\n")
                if equipped in ["seasonedwarrior"] and "Seasoned Warrior" in Titles:
                    Player["Title"] = "Seasoned Warrior"
                    print("\nTitle Equipped\n")
                if equipped in ["elitecombatant"] and "Elite Combatant" in Titles:
                    Player["Title"] = "Elite Combatant"
                    print("\nTitle Equipped\n")
                if equipped in ["champion"] and "Champion" in Titles:
                    Player["Title"] = "Champion"
                    print("\nTitle Equipped\n")
                if equipped in ["warlord"] and "Warlord" in Titles:
                    Player["Title"] = "Warlord"
                    print("\nTitle Equipped\n")
                if equipped in ["conqueror"] and "Conqueror" in Titles:
                    Player["Title"] = "Conqueror"
                    print("\nTitle Equipped\n")
                if equipped in ["livinglegend"] and "Living Legend" in Titles:
                    Player["Title"] = "Living Legend"
                    print("\nTitle Equipped\n")
                if equipped in ["eternalwarrior"] and "Eternal Warrior" in Titles:
                    Player["Title"] = "Eternal Warrior"
                    print("\nTitle Equipped\n")
                if equipped in ["winner"] and "Winner" in Titles:
                    Player["Title"] = "Winner"
                    print("\nTitle Equipped\n")
                if equipped in ["theprofessional"] and "The Professional" in Titles:
                    Player["Title"] = "The Professional"
                    print("\nTitle Equipped\n")
                if equipped in ["indomitable"] and "Indomitable" in Titles:
                    Player["Title"] = "Indomitable"
                    print("\nTitle Equipped\n")
                if equipped in ["unstoppableforce"] and "Unstoppable Force" in Titles:
                    Player["Title"] = "Unstoppable Force"
                    print("\nTitle Equipped\n")
                if equipped in ["theoneaboveall"] and "The One Above All" in Titles:
                    Player["Title"] = "The One Above All"
                    print("\nTitle Equipped\n")
                if equipped in ["loser"] and "Loser" in Titles:
                    Player["Title"] = "Loser"
                    print("\nTitle Equipped\n")
                if equipped in ["scarred"] and "Scarred" in Titles:
                    Player["Title"] = "Scarred"
                    print("\nTitle Equipped\n")
                if equipped in ["tenacious"] and "Tenacious" in Titles:
                    Player["Title"] = "Tenacious"
                    print("\nTitle Equipped\n")
                if equipped in ["theimmovable"] and "The Immovable" in Titles:
                    Player["Title"] = "The Immovable"
                    print("\nTitle Equipped\n")
                if equipped in ["theeverenduring"] and "The Ever Enduring" in Titles:
                    Player["Title"] = "The Ever Enduring"
                    print("\nTitle Equipped\n")
                if equipped in ["unscathed"] and "Unscathed" in Titles:
                    Player["Title"] = "Unscathed"
                    print("\nTitle Equipped\n")
                if equipped in ["flawlessvictor"] and "Flawless Victor" in Titles:
                    Player["Title"] = "Flawless Victor"
                    print("\nTitle Equipped\n")
                if equipped in ["phantommenace"] and "Phantom Menace" in Titles:
                    Player["Title"] = "Phantom Menace"
                    print("\nTitle Equipped\n")
                if equipped in ["untouchableduelist"] and "Untouchable Duelist" in Titles:
                    Player["Title"] = "Untouchable Duelist"
                    print("\nTitle Equipped\n")
                if equipped in ["thepeerlesschampion"] and "The Peerless Champion" in Titles:
                    Player["Title"] = "The Peerless Champion"
                    print("\nTitle Equipped\n")
                if equipped in ["bossdemolisher"] and "Boss Demolisher" in Titles:
                    Player["Title"] = "Boss Demolisher"
                    print("\nTitle Equipped\n")
                if equipped in ["giantannihilator"] and "Giant Annihilator" in Titles:
                    Player["Title"] = "Giant Annihilator"
                    print("\nTitle Equipped\n")
                if equipped in ["thebaneoftitans"] and "The Bane Of Titans" in Titles:
                    Player["Title"] = "The Bane Of Titans"
                    print("\nTitle Equipped\n")
                if equipped in ["legendhunter"] and "Legend Hunter" in Titles:
                    Player["Title"] = "Legend Hunter"
                    print("\nTitle Equipped\n")
                if equipped in ["oneofthegreats"] and "One Of The Greats" in Titles:
                    Player["Title"] = "One Of The Greats"
                    print("\nTitle Equipped\n")
                if equipped in ["pennypincher"] and "Penny Pincher" in Titles:
                    Player["Title"] = "Penny Pincher"
                    print("\nTitle Equipped\n")
                if equipped in ["hoarder"] and "Hoarder" in Titles:
                    Player["Title"] = "Hoarder"
                    print("\nTitle Equipped\n")
                if equipped in ["noble"] and "Noble" in Titles:
                    Player["Title"] = "Noble"
                    print("\nTitle Equipped\n")
                if equipped in ["tycoon"] and "Tycoon" in Titles:
                    Player["Title"] = "Tycoon"
                    print("\nTitle Equipped\n")
                if equipped in ["midas"] and "Midas" in Titles:
                    Player["Title"] = "Midas"
                    print("\nTitle Equipped\n")
                if equipped in ["spender"] and "Spender" in Titles:
                    Player["Title"] = "Spender"
                    print("\nTitle Equipped\n")
                if equipped in ["bigspender"] and "Big Spender" in Titles:
                    Player["Title"] = "Big Spender"
                    print("\nTitle Equipped\n")
                if equipped in ["highroller"] and "High Roller" in Titles:
                    Player["Title"] = "High Roller"
                    print("\nTitle Equipped\n")
                if equipped in ["deeppockets"] and "Deep Pockets" in Titles:
                    Player["Title"] = "Deep Pockets"
                    print("\nTitle Equipped\n")
                if equipped in ["patronoftreasure"] and "Patron Of Treasure" in Titles:
                    Player["Title"] = "Patron Of Treasure"
                    print("\nTitle Equipped\n")
                if equipped in ["trainee"] and "Trainee" in Titles:
                    Player["Title"] = "Trainee"
                    print("\nTitle Equipped\n")
                if equipped in ["dedicated"] and "Dedicated" in Titles:
                    Player["Title"] = "Dedicated"
                    print("\nTitle Equipped\n")
                if equipped in ["fanatictrainer"] and "Fanatic Trainer" in Titles:
                    Player["Title"] = "Fanatic Trainer"
                    print("\nTitle Equipped\n")
                if equipped in ["tireless"] and "Tireless" in Titles:
                    Player["Title"] = "Tireless"
                    print("\nTitle Equipped\n")
                if equipped in ["pillarofdiscipline"] and "Pillar Of Discipline" in Titles:
                    Player["Title"] = "Pillar Of Discipline"
                    print("\nTitle Equipped\n")
                if equipped in ["virile"] and "Virile" in Titles:
                    Player["Title"] = "Virile"
                    print("\nTitle Equipped\n")
                if equipped in ["hearty"] and "Hearty" in Titles:
                    Player["Title"] = "Hearty"
                    print("\nTitle Equipped\n")
                if equipped in ["bulky"] and "Bulky" in Titles:
                    Player["Title"] = "Bulky"
                    print("\nTitle Equipped\n")
                if equipped in ["behemoth"] and "Behemoth" in Titles:
                    Player["Title"] = "Behemoth"
                    print("\nTitle Equipped\n")
                if equipped in ["thejadeemperor"] and "The Jade Emperor" in Titles:
                    Player["Title"] = "The Jade Emperor"
                    print("\nTitle Equipped\n")
                
                
        
    elif Choice in ["system","s","4"]:
        print("\n---------------\n""Save\n""---------------\n""Load\n---------------\nExit\n---------------\nSet Name\n---------------\nStatistics\n---------------\nText Speed\n---------------\n\n")
        Choice = input("")
        Choice = Choice.lower()
        Choice = "".join(Choice.split())
                
        if Choice in ["save","s","1"]:

            Say = True
        
            save_game(Say)

        
        elif Choice in ["load","l","2"]:


            load_game()
            
        elif Choice in ["exit","e","3"]:
            save_game()
            exit()
        elif Choice in ["setname","sn","4"]:
            print("\n\nChoose your name.\n")
            name = input("")
            print(f"{name} is entered\n\n")
            
        elif Choice in ["statistics","st","stats","stat","5","statistic"]:
            print(f"\nBattles Fought:" ,Statistics["Battles Fought"],"")
            print(f"Battles Won: ",Statistics["Battles Won"],"")
            print(f"Battles Lost: ",Statistics["Battles Lost"],"")
            print(f"Enemies Killed: ",Statistics["Enemies Killed"],"")
            print(f"Damageless Battles Won:" ,Statistics["Damageless Battles Won"],"")
            print(f"Bosses Killed: ",Statistics["Bosses Killed"],"")
            print(f"Training Sessions: ",Statistics["Training Sessions"],"")
            print(f"Gold Earned: ",Statistics["Gold Earned"],"")
            print(f"Gold Spent: ",Statistics["Gold Spent"],"")
        elif Choice in ["textspeed","6","ts","text","speed","t"]:
            print("\nChoose what speed you want the text to move at:\n\n1. Instantaneous\n\n2. Typewriting")
            Choice = input("")
            Choice = Choice.lower()
            Choice = "".join(Choice.split())
            if Choice in ["instantaneous","i","1"]:
                typewriter = False
            if Choice in ["typewriting","t","2"]:
                typewriter = True

            
    elif Choice in ["facilities","f","fc","3"]:

        
        print("\n---------------\nSimulation\n---------------\nMarket\n---------------\nMine\n---------------\nForest\n---------------\n"f"Training {Unlocked_Functions['Training']['Status']}\n""---------------\n"f"Smithing {Unlocked_Functions['Smithing']['Status']}\n""---------------\n"f"Alchemy {Unlocked_Functions['Alchemy']['Status']}\n---------------")
        Choice = input("")
        Choice = Choice.lower()
        
        if Choice in ["simulation","sim","1"]:
            chance = 0
            print("What skills do you want to learn?\n\nPress Enter to go back\n\n1. Melee Moves\n\n2. Magic Spells\n")
            Choice = input("").lower()
            Choice = "".join(Choice.split())
            if Choice in ["1","meleemoves","mm","melee","meleemove"]:
                print("What area do you want to practice a move for?\n\nPress Enter to go back\n\n1. Head\n\n2. Arms\n\n3. Legs\n")

                Melee_Choice = input("").lower()
                Melee_Choice = "".join(Melee_Choice.split())
                if Melee_Choice in ["1","head","heads"]:
                    print(f"\n Headbutt (5% Chance) (",Skills["Headbutt"]["Level"],")")
                    print(f"\n Bite (5% Chance) (",Skills["Bite"]["Level"],")")

                elif Melee_Choice in ["2","arms","arm"]:
                    print(f"\n Impulsive Swing (5% Chance) (",Skills["Impulsive Swing"]["Level"],")")
                    print(f"\n Jab (5% Chance) (",Skills["Jab"]["Level"],")")
                    print(f"\n Aimed Shot (5% Chance) (",Skills["Aimed Shot"]["Level"],")")
                    print(f"\n Straight Punch (5% Chance) (",Skills["Straight Punch"]["Level"],")")
                    print(f"\n Tackle (5% Chance) (",Skills["Tackle"]["Level"],")")
                    print(f"\n Slash (5% Chance) (",Skills["Slash"]["Level"],")")
                    print(f"\n Quick Stab (5% Chance) (",Skills["Quick Stab"]["Level"],")")

                elif Melee_Choice in ["3","legs","leg"]:
                    print(f"\n Spinning Back Kick (5% Chance)  (",Skills["Spinning Back Kick"]["Level"],")")
                    print(f"\n Axe Kick (5% Chance) (",Skills["Axe Kick"]["Level"],")")
                    print(f"\n Front Kick (5% Chance) (",Skills["Front Kick"]["Level"],")")
                    print(f"\n Groundbreaker (5% Chance) (",Skills["Groundbreaker"]["Level"],")")


            if Choice in ["2","magicspells","ms","magic","spells"]:
                print("What category of spell do you want to practice?\n\nPress Enter to go back\n\n1. Fire\n\n2. Water\n\n3. Lightning\n\n4. Ground\n\n5. Nature\n\n6. Mind\n\n7. Ice\n\n8. Wind\n\n9. Dark\n\n10. Light\n\n11. Arcane\n\n12. Support\n\n13. Detection\n")
                Spell_Choice = input("").lower()
                Spell_Choice = "".join(Spell_Choice.split())
                
                if Spell_Choice in ["1","fire"]:
                    print(f"\n Fireball (5% Chance)  (",Skills["Fireball"]["Level"],")")
                elif Spell_Choice in ["12","support"]:
                    print(f"\n Heal (5% Chance)  (",Skills["Heal"]["Level"],")")
                elif Spell_Choice in ["13","detection"]:
                    print(f"\n Analyse (5% Chance)  (",Skills["Analyse"]["Level"],")")
                elif Spell_Choice in ["7","ice"]:
                    print(f"\n Ice Shard (5% Chance) (",Skills["Ice Shard"]["Level"],")")
                elif Spell_Choice in ["3","lightning"]:
                    print(f"\n Shock (5% Chance) (",Skills["Shock"]["Level"],")")
                elif Spell_Choice in ["10","light"]:
                    print(f"\n Purify (5% Chance) (",Skills["Purify"]["Level"],")")
                elif Spell_Choice in ["water","2"]:
                    print(f"\n River Fist (5% Chance) (",Skills["River Fist"]["Level"],")")
                elif Spell_Choice in ["4","ground"]:
                    print(f"\n Mud Shot (5% Chance) (",Skills["Mud Shot"]["Level"],")")
                    print(f"\n Tremor (5% Chance) (",Skills["Tremor"]["Level"],")")

                elif Spell_Choice in ["9","dark"]:
                    print(f"\n Life Drain (5% Chance) (",Skills["Life Drain"]["Level"],")")
                    print(f"\n Corrupting Touch (5% Chance) (",Skills["Corrupting Touch"]["Level"],")")
                    print(f"\n Devour Essence (5% Chance) (",Skills["Devour Essence"]["Level"],")")
                    print(f"\n Toxin Spray (5% Chance) (",Skills["Toxin Spray"]["Level"],")")

                elif Spell_Choice in ["6","mind"]:
                    print(f"\n Domination (5% Chance) (",Skills["Domination"]["Level"],")")
                elif Spell_Choice in ["8","wind"]:
                    print(f"\n Stone Slipstream (5% Chance) (",Skills["Stone Slipstream"]["Level"],")")
                elif Spell_Choice in ["5","nature"]:
                    print(f"\n Grappling Vines (5% Chance) (",Skills["Grappling Vines"]["Level"],")")
                elif Spell_Choice in ["11","arcane"]:
                    print(f"\n Mana Blast (5% Chance) (",Skills["Mana Blast"]["Level"],")")
                    print(f"\n Empower (5% Chance) (",Skills["Empower"]["Level"],")")





            Choice = input("").lower()
            Choice = "".join(Choice.split())
            Player_copy = copy.deepcopy(Player)
            if Choice in ["spinningbackkick"] and Skills["Spinning Back Kick"]["Level"] != "Not Learned":
                while "Spinning Back Kick" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Spinning Back Kick to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["spinningbackkick",""]:
                        print("Not a correct input")
                    if action in ["spinningbackkick"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Spinning Back Kick"]["Cost"]
                        Amount_Practiced["Spinning Back Kick"] += 1
                        if Amount_Practiced["Spinning Back Kick"] == 100:
                            Combat_Skill_list["Spinning Back Kick"]["Level"] = "Rookie"
                            Combat_Skill_list["Spinning Back Kick"]["Damage"] *= 1.1
                            Combat_Skill_list["Spinning Back Kick"]["Cost"] *= 0.9
                            print("You improve your proficiency of Spinning Back Kick to ",Combat_Skill_list["Spinning Back Kick"]["Level"])
                        if Amount_Practiced["Spinning Back Kick"] == 500:
                            Combat_Skill_list["Spinning Back Kick"]["Level"] = "Competent"
                            Combat_Skill_list["Spinning Back Kick"]["Damage"] = Skills["Spinning Back Kick"]["Damage"] * 1.25
                            Combat_Skill_list["Spinning Back Kick"]["Cost"] = Skills["Spinning Back Kick"]["Cost"] * 0.9
                            print("You improve your proficiency of Spinning Back Kick to ",Combat_Skill_list["Spinning Back Kick"]["Level"])
                        if Amount_Practiced["Spinning Back Kick"] == 1000:
                            Combat_Skill_list["Spinning Back Kick"]["Level"] = "Proficient"
                            Combat_Skill_list["Spinning Back Kick"]["Damage"] = Skills["Spinning Back Kick"]["Damage"] * 1.45
                            Combat_Skill_list["Spinning Back Kick"]["Cost"] = Skills["Spinning Back Kick"]["Cost"] * 0.85
                            print("You improve your proficiency of Spinning Back Kick to ",Combat_Skill_list["Spinning Back Kick"]["Level"])
                        if Amount_Practiced["Spinning Back Kick"] == 2500:
                            Combat_Skill_list["Spinning Back Kick"]["Level"] = "Expert"
                            Combat_Skill_list["Spinning Back Kick"]["Damage"] = Skills["Spinning Back Kick"]["Damage"] * 1.7
                            Combat_Skill_list["Spinning Back Kick"]["Cost"] = Skills["Spinning Back Kick"]["Cost"] * 0.8
                            print("You improve your proficiency of Spinning Back Kick to ",Combat_Skill_list["Spinning Back Kick"]["Level"])
                        if Amount_Practiced["Spinning Back Kick"] == 10000:
                            Combat_Skill_list["Spinning Back Kick"]["Level"] = "Master"
                            Combat_Skill_list["Spinning Back Kick"]["Damage"] = Skills["Spinning Back Kick"]["Damage"] * 2
                            Combat_Skill_list["Spinning Back Kick"]["Cost"] = Skills["Spinning Back Kick"]["Cost"] * 0.7
                            print("You improve your proficiency of Spinning Back Kick to ",Combat_Skill_list["Spinning Back Kick"]["Level"])
                        Combat_Skill_list["Spinning Back Kick"]["Damage"] = round(Combat_Skill_list["Spinning Back Kick"]["Damage"])
                        Combat_Skill_list["Spinning Back Kick"]["Cost"] = round(Combat_Skill_list["Spinning Back Kick"]["Cost"])
                    elif action in [""]:
                        break
                    

            elif Choice in ["axekick"] and Skills["Axe Kick"]["Level"] != "Not Learned":
                while "Axe Kick" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Axe Kick to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["axekick",""]:
                        print("Not a correct input")
                    if action in ["axekick"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Axe Kick"]["Cost"]
                        Amount_Practiced["Axe Kick"] += 1
                        if Amount_Practiced["Axe Kick"] == 100:
                            Combat_Skill_list["Axe Kick"]["Level"] = "Rookie"
                            Combat_Skill_list["Axe Kick"]["Damage"] *= 1.1
                            Combat_Skill_list["Axe Kick"]["Cost"] *= 0.95
                            print("You improve your proficiency of Axe Kick to ",Combat_Skill_list["Axe Kick"]["Level"])
                        if Amount_Practiced["Axe Kick"] == 500:
                            Combat_Skill_list["Axe Kick"]["Level"] = "Competent"
                            Combat_Skill_list["Axe Kick"]["Damage"] = Skills["Axe Kick"]["Damage"] * 1.25
                            Combat_Skill_list["Axe Kick"]["Cost"] = Skills["Axe Kick"]["Cost"] * 0.9
                            print("You improve your proficiency of Axe Kick to ",Combat_Skill_list["Axe Kick"]["Level"])
                        if Amount_Practiced["Axe Kick"] == 1000:
                            Combat_Skill_list["Axe Kick"]["Level"] = "Proficient"
                            Combat_Skill_list["Axe Kick"]["Damage"] = Skills["Axe Kick"]["Damage"] * 1.45
                            Combat_Skill_list["Axe Kick"]["Cost"] = Skills["Axe Kick"]["Cost"] * 0.85
                            print("You improve your proficiency of Axe Kick to ",Combat_Skill_list["Axe Kick"]["Level"])
                        if Amount_Practiced["Axe Kick"] == 2500:
                            Combat_Skill_list["Axe Kick"]["Level"] = "Expert"
                            Combat_Skill_list["Axe Kick"]["Damage"] = Skills["Axe Kick"]["Damage"] * 1.7
                            Combat_Skill_list["Axe Kick"]["Cost"] = Skills["Axe Kick"]["Cost"] * 0.8
                            print("You improve your proficiency of Axe Kick to ",Combat_Skill_list["Axe Kick"]["Level"])
                        if Amount_Practiced["Axe Kick"] == 10000:
                            Combat_Skill_list["Axe Kick"]["Level"] = "Master"
                            Combat_Skill_list["Axe Kick"]["Damage"] = Skills["Axe Kick"]["Damage"] * 2
                            Combat_Skill_list["Axe Kick"]["Cost"] = Skills["Axe Kick"]["Cost"] * 0.7
                            print("You improve your proficiency of Axe Kick to ",Combat_Skill_list["Axe Kick"]["Level"])
                        Combat_Skill_list["Axe Kick"]["Damage"] = round(Combat_Skill_list["Axe Kick"]["Damage"])
                        Combat_Skill_list["Axe Kick"]["Cost"] = round(Combat_Skill_list["Axe Kick"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["headbutt"] and Skills["Headbutt"]["Level"] != "Not Learned":
                while "Headbutt" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Headbutt to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["headbutt",""]:
                        print("Not a correct input")
                    if action in ["headbutt"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Headbutt"]["Cost"]
                        Amount_Practiced["Headbutt"] += 1
                        if Amount_Practiced["Headbutt"] == 100:
                            Combat_Skill_list["Headbutt"]["Level"] = "Rookie"
                            Combat_Skill_list["Headbutt"]["Damage"] *= 1.1
                            Combat_Skill_list["Headbutt"]["Cost"] *= 0.95
                            print("You improve your proficiency of Headbutt to ",Combat_Skill_list["Headbutt"]["Level"])
                        if Amount_Practiced["Headbutt"] == 500:
                            Combat_Skill_list["Headbutt"]["Level"] = "Competent"
                            Combat_Skill_list["Headbutt"]["Damage"] = Skills["Headbutt"]["Damage"] * 1.25
                            Combat_Skill_list["Headbutt"]["Cost"] = Skills["Headbutt"]["Cost"] * 0.9
                            print("You improve your proficiency of Headbutt to ",Combat_Skill_list["Headbutt"]["Level"])
                        if Amount_Practiced["Headbutt"] == 1000:
                            Combat_Skill_list["Headbutt"]["Level"] = "Proficient"
                            Combat_Skill_list["Headbutt"]["Damage"] = Skills["Headbutt"]["Damage"] * 1.45
                            Combat_Skill_list["Headbutt"]["Cost"] = Skills["Headbutt"]["Cost"] * 0.85
                            print("You improve your proficiency of Headbutt to ",Combat_Skill_list["Headbutt"]["Level"])
                        if Amount_Practiced["Headbutt"] == 2500:
                            Combat_Skill_list["Headbutt"]["Level"] = "Expert"
                            Combat_Skill_list["Headbutt"]["Damage"] = Skills["Headbutt"]["Damage"] * 1.7
                            Combat_Skill_list["Headbutt"]["Cost"] = Skills["Headbutt"]["Cost"] * 0.8
                            print("You improve your proficiency of Headbutt to ",Combat_Skill_list["Headbutt"]["Level"])
                        if Amount_Practiced["Headbutt"] == 10000:
                            Combat_Skill_list["Headbutt"]["Level"] = "Master"
                            Combat_Skill_list["Headbutt"]["Damage"] = Skills["Headbutt"]["Damage"] * 2
                            Combat_Skill_list["Headbutt"]["Cost"] = Skills["Headbutt"]["Cost"] * 0.7
                            print("You improve your proficiency of Headbutt to ",Combat_Skill_list["Headbutt"]["Level"])
                        Combat_Skill_list["Headbutt"]["Damage"] = round(Combat_Skill_list["Headbutt"]["Damage"])
                        Combat_Skill_list["Headbutt"]["Cost"] = round(Combat_Skill_list["Headbutt"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["fireball"] and Skills["Fireball"]["Level"] != "Not Learned":
                while "Fireball" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Fireball to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["fireball",""]:
                        print("Not a correct input")
                    if action in ["fireball"]:
                        Player_copy["Mana"] -= Spell_list["Fireball"]["Cost"]
                        Amount_Practiced["Fireball"] += 1
                        if Amount_Practiced["Fireball"] == 100:
                            Spell_list["Fireball"]["Level"] = "Rookie"
                            Spell_list["Fireball"]["Damage"] *= 1.1
                            Spell_list["Fireball"]["Cost"] *= 0.95
                            print("You improve your proficiency of Fireball to ",Spell_list["Fireball"]["Level"])
                        if Amount_Practiced["Fireball"] == 500:
                            Spell_list["Fireball"]["Level"] = "Competent"
                            Spell_list["Fireball"]["Damage"] = Skills["Fireball"]["Damage"] * 1.25
                            Spell_list["Fireball"]["Cost"] = Skills["Fireball"]["Cost"] * 0.9
                            print("You improve your proficiency of Fireball to ",Spell_list["Fireball"]["Level"])
                        if Amount_Practiced["Fireball"] == 1000:
                            Spell_list["Fireball"]["Level"] = "Proficient"
                            Spell_list["Fireball"]["Damage"] = Skills["Fireball"]["Damage"] * 1.45
                            Spell_list["Fireball"]["Cost"] = Skills["Fireball"]["Cost"] * 0.85
                            print("You improve your proficiency of Fireball to ",Spell_list["Fireball"]["Level"])
                        if Amount_Practiced["Fireball"] == 2500:
                            Spell_list["Fireball"]["Level"] = "Expert"
                            Spell_list["Fireball"]["Damage"] = Skills["Fireball"]["Damage"] * 1.7
                            Spell_list["Fireball"]["Cost"] = Skills["Fireball"]["Cost"] * 0.8
                            print("You improve your proficiency of Fireball to ",Spell_list["Fireball"]["Level"])
                        if Amount_Practiced["Fireball"] == 10000:
                            Spell_list["Fireball"]["Level"] = "Master"
                            Spell_list["Fireball"]["Damage"] = Skills["Fireball"]["Damage"] * 2
                            Spell_list["Fireball"]["Cost"] = Skills["Fireball"]["Cost"] * 0.7
                            print("You improve your proficiency of Fireball to ",Spell_list["Fireball"]["Level"])
                        Spell_list["Fireball"]["Damage"] = round(Spell_list["Fireball"]["Damage"])
                        Spell_list["Fireball"]["Cost"] = round(Spell_list["Fireball"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["heal"] and Skills["Heal"]["Level"] != "Not Learned":
                while "Heal" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Heal to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["heal",""]:
                        print("Not a correct input")
                    if action in ["heal"]:
                        Player_copy["Mana"] -= Spell_list["Heal"]["Cost"]
                        Amount_Practiced["Heal"] += 1
                        if Amount_Practiced["Heal"] == 100:
                            Spell_list["Heal"]["Level"] = "Rookie"
                            Spell_list["Heal"]["Power"] *= 1.1
                            Spell_list["Heal"]["Cost"] *= 0.95
                            print("You improve your proficiency of Heal to ",Spell_list["Heal"]["Level"])
                        if Amount_Practiced["Heal"] == 500:
                            Spell_list["Heal"]["Level"] = "Competent"
                            Spell_list["Heal"]["Power"] = Skills["Heal"]["Power"] * 1.25
                            Spell_list["Heal"]["Cost"] = Skills["Heal"]["Cost"] * 0.9
                            print("You improve your proficiency of Heal to ",Spell_list["Heal"]["Level"])
                        if Amount_Practiced["Heal"] == 1000:
                            Spell_list["Heal"]["Level"] = "Proficient"
                            Spell_list["Heal"]["Power"] = Skills["Heal"]["Power"] * 1.45
                            Spell_list["Heal"]["Cost"] = Skills["Heal"]["Cost"] * 0.85
                            print("You improve your proficiency of Heal to ",Spell_list["Heal"]["Level"])
                        if Amount_Practiced["Heal"] == 2500:
                            Spell_list["Heal"]["Level"] = "Expert"
                            Spell_list["Heal"]["Power"] = Skills["Heal"]["Power"] * 1.7
                            Spell_list["Heal"]["Cost"] = Skills["Heal"]["Cost"] * 0.8
                            print("You improve your proficiency of Heal to ",Spell_list["Heal"]["Level"])
                        if Amount_Practiced["Heal"] == 10000:
                            Spell_list["Heal"]["Level"] = "Master"
                            Spell_list["Heal"]["Power"] = Skills["Heal"]["Power"] * 2
                            Spell_list["Heal"]["Cost"] = Skills["Heal"]["Cost"] * 0.7
                            print("You improve your proficiency of Heal to ",Spell_list["Heal"]["Level"])
                        Spell_list["Heal"]["Power"] = round(Spell_list["Heal"]["Power"])
                        Spell_list["Heal"]["Cost"] = round(Spell_list["Heal"]["Cost"])
                    elif action in [""]:
                        break
                        
            elif Choice in ["analyse"] and Skills["Analyse"]["Level"] != "Not Learned":
                while "Analyse" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Analyse to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["analyse",""]:
                        print("Not a correct input")
                    if action in ["analyse"]:
                        Player_copy["Stamina"] -= Spell_list["Analyse"]["Cost"]
                        Amount_Practiced["Analyse"] += 1
                        if Amount_Practiced["Analyse"] == 100:
                            Spell_list["Analyse"]["Level"] = "Rookie"
                            Spell_list["Analyse"]["Power"] *= 1.1
                            Spell_list["Analyse"]["Cost"] *= 0.95
                            print("You improve your proficiency of Analyse to ",Spell_list["Analyse"]["Level"])
                        if Amount_Practiced["Analyse"] == 500:
                            Spell_list["Analyse"]["Level"] = "Competent"
                            Spell_list["Analyse"]["Power"] = Skills["Analyse"]["Power"] * 1.25
                            Spell_list["Analyse"]["Cost"] = Skills["Analyse"]["Cost"] * 0.9
                            print("You improve your proficiency of Analyse to ",Spell_list["Analyse"]["Level"])
                        if Amount_Practiced["Analyse"] == 1000:
                            Spell_list["Analyse"]["Level"] = "Proficient"
                            Spell_list["Analyse"]["Power"] = Skills["Analyse"]["Power"] * 1.45
                            Spell_list["Analyse"]["Cost"] = Skills["Analyse"]["Cost"] * 0.85
                            print("You improve your proficiency of Analyse to ",Spell_list["Analyse"]["Level"])
                        if Amount_Practiced["Analyse"] == 2500:
                            Spell_list["Analyse"]["Level"] = "Expert"
                            Spell_list["Analyse"]["Power"] = Skills["Analyse"]["Power"] * 1.7
                            Spell_list["Analyse"]["Cost"] = Skills["Analyse"]["Cost"] * 0.8
                            print("You improve your proficiency of Analyse to ",Spell_list["Analyse"]["Level"])
                        if Amount_Practiced["Analyse"] == 10000:
                            Spell_list["Analyse"]["Level"] = "Master"
                            Spell_list["Analyse"]["Power"] = Skills["Analyse"]["Power"] * 2
                            Spell_list["Analyse"]["Cost"] = Skills["Analyse"]["Cost"] * 0.7
                            print("You improve your proficiency of Analyse to ",Spell_list["Analyse"]["Level"])
                        Spell_list["Analyse"]["Damage"] = round(Spell_list["Analyse"]["Damage"])
                        Spell_list["Analyse"]["Cost"] = round(Spell_list["Analyse"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["iceshard"] and Skills["Ice Shard"]["Level"] != "Not Learned":
                while "Ice Shard" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Ice Shard to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["iceshard",""]:
                        print("Not a correct input")
                    if action in ["iceshard"]:
                        Player_copy["Mana"] -= Spell_list["Ice Shard"]["Cost"]
                        Amount_Practiced["Ice Shard"] += 1
                        if Amount_Practiced["Ice Shard"] == 100:
                            Spell_list["Ice Shard"]["Level"] = "Rookie"
                            Spell_list["Ice Shard"]["Damage"] *= 1.1
                            Spell_list["Ice Shard"]["Cost"] *= 0.95    
                        if Amount_Practiced["Ice Shard"] == 500:
                            Spell_list["Ice Shard"]["Level"] = "Competent"
                            Spell_list["Ice Shard"]["Damage"] = Skills["Ice Shard"]["Damage"] * 1.25
                            Spell_list["Ice Shard"]["Cost"] = Skills["Ice Shard"]["Cost"] * 0.9
                            print("You improve your proficiency of Ice Shard to ",Spell_list["Ice Shard"]["Level"])
                        if Amount_Practiced["Ice Shard"] == 1000:
                            Spell_list["Ice Shard"]["Level"] = "Proficient"
                            Spell_list["Ice Shard"]["Damage"] = Skills["Ice Shard"]["Damage"] * 1.45
                            Spell_list["Ice Shard"]["Cost"] = Skills["Ice Shard"]["Cost"] * 0.85
                            print("You improve your proficiency of Ice Shard to ",Spell_list["Ice Shard"]["Level"])
                        if Amount_Practiced["Ice Shard"] == 2500:
                            Spell_list["Ice Shard"]["Level"] = "Expert"
                            Spell_list["Ice Shard"]["Damage"] = Skills["Ice Shard"]["Damage"] * 1.7
                            Spell_list["Ice Shard"]["Cost"] = Skills["Ice Shard"]["Cost"] * 0.8
                            print("You improve your proficiency of Ice Shard to ",Spell_list["Ice Shard"]["Level"])
                        if Amount_Practiced["Ice Shard"] == 10000:
                            Spell_list["Ice Shard"]["Level"] = "Master"
                            Spell_list["Ice Shard"]["Damage"] = Skills["Ice Shard"]["Damage"] * 2
                            Spell_list["Ice Shard"]["Cost"] = Skills["Ice Shard"]["Cost"] * 0.7
                            print("You improve your proficiency of Ice Shard to ",Spell_list["Ice Shard"]["Level"])
                        Spell_list["Ice Shard"]["Damage"] = round(Spell_list["Ice Shard"]["Damage"])
                        Spell_list["Ice Shard"]["Cost"] = round(Spell_list["Ice Shard"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["shock"] and Skills["Shock"]["Level"] != "Not Learned":
                while "Shock" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Shock to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["shock",""]:
                        print("Not a correct input")
                    if action in ["shock"]:
                        Player_copy["Mana"] -= Spell_list["Shock"]["Cost"]
                        Amount_Practiced["Shock"] += 1
                        if Amount_Practiced["Shock"] == 100:
                            Spell_list["Shock"]["Level"] = "Rookie"
                            Spell_list["Shock"]["Damage"] *= 1.1
                            Spell_list["Shock"]["Cost"] *= 0.95
                            print("You improve your proficiency of Shock to ",Spell_list["Shock"]["Level"])
                        if Amount_Practiced["Shock"] == 500:
                            Spell_list["Shock"]["Level"] = "Competent"
                            Spell_list["Shock"]["Damage"] = Skills["Shock"]["Damage"] * 1.25
                            Spell_list["Shock"]["Cost"] = Skills["Shock"]["Cost"] * 0.9
                            print("You improve your proficiency of Shock to ",Spell_list["Shock"]["Level"])
                        if Amount_Practiced["Shock"] == 1000:
                            Spell_list["Shock"]["Level"] = "Proficient"
                            Spell_list["Shock"]["Damage"] = Skills["Shock"]["Damage"] * 1.45
                            Spell_list["Shock"]["Cost"] = Skills["Shock"]["Cost"] * 0.85
                            print("You improve your proficiency of Shock to ",Spell_list["Shock"]["Level"])
                        if Amount_Practiced["Shock"] == 2500:
                            Spell_list["Shock"]["Level"] = "Expert"
                            Spell_list["Shock"]["Damage"] = Skills["Shock"]["Damage"] * 1.7
                            Spell_list["Shock"]["Cost"] = Skills["Shock"]["Cost"] * 0.8
                            print("You improve your proficiency of Shock to ",Spell_list["Shock"]["Level"])
                        if Amount_Practiced["Shock"] == 10000:
                            Spell_list["Shock"]["Level"] = "Master"
                            Spell_list["Shock"]["Damage"] = Skills["Shock"]["Damage"] * 2
                            Spell_list["Shock"]["Cost"] = Skills["Shock"]["Cost"] * 0.7
                            print("You improve your proficiency of Shock to ",Spell_list["Shock"]["Level"])
                        Spell_list["Shock"]["Damage"] = round(Spell_list["Shock"]["Damage"])
                        Spell_list["Shock"]["Cost"] = round(Spell_list["Shock"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["riverfist"] and Skills["River Fist"]["Level"] != "Not Learned":
                while "River Fist" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter River Fist to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["riverfist",""]:
                        print("Not a correct input")
                    if action in ["riverfist"]:
                        Player_copy["Mana"] -= Spell_list["River Fist"]["Cost"]
                        Amount_Practiced["River Fist"] += 1
                        if Amount_Practiced["River Fist"] == 100:
                            Spell_list["River Fist"]["Level"] = "Rookie"
                            Spell_list["River Fist"]["Damage"] *= 1.1
                            Spell_list["River Fist"]["Cost"] *= 0.95
                            print("You improve your proficiency of River Fist to ",Spell_list["River Fist"]["Level"])
                        if Amount_Practiced["River Fist"] == 500:
                            Spell_list["River Fist"]["Level"] = "Competent"
                            Spell_list["River Fist"]["Damage"] = Skills["River Fist"]["Damage"] * 1.25
                            Spell_list["River Fist"]["Cost"] = Skills["River Fist"]["Cost"] * 0.9
                            print("You improve your proficiency of River Fist to ",Spell_list["River Fist"]["Level"])
                        if Amount_Practiced["River Fist"] == 1000:
                            Spell_list["River Fist"]["Level"] = "Proficient"
                            Spell_list["River Fist"]["Damage"] = Skills["River Fist"]["Damage"] * 1.45
                            Spell_list["River Fist"]["Cost"] = Skills["River Fist"]["Cost"] * 0.85
                            print("You improve your proficiency of River Fist to ",Spell_list["River Fist"]["Level"])
                        if Amount_Practiced["River Fist"] == 2500:
                            Spell_list["River Fist"]["Level"] = "Expert"
                            Spell_list["River Fist"]["Damage"] = Skills["River Fist"]["Damage"] * 1.7
                            Spell_list["River Fist"]["Cost"] = Skills["River Fist"]["Cost"] * 0.8
                            print("You improve your proficiency of River Fist to ",Spell_list["River Fist"]["Level"])
                        if Amount_Practiced["River Fist"] == 10000:
                            Spell_list["River Fist"]["Level"] = "Master"
                            Spell_list["River Fist"]["Damage"] = Skills["River Fist"]["Damage"] * 2
                            Spell_list["River Fist"]["Cost"] = Skills["River Fist"]["Cost"] * 0.7
                            print("You improve your proficiency of River Fist to ",Spell_list["River Fist"]["Level"])
                        Spell_list["River Fist"]["Damage"] = round(Spell_list["River Fist"]["Damage"])
                        Spell_list["River Fist"]["Cost"] = round(Spell_list["River Fist"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["mudshot"] and Skills["Mud Shot"]["Level"] != "Not Learned":
                while "Mud Shot" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Mud Shot to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["mudshot",""]:
                        print("Not a correct input")
                    if action in ["mudshot"]:
                        Player_copy["Mana"] -= Spell_list["Mud Shot"]["Cost"]
                        Amount_Practiced["Mud Shot"] += 1
                        if Amount_Practiced["Mud Shot"] == 100:
                            Spell_list["Mud Shot"]["Level"] = "Rookie"
                            Spell_list["Mud Shot"]["Damage"] *= 1.1
                            Spell_list["Mud Shot"]["Cost"] *= 0.95
                            print("You improve your proficiency of Mud Shot to ",Spell_list["Mud Shot"]["Level"])
                        if Amount_Practiced["Mud Shot"] == 500:
                            Spell_list["Mud Shot"]["Level"] = "Competent"
                            Spell_list["Mud Shot"]["Damage"] = Skills["Mud Shot"]["Damage"] * 1.25
                            Spell_list["Mud Shot"]["Cost"] = Skills["Mud Shot"]["Cost"] * 0.9
                            print("You improve your proficiency of Mud Shot to ",Spell_list["Mud Shot"]["Level"])
                        if Amount_Practiced["Mud Shot"] == 1000:
                            Spell_list["Mud Shot"]["Level"] = "Proficient"
                            Spell_list["Mud Shot"]["Damage"] = Skills["Mud Shot"]["Damage"] * 1.45
                            Spell_list["Mud Shot"]["Cost"] = Skills["Mud Shot"]["Cost"] * 0.85
                            print("You improve your proficiency of Mud Shot to ",Spell_list["Mud Shot"]["Level"])
                        if Amount_Practiced["Mud Shot"] == 2500:
                            Spell_list["Mud Shot"]["Level"] = "Expert"
                            Spell_list["Mud Shot"]["Damage"] = Skills["Mud Shot"]["Damage"] * 1.7
                            Spell_list["Mud Shot"]["Cost"] = Skills["Mud Shot"]["Cost"] * 0.8
                            print("You improve your proficiency of Mud Shot to ",Spell_list["Mud Shot"]["Level"])
                        if Amount_Practiced["Mud Shot"] == 10000:
                            Spell_list["Mud Shot"]["Level"] = "Master"
                            Spell_list["Mud Shot"]["Damage"] = Skills["Mud Shot"]["Damage"] * 2
                            Spell_list["Mud Shot"]["Cost"] = Skills["Mud Shot"]["Cost"] * 0.7
                            print("You improve your proficiency of Mud Shot to ",Spell_list["Mud Shot"]["Level"])
                        Spell_list["Mud Shot"]["Damage"] = round(Spell_list["Mud Shot"]["Damage"])
                        Spell_list["Mud Shot"]["Cost"] = round(Spell_list["Mud Shot"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["lifedrain"] and Skills["Life Drain"]["Level"] != "Not Learned":
                while "Life Drain" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Life Drain to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["lifedrain",""]:
                        print("Not a correct input")
                    if action in ["lifedrain"]:
                        Player_copy["Mana"] -= Spell_list["Life Drain"]["Cost"]
                        Amount_Practiced["Life Drain"] += 1
                        if Amount_Practiced["Life Drain"] == 100:
                            Spell_list["Life Drain"]["Level"] = "Rookie"
                            Spell_list["Life Drain"]["Damage"] *= 1.1
                            Spell_list["Life Drain"]["Cost"] *= 0.95
                            print("You improve your proficiency of Life Drain to ",Spell_list["Life Drain"]["Level"])
                        if Amount_Practiced["Life Drain"] == 500:
                            Spell_list["Life Drain"]["Level"] = "Competent"
                            Spell_list["Life Drain"]["Damage"] = Skills["Life Drain"]["Damage"] * 1.25
                            Spell_list["Life Drain"]["Cost"] = Skills["Life Drain"]["Cost"] * 0.9
                            print("You improve your proficiency of Life Drain to ",Spell_list["Life Drain"]["Level"])
                        if Amount_Practiced["Life Drain"] == 1000:
                            Spell_list["Life Drain"]["Level"] = "Proficient"
                            Spell_list["Life Drain"]["Damage"] = Skills["Life Drain"]["Damage"] * 1.45
                            Spell_list["Life Drain"]["Cost"] = Skills["Life Drain"]["Cost"] * 0.85
                            print("You improve your proficiency of Life Drain to ",Spell_list["Life Drain"]["Level"])
                        if Amount_Practiced["Life Drain"] == 2500:
                            Spell_list["Life Drain"]["Level"] = "Expert"
                            Spell_list["Life Drain"]["Damage"] = Skills["Life Drain"]["Damage"] * 1.7
                            Spell_list["Life Drain"]["Cost"] = Skills["Life Drain"]["Cost"] * 0.8
                            print("You improve your proficiency of Life Drain to ",Spell_list["Life Drain"]["Level"])
                        if Amount_Practiced["Life Drain"] == 10000:
                            Spell_list["Life Drain"]["Level"] = "Master"
                            Spell_list["Life Drain"]["Damage"] = Skills["Life Drain"]["Damage"] * 2
                            Spell_list["Life Drain"]["Cost"] = Skills["Life Drain"]["Cost"] * 0.7
                            print("You improve your proficiency of Life Drain to ",Spell_list["Life Drain"]["Level"])
                        Spell_list["Life Drain"]["Damage"] = round(Spell_list["Life Drain"]["Damage"])
                        Spell_list["Life Drain"]["Cost"] = round(Spell_list["Life Drain"]["Cost"])
                    elif action in [""]:
                        break



            elif Choice in ["purify"] and Skills["Purify"]["Level"] != "Not Learned":
                while "Purify" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Purify to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["purify",""]:
                        print("Not a correct input")
                    if action in ["purify"]:
                        Player_copy["Mana"] -= Spell_list["Purify"]["Cost"]
                        Amount_Practiced["Purify"] += 1
                        if Amount_Practiced["Purify"] == 100:
                            Spell_list["Purify"]["Level"] = "Rookie"
                            Spell_list["Purify"]["Damage"] *= 1.1
                            Spell_list["Purify"]["Cost"] *= 0.95
                            print("You improve your proficiency of Purify to ",Spell_list["Purify"]["Level"])
                        if Amount_Practiced["Purify"] == 500:
                            Spell_list["Purify"]["Level"] = "Competent"
                            Spell_list["Purify"]["Damage"] = Skills["Purify"]["Damage"] * 1.25
                            Spell_list["Purify"]["Cost"] = Skills["Purify"]["Cost"] * 0.9
                            print("You improve your proficiency of Purify to ",Spell_list["Purify"]["Level"])
                        if Amount_Practiced["Purify"] == 1000:
                            Spell_list["Purify"]["Level"] = "Proficient"
                            Spell_list["Purify"]["Damage"] = Skills["Purify"]["Damage"] * 1.45
                            Spell_list["Purify"]["Cost"] = Skills["Purify"]["Cost"] * 0.85
                            print("You improve your proficiency of Purify to ",Spell_list["Purify"]["Level"])
                        if Amount_Practiced["Purify"] == 2500:
                            Spell_list["Purify"]["Level"] = "Expert"
                            Spell_list["Purify"]["Damage"] = Skills["Purify"]["Damage"] * 1.7
                            Spell_list["Purify"]["Cost"] = Skills["Purify"]["Cost"] * 0.8
                            print("You improve your proficiency of Purify to ",Spell_list["Purify"]["Level"])
                        if Amount_Practiced["Purify"] == 10000:
                            Spell_list["Purify"]["Level"] = "Master"
                            Spell_list["Purify"]["Damage"] = Skills["Purify"]["Damage"] * 2
                            Spell_list["Purify"]["Cost"] = Skills["Purify"]["Cost"] * 0.7
                            print("You improve your proficiency of Purify to ",Spell_list["Purify"]["Level"])
                        Spell_list["Purify"]["Damage"] = round(Spell_list["Purify"]["Damage"])
                        Spell_list["Purify"]["Cost"] = round(Spell_list["Purify"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["grapplingvines"] and Skills["Grappling Vines"]["Level"] != "Not Learned":
                while "Grappling Vines" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Grappling Vines to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["grapplingvines",""]:
                        print("Not a correct input")
                    if action in ["grapplingvines"]:
                        Player_copy["Mana"] -= Spell_list["Grappling Vines"]["Cost"]
                        Amount_Practiced["Grappling Vines"] += 1
                        if Amount_Practiced["Grappling Vines"] == 100:
                            Spell_list["Grappling Vines"]["Level"] = "Rookie"
                            Spell_list["Grappling Vines"]["Damage"] *= 1.1
                            Spell_list["Grappling Vines"]["Cost"] *= 0.95
                            print("You improve your proficiency of Grappling Vines to ",Spell_list["Grappling Vines"]["Level"])
                        if Amount_Practiced["Grappling Vines"] == 500:
                            Spell_list["Grappling Vines"]["Level"] = "Competent"
                            Spell_list["Grappling Vines"]["Damage"] = Skills["Grappling Vines"]["Damage"] * 1.25
                            Spell_list["Grappling Vines"]["Cost"] = Skills["Grappling Vines"]["Cost"] * 0.9
                            print("You improve your proficiency of Grappling Vines to ",Spell_list["Grappling Vines"]["Level"])
                        if Amount_Practiced["Grappling Vines"] == 1000:
                            Spell_list["Grappling Vines"]["Level"] = "Proficient"
                            Spell_list["Grappling Vines"]["Damage"] = Skills["Grappling Vines"]["Damage"] * 1.45
                            Spell_list["Grappling Vines"]["Cost"] = Skills["Grappling Vines"]["Cost"] * 0.85
                            print("You improve your proficiency of Grappling Vines to ",Spell_list["Grappling Vines"]["Level"])
                        if Amount_Practiced["Grappling Vines"] == 2500:
                            Spell_list["Grappling Vines"]["Level"] = "Expert"
                            Spell_list["Grappling Vines"]["Damage"] = Skills["Grappling Vines"]["Damage"] * 1.7
                            Spell_list["Grappling Vines"]["Cost"] = Skills["Grappling Vines"]["Cost"] * 0.8
                            print("You improve your proficiency of Grappling Vines to ",Spell_list["Grappling Vines"]["Level"])
                        if Amount_Practiced["Grappling Vines"] == 10000:
                            Spell_list["Grappling Vines"]["Level"] = "Master"
                            Spell_list["Grappling Vines"]["Damage"] = Skills["Grappling Vines"]["Damage"] * 2
                            Spell_list["Grappling Vines"]["Cost"] = Skills["Grappling Vines"]["Cost"] * 0.7
                            print("You improve your proficiency of Grappling Vines to ",Spell_list["Grappling Vines"]["Level"])
                        Spell_list["Grappling Vines"]["Damage"] = round(Spell_list["Grappling Vines"]["Damage"])
                        Spell_list["Grappling Vines"]["Cost"] = round(Spell_list["Grappling Vines"]["Cost"])
                    elif action in [""]:
                        break



            elif Choice in ["domination"] and Skills["Domination"]["Level"] != "Not Learned":
                while "Domination" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Domination to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["domination",""]:
                        print("Not a correct input")
                    if action in ["domination"]:
                        Player_copy["Mana"] -= Spell_list["Domination"]["Cost"]
                        Amount_Practiced["Domination"] += 1
                        if Amount_Practiced["Domination"] == 100:
                            Spell_list["Domination"]["Level"] = "Rookie"
                            Spell_list["Domination"]["Damage"] *= 1.1
                            Spell_list["Domination"]["Cost"] *= 0.95
                            print("You improve your proficiency of Domination to ",Spell_list["Domination"]["Level"])
                        if Amount_Practiced["Domination"] == 500:
                            Spell_list["Domination"]["Level"] = "Competent"
                            Spell_list["Domination"]["Damage"] = Skills["Domination"]["Damage"] * 1.25
                            Spell_list["Domination"]["Cost"] = Skills["Domination"]["Cost"] * 0.9
                            print("You improve your proficiency of Domination to ",Spell_list["Domination"]["Level"])
                        if Amount_Practiced["Domination"] == 1000:
                            Spell_list["Domination"]["Level"] = "Proficient"
                            Spell_list["Domination"]["Damage"] = Skills["Domination"]["Damage"] * 1.45
                            Spell_list["Domination"]["Cost"] = Skills["Domination"]["Cost"] * 0.85
                            print("You improve your proficiency of Domination to ",Spell_list["Domination"]["Level"])
                        if Amount_Practiced["Domination"] == 2500:
                            Spell_list["Domination"]["Level"] = "Expert"
                            Spell_list["Domination"]["Damage"] = Skills["Domination"]["Damage"] * 1.7
                            Spell_list["Domination"]["Cost"] = Skills["Domination"]["Cost"] * 0.8
                            print("You improve your proficiency of Domination to ",Spell_list["Domination"]["Level"])
                        if Amount_Practiced["Domination"] == 10000:
                            Spell_list["Domination"]["Level"] = "Master"
                            Spell_list["Domination"]["Damage"] = Skills["Domination"]["Damage"] * 2
                            Spell_list["Domination"]["Cost"] = Skills["Domination"]["Cost"] * 0.7
                            print("You improve your proficiency of Domination to ",Spell_list["Domination"]["Level"])
                        Spell_list["Domination"]["Damage"] = round(Spell_list["Domination"]["Damage"])
                        Spell_list["Domination"]["Cost"] = round(Spell_list["Domination"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["stoneslipstream"] and Skills["Stone Slipstream"]["Level"] != "Not Learned":
                while "Stone Slipstream" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Stone Slipstream to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["stoneslipstream",""]:
                        print("Not a correct input")
                    if action in ["stoneslipstream"]:
                        Player_copy["Mana"] -= Spell_list["Stone Slipstream"]["Cost"]
                        Amount_Practiced["Stone Slipstream"] += 1
                        if Amount_Practiced["Stone Slipstream"] == 100:
                            Spell_list["Stone Slipstream"]["Level"] = "Rookie"
                            Spell_list["Stone Slipstream"]["Damage"] *= 1.1
                            Spell_list["Stone Slipstream"]["Cost"] *= 0.95
                            print("You improve your proficiency of Stone Slipstream to ",Spell_list["Stone Slipstream"]["Level"])
                        if Amount_Practiced["Stone Slipstream"] == 500:
                            Spell_list["Stone Slipstream"]["Level"] = "Competent"
                            Spell_list["Stone Slipstream"]["Damage"] = Skills["Stone Slipstream"]["Damage"] * 1.25
                            Spell_list["Stone Slipstream"]["Cost"] = Skills["Stone Slipstream"]["Cost"] * 0.9
                            print("You improve your proficiency of Stone Slipstream to ",Spell_list["Stone Slipstream"]["Level"])
                        if Amount_Practiced["Stone Slipstream"] == 1000:
                            Spell_list["Stone Slipstream"]["Level"] = "Proficient"
                            Spell_list["Stone Slipstream"]["Damage"] = Skills["Stone Slipstream"]["Damage"] * 1.45
                            Spell_list["Stone Slipstream"]["Cost"] = Skills["Stone Slipstream"]["Cost"] * 0.85
                            print("You improve your proficiency of Stone Slipstream to ",Spell_list["Stone Slipstream"]["Level"])
                        if Amount_Practiced["Stone Slipstream"] == 2500:
                            Spell_list["Stone Slipstream"]["Level"] = "Expert"
                            Spell_list["Stone Slipstream"]["Damage"] = Skills["Stone Slipstream"]["Damage"] * 1.7
                            Spell_list["Stone Slipstream"]["Cost"] = Skills["Stone Slipstream"]["Cost"] * 0.8
                            print("You improve your proficiency of Stone Slipstream to ",Spell_list["Stone Slipstream"]["Level"])
                        if Amount_Practiced["Stone Slipstream"] == 10000:
                            Spell_list["Stone Slipstream"]["Level"] = "Master"
                            Spell_list["Stone Slipstream"]["Damage"] = Skills["Stone Slipstream"]["Damage"] * 2
                            Spell_list["Stone Slipstream"]["Cost"] = Skills["Stone Slipstream"]["Cost"] * 0.7
                            print("You improve your proficiency of Stone Slipstream to ",Spell_list["Stone Slipstream"]["Level"])
                        Spell_list["Stone Slipstream"]["Damage"] = round(Spell_list["Stone Slipstream"]["Damage"])
                        Spell_list["Stone Slipstream"]["Cost"] = round(Spell_list["Stone Slipstream"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["corruptingtouch"] and Skills["Corrupting Touch"]["Level"] != "Not Learned":
                while "Corrupting Touch" not in Spell_list and Player_copy["Mana"] > 0:
                    print("\nEnter Corrupting Touch to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["corruptingtouch",""]:
                        print("Not a correct input")
                    if action in ["corruptingtouch"]:
                        Player_copy["Mana"] -= Spell_list["Corrupting Touch"]["Cost"]
                        Amount_Practiced["Corrupting Touch"] += 1
                        if Amount_Practiced["Corrupting Touch"] == 100:
                            Spell_list["Corrupting Touch"]["Level"] = "Rookie"
                            Spell_list["Corrupting Touch"]["Damage"] *= 1.1
                            Spell_list["Corrupting Touch"]["Cost"] *= 0.95
                            print("You improve your proficiency of Corrupting Touch to ",Spell_list["Corrupting Touch"]["Level"])
                        if Amount_Practiced["Corrupting Touch"] == 500:
                            Spell_list["Corrupting Touch"]["Level"] = "Competent"
                            Spell_list["Corrupting Touch"]["Damage"] = Skills["Corrupting Touch"]["Damage"] * 1.25
                            Spell_list["Corrupting Touch"]["Cost"] = Skills["Corrupting Touch"]["Cost"] * 0.9
                            print("You improve your proficiency of Corrupting Touch to ",Spell_list["Corrupting Touch"]["Level"])
                        if Amount_Practiced["Corrupting Touch"] == 1000:
                            Spell_list["Corrupting Touch"]["Level"] = "Proficient"
                            Spell_list["Corrupting Touch"]["Damage"] = Skills["Corrupting Touch"]["Damage"] * 1.45
                            Spell_list["Corrupting Touch"]["Cost"] = Skills["Corrupting Touch"]["Cost"] * 0.85
                            print("You improve your proficiency of Corrupting Touch to ",Spell_list["Corrupting Touch"]["Level"])
                        if Amount_Practiced["Corrupting Touch"] == 2500:
                            Spell_list["Corrupting Touch"]["Level"] = "Expert"
                            Spell_list["Corrupting Touch"]["Damage"] = Skills["Corrupting Touch"]["Damage"] * 1.7
                            Spell_list["Corrupting Touch"]["Cost"] = Skills["Corrupting Touch"]["Cost"] * 0.8
                            print("You improve your proficiency of Corrupting Touch to ",Spell_list["Corrupting Touch"]["Level"])
                        if Amount_Practiced["Corrupting Touch"] == 10000:
                            Spell_list["Corrupting Touch"]["Level"] = "Master"
                            Spell_list["Corrupting Touch"]["Damage"] = Skills["Corrupting Touch"]["Damage"] * 2
                            Spell_list["Corrupting Touch"]["Cost"] = Skills["Corrupting Touch"]["Cost"] * 0.7
                            print("You improve your proficiency of Corrupting Touch to ",Spell_list["Corrupting Touch"]["Level"])
                        Spell_list["Corrupting Touch"]["Damage"] = round(Spell_list["Corrupting Touch"]["Damage"])
                        Spell_list["Corrupting Touch"]["Cost"] = round(Spell_list["Corrupting Touch"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["impulsiveswing"] and Skills["Impulsive Swing"]["Level"] != "Not Learned":
                while "Impulsive Swing" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Impulsive Swing to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["impulsiveswing",""]:
                        print("Not a correct input")
                    if action in ["impulsiveswing"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Impulsive Swing"]["Cost"]
                        Amount_Practiced["Impulsive Swing"] += 1
                        if Amount_Practiced["Impulsive Swing"] == 100:
                            Spell_list["Impulsive Swing"]["Level"] = "Rookie"
                            Spell_list["Impulsive Swing"]["Damage"] *= 1.1
                            Spell_list["Impulsive Swing"]["Cost"] *= 0.95
                            print("You improve your proficiency of Impulsive Swing to ",Combat_Skill_list["Impulsive Swing"]["Level"])
                        if Amount_Practiced["Impulsive Swing"] == 500:
                            Spell_list["Impulsive Swing"]["Level"] = "Competent"
                            Spell_list["Impulsive Swing"]["Damage"] = Skills["Impulsive Swing"]["Damage"] * 1.25
                            Spell_list["Impulsive Swing"]["Cost"] = Skills["Impulsive Swing"]["Cost"] * 0.9
                            print("You improve your proficiency of Impulsive Swing to ",Combat_Skill_list["Impulsive Swing"]["Level"])
                        if Amount_Practiced["Impulsive Swing"] == 1000:
                            Spell_list["Impulsive Swing"]["Level"] = "Proficient"
                            Spell_list["Impulsive Swing"]["Damage"] = Skills["Impulsive Swing"]["Damage"] * 1.45
                            Spell_list["Impulsive Swing"]["Cost"] = Skills["Impulsive Swing"]["Cost"] * 0.85
                            print("You improve your proficiency of Impulsive Swing to ",Combat_Skill_list["Impulsive Swing"]["Level"])
                        if Amount_Practiced["Impulsive Swing"] == 2500:
                            Spell_list["Impulsive Swing"]["Level"] = "Expert"
                            Spell_list["Impulsive Swing"]["Damage"] = Skills["Impulsive Swing"]["Damage"] * 1.7
                            Spell_list["Impulsive Swing"]["Cost"] = Skills["Impulsive Swing"]["Cost"] * 0.8
                            print("You improve your proficiency of Impulsive Swing to ",Combat_Skill_list["Impulsive Swing"]["Level"])
                        if Amount_Practiced["Impulsive Swing"] == 10000:
                            Spell_list["Impulsive Swing"]["Level"] = "Master"
                            Spell_list["Impulsive Swing"]["Damage"] = Skills["Impulsive Swing"]["Damage"] * 2
                            Spell_list["Impulsive Swing"]["Cost"] = Skills["Impulsive Swing"]["Cost"] * 0.7
                            print("You improve your proficiency of Impulsive Swing to ",Combat_Skill_list["Impulsive Swing"]["Level"])
                        Combat_Skill_list["Impulsive Swing"]["Damage"] = round(Combat_Skill_list["Impulsive Swing"]["Damage"])
                        Combat_Skill_list["Impulsive Swing"]["Cost"] = round(Combat_Skill_list["Impulsive Swing"]["Cost"])
                    elif action in [""]:
                        break
                        
            elif Choice in ["jab"] and Skills["Jab"]["Level"] != "Not Learned":
                while "Jab" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Jab to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["jab",""]:
                        print("Not a correct input")
                    if action in ["jab"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Jab"]["Cost"]
                        Amount_Practiced["Jab"] += 1
                        if Amount_Practiced["Jab"] == 100:
                            Spell_list["Jab"]["Level"] = "Rookie"
                            Spell_list["Jab"]["Damage"] *= 1.1
                            Spell_list["Jab"]["Cost"] *= 0.95
                            print("You improve your proficiency of Jab to ",Combat_Skill_list["Jab"]["Level"])
                        if Amount_Practiced["Jab"] == 500:
                            Spell_list["Jab"]["Level"] = "Competent"
                            Spell_list["Jab"]["Damage"] = Skills["Jab"]["Damage"] * 1.25
                            Spell_list["Jab"]["Cost"] = Skills["Jab"]["Cost"] * 0.9
                            print("You improve your proficiency of Jab to ",Combat_Skill_list["Jab"]["Level"])
                        if Amount_Practiced["Jab"] == 1000:
                            Spell_list["Jab"]["Level"] = "Proficient"
                            Spell_list["Jab"]["Damage"] = Skills["Jab"]["Damage"] * 1.45
                            Spell_list["Jab"]["Cost"] = Skills["Jab"]["Cost"] * 0.85
                            print("You improve your proficiency of Jab to ",Combat_Skill_list["Jab"]["Level"])
                        if Amount_Practiced["Jab"] == 2500:
                            Spell_list["Jab"]["Level"] = "Expert"
                            Spell_list["Jab"]["Damage"] = Skills["Jab"]["Damage"] * 1.7
                            Spell_list["Jab"]["Cost"] = Skills["Jab"]["Cost"] * 0.8
                            print("You improve your proficiency of Jab to ",Combat_Skill_list["Jab"]["Level"])
                        if Amount_Practiced["Jab"] == 10000:
                            Spell_list["Jab"]["Level"] = "Master"
                            Spell_list["Jab"]["Damage"] = Skills["Jab"]["Damage"] * 2
                            Spell_list["Jab"]["Cost"] = Skills["Jab"]["Cost"] * 0.7
                            print("You improve your proficiency of Jab to ",Combat_Skill_list["Jab"]["Level"])
                        Combat_Skill_list["Jab"]["Damage"] = round(Combat_Skill_list["Jab"]["Damage"])
                        Combat_Skill_list["Jab"]["Cost"] = round(Combat_Skill_list["Jab"]["Cost"])
                    elif action in [""]:
                        break



            elif Choice in ["tremor"] and Skills["Tremor"]["Level"] != "Not Learned":
                while "Tremor" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Tremor to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["tremor",""]:
                        print("Not a correct input")
                    if action in ["tremor"]:
                        Player_copy["Stamina"] -= Spell_list["Tremor"]["Cost"]
                        Amount_Practiced["Tremor"] += 1
                        if Amount_Practiced["Tremor"] == 100:
                            Spell_list["Tremor"]["Level"] = "Rookie"
                            Spell_list["Tremor"]["Damage"] *= 1.1
                            Spell_list["Tremor"]["Cost"] *= 0.95
                            print("You improve your proficiency of Tremor to ",Spell_list["Tremor"]["Level"])
                        if Amount_Practiced["Tremor"] == 500:
                            Spell_list["Tremor"]["Level"] = "Competent"
                            Spell_list["Tremor"]["Damage"] = Skills["Tremor"]["Damage"] * 1.25
                            Spell_list["Tremor"]["Cost"] = Skills["Tremor"]["Cost"] * 0.9
                            print("You improve your proficiency of Tremor to ",Spell_list["Tremor"]["Level"])
                        if Amount_Practiced["Tremor"] == 1000:
                            Spell_list["Tremor"]["Level"] = "Proficient"
                            Spell_list["Tremor"]["Damage"] = Skills["Tremor"]["Damage"] * 1.45
                            Spell_list["Tremor"]["Cost"] = Skills["Tremor"]["Cost"] * 0.85
                            print("You improve your proficiency of Tremor to ",Spell_list["Tremor"]["Level"])
                        if Amount_Practiced["Tremor"] == 2500:
                            Spell_list["Tremor"]["Level"] = "Expert"
                            Spell_list["Tremor"]["Damage"] = Skills["Tremor"]["Damage"] * 1.7
                            Spell_list["Tremor"]["Cost"] = Skills["Tremor"]["Cost"] * 0.8
                            print("You improve your proficiency of Tremor to ",Spell_list["Tremor"]["Level"])
                        if Amount_Practiced["Tremor"] == 10000:
                            Spell_list["Tremor"]["Level"] = "Master"
                            Spell_list["Tremor"]["Damage"] = Skills["Tremor"]["Damage"] * 2
                            Spell_list["Tremor"]["Cost"] = Skills["Tremor"]["Cost"] * 0.7
                            print("You improve your proficiency of Tremor to ",Spell_list["Tremor"]["Level"])
                        Spell_list["Tremor"]["Damage"] = round(Spell_list["Tremor"]["Damage"])
                        Spell_list["Tremor"]["Cost"] = round(Spell_list["Tremor"]["Cost"])
                    elif action in [""]:
                        break
            
            elif Choice in ["groundbreaker"] and Skills["Groundbreaker"]["Level"] != "Not Learned":
                while "Groundbreaker" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Groundbreaker to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["groundbreaker",""]:
                        print("Not a correct input")
                    if action in ["groundbreaker"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Groundbreaker"]["Cost"]
                        Amount_Practiced["Groundbreaker"] += 1
                        if Amount_Practiced["Groundbreaker"] == 100:
                            Spell_list["Groundbreaker"]["Level"] = "Rookie"
                            Spell_list["Groundbreaker"]["Damage"] *= 1.1
                            Spell_list["Groundbreaker"]["Cost"] *= 0.95
                            print("You improve your proficiency of Groundbreaker to ",Combat_Skill_list["Groundbreaker"]["Level"])
                        if Amount_Practiced["Groundbreaker"] == 500:
                            Spell_list["Groundbreaker"]["Level"] = "Competent"
                            Spell_list["Groundbreaker"]["Damage"] = Skills["Groundbreaker"]["Damage"] * 1.25
                            Spell_list["Groundbreaker"]["Cost"] = Skills["Groundbreaker"]["Cost"] * 0.9
                            print("You improve your proficiency of Groundbreaker to ",Combat_Skill_list["Groundbreaker"]["Level"])
                        if Amount_Practiced["Groundbreaker"] == 1000:
                            Spell_list["Groundbreaker"]["Level"] = "Proficient"
                            Spell_list["Groundbreaker"]["Damage"] = Skills["Groundbreaker"]["Damage"] * 1.45
                            Spell_list["Groundbreaker"]["Cost"] = Skills["Groundbreaker"]["Cost"] * 0.85
                            print("You improve your proficiency of Groundbreaker to ",Combat_Skill_list["Groundbreaker"]["Level"])
                        if Amount_Practiced["Groundbreaker"] == 2500:
                            Spell_list["Groundbreaker"]["Level"] = "Expert"
                            Spell_list["Groundbreaker"]["Damage"] = Skills["Groundbreaker"]["Damage"] * 1.7
                            Spell_list["Groundbreaker"]["Cost"] = Skills["Groundbreaker"]["Cost"] * 0.8
                            print("You improve your proficiency of Groundbreaker to ",Combat_Skill_list["Groundbreaker"]["Level"])
                        if Amount_Practiced["Groundbreaker"] == 10000:
                            Spell_list["Groundbreaker"]["Level"] = "Master"
                            Spell_list["Groundbreaker"]["Damage"] = Skills["Groundbreaker"]["Damage"] * 2
                            Spell_list["Groundbreaker"]["Cost"] = Skills["Groundbreaker"]["Cost"] * 0.7
                            print("You improve your proficiency of Groundbreaker to ",Combat_Skill_list["Groundbreaker"]["Level"])
                        Combat_Skill_list["Groundbreaker"]["Damage"] = round(Combat_Skill_list["Groundbreaker"]["Damage"])
                        Combat_Skill_list["Groundbreaker"]["Cost"] = round(Combat_Skill_list["Groundbreaker"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["devouressence"] and Skills["Devour Essence"]["Level"] != "Not Learned":
                while "Devour Essence" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Devour Essence to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["devouressence",""]:
                        print("Not a correct input")
                    if action in ["devouressence"]:
                        Player_copy["Stamina"] -= Spell_list["Devour Essence"]["Cost"]
                        Amount_Practiced["Devour Essence"] += 1
                        if Amount_Practiced["Devour Essence"] == 100:
                            Spell_list["Devour Essence"]["Level"] = "Rookie"
                            Spell_list["Devour Essence"]["Damage"] *= 1.1
                            Spell_list["Devour Essence"]["Cost"] *= 0.95
                            print("You improve your proficiency of Devour Essence to ",Spell_list["Devour Essence"]["Level"])
                        if Amount_Practiced["Devour Essence"] == 500:
                            Spell_list["Devour Essence"]["Level"] = "Competent"
                            Spell_list["Devour Essence"]["Damage"] = Skills["Devour Essence"]["Damage"] * 1.25
                            Spell_list["Devour Essence"]["Cost"] = Skills["Devour Essence"]["Cost"] * 0.9
                            print("You improve your proficiency of Devour Essence to ",Spell_list["Devour Essence"]["Level"])
                        if Amount_Practiced["Devour Essence"] == 1000:
                            Spell_list["Devour Essence"]["Level"] = "Proficient"
                            Spell_list["Devour Essence"]["Damage"] = Skills["Devour Essence"]["Damage"] * 1.45
                            Spell_list["Devour Essence"]["Cost"] = Skills["Devour Essence"]["Cost"] * 0.85
                            print("You improve your proficiency of Devour Essence to ",Spell_list["Devour Essence"]["Level"])
                        if Amount_Practiced["Devour Essence"] == 2500:
                            Spell_list["Devour Essence"]["Level"] = "Expert"
                            Spell_list["Devour Essence"]["Damage"] = Skills["Devour Essence"]["Damage"] * 1.7
                            Spell_list["Devour Essence"]["Cost"] = Skills["Devour Essence"]["Cost"] * 0.8
                            print("You improve your proficiency of Devour Essence to ",Spell_list["Devour Essence"]["Level"])
                        if Amount_Practiced["Devour Essence"] == 10000:
                            Spell_list["Devour Essence"]["Level"] = "Master"
                            Spell_list["Devour Essence"]["Damage"] = Skills["Devour Essence"]["Damage"] * 2
                            Spell_list["Devour Essence"]["Cost"] = Skills["Devour Essence"]["Cost"] * 0.7
                            print("You improve your proficiency of Devour Essence to ",Spell_list["Devour Essence"]["Level"])
                        Spell_list["Devour Essence"]["Damage"] = round(Spell_list["Devour Essence"]["Damage"])
                        Spell_list["Devour Essence"]["Cost"] = round(Spell_list["Devour Essence"]["Cost"])
                    elif action in [""]:
                        break
                        
            elif Choice in ["empower"] and Skills["Empower"]["Level"] != "Not Learned":
                while "Empower" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Empower to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["empower",""]:
                        print("Not a correct input")
                    if action in ["empower"]:
                        Player_copy["Stamina"] -= Spell_list["Empower"]["Cost"]
                        Amount_Practiced["Empower"] += 1
                        if Amount_Practiced["Empower"] == 100:
                            Spell_list["Empower"]["Level"] = "Rookie"
                            Spell_list["Empower"]["Damage"] *= 1.1
                            Spell_list["Empower"]["Cost"] *= 0.95
                            print("You improve your proficiency of Empower to ",Spell_list["Empower"]["Level"])
                        if Amount_Practiced["Empower"] == 500:
                            Spell_list["Empower"]["Level"] = "Competent"
                            Spell_list["Empower"]["Damage"] = Skills["Empower"]["Damage"] * 1.25
                            Spell_list["Empower"]["Cost"] = Skills["Empower"]["Cost"] * 0.9
                            print("You improve your proficiency of Empower to ",Spell_list["Empower"]["Level"])
                        if Amount_Practiced["Empower"] == 1000:
                            Spell_list["Empower"]["Level"] = "Proficient"
                            Spell_list["Empower"]["Damage"] = Skills["Empower"]["Damage"] * 1.45
                            Spell_list["Empower"]["Cost"] = Skills["Empower"]["Cost"] * 0.85
                            print("You improve your proficiency of Empower to ",Spell_list["Empower"]["Level"])
                        if Amount_Practiced["Empower"] == 2500:
                            Spell_list["Empower"]["Level"] = "Expert"
                            Spell_list["Empower"]["Damage"] = Skills["Empower"]["Damage"] * 1.7
                            Spell_list["Empower"]["Cost"] = Skills["Empower"]["Cost"] * 0.8
                            print("You improve your proficiency of Empower to ",Spell_list["Empower"]["Level"])
                        if Amount_Practiced["Empower"] == 10000:
                            Spell_list["Empower"]["Level"] = "Master"
                            Spell_list["Empower"]["Damage"] = Skills["Empower"]["Damage"] * 2
                            Spell_list["Empower"]["Cost"] = Skills["Empower"]["Cost"] * 0.7
                            print("You improve your proficiency of Empower to ",Spell_list["Empower"]["Level"])
                        Spell_list["Empower"]["Damage"] = round(Spell_list["Empower"]["Damage"])
                        Spell_list["Empower"]["Cost"] = round(Spell_list["Empower"]["Cost"])
                    elif action in [""]:
                        break
                        
            elif Choice in ["toxinspray"] and Skills["Toxin Spray"]["Level"] != "Not Learned":
                while "Toxin Spray" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Toxin Spray to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["toxinspray",""]:
                        print("Not a correct input")
                    if action in ["toxinspray"]:
                        Player_copy["Stamina"] -= Spell_list["Toxin Spray"]["Cost"]
                        Amount_Practiced["Toxin Spray"] += 1
                        if Amount_Practiced["Toxin Spray"] == 100:
                            Spell_list["Toxin Spray"]["Level"] = "Rookie"
                            Spell_list["Toxin Spray"]["Damage"] *= 1.1
                            Spell_list["Toxin Spray"]["Cost"] *= 0.95
                            print("You improve your proficiency of Toxin Spray to ",Spell_list["Toxin Spray"]["Level"])
                        if Amount_Practiced["Toxin Spray"] == 500:
                            Spell_list["Toxin Spray"]["Level"] = "Competent"
                            Spell_list["Toxin Spray"]["Damage"] = Skills["Toxin Spray"]["Damage"] * 1.25
                            Spell_list["Toxin Spray"]["Cost"] = Skills["Toxin Spray"]["Cost"] * 0.9
                            print("You improve your proficiency of Toxin Spray to ",Spell_list["Toxin Spray"]["Level"])
                        if Amount_Practiced["Toxin Spray"] == 1000:
                            Spell_list["Toxin Spray"]["Level"] = "Proficient"
                            Spell_list["Toxin Spray"]["Damage"] = Skills["Toxin Spray"]["Damage"] * 1.45
                            Spell_list["Toxin Spray"]["Cost"] = Skills["Toxin Spray"]["Cost"] * 0.85
                            print("You improve your proficiency of Toxin Spray to ",Spell_list["Toxin Spray"]["Level"])
                        if Amount_Practiced["Toxin Spray"] == 2500:
                            Spell_list["Toxin Spray"]["Level"] = "Expert"
                            Spell_list["Toxin Spray"]["Damage"] = Skills["Toxin Spray"]["Damage"] * 1.7
                            Spell_list["Toxin Spray"]["Cost"] = Skills["Toxin Spray"]["Cost"] * 0.8
                            print("You improve your proficiency of Toxin Spray to ",Spell_list["Toxin Spray"]["Level"])
                        if Amount_Practiced["Toxin Spray"] == 10000:
                            Spell_list["Toxin Spray"]["Level"] = "Master"
                            Spell_list["Toxin Spray"]["Damage"] = Skills["Toxin Spray"]["Damage"] * 2
                            Spell_list["Toxin Spray"]["Cost"] = Skills["Toxin Spray"]["Cost"] * 0.7
                            print("You improve your proficiency of Toxin Spray to ",Spell_list["Toxin Spray"]["Level"])
                        Spell_list["Toxin Spray"]["Damage"] = round(Spell_list["Toxin Spray"]["Damage"])
                        Spell_list["Toxin Spray"]["Cost"] = round(Spell_list["Toxin Spray"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["straightpunch"] and Skills["Straight Punch"]["Level"] != "Not Learned":
                while "Straight Punch" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Straight Punch to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["straightpunch",""]:
                        print("Not a correct input")
                    if action in ["straightpunch"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Straight Punch"]["Cost"]
                        Amount_Practiced["Straight Punch"] += 1
                        if Amount_Practiced["Straight Punch"] == 100:
                            Spell_list["Straight Punch"]["Level"] = "Rookie"
                            Spell_list["Straight Punch"]["Damage"] *= 1.1
                            Spell_list["Straight Punch"]["Cost"] *= 0.95
                            print("You improve your proficiency of Straight Punch to ",Combat_Skill_list["Straight Punch"]["Level"])
                        if Amount_Practiced["Straight Punch"] == 500:
                            Spell_list["Straight Punch"]["Level"] = "Competent"
                            Spell_list["Straight Punch"]["Damage"] = Skills["Straight Punch"]["Damage"] * 1.25
                            Spell_list["Straight Punch"]["Cost"] = Skills["Straight Punch"]["Cost"] * 0.9
                            print("You improve your proficiency of Straight Punch to ",Combat_Skill_list["Straight Punch"]["Level"])
                        if Amount_Practiced["Straight Punch"] == 1000:
                            Spell_list["Straight Punch"]["Level"] = "Proficient"
                            Spell_list["Straight Punch"]["Damage"] = Skills["Straight Punch"]["Damage"] * 1.45
                            Spell_list["Straight Punch"]["Cost"] = Skills["Straight Punch"]["Cost"] * 0.85
                            print("You improve your proficiency of Straight Punch to ",Combat_Skill_list["Straight Punch"]["Level"])
                        if Amount_Practiced["Straight Punch"] == 2500:
                            Spell_list["Straight Punch"]["Level"] = "Expert"
                            Spell_list["Straight Punch"]["Damage"] = Skills["Straight Punch"]["Damage"] * 1.7
                            Spell_list["Straight Punch"]["Cost"] = Skills["Straight Punch"]["Cost"] * 0.8
                            print("You improve your proficiency of Straight Punch to ",Combat_Skill_list["Straight Punch"]["Level"])
                        if Amount_Practiced["Straight Punch"] == 10000:
                            Spell_list["Straight Punch"]["Level"] = "Master"
                            Spell_list["Straight Punch"]["Damage"] = Skills["Straight Punch"]["Damage"] * 2
                            Spell_list["Straight Punch"]["Cost"] = Skills["Straight Punch"]["Cost"] * 0.7
                            print("You improve your proficiency of Straight Punch to ",Combat_Skill_list["Straight Punch"]["Level"])
                        Combat_Skill_list["Straight Punch"]["Damage"] = round(Combat_Skill_list["Straight Punch"]["Damage"])
                        Combat_Skill_list["Straight Punch"]["Cost"] = round(Combat_Skill_list["Straight Punch"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["frontkick"] and Skills["Front Kick"]["Level"] != "Not Learned":
                while "Front Kick" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Front Kick to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["frontkick",""]:
                        print("Not a correct input")
                    if action in ["frontkick"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Front Kick"]["Cost"]
                        Amount_Practiced["Front Kick"] += 1
                        if Amount_Practiced["Front Kick"] == 100:
                            Spell_list["Front Kick"]["Level"] = "Rookie"
                            Spell_list["Front Kick"]["Damage"] *= 1.1
                            Spell_list["Front Kick"]["Cost"] *= 0.95
                            print("You improve your proficiency of Front Kick to ",Combat_Skill_list["Front Kick"]["Level"])
                        if Amount_Practiced["Front Kick"] == 500:
                            Spell_list["Front Kick"]["Level"] = "Competent"
                            Spell_list["Front Kick"]["Damage"] = Skills["Front Kick"]["Damage"] * 1.25
                            Spell_list["Front Kick"]["Cost"] = Skills["Front Kick"]["Cost"] * 0.9
                            print("You improve your proficiency of Front Kick to ",Combat_Skill_list["Front Kick"]["Level"])
                        if Amount_Practiced["Front Kick"] == 1000:
                            Spell_list["Front Kick"]["Level"] = "Proficient"
                            Spell_list["Front Kick"]["Damage"] = Skills["Front Kick"]["Damage"] * 1.45
                            Spell_list["Front Kick"]["Cost"] = Skills["Front Kick"]["Cost"] * 0.85
                            print("You improve your proficiency of Front Kick to ",Combat_Skill_list["Front Kick"]["Level"])
                        if Amount_Practiced["Front Kick"] == 2500:
                            Spell_list["Front Kick"]["Level"] = "Expert"
                            Spell_list["Front Kick"]["Damage"] = Skills["Front Kick"]["Damage"] * 1.7
                            Spell_list["Front Kick"]["Cost"] = Skills["Front Kick"]["Cost"] * 0.8
                            print("You improve your proficiency of Front Kick to ",Combat_Skill_list["Front Kick"]["Level"])
                        if Amount_Practiced["Front Kick"] == 10000:
                            Spell_list["Front Kick"]["Level"] = "Master"
                            Spell_list["Front Kick"]["Damage"] = Skills["Front Kick"]["Damage"] * 2
                            Spell_list["Front Kick"]["Cost"] = Skills["Front Kick"]["Cost"] * 0.7
                            print("You improve your proficiency of Front Kick to ",Combat_Skill_list["Front Kick"]["Level"])
                        Combat_Skill_list["Front Kick"]["Damage"] = round(Combat_Skill_list["Front Kick"]["Damage"])
                        Combat_Skill_list["Front Kick"]["Cost"] = round(Combat_Skill_list["Front Kick"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["quickstab"] and Skills["Quick Stab"]["Level"] != "Not Learned":
                while "Quick Stab" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Quick Stab to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["quickstab",""]:
                        print("Not a correct input")
                    if action in ["quickstab"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Quick Stab"]["Cost"]
                        Amount_Practiced["Quick Stab"] += 1
                        if Amount_Practiced["Quick Stab"] == 100:
                            Spell_list["Quick Stab"]["Level"] = "Rookie"
                            Spell_list["Quick Stab"]["Damage"] *= 1.1
                            Spell_list["Quick Stab"]["Cost"] *= 0.95
                            print("You improve your proficiency of Quick Stab to ",Combat_Skill_list["Quick Stab"]["Level"])
                        if Amount_Practiced["Quick Stab"] == 500:
                            Spell_list["Quick Stab"]["Level"] = "Competent"
                            Spell_list["Quick Stab"]["Damage"] = Skills["Quick Stab"]["Damage"] * 1.25
                            Spell_list["Quick Stab"]["Cost"] = Skills["Quick Stab"]["Cost"] * 0.9
                            print("You improve your proficiency of Quick Stab to ",Combat_Skill_list["Quick Stab"]["Level"])
                        if Amount_Practiced["Quick Stab"] == 1000:
                            Spell_list["Quick Stab"]["Level"] = "Proficient"
                            Spell_list["Quick Stab"]["Damage"] = Skills["Quick Stab"]["Damage"] * 1.45
                            Spell_list["Quick Stab"]["Cost"] = Skills["Quick Stab"]["Cost"] * 0.85
                            print("You improve your proficiency of Quick Stab to ",Combat_Skill_list["Quick Stab"]["Level"])
                        if Amount_Practiced["Quick Stab"] == 2500:
                            Spell_list["Quick Stab"]["Level"] = "Expert"
                            Spell_list["Quick Stab"]["Damage"] = Skills["Quick Stab"]["Damage"] * 1.7
                            Spell_list["Quick Stab"]["Cost"] = Skills["Quick Stab"]["Cost"] * 0.8
                            print("You improve your proficiency of Quick Stab to ",Combat_Skill_list["Quick Stab"]["Level"])
                        if Amount_Practiced["Quick Stab"] == 10000:
                            Spell_list["Quick Stab"]["Level"] = "Master"
                            Spell_list["Quick Stab"]["Damage"] = Skills["Quick Stab"]["Damage"] * 2
                            Spell_list["Quick Stab"]["Cost"] = Skills["Quick Stab"]["Cost"] * 0.7
                            print("You improve your proficiency of Quick Stab to ",Combat_Skill_list["Quick Stab"]["Level"])
                        Combat_Skill_list["Quick Stab"]["Damage"] = round(Combat_Skill_list["Quick Stab"]["Damage"])
                        Combat_Skill_list["Quick Stab"]["Cost"] = round(Combat_Skill_list["Quick Stab"]["Cost"])
                    elif action in [""]:
                        break

            elif Choice in ["slash"] and Skills["Slash"]["Level"] != "Not Learned":
                while "Slash" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Slash to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["slash",""]:
                        print("Not a correct input")
                    if action in ["slash"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Slash"]["Cost"]
                        Amount_Practiced["Slash"] += 1
                        if Amount_Practiced["Slash"] == 100:
                            Spell_list["Slash"]["Level"] = "Rookie"
                            Spell_list["Slash"]["Damage"] *= 1.1
                            Spell_list["Slash"]["Cost"] *= 0.95
                            print("You improve your proficiency of Slash to ",Combat_Skill_list["Slash"]["Level"])
                        if Amount_Practiced["Slash"] == 500:
                            Spell_list["Slash"]["Level"] = "Competent"
                            Spell_list["Slash"]["Damage"] = Skills["Slash"]["Damage"] * 1.25
                            Spell_list["Slash"]["Cost"] = Skills["Slash"]["Cost"] * 0.9
                            print("You improve your proficiency of Slash to ",Combat_Skill_list["Slash"]["Level"])
                        if Amount_Practiced["Slash"] == 1000:
                            Spell_list["Slash"]["Level"] = "Proficient"
                            Spell_list["Slash"]["Damage"] = Skills["Slash"]["Damage"] * 1.45
                            Spell_list["Slash"]["Cost"] = Skills["Slash"]["Cost"] * 0.85
                            print("You improve your proficiency of Slash to ",Combat_Skill_list["Slash"]["Level"])
                        if Amount_Practiced["Slash"] == 2500:
                            Spell_list["Slash"]["Level"] = "Expert"
                            Spell_list["Slash"]["Damage"] = Skills["Slash"]["Damage"] * 1.7
                            Spell_list["Slash"]["Cost"] = Skills["Slash"]["Cost"] * 0.8
                            print("You improve your proficiency of Slash to ",Combat_Skill_list["Slash"]["Level"])
                        if Amount_Practiced["Slash"] == 10000:
                            Spell_list["Slash"]["Level"] = "Master"
                            Spell_list["Slash"]["Damage"] = Skills["Slash"]["Damage"] * 2
                            Spell_list["Slash"]["Cost"] = Skills["Slash"]["Cost"] * 0.7
                            print("You improve your proficiency of Slash to ",Combat_Skill_list["Slash"]["Level"])
                        Combat_Skill_list["Slash"]["Damage"] = round(Combat_Skill_list["Slash"]["Damage"])
                        Combat_Skill_list["Slash"]["Cost"] = round(Combat_Skill_list["Slash"]["Cost"])
                    elif action in [""]:
                        break
                        
            elif Choice in ["bite"] and Skills["Bite"]["Level"] != "Not Learned":
                while "Bite" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Bite to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["bite",""]:
                        print("Not a correct input")
                    if action in ["bite"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Bite"]["Cost"]
                        Amount_Practiced["Bite"] += 1
                        if Amount_Practiced["Bite"] == 100:
                            Spell_list["Bite"]["Level"] = "Rookie"
                            Spell_list["Bite"]["Damage"] *= 1.1
                            Spell_list["Bite"]["Cost"] *= 0.95
                            print("You improve your proficiency of Bite to ",Combat_Skill_list["Bite"]["Level"])
                        if Amount_Practiced["Bite"] == 500:
                            Spell_list["Bite"]["Level"] = "Competent"
                            Spell_list["Bite"]["Damage"] = Skills["Bite"]["Damage"] * 1.25
                            Spell_list["Bite"]["Cost"] = Skills["Bite"]["Cost"] * 0.9
                            print("You improve your proficiency of Bite to ",Combat_Skill_list["Bite"]["Level"])
                        if Amount_Practiced["Bite"] == 1000:
                            Spell_list["Bite"]["Level"] = "Proficient"
                            Spell_list["Bite"]["Damage"] = Skills["Bite"]["Damage"] * 1.45
                            Spell_list["Bite"]["Cost"] = Skills["Bite"]["Cost"] * 0.85
                            print("You improve your proficiency of Bite to ",Combat_Skill_list["Bite"]["Level"])
                        if Amount_Practiced["Bite"] == 2500:
                            Spell_list["Bite"]["Level"] = "Expert"
                            Spell_list["Bite"]["Damage"] = Skills["Bite"]["Damage"] * 1.7
                            Spell_list["Bite"]["Cost"] = Skills["Bite"]["Cost"] * 0.8
                            print("You improve your proficiency of Bite to ",Combat_Skill_list["Bite"]["Level"])
                        if Amount_Practiced["Bite"] == 10000:
                            Spell_list["Bite"]["Level"] = "Master"
                            Spell_list["Bite"]["Damage"] = Skills["Bite"]["Damage"] * 2
                            Spell_list["Bite"]["Cost"] = Skills["Bite"]["Cost"] * 0.7
                            print("You improve your proficiency of Bite to ",Combat_Skill_list["Bite"]["Level"])
                        Combat_Skill_list["Bite"]["Damage"] = round(Combat_Skill_list["Bite"]["Damage"])
                        Combat_Skill_list["Bite"]["Cost"] = round(Combat_Skill_list["Bite"]["Cost"])
                    elif action in [""]:
                        break
                        
            elif Choice in ["manablast"] and Skills["Mana Blast"]["Level"] != "Not Learned":
                while "Mana Blast" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Mana Blast to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["manablast",""]:
                        print("Not a correct input")
                    if action in ["manablast"]:
                        Player_copy["Mana"] -= Spell_list["Mana Blast"]["Cost"]
                        Amount_Practiced["Mana Blast"] += 1
                        if Amount_Practiced["Mana Blast"] == 100:
                            Spell_list["Mana Blast"]["Level"] = "Rookie"
                            Spell_list["Mana Blast"]["Damage"] *= 1.1
                            Spell_list["Mana Blast"]["Cost"] *= 0.95
                            print("You improve your proficiency of Mana Blast to ",Spell_list["Mana Blast"]["Level"])
                        if Amount_Practiced["Mana Blast"] == 500:
                            Spell_list["Mana Blast"]["Level"] = "Competent"
                            Spell_list["Mana Blast"]["Damage"] = Skills["Mana Blast"]["Damage"] * 1.25
                            Spell_list["Mana Blast"]["Cost"] = Skills["Mana Blast"]["Cost"] * 0.9
                            print("You improve your proficiency of Mana Blast to ",Spell_list["Mana Blast"]["Level"])
                        if Amount_Practiced["Mana Blast"] == 1000:
                            Spell_list["Mana Blast"]["Level"] = "Proficient"
                            Spell_list["Mana Blast"]["Damage"] = Skills["Mana Blast"]["Damage"] * 1.45
                            Spell_list["Mana Blast"]["Cost"] = Skills["Mana Blast"]["Cost"] * 0.85
                            print("You improve your proficiency of Mana Blast to ",Spell_list["Mana Blast"]["Level"])
                        if Amount_Practiced["Mana Blast"] == 2500:
                            Spell_list["Mana Blast"]["Level"] = "Expert"
                            Spell_list["Mana Blast"]["Damage"] = Skills["Mana Blast"]["Damage"] * 1.7
                            Spell_list["Mana Blast"]["Cost"] = Skills["Mana Blast"]["Cost"] * 0.8
                            print("You improve your proficiency of Mana Blast to ",Spell_list["Mana Blast"]["Level"])
                        if Amount_Practiced["Mana Blast"] == 10000:
                            Spell_list["Mana Blast"]["Level"] = "Master"
                            Spell_list["Mana Blast"]["Damage"] = Skills["Mana Blast"]["Damage"] * 2
                            Spell_list["Mana Blast"]["Cost"] = Skills["Mana Blast"]["Cost"] * 0.7
                            print("You improve your proficiency of Mana Blast to ",Spell_list["Mana Blast"]["Level"])
                        Spell_list["Mana Blast"]["Damage"] = round(Spell_list["Mana Blast"]["Damage"])
                        Spell_list["Mana Blast"]["Cost"] = round(Spell_list["Mana Blast"]["Cost"])
                    elif action in [""]:
                        break


            elif Choice in ["tackle"] and Skills["Tackle"]["Level"] != "Not Learned":
                while "Tackle" not in Combat_Skill_list and Player_copy["Stamina"] > 0:
                    print("\nEnter Tackle to practice the move\n\nPress enter to go back\n")
                    action = input("").lower()
                    action = "".join(action.split())
                    if action not in ["tackle",""]:
                        print("Not a correct input")
                    if action in ["tackle"]:
                        Player_copy["Stamina"] -= Combat_Skill_list["Tackle"]["Cost"]
                        Amount_Practiced["Tackle"] += 1
                        if Amount_Practiced["Tackle"] == 100:
                            Spell_list["Tackle"]["Level"] = "Rookie"
                            Spell_list["Tackle"]["Damage"] *= 1.1
                            Spell_list["Tackle"]["Cost"] *= 0.95
                            print("You improve your proficiency of Tackle to ",Combat_Skill_list["Tackle"]["Level"])
                        if Amount_Practiced["Tackle"] == 500:
                            Spell_list["Tackle"]["Level"] = "Competent"
                            Spell_list["Tackle"]["Damage"] = Skills["Tackle"]["Damage"] * 1.25
                            Spell_list["Tackle"]["Cost"] = Skills["Tackle"]["Cost"] * 0.9
                            print("You improve your proficiency of Tackle to ",Combat_Skill_list["Tackle"]["Level"])
                        if Amount_Practiced["Tackle"] == 1000:
                            Spell_list["Tackle"]["Level"] = "Proficient"
                            Spell_list["Tackle"]["Damage"] = Skills["Tackle"]["Damage"] * 1.45
                            Spell_list["Tackle"]["Cost"] = Skills["Tackle"]["Cost"] * 0.85
                            print("You improve your proficiency of Tackle to ",Combat_Skill_list["Tackle"]["Level"])
                        if Amount_Practiced["Tackle"] == 2500:
                            Spell_list["Tackle"]["Level"] = "Expert"
                            Spell_list["Tackle"]["Damage"] = Skills["Tackle"]["Damage"] * 1.7
                            Spell_list["Tackle"]["Cost"] = Skills["Tackle"]["Cost"] * 0.8
                            print("You improve your proficiency of Tackle to ",Combat_Skill_list["Tackle"]["Level"])
                        if Amount_Practiced["Tackle"] == 10000:
                            Spell_list["Tackle"]["Level"] = "Master"
                            Spell_list["Tackle"]["Damage"] = Skills["Tackle"]["Damage"] * 2
                            Spell_list["Tackle"]["Cost"] = Skills["Tackle"]["Cost"] * 0.7
                            print("You improve your proficiency of Tackle to ",Combat_Skill_list["Tackle"]["Level"])
                        Combat_Skill_list["Tackle"]["Damage"] = round(Combat_Skill_list["Tackle"]["Damage"])
                        Combat_Skill_list["Tackle"]["Cost"] = round(Combat_Skill_list["Tackle"]["Cost"])
                    elif action in [""]:
                        break
                
            else:
                print("You have already learnt this skill")

            if Player_copy["Mana"] < 0 or Player_copy["Stamina"] < 0:
                print("\nYou are Exhausted.\n\n")
                print("     Wait 1 Minute.\n")
                time.sleep(60)




        elif Choice in ["market","m","2"]:
            print("\n Welcome to the market! \n\n Which merchant would you like to visit?\n\n1. Book Merchant\n\n2. Gear Merchant")

            option = input("")


            if option in ["bookmerchant","bm","b","1"]:
                print("Do you want to purchase a chest for 1000 Gold?\n\n * This will give you a random skill book")
                if Player["Gold"] >= 1000:
                    Player["Gold"] -= 1000
                    Statistics["Gold Spent"] += 1000
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


            if option in ["gearmerchant","2","gm","g"]:
                found = False
                print("\nWhat type of gear do you want to buy?\n\n1. Helmet\n2. Shoulderwear\n3. Chestplate\n4. Armwear\n5. Legwear\n6. Footwear\n7. Weapon\n8. Offhand\n")
                the_choice_made_by_the_user_in_response_to_being_asked_a_prompt = input("")
                the_choice_made_by_the_user_in_response_to_being_asked_a_prompt = the_choice_made_by_the_user_in_response_to_being_asked_a_prompt.lower()
                the_choice_made_by_the_user_in_response_to_being_asked_a_prompt = "".join(the_choice_made_by_the_user_in_response_to_being_asked_a_prompt.split())
                
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["1","helmet","h"]:
                    print("What helmet would you like to buy?\n\n")
                    if "Copper Helmet" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Helmet (50 Gold)")
                        found = True
                    if "Bronze Helmet" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Helmet (100 Gold)")
                        found = True
                    if "Iron Helmet" not in inventory["Gear"] and Player["Gold"] >= 175:
                        print(" Iron Helmet (175 Gold)")
                        found = True
                    if not found:
                        print("No helmet you can afford")
                        continue
                    helmet_choice = input("")
                    helmet_choice = helmet_choice.lower()
                    helmet_choice = "".join(helmet_choice.split())
                    if (helmet_choice in ["copperhelmet","copper"] and "Copper Helmet" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Helmet")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if (helmet_choice in ["bronzehelmet","bronze"] and "Bronze Helmet" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Helmet")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (helmet_choice in ["ironhelmet","iron"] and "Iron Helmet" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Helmet")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["2","shoulderwear","s"]:
                    print("What Shoulderwear would you like to buy?\n\n")
                    if "Copper Shoulder Guards" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Shoulder Guards (50 Gold)")
                        found = True
                    if "Bronze Shoulder Guards" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Shoulder Guards (100 Gold)")
                        found = True
                    if "Iron Shoulder Guards" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Shoulder Guards (175 Gold)")
                        found = True
                    if not found:
                        print("No shoulderwear you can afford")
                        continue
                    shoulderwear_choice = input("")
                    shoulderwear_choice = shoulderwear_choice.lower()
                    shoulderwear_choice = "".join(shoulderwear_choice.split())
                    if (shoulderwear_choice in ["coppershoulderguards","copper"] and "Copper Shoulder Guards" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Shoulder Guards")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if (shoulderwear_choice in ["bronzeshoulderguards","copper"] and "Bronze Shoulder Guards" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Shoulder Guards")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (shoulderwear_choice in ["ironshoulderguards","iron"] and "Iron Shoulder Guards" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Shoulder Guards")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["3","chestplate","c"]:
                    print("What Chestplate would you like to buy?\n\n")
                    if "Copper Chestplate" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Chestplate (50 Gold)")
                        found = True
                    if "Bronze Chestplate" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Chestplate (100 Gold)")
                        found = True
                    if "Iron Chestplate" not in inventory["Gear"] and Player["Gold"] >= 175:
                        print(" Iron Chestplate (175 Gold)")
                        found = True
                    if not found:
                        print("No chestplate you can afford")
                        continue
                    chestplate_choice = input("")
                    chestplate_choice = chestplate_choice.lower()
                    chestplate_choice = "".join(chestplate_choice.split())
                    if (chestplate_choice in ["copperchestplate","copper"] and "Copper Chestplate" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Chestplate")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if (chestplate_choice in ["bronzechestplate","copper"] and "Bronze Chestplate" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Chestplate")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (chestplate_choice in ["ironchestplate","iron"] and "Iron Chestplate" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Chestplate")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["4","armwear","a"]:
                    print("What Armwear would you like to buy?\n\n")
                    if "Copper Gardbrace" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Gardbrace (50 Gold)")
                        found = True
                    if "Bronze Gardbrace" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Gardbrace (100 Gold)")
                        found = True
                    if "Iron Gardbrace" not in inventory["Gear"] and Player["Gold"] >= 175:
                        print(" Iron Gardbrace (175 Gold)")
                        found = True
                    if not found:
                        print("No armwear you can afford")
                        continue
                    armwear_choice = input("")
                    armwear_choice = armwear_choice.lower()
                    armwear_choice = "".join(armwear_choice.split())
                    if armwear_choice in (["coppergardbrace","copper"] and "Copper Gardbrace" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Gardbrace")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if armwear_choice in (["bronzegardbrace","bronze"] and "Bronze Gardbrace" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Gardbrace")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (armwear_choice in ["irongardbrace","iron"] and "Iron Gardbrace" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Gardbrace")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["5","legwear","l"]:
                    print("What Legwear would you like to buy?\n\n")
                    if "Copper Greaves" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Greaves (50 Gold)")
                        found = True
                    if "Bronze Greaves" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Greaves (100 Gold)")
                        found = True
                    if "Iron Greaves" not in inventory["Gear"] and Player["Gold"] >= 175:
                        print(" Iron Greaves (175 Gold)")
                        found = True
                    if not found:
                        print("No legwear you can afford")
                        continue
                    legwear_choice = input("")
                    legwear_choice = legwear_choice.lower()
                    legwear_choice = "".join(legwear_choice.split())
                    if legwear_choice in (["coppergreaves","copper"] and "Copper Greaves" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Greaves")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if legwear_choice in (["bronzegreaves","bronze"] and "Bronze Greaves" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Greaves")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (legwear_choice in ["irongreaves","iron"] and "Iron Greaves" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Greaves")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["6","footwear","b"]:
                    print("What Footwear would you like to buy?\n\n")
                    if "Copper Boots" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Boots (50 Gold)")
                        found = True
                    if "Bronze Boots" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Boots (100 Gold)")
                        found = True
                    if "Iron Boots" not in inventory["Gear"] and Player["Gold"] >= 175:
                        print(" Iron Boots (175 Gold)")
                        found = True
                    if not found:
                        print("No footwear you can afford")
                        continue
                    footwear_choice = input("")
                    footwear_choice = footwear_choice.lower()
                    footwear_choice = "".join(footwear_choice.split())
                    if footwear_choice in (["copperboots","copper"] and "Copper Boots" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Boots")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if footwear_choice in (["bronzeboots","bronze"] and "Bronze Boots" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Boots")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (footwear_choice in ["ironboots","iron"] and "Iron Boots" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Boots")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["7","weapon","w"]:
                    print("What weapon would you like to buy?\n\n")
                    if "Copper Dagger" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Dagger (50 Gold)")
                        found = True
                    if "Copper Sword" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Sword (50 Gold)")
                        found = True
                    if "Copper Greatsword" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Greatsword (50 Gold)")
                        found = True
                    if "Copper Spear" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Spear (50 Gold)")
                        found = True
                    if "Copper Mace" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Mace (50 Gold)")
                        found = True
                    if "Copper Bow" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Bow (50 Gold)")
                        found = True
                    if "Copper Axe" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Axe (50 Gold)")
                        found = True
                    if "Crude Staff" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Crude Staff (100 Gold)")
                        found = True
                    if "Twig Wand" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Twig Wand (100 Gold)")
                        found = True
                    if "Bronze Dagger" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Bronze Dagger (100 Gold)")
                        found = True
                    if "Bronze Sword" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Sword")
                        found = True
                    if "Bronze Greatsword" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Greatsword (100 Gold)")
                        found = True
                    if "Bronze Spear" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Spear (100 Gold)")
                        found = True
                    if "Bronze Mace" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Mace (100 Gold)")
                        found = True
                    if "Bronze Bow" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Bow (100 Gold)")
                        found = True
                    if "Bronze Axe" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Axe (100 Gold)")
                        found = True
                    if "Carved Staff" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Carved Staff (100 Gold)")
                        found = True
                    if "Carved Wand" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Carved Wand (100 Gold)")
                        found = True
                    if "Iron Dagger" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Iron Dagger (100 Gold)")
                        found = True
                    if "Iron Sword" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Sword")
                        found = True
                    if "Iron Greatsword" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Greatsword (100 Gold)")
                        found = True
                    if "Iron Spear" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Spear (100 Gold)")
                        found = True
                    if "Iron Mace" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Mace (100 Gold)")
                        found = True
                    if "Iron Bow" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Bow (100 Gold)")
                        found = True
                    if "Iron Axe" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Iron Axe (100 Gold)")
                        found = True
                    if "Runed Staff" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Runed Staff (100 Gold)")
                        found = True
                    if "Crystal Wand" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Crystal Wand (100 Gold)")
                        found = True
                    if not found:
                        print("\n\n No weapon you can afford")
                        continue
                    weapon_choice = input("")
                    weapon_choice = weapon_choice.lower()
                    weapon_choice = "".join(weapon_choice.split())
                    if (weapon_choice in ["copperdagger"] and "Copper Dagger" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Dagger")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["coppersword"] and "Copper Sword" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Sword")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["coppergreatsword"] and "Copper Greatsword" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Greatsword")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["copperspear"] and "Copper Spear" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Spear")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["coppermace"] and "Copper Mace" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Mace")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["copperbow"] and "Copper Bow" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Bow")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["copperaxe"] and "Copper Axe" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Axe")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["crudestaff"] and "Crude Staff" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Crude Staff")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["twigwand"] and "Twig Wand" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Twig Wand")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzedagger"] and "Bronze Dagger" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Dagger")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzesword"] and "Bronze Sword" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Sword")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzegreatsword"] and "Bronze Greatsword" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Greatsword")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzespear"] and "Bronze Spear" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Spear")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzemace"] and "Bronze Mace" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Mace")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzebow"] and "Bronze Bow" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Bow")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["bronzeaxe"] and "Bronze Axe" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Axe")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["carvedstaff"] and "Carved Staff" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Carved Staff")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["carvedwand"] and "Carved Wand" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Carved Wand")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    elif (weapon_choice in ["irondagger"] and "Iron Dagger" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Dagger")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["ironsword"] and "Iron Sword" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Sword")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["irongreatsword"] and "Iron Greatsword" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Greatsword")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["ironspear"] and "Iron Spear" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Spear")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["ironmace"] and "Iron Mace" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Mace")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["ironbow"] and "Iron Bow" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Bow")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["ironaxe"] and "Iron Axe" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Axe")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["runedstaff"] and "Runed Staff" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Runed Staff")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    elif (weapon_choice in ["crystalwand"] and "Crystal Wand" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Crystal Wand")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
                    else:
                        print("Cannot Purchase")
                        
                if the_choice_made_by_the_user_in_response_to_being_asked_a_prompt in ["8","offhand","o"]:
                    print("What Offhand item would you like to buy?\n\n")
                    if "Copper Dagger" not in inventory["Gear"] and Player["Gold"] >= 50:
                        print(" Copper Shield (50 Gold)")
                        found = True
                    if "Bronze Dagger" not in inventory["Gear"] and Player["Gold"] >= 100:
                        print(" Bronze Shield (100 Gold)")
                        found = True
                    if "Iron Dagger" not in inventory["Gear"] and Player["Gold"] >= 175:
                        print(" Iron Shield (175 Gold)")
                        found = True
                    if not found:
                        print("No offhand item you can afford")
                        continue
                    offhand_choice = input("")
                    offhand_choice = offhand_choice.lower()
                    offhand_choice = "".join(offhand_choice.split())
                    if (offhand_choice in ["coppershield","copper"] and "Copper Shield" not in inventory["Gear"]) and Player["Gold"] >= 50:
                        inventory["Gear"].append("Copper Shield")
                        Player["Gold"] -= 50
                        Statistics["Gold Spent"] += 50
                        print("Gear Purchased")
                    if (offhand_choice in ["bronzeshield","bronze"] and "Bronze Shield" not in inventory["Gear"]) and Player["Gold"] >= 100:
                        inventory["Gear"].append("Bronze Shield")
                        Player["Gold"] -= 100
                        Statistics["Gold Spent"] += 100
                        print("Gear Purchased")
                    if (offhand_choice in ["ironshield","iron"] and "Iron Shield" not in inventory["Gear"]) and Player["Gold"] >= 175:
                        inventory["Gear"].append("Iron Shield")
                        Player["Gold"] -= 175
                        Statistics["Gold Spent"] += 175
                        print("Gear Purchased")
        elif Choice in ["training","t","5"]:
            if Skill_Tree["Training"]["Lock"] == "(Unlocked)":
                print("Choose Your Training:\n\n"f"Sword Swing {Skill_Tree['Training']['Sword Swing']['Status']}\nRun {Skill_Tree['Training']['Running']['Status']}\nWeight Carry {Skill_Tree['Training']['Weight Carry']['Status']}\nDead Hang {Skill_Tree['Training']['Dead Hang']['Status']}\nNeck Bridge {Skill_Tree['Training']['Neck Bridge']['Status']}\nPush Up {Skill_Tree['Training']['Push Up']['Status']}")
                training = input("")
                training = training.lower()
                training = "".join(training.split())
                rep = 0
                if training in ["1","swordswing","s","ss"]:
                    if Skill_Tree["Training"]["Sword Swing"]["Status"] == "(Unlocked)":
                        amount = (Body_Condition["Biceps"]["Strength"]* 1.2) + (Body_Condition["Triceps"]["Strength"] * 0.8) + (Body_Condition["Shoulders"]["Strength"]* 0.5)
                        amount = round(amount)
                        print(f"\ntype 'swing' to swing ({rep}/{amount})\n")
                        action = input("")
                        if Player["Title"] == "Well Built":
                            Max_Limit += 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit += 50
                        else:
                            pass
                        while True:
                            if action not in ["swing"]:
                                print("Not a correct input")
                            if action in ["swing"]:
                                rep += 1
                            if rep == amount:
                                h = random.randint(1,3)
                                time.sleep(2)
                                if h == 1:
                                    if Body_Condition["Biceps"]["Strength"] < Max_Limit:
                                        Body_Condition["Biceps"]["Strength"] += 1
                                        print(" \n Biceps + 1")
                                if h == 2:
                                    if Body_Condition["Triceps"]["Strength"] < Max_Limit:
                                        Body_Condition["Triceps"]["Strength"] += 1
                                        print("\n Triceps + 1")
                                if h == 3:
                                    if Body_Condition["Shoulders"]["Strength"] < Max_Limit:
                                        Body_Condition["Shoulders"]["Strength"] += 1
                                        print("\n Shoulders + 1")
                                Statistics["Training Sessions"] += 1
                                break
                            print(f"\ntype 'swing' to swing ({rep}/{amount})\n")
                            action = input("\n")
                        if Player["Title"] == "Well Built":
                            Max_Limit -= 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit -= 50
                        else:
                            pass
                    else:
                        print("\n\nThis is Locked\n\n\n\n\n")
                if training in ["2","run","r"]:
                    if Skill_Tree["Training"]["Running"]["Status"] == "(Unlocked)":

                        while True:
                            print("Set your distance in km")

                            try:
                                distance = int(input(""))
                                if Player["Speed"] < 500:
                                    distance = distance * (1- Player["Speed"] * 0.001)
                                else:
                                    distance = distance * 0.5
                                distance_in_seconds = distance * 60
                                distance_in_seconds = round(distance_in_seconds)

                                if distance_in_seconds > Player["Stamina"]:
                                    print("You don't have enough stamina.\n")
                                    continue

                                break
                            except ValueError:
                                print("Not a integer.\n")
                        distance = round(distance,2)
                        print(f"Running for {distance} minute(s)...\n")
                        if Player["Title"] == "Well Built":
                            Max_Limit += 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit += 50
                        else:
                            pass
                        Player_Stamina = Player["Stamina"]

                        for i in range(distance_in_seconds, 0, -1):
                            time.sleep(1)

                            distance_in_seconds -= 1
                            Player_Stamina -= 1

                        if distance_in_seconds == 0:

                            time.sleep(2)

                            h = random.randint(1,2)

                            if h == 1:
                                if Body_Condition["Legs"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Legs"]["Strength"] += (random.randint(1,distance))
                                    print(f"\nLegs + {distance}")
                                else:
                                    print("Max Limit Reached")

                            elif h == 2:
                                if Body_Condition["Abdomen"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Abdomen"]["Strength"] += (random.randint(1,distance))
                                    print(f"\nAbdomen + {distance}")
                                else:
                                    print("Max Limit Reached")
                            Statistics["Training Sessions"] += 1
                            if Player["Title"] == "Well Built":
                                Max_Limit -= 25
                            elif Player["Title"] == "Peak Physique":
                                Max_Limit -= 50
                            else:
                                pass
                    else:
                        print("\n\nThis is Locked\n\n\n\n\n")
                    print("\nYou are tired")
                    print("\nWait a minute")
                    time.sleep(60)
                    back = input("\n---------------\n\nPress enter to return\n\n")
                    


                if training in ["3","weightcarry","wc","w"]:
                    if Skill_Tree["Training"]["Weight Carry"]["Status"] == "(Unlocked)":

                        while True:
                            print("\n\nSet your weight in kg\n")

                            try:
                                weight = int(input(""))
                                if Player["Attack"] < 500:
                                    weight = weight * (1- Player["Attack"] * 0.001)
                                else:
                                    weight = weight * 0.5
                                distance = weight 
                                distance_in_seconds = distance * 60
                                distance_in_seconds = round(distance_in_seconds)

                                if distance_in_seconds > Player["Stamina"]:
                                    print("You don't have enough stamina.\n")
                                    continue

                                break

                            except ValueError:
                                print("Not a integer.\n")
                        distance = round(distance,2)
                        print(f"Carrying for {distance} minute(s)...\n")
                        if Player["Title"] == "Well Built":
                            Max_Limit += 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit += 50
                        else:
                            pass

                        Player_Stamina = Player["Stamina"]

                        for i in range(distance_in_seconds, 0, -1):
                            time.sleep(1)

                            distance_in_seconds -= 1
                            Player_Stamina -= 1

                        if distance_in_seconds == 0:

                            time.sleep(2)

                            h = random.randint(1,4)

                            if h == 1:
                                if Body_Condition["Legs"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Legs"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nLegs + {distance}")
                                else:
                                    print("Max Limit Reached")

                            elif h == 2:
                                if Body_Condition["Back"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Back"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nBack + {distance}")
                                else:
                                    print("Max Limit Reached")
                            elif h == 3:
                                if Body_Condition["Shoulders"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Shoulders"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nShoulders + {distance}")
                                else:
                                    print("Max Limit Reached")
                            elif h == 4:
                                if Body_Condition["Trapezius"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Trapezius"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nTrapezius + {distance}")
                                else:
                                    print("Max Limit Reached")
                            Statistics["Training Sessions"] += 1
                            if Player["Title"] == "Well Built":
                                Max_Limit -= 25
                            elif Player["Title"] == "Peak Physique":
                                Max_Limit -= 50
                            else:
                                pass
                    else:
                        print("\n\nThis is Locked\n\n\n\n\n")
                    print("\nYou are tired")
                    print("\nWait a minute")
                    time.sleep(60)
                    back = input("\n---------------\n\nPress enter to return\n\n")

                if training in ["4","deadhang","dh","d"]:
                    if Skill_Tree["Training"]["Dead Hang"]["Status"] == "(Unlocked)":

                        while True:
                            print("\n\nSet your weight in kg\n")

                            try:
                                weight = int(input(""))
                                if Player["Attack"] < 500:
                                    weight = weight * (1- Player["Attack"] * 0.001)
                                else:
                                    weight = weight * 0.5
                                distance = weight 
                                distance_in_seconds = distance * 60
                                distance_in_seconds = round(distance_in_seconds)

                                if distance_in_seconds > Player["Stamina"]:
                                    print("You don't have enough stamina.\n")
                                    continue

                                break

                            except ValueError:
                                print("Not a integer.\n")
                        distance = round(distance,2)
                        print(f"Hanging for {distance} minute(s)...\n")
                        if Player["Title"] == "Well Built":
                            Max_Limit += 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit += 50
                        else:
                            pass
                        Player_Stamina = Player["Stamina"]

                        for i in range(distance_in_seconds, 0, -1):
                            time.sleep(1)

                            distance_in_seconds -= 1
                            Player_Stamina -= 1

                        if distance_in_seconds == 0:

                            time.sleep(2)

                            h = random.randint(1,3)

                            if h == 1:
                                if Body_Condition["Legs"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Legs"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nLegs + {distance}")
                                else:
                                    print("Max Limit Reached")

                            elif h == 2:
                                if Body_Condition["Shoulders"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Shoulders"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nBack + {distance}")
                                else:
                                    print("Max Limit Reached")
                            elif h == 3:
                                if Body_Condition["Trapezius"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Trapezius"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nTrapezius + {distance}")
                                else:
                                    print("Max Limit Reached")
                            Statistics["Training Sessions"] += 1
                            if Player["Title"] == "Well Built":
                                Max_Limit -= 25
                            elif Player["Title"] == "Peak Physique":
                                Max_Limit -= 50
                            else:
                                pass
                    else:
                        print("\n\nThis is Locked\n\n\n\n\n")
                    print("\nYou are tired")
                    print("\nWait a minute")
                    time.sleep(60)
                    back = input("\n---------------\n\nPress enter to return\n\n")

                if training in ["5","neckbridge","nb","n"]:
                    if Skill_Tree["Training"]["Neck Bridge"]["Status"] == "(Unlocked)":

                        while True:
                            print("\n\nSet your Time in Minutes\n")

                            try:
                                weight = int(input(""))
                                distance = weight 
                                distance_in_seconds = distance * 60
                                distance_in_seconds = round(distance_in_seconds)

                                if distance_in_seconds > Player["Stamina"]:
                                    print("You don't have enough stamina.\n")
                                    continue

                                break

                            except ValueError:
                                print("Not a integer.\n")
                        distance = round(distance,2)
                        print(f"Bridging for {distance} minute(s)...\n")

                        if Player["Title"] == "Well Built":
                            Max_Limit += 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit += 50
                        else:
                            pass

                        Player_Stamina = Player["Stamina"]

                        for i in range(distance_in_seconds, 0, -1):
                            time.sleep(1)

                            distance_in_seconds -= 1
                            Player_Stamina -= 1

                        if distance_in_seconds == 0:

                            time.sleep(2)

                            h = random.randint(1,3)

                            if h == 1:
                                if Body_Condition["Head"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Head"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nLegs + {distance}")
                                else:
                                    print("Max Limit Reached")

                            elif h == 2:
                                if Body_Condition["Back"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Back"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nBack + {distance}")
                                else:
                                    print("Max Limit Reached")
                            elif h == 3:
                                if Body_Condition["Trapezius"]["Strength"] < Max_Limit:
                                    distance = round(distance)
                                    Body_Condition["Trapezius"]["Strength"] += (random.randint(1,weight))
                                    print(f"\nTrapezius + {distance}")
                                else:
                                    print("Max Limit Reached")
                            if Player["Title"] == "Well Built":
                                Max_Limit -= 25
                            elif Player["Title"] == "Peak Physique":
                                Max_Limit -= 50
                            else:
                                pass
                            Statistics["Training Sessions"] += 1
                    else:
                        print("\n\nThis is Locked\n\n\n\n\n")
                    print("\nYou are tired")
                    print("\nWait a minute")
                    time.sleep(60)
                    back = input("\n---------------\n\nPress enter to return\n\n")
                if training in ["6","pushup","p","pu"]:
                    if Skill_Tree["Training"]["Push Up"]["Status"] == "(Unlocked)":
                        amount = (Body_Condition["Chest"]["Strength"]* 1.2) + (Body_Condition["Triceps"]["Strength"] * 0.8) + (Body_Condition["Shoulders"]["Strength"]* 0.5)
                        amount = round(amount)
                        print(f"\ntype 'push up' to do a push up ({rep}/{amount})\n")
                        if Player["Title"] == "Well Built":
                            Max_Limit += 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit += 50
                        else:
                            pass
                        action = input("")
                        action = action.lower()
                        action = "".join(action.split())
                        while True:
                            if action not in ["pushup"]:
                                print("Not a correct input")
                            if action in ["pushup"]:
                                rep += 1
                            if rep == amount:
                                h = random.randint(1,3)
                                time.sleep(2)
                                if h == 1:
                                    if Body_Condition["Chest"]["Strength"] < Max_Limit:
                                        Body_Condition["Chest"]["Strength"] += 1
                                        print("\n Chest + 1")
                                if h == 2:
                                    if Body_Condition["Triceps"]["Strength"] < Max_Limit:
                                        Body_Condition["Triceps"]["Strength"] += 1
                                        print("\n Triceps + 1")
                                if h == 3:
                                    if Body_Condition["Shoulders"]["Strength"] < Max_Limit:
                                        Body_Condition["Shoulders"]["Strength"] += 1
                                        print("\n Shoulders + 1")
                                Statistics["Training Sessions"] += 1
                                break
                            print(f"\ntype 'push up' to do a push up ({rep}/{amount})\n")
                            action = input("\n")
                            action = action.lower()
                            action = "".join(action.split())
                        if Player["Title"] == "Well Built":
                            Max_Limit -= 25
                        elif Player["Title"] == "Peak Physique":
                            Max_Limit -= 50
                        else:
                            pass
                    else:
                        print("\n\nThis is Locked\n\n\n\n\n")
                    
            else:
                print("\n\nThis is Locked\n\n\n\n\n")

        elif Choice in ["mine","3"]:
            while True:
                try:
                    volume = float(input("\nInput how long you want to mine for in minutes\n\n"))
                    break
                except:
                    print("\n\nNot a number\n")
            time_in_seconds = volume * 60
            time_to_wait = 0
            print("\nMining...\n")
            time_in_seconds = round(time_in_seconds)
            Player_Stamina = Player["Stamina"]
            while time_in_seconds != 0 and Player_Stamina != 0:
                time_in_seconds -= 1
                Player_Stamina -= 5
                time.sleep(1)
                time_to_wait += 1
                s = random.randint(1,100)
                if s <= 2:
                    if Player["Tower Level"] >= 0:
                        items = ["Iron","Bronze","Copper"]
                        rarity_weights = [10,30,60]
                        drop = random.choices(items, weights=rarity_weights, k=1)[0]
                        print(f"\n{drop} Found!\n")
                    if drop in inventory:
                        inventory[drop] += 1
                    else:
                        inventory[drop] = 1
            if Player_Stamina == 0:
                print("\nYou have exhausted your stamina\n")
                print(f"\nWait {time_to_wait} seconds(s)\n")
                time.sleep(time_to_wait) 
            else:
                print("\nTimes up!\n")
                time_to_wait = time_to_wait * 0.5
                time_to_wait = round(time_to_wait)
                if Player_Stamina > (Player["Stamina"] * 0.5):
                    wait_time = 0
                else:
                    print(f"\nWait {time_to_wait} seconds(s)\n")
                    time.sleep(time_to_wait)
                
        elif Choice in ["forest","4","f"]:
            while True:
                try:
                    volume = float(input("\nInput how long you want to forage for in minutes\n\n"))
                    break
                except:
                    print("\n\nNot a number\n")
            time_in_seconds = volume * 60
            time_to_wait = 0
            print("\nForaging...\n")
            time_in_seconds = round(time_in_seconds)
            Player_Stamina = Player["Stamina"]
            while time_in_seconds != 0 and Player_Stamina != 0:
                time_in_seconds -= 1
                Player_Stamina -= 2
                time_to_wait += 1
                time.sleep(1)
                s = random.randint(1,100)
                if s <= 3:
                    drop = random.choice(["Mana Herb","Healing Herb","Bitter Herb","IronStem Herb","Sweet Herb","Sunleaf","Frostleaf","Emberleaf","Spirit Bloom","Crystal Bloom","Shock Moss","Battle Bloom","Cloud Flower","Focus Flower"])
                    print(f"\n{drop} Found!\n")
                    if drop in inventory:
                        inventory[drop] += 1
                    else:
                        inventory[drop] = 1
            if Player_Stamina == 0:
                print("\nYou have exhausted your stamina\n")
                print(f"\nWait {time_to_wait} seconds(s)\n")
                time.sleep(time_to_wait)
            else:
                print("\nTimes up!\n")
                time_to_wait = time_to_wait * 0.5
                time_to_wait = round(time_to_wait)
                if Player_Stamina > (Player["Stamina"] * 0.5):
                    wait_time = 0
                else:
                    print(f"\nWait {time_to_wait} seconds(s)\n")
                    time.sleep(time_to_wait)
        elif Choice in ["6","smithing","smith"]:
            if Skill_Tree["Smithing"]["Lock"] == "(Unlocked)":
                pass
            else:
                print("\n\nThis is Locked\n\n\n\n\n")
        elif Choice in ["7","alchemy","a"]:
            if Skill_Tree["Alchemy"]["Lock"] == "(Unlocked)":
                potion_type = "None"
                Power = 0
                while True:
                    print("\n Choose what Herb to add.\n\n Press Enter to cancel\n\n")
                    item = input("").lower()
                    item = "".join(item.split())
                    if "Healing Herb" in inventory and item in ["healingherb"]:
                        if inventory["Healing Herb"] >= 1:
                            potion_type = "Health"
                            inventory["Healing Herb"] -= 1
                            break
                    elif "Mana Herb" in inventory and item in ["manaherb"]:
                        if inventory["Mana Herb"] >= 1:
                            potion_type = "Mana"
                            inventory["Mana Herb"] -= 1
                            break
                    elif "Bitter Herb" in inventory and item in ["bitterherb"]:
                        if inventory["Bitter Herb"] >= 1:
                            potion_type = "Bleed Cure"
                            inventory["Bitter Herb"] -= 1
                            break
                    elif "Ironstem Herb" in inventory and item in ["ironstemherb"]:
                        if inventory["Ironstem Herb"] >= 1:
                            potion_type = "Defense"
                            inventory["Ironstem Herb"] -= 1
                            break
                    elif "Sweet Herb" in inventory and item in ["sweetherb"]:
                        if inventory["Sweet Herb"] >= 1:
                            potion_type = "Stamina"
                            inventory["Sweet Herb"] -= 1
                            break
                    elif "Sunleaf" in inventory and item in ["sunleaf"]:
                        if inventory["Sunleaf"] >= 1:
                            potion_type = "Boost Holy"
                            inventory["Sunleaf"] -= 1
                            break
                    elif "Frostleaf" in inventory and item in ["frostleaf"]:
                        if inventory["Frostleaf"] >= 1:
                            potion_type = "Burn Cure"
                            inventory["Frostleaf"] -= 1
                            break
                    elif "Emberleaf" in inventory and item in ["emberleaf"]:
                        if inventory["Emberleaf"] >= 1:
                            potion_type = "Freeze Cure"
                            inventory["Emberleaf"] -= 1
                            break
                    elif "Spirit Bloom" in inventory and item in ["spiritbloom"]:
                        if inventory["Spirit Bloom"] >= 1:
                            potion_type = "Spell Power"
                            inventory["Spirit Bloom"] -= 1
                            break
                    elif "Crystal Bloom" in inventory and item in ["crystalbloom"]:
                        if inventory["Crystal Bloom"] >= 1:
                            potion_type = "Magic Density"
                            inventory["Crystal Bloom"] -= 1
                            break
                    elif "Shock Moss" in inventory and item in ["shockmoss"]:
                        if inventory["Shock Moss"] >= 1:
                            potion_type = "Speed"
                            inventory["Shock Moss"] -= 1
                            break
                    elif "Battle Bloom" in inventory and item in ["battlebloom"]:
                        if inventory["Battle Bloom"] >= 1:
                            potion_type = "Attack"
                            inventory["Battle Bloom"] -= 1
                            break
                    elif "Cloud Flower" in inventory and item in ["cloudflower"]:
                        if inventory["Cloud Flower"] >= 1:
                            potion_type = "Evasion"
                            inventory["Cloud Flower"] -= 1
                            break
                    elif "Focus Flower" in inventory and item in ["focusflower"]:
                        if inventory["Focus Flower"] >= 1:
                            potion_type = "Accuracy"
                            inventory["Focus Flower"] -= 1
                            break
                    elif "Galvano Flower" in inventory and item in ["galvanoflower"]:
                        if inventory["Galvano Flower"] >= 1:
                            potion_type = "Electric Resistance"
                            inventory["Galvano Flower"] -= 1
                            break
                    elif "Toxic Mushroom" in inventory and item in ["toxicmushroom"]:
                        if inventory["Toxic Mushroom"] >= 1:
                            potion_type = "Poison Cure"
                            inventory["Toxin Mushroom"] -= 1
                            break
                    elif item in [""]:
                        break
                    else:
                        print("\n Not a Herb you have\n")
                while True:
                    print("\n Choose what Monster Drop to add.       ( Add proper spacing )\n\n Press Enter to cancel\n\n")
                    Drop = input("").title()
                    Drop_Prop = Drop.lower()
                    Drop_Prop = "".join(Drop_Prop.split())
                    if Drop_Prop in ["bones"] and Drop in inventory:
                        Power = random.uniform(1.01,1.05)
                        break
                    elif Drop_Prop in ["rottingflesh"] and Drop in inventory:
                        Power = random.uniform(1.05,1.1)
                        break
                    elif Drop_Prop in ["orctusk"] and Drop in inventory:
                        Power = random.uniform(1.1,1.15)
                        break
                    elif Drop_Prop in ["warbeastfang","beasthide"] and Drop in inventory:
                        Power = random.uniform(1.15,1.2)
                        break
                    elif Drop_Prop in ["bloodsword","knightsemblem"] and Drop in inventory:
                        Power = random.uniform(1.2,1.25)
                        break
                    elif Drop == "":
                        break
                    else:
                        print("\n You do not have this drop\n")
                if Power != 0 and potion_type != "None":
                    if potion_type in ["Electric Resistance"]:
                        inventory["Potions"].append({"Type": "Electric Resistance Potion"})
                        print("\n Electric Resistance Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Freeze Cure"]:
                        inventory["Potions"].append({"Type": "Freeze Cure Potion"})
                        print("\n Freeze Cure Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Burn Cure"]:
                        inventory["Potions"].append({"Type": "Burn Cure Potion"})
                        print("\n Burn Cure Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Bleed Cure"]:
                        inventory["Potions"].append({"Type": "Bleed Cure Potion"})
                        print("\n Bleed Cure Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Poison Cure"]:
                        inventory["Potions"].append({"Type": "Poison Cure Potion"})
                        print("\n Poison Cure Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Health"]:
                        inventory["Potions"].append({"Type": "Health Potion","Power":Power})
                        print("\n Health Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Mana"]:
                        inventory["Potions"].append({"Type": "Mana Potion","Power":Power})
                        print("\n Mana Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Defense"]:
                        inventory["Potions"].append({"Type": "Defense Potion","Power":Power})
                        print("\n Defense Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Stamina"]:
                        inventory["Potions"].append({"Type": "Stamina Potion","Power":Power})
                        print("\n Stamina Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Boost Holy"]:
                        inventory["Potions"].append({"Type": "Holy Potion","Power":Power})
                        print("\n Holy Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Spell Power"]:
                        inventory["Potions"].append({"Type": "Spell Potion","Power":Power})
                        print("\n Spell Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Magic Density"]:
                        inventory["Potions"].append({"Type": "Dense Potion","Power":Power})
                        print("\n Dense Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Speed"]:
                        inventory["Potions"].append({"Type": "Hasty Potion","Power":Power})
                        print("\n Hasty Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Attack"]:
                        inventory["Potions"].append({"Type": "Battle Potion","Power":Power})
                        print("\n Battle Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Evasion"]:
                        inventory["Potions"].append({"Type": "Evasion Potion","Power":Power})
                        print("\n Evasion Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1
                    if potion_type in ["Accuracy"]:
                        inventory["Potions"].append({"Type": "Focus Potion","Power":Power})
                        print("\n Focus Potion Brewed!\n\n")
                        Statistics["Potions Brewed"] += 1


                    
                    
            else:
                print("\n\nThis is Locked\n\n\n\n\n")



