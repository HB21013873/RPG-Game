import random
import time
from datetime import datetime
import sys
import builtins
from Text_Writing_Style import TypeWriter as TW
from Enemy_Moves import Enemy_Move as EM
tw = TW(delay=0.02, jitter=True)
typewriter = True
def print(*args, sep=" ", end="\n"):
    if typewriter:
        text = sep.join(str(arg) for arg in args)
        tw.write(text, newline=False)
        sys.stdout.write(end)
    else:
        builtins.print(*args, sep=sep, end=end)


    
class Enemy_Battle:

    
    
    def Enemy1_Battle(Enemy1,b,Player,Player_copy,Evasion1_Stopper,Defense1_Stopper,name,Game,Turn_Time,Player_Skip,typewriters,**kwargs):

        global typewriter
        typewriter = typewriters
        Enemy2 = kwargs.get("Enemy2",None)
        Enemy3 = kwargs.get("Enemy3",None)

        Move = []
        Attack_Chance = 0
        Defense_Chance = 0
        Spell_Caster = False
        target = Enemy1

        
        if Enemy1["Spell Caster"] == True or Enemy1["Mana"] > 0:
            Spell_Caster = random.choice([False,True])
            

        

        if "Cultist" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Life Drain","Corrupting Touch","Empower"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Quick Stab","Blood Offering"]
        elif "Berserker" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Ice Shard","Empower"]                       
            elif Spell_Caster == False:
                Move += ["Headbutt","Implusive Swing","Bite","Slash","Quick Stab","Blood Frenzy"]
        elif "Rat" in Enemy1["Type"]:
            Attack_Chance = 0.4
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Golem" in Enemy1["Type"]:
            Attack_Chance = 0.4
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Tremor"]                      
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Tackle","Groundbreaker"]
        elif "Skeleton" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Life Drain"]               
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Front Kick"]
        elif "Warrior" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard"] 
            elif Spell_Caster == False:
                Move += ["Straight Punch","Slash","Quick Stab","Axe Kick","Front Kick"]
        elif "Apprentice" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock","Life Drain"]                        
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Front Kick"]
        elif "Wolf" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Slash","Tackle"]
        elif "Bandit" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Fireball","Empower"]                      
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Slash","Quick Stab"]
        elif "Kobold" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Bite","Front Kick"]
        elif "Goblin" in Enemy1["Type"]and "Fighter" not in Enemy1["Type"] and "Archer" not in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Empower"]    
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Front Kick"]
        elif "Ghost" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Life Drain","Devour Essence"]
        elif "Imp" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Life Drain","Mana Blast"]                 
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Front Kick"]
        elif "Gladiator" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Empower"] 
            elif Spell_Caster == False:
                Move += ["Straight Punch","Spinning Back Kick","Headbutt","Slash","Quick Stab"]
        elif "Executioner" in Enemy1["Type"]:
            Attack_Chance = 0.9
            Defense_Chance = 0.95
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Slash","Front Kick"]
        elif "Scavenger" in Enemy1["Type"]:
            Attack_Chance = 0.3
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Quick Stab","Front Kick"]
        elif "Homunculus" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Life Drain","Devour Essence"]                    
            elif Spell_Caster == False:
                Move += ["Straight Punch","Front Kick"]
        elif "Archer" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Aimed Shot"]
        elif "Spearman" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball"]                     
            elif Spell_Caster == False:
                Move += ["Front Kick","Slash","Quick Stab"]
        elif "Spirit" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Life Drain"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing"]
        elif "Summoner" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower","Summon"]      
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Front Kick"]
        elif "Demon" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Fireball","Devour Essence","Life Drain"]                        
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Bite","Front Kick"]
        elif "Hound" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Fighter" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock","Empower"]
            elif Spell_Caster == False:
                Move += ["Straight Punch","Front Kick","Spinning Back Kick"]
        elif "Rogue" in Enemy1["Type"] and ("Archer" or "Fighter")not in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]                     
            elif Spell_Caster == False:
                Move += ["Straight Punch","Front Kick","Slash","Quick Stab"]
        elif "Knight" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]                      
            elif Spell_Caster == False:
                Move += ["Straight Punch","Slash","Quick Stab","Front Kick"]
        elif "Duelist" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]           
            elif Spell_Caster == False:
                Move += ["Straight Punch","Slash","Quick Stab","Front Kick"]
        elif "Beast" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Slash","Tackle"]
        elif "Mage" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Ice Shard","Shock","Fireball","Life Drain","Purify","Grappling Vines","River Fist","Mud Shot","Stone Slipstream","Dominate","Heal"]                
            elif Spell_Caster == False:
                Move += ["Straight Punch","Front Kick"]
        elif "Slime" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch"]                    
            elif Spell_Caster == False:
                Move += ["Headbutt","Tackle"]
        elif "Trainee" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]                      
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch","Axe Kick","Spinning Back Kick","Slash","Quick Stab","Front Kick"]
        elif "Dog" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]                    
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Artificer" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock","Life Drain"]                     
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch","Axe Kick","Front Kick"]
        elif "Spider" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]                
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Snake" in Enemy1["Type"] or "Serpent" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.55
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Crawler" in Enemy1["Type"]:
            Attack_Chance = 0.4
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite"]
        elif "Elemental" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast"] 
            elif Spell_Caster == False:
                Move += ["Straight Punch","Front Kick"]
        elif "Horror" in Enemy1["Type"]:
            Attack_Chance = 0.9
            Defense_Chance = 0.95
            if Spell_Caster == True:
                Move += ["Mana Blast","Life Drain","Corrupting Touch","Devour Essence"]     
            elif Spell_Caster == False:
                Move += ["Straight Punch","Impulsive Swing","Bite","Front Kick"]
        elif "Crow" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.55
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Walker" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Front Kick","Straight Punch"]
        elif "Wraith" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Life Drain","Corrupting Touch","Devour Essence"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch"]
        elif "Warrior" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Slash","Quick Stab","Front Kick"]
        elif "Servant" in Enemy1["Type"]:
            Attack_Chance = 0.9
            Defense_Chance = 0.95
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Bat" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]       
            elif Spell_Caster == False:
                Move += ["Headbutt","Bite","Tackle"]
        elif "Stalker" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch","Life Drain","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Front Kick","Straight Punch"]
        elif "Sprite" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast"]                       
            elif Spell_Caster == False:
                Move += ["Headbutt","Front Kick"]
        elif "Lord" in Enemy1["Type"]:
            Attack_Chance = 0.9
            Defense_Chance = 0.95
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock","Empower"]                       
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Assassin" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch","Quick Stab","Front Kick"]
        elif "Spawn" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Life Drain","Corrupting Touch"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Slash","Front Kick"]
        elif "Acolyte" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Life Drain","Devour Essence"]                            
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Blacksmith" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Empower"]          
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Soldier" in Enemy1["Type"]:
            Attack_Chance = 0.9
            Defense_Chance = 0.95
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch","Slash","Quick Stab","Front Kick"]
        elif "Experiment" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast","Corrupting Touch","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Front Kick","Tackle"]
        elif "Ogre" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Bite","Front Kick"]
        elif "Potion" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Toxin Spray"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Tackle"]
        elif "Ooze" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast","Toxin Spray"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Tackle"]
        elif "Warden" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Shock","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Guard" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Raider" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.85
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Robber" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.7
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Front Kick"]
        elif "Troll" in Enemy1["Type"]:
            Attack_Chance = 0.7
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]                        
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Front Kick"]
        elif "Thief" in Enemy1["Type"]:
            Attack_Chance = 0.4
            Defense_Chance = 0.6
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]    
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Quick Stab","Front Kick"]
        elif "Guardian" in Enemy1["Type"]:
            Attack_Chance = 0.5
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch","Front Kick"]
        elif "Lich" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Life Drain","Corrupting Touch","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]
        elif "Champion" in Enemy1["Type"]:
            Attack_Chance = 0.8
            Defense_Chance = 0.9
            if Spell_Caster == True:
                Move += ["Mana Blast","Fireball","Ice Shard","Shock","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Straight Punch","Slash","Quick Stab","Front Kick"]
        elif "Automaton" in Enemy1["Type"]:
            Attack_Chance = 0.6
            Defense_Chance = 0.8
            if Spell_Caster == True:
                Move += ["Mana Blast","Empower"]
            elif Spell_Caster == False:
                Move += ["Headbutt","Impulsive Swing","Straight Punch","Front Kick"]




        if "Venom" in Enemy1["Type"] or "Swamp" in Enemy1["Type"] or "Bog" in Enemy1["Type"] or "Acid" in Enemy1["Type"] or "Toxic" in Enemy1["Type"] or "Venom" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Poison"
            Move += ["Toxic Spray"]
        if "Rot" in Enemy1["Type"] or "Plague" in Enemy1["Type"] or "Disease" in Enemy1["Type"] or "Ruin" in Enemy1["Type"] or "Bone" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Decay"
            Move += ["Corrupting Touch"]
        if "Ice" in Enemy1["Type"] or "Frost" in Enemy1["Type"] or "Frozen" in Enemy1["Type"] or "Snow" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Ice"
            Move += ["Ice Shard"]
        if "Lightning" in Enemy1["Type"] or "Storm" in Enemy1["Type"] or "Tempest" in Enemy1["Type"] or "Thunder" in Enemy1["Type"] or "Charged" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Lightning"
            Move += ["Shock"]
        if "Shadow" in Enemy1["Type"] or "Void" in Enemy1["Type"] or "Dark" in Enemy1["Type"] or "Night" in Enemy1["Type"] or "Phantom" in Enemy1["Type"] or "Lich" in Enemy1["Type"] or "Abyss" in Enemy1["Type"] or "Nightmare" in Enemy1["Type"] or "Demon Lord" in Enemy1["Type"] or "Cursed" in Enemy1["Type"] or "Eclipsed" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Dark"
            Move += ["Corrupting Touch","Life Drain"]
        if "Alchemical" in Enemy1["Type"] or "Mutant" in Enemy1["Type"] or "Experiment" in Enemy1["Type"] or "Potion" in Enemy1["Type"] or "Mutation" in Enemy1["Type"] or "Living" in Enemy1["Type"] or "Mad Alchemist" in Enemy1["Type"] or "Tiny" in Enemy1["Type"] or "Chemical" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Chemical"
            Move += ["Toxin Spray"]
        if "Fire" in Enemy1["Type"] or "Flame" in Enemy1["Type"] or "Burning" in Enemy1["Type"] or "Molten" in Enemy1["Type"] or "Inferno" in Enemy1["Type"] or  "Demon" in Enemy1["Type"] or "Ash" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Fire"
            Move += ["Fireball"]
        if "Shield" in Enemy1["Type"] or "Stone" in Enemy1["Type"] or "Heavy" in Enemy1["Type"] or "Rust" in Enemy1["Type"] or "Steel" in Enemy1["Type"]:
            Enemy1["Defense"] += round(Enemy1["Defense"] * 0.01)
            Move += ["Groundbreaker"]
        if "Ritual" in Enemy1["Type"] or "Ancient" in Enemy1["Type"] or "Tomb" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Cursed"
            Move += ["Devour Essence"]
        if "Bridge" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Bridge"
        if "Armory" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Armory"
        if "Arena" in Enemy1["Type"] or "Pit" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Crowd"
            Move += ["Empower"]
        if "Rogue" in Enemy1["Type"] or "Wind" in Enemy1["Type"] or "Dust" in Enemy1["Type"]:
            Enemy1["Attribute "] = "Agile"
            Enemy1["Speed"] += round(Enemy1["Speed"] * 0.01)
            Move += ["Stone Slipstream"]
        if "War" in Enemy1["Type"]:
            Enemy1["Attribute"] = "Aggressive"
            Enemy1["Attack"] += round(Enemy1["Attack"] * 0.05)
            Move += ["Empower"]

        if Enemy1["Category"] == "Undead":
            Move += ["Corrupting Touch"]
            if Attack_Chance <= 0.9 and Defense_Chance <= 0.9:
                Attack_Chance += 0.1
                Defense_Chance += 0.1
            else:
                Attack_Chance = 1
                Defense_Chance = 0

        if Enemy1["Category"] == "Humanoid":
            Move += ["Mana Blast"]
            if Attack_Chance >= 0.1:
                Attack_Chance -= 0.1
            else:
                Attack_Chance = 0
                
        if Enemy1["Category"] == "Demon":
            Move += ["Fireball"]
            if Attack_Chance <= 0.8 and Defense_Chance <= 0.8:
                Attack_Chance += 0.2
                Defense_Chance += 0.2
            else:
                Attack_Chance = 1
                Defense_Chance = 0
        if Enemy1["Category"] == "Beast":
            Move += ["Empower"]
            if Attack_Chance <= 0.8 and Defense_Chance <= 0.8:
                Attack_Chance += 0.2
                Defense_Chance += 0.2
            else:
                Attack_Chance = 1
                Defense_Chance = 0
                
        if Enemy1["Category"] == "Abberation":
            m = random.randint(1,3)
            if m == 1:
                if Attack_Chance <= 0.8 and Defense_Chance <= 0.8:
                    Attack_Chance += 0.2
                    Defense_Chance += 0.2
                else:
                    Attack_Chance = 1
                    Defense_Chance = 0
            if m == 2:
                if Attack_Chance >= 0.2:
                    Attack_Chance -= 0.2
                else:
                    Attack_Chance = 0
            if m == 3:
                if Attack_Chance >= 0.2 and Defense_Chance >= 0.2:
                    Attack_Chance -= 0.2
                    Defense_Chance -= 0.2
                else:
                    Attack_Chance = 0
                    Defense_Chance = 0
        if Enemy1["Category"] == "Construct":
            if Attack_Chance >= 0.1:
                Attack_Chance -= 0.1
            else:
                Attack_Chance = 0
        if Enemy1["Category"] == "Elemental":
            Enemy1["Magic Density"] *= 1.01
            Enemy1["Magic Density"] = round(Enemy1["Magic Density"])
        if Enemy1["Behaviour"] == "Aggressive":
            if Attack_Chance <= 0.8 and Defense_Chance <= 0.8:
                Attack_Chance += 0.2
                Defense_Chance += 0.2
            else:
                Attack_Chance = 1
                Defense_Chance = 0
        if Enemy1["Behaviour"] == "Defensive":
            if Attack_Chance >= 0.1:
                Attack_Chance -= 0.1
            else:
                Attack_Chance = 0
        if Enemy1["Behaviour"] == "Evasive":
            if Attack_Chance >= 0.1 and Defense_Chance >= 0.1:
                Attack_Chance -= 0.1
                Defense_Chance -= 0.1
            else:
                Attack_Chance = 0
                Defense_Chance = 0
            
        Move = random.choice(Move)
            
                
        ratio = random.random()
        if ratio <= Attack_Chance:
                if Move in ["Mana Blast"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Arcane.Mana_Blast(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Fireball"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Fire.Fireball(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Ice Shard"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Ice.Ice_Shard(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Shock"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Lightning.Shock(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Life Drain"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Dark.Life_Drain(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Straight Punch"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Arms.Straight_Punch(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Impulsive Swing"]:
                    Player_copy,Enemy1,Turn_Time,Player_Skip = EM.Melee_Moves.Arms.Impulsive_Swing(Player_Skip,Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Front Kick"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Legs.Front_Kick(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Empower"]:
                    target = EM.Spell_Moves.Arcane.Empower(target,typewriter)
                elif Move in ["Headbutt"]:
                    Player_copy,Enemy1,Turn_Time,Player_Skip = EM.Melee_Moves.Head.Headbutt(Player_Skip,Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Bite"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Arms.Straight_Punch(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Slash"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Arms.Slash(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Quick Stab"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Arms.Quick_Stab(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Tackle"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Arms.Tackle(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Devour Essence"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Dark.Devour_Essence(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Spinning Back Kick"]:
                    Player_copy,Enemy1,Turn_Time,Player_Skip = EM.Melee_Moves.Legs.Spinning_Back_Kick(Player_Skip,Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Corrupting Touch"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Dark.Corrupting_Touch(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Purify"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Light.Purify(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Grappling Vines"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Nature.Grappling_Vines(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["River Fist"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Water.River_Fist(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Mud Shot"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Earth.Mud_Shot(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Stone Slipstream"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Wind.Stone_Slipstream(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Dominate"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Mind.Dominate(Player_copy,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Heal"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Support.Heal(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Axe Kick"]:
                    Player_copy,Enemy1,Turn_Time,Player_Skip = EM.Melee_Moves.Legs.Axe_Kick(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Toxin Spray"]:
                    Player_copy,Enemy1,Turn_Time = EM.Spell_Moves.Elemental.Dark.Toxin_Spray(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Blood Offering"]:
                    target = EM.Methods.Blood_Offering(target,typewriter)
                elif Move in ["Blood Frenzy"]:
                    target = EM.Methods.Blood_Frenzy(target,typewriter)
                elif Move in ["Aimed Shot"]:
                    Player_copy,Enemy1,Turn_Time = EM.Melee_Moves.Arms.Aimed_Shot(Player_copy,typewriter,Enemy1=Enemy1,Turn_Time=Turn_Time,target=target)
                elif Move in ["Summon"]:
                    target,Ally = EM.Spell_Moves.Arcane.Summon(target,typewriter)
                    target = Result["Returning"][0]
                    if Enemy2 == None:
                        Enemy2 = Result["Returning"][1]
                        b = 2
                    elif Enemy3 == None:
                        Enemy3 = Result["Returning"][1]
                        b = 3
        elif ratio > Attack_Chance and ratio <= Defense_Chance:                    
            Turn_Time -= Turn_Time
            if Enemy1["Mana"] > 10:
                Heal = (1+ (Enemy1["Max Health"]* 0.05))
                Heal = round(Heal)
                Enemy1["Mana"] -= (Enemy1["Mana"] * 0.1)
                Enemy1["Mana"] = round(Enemy1["Mana"])
                Enemy1["Health"] += Heal
                print(f"\n",Enemy1["Type"]," casts a heal spell\n")
                print(f"\n+ {Heal} health\n")
            else:
                print(f"\n",Enemy1["Type"]," does not have enough mana to cast a heal spell\n")
                print(f"\n",Enemy1["Type"]," braces to withstand your next attack\n")
                Enemy1["Defense"] += 10
                Defense1_Stopper = True

                
        elif ratio > Defense_Chance:
            Turn_Time -= Turn_Time
            Enemy1["Evasion"] += (Enemy1["Evasion"] * 0.1)
            Enemy1["Evasion"] = round(Enemy1["Evasion"])
            print(f"\n",Enemy1["Type"]," moves away growing wary\n")
            print("+ 10 Evasion")
            Evasion1_Stopper = True





        return  Enemy1,Enemy2,Enemy3,Player_copy,Evasion1_Stopper,Defense1_Stopper,Turn_Time,Player_Skip,Move,b

    def Enemy2_Battle(Enemy2,Player,Player_copy,Evasion2_Stopper,Defense2_Stopper,name,Game,Turn_Time,Player_Skip,typewriters):
        global typewriter
        typewriter = typewriters
        Attack_Weight = 0
        Defense_Weight = 0
        Evasion_Weight = 0
        Spell_Caster = False
        target = Enemy2
        
        if Enemy2["Category"] == "Undead":
            Attack_Weight += 3
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.3):
                Defense_Weight += 2
                Evasion_Weight += 2
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy2["Category"] == "Humanoid":
            Attack_Weight += 3
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.5):
                Defense_Weight += 3
                Evasion_Weight += 2
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy2["Category"] == "Demon":
            Attack_Weight += 4
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.5):
                Defense_Weight += 2
                Evasion_Weight += 2
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy2["Category"] == "Beast":
            Attack_Weight += 3
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.25):
                Defense_Weight += 2
                Evasion_Weight += 3
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy2["Category"] == "Abberation":
            Attack_Weight += 2
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.4):
                Defense_Weight += 3
                Evasion_Weight += 2
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
        if Enemy2["Category"] == "Construct":
            Attack_Weight += 3
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.6):
                Defense_Weight += 4
                Evasion_Weight += 2
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
        if Enemy2["Category"] == "Elemental":
            Attack_Weight += 4
            if Enemy2["Health"] < (Enemy2["Max Health"] * 0.5):
                Defense_Weight += 2
                Evasion_Weight += 2
            if Enemy2["Stamina"] <= 0:
                Attack_Weight = -100
        if Enemy2["Behaviour"] == "Aggressive":
            Attack_Weight += 2
        if Enemy2["Behaviour"] == "Defensive":
            Defense_Weight +=2
        if Enemy2["Behaviour"] == "Evasive":
            Evasion_Weight += 3
        if Enemy2["Spell Caster"] == True:
            Spell_Caster = random.choice([False,True])

        if "Venom" in Enemy2["Type"] or "Swamp" in Enemy2["Type"] or "Bog" in Enemy2["Type"] or "Acid" in Enemy2["Type"] or "Toxic" in Enemy2["Type"] or "Poison" in Enemy2["Type"]:
            print("Poison Activated")
            Enemy2["Attribute"] = "Poison"
        if "Rot" in Enemy2["Type"] or "Plague" in Enemy2["Type"] or "Disease" in Enemy2["Type"] or "Ruin" in Enemy2["Type"] or "Bone" in Enemy2["Type"]:
            print("Rot Activated")
            Enemy2["Attribute"] = "Decay"
        if "Ice" in Enemy2["Type"] or "Frost" in Enemy2["Type"] or "Frozen" in Enemy2["Type"] or "Snow" in Enemy2["Type"]:
            print("Ice Activated")
            Enemy2["Attribute"] = "Ice"
        if "Lightning" in Enemy2["Type"] or "Storm" in Enemy2["Type"] or "Tempest" in Enemy2["Type"] or "Thunder" in Enemy2["Type"] or "Charged" in Enemy2["Type"]:
            print("Lightning Activated")
            Enemy2["Attribute"] = "Lightning"
        if "Shadow" in Enemy2["Type"] or "Void" in Enemy2["Type"] or "Dark" in Enemy2["Type"] or "Night" in Enemy2["Type"] or "Phantom" in Enemy2["Type"] or "Lich" in Enemy2["Type"] or "Abyss" in Enemy2["Type"] or "Nightmare" in Enemy2["Type"] or "Demon Lord" in Enemy2["Type"] or "Cursed" in Enemy2["Type"]:
            print("Dark Activated")
            Enemy2["Attribute"] = "Dark"
        if "Alchemical" in Enemy2["Type"] or "Mutant" in Enemy2["Type"] or "Experiment" in Enemy2["Type"] or "Potion" in Enemy2["Type"] or "Mutation" in Enemy2["Type"] or "Living" in Enemy2["Type"] or "Mad Alchemist" in Enemy2["Type"] or "Tiny" in Enemy2["Type"] or "Chemical" in Enemy2["Type"]:
            print("Chemical Activated")
            Enemy2["Attribute"] = "Chemical"
        if "Fire" in Enemy2["Type"] or "Flame" in Enemy2["Type"] or "Burning" in Enemy2["Type"] or "Molten" in Enemy2["Type"] or "Inferno" in Enemy2["Type"] or  "Demon" in Enemy2["Type"] or "Ash" in Enemy2["Type"]:
            print("Fire Activated")
            Enemy2["Attribute"] = "Fire"
        if "Shield" in Enemy2["Type"] or "Stone" in Enemy2["Type"] or "Heavy" in Enemy2["Type"] or "Rust" in Enemy2["Type"] or "Steel" in Enemy2["Type"]:
            print("Defense Buff Activated")
            Enemy2["Defense"] += round(Enemy2["Defense"] * 0.01)


        if "Ritual" in Enemy2["Type"] or "Ancient" in Enemy2["Type"] or "Tomb" in Enemy2["Type"]:
            print("Cursed Activated")
            Enemy2["Attribute"] = "Cursed"
        if "Bridge" in Enemy2["Type"]:
            print("Bridge Attribute Activated")
            Enemy2["Attribute"] = "Bridge"
        if "Armory" in Enemy2["Type"]:
            print("Armor Activated")
            Enemy2["Activated"] = "Armory"
        if "Arena" in Enemy2["Type"]:
            print("Crowd Bonus")
            Enemy2["Attribute"] = "Crowd"

        if "Rogue" in Enemy2["Type"] or "Wind" in Enemy2["Type"] or "Dust" in Enemy2["Type"]:
            print("Agility Bonus")
            Enemy2["Attribute "] = "Agile"
            Enemy2["Speed"] += round(Enemy2["Speed"] * 0.01)
        if "War" in Enemy2["Type"]:
            Attack_Weight += 2
            Enemy2["Attack"] += round(Enemy2["Attack"] * 0.05)

            
        variance = random.choice(["Attack","Defense","Evasion"])
        if variance == "Attack":
            Attack_Weight += 3
        if variance == "Defense":
            Defense_Weight +=1
        if variance == "Evasion":
            Evasion_Weight +=1
        Action = max(Evasion_Weight,Attack_Weight,Defense_Weight)

        if Action == Attack_Weight:
            Turn_Time -= 0.5
            if  Spell_Caster == True:
                if Enemy2["Mana"] > 50:
                    Damage = int( 25   * Enemy2["Magic Damage"]    / ( Player_copy["Defense"]))    * (1 + Enemy2["Magic Density"] / 100)
                    Damage = round(Damage)
                    Enemy2["Mana"] -= 50
                    Player_copy["Health"] -= Damage
                    print(f"\n",Enemy2["Type"],f" casts mana blast at  {name}\n")
                    print(f"\n\n",Damage,"Damage done\n")
                    if Enemy2["Attribute"] == "Decay":
                        Decay = Player_copy["Health"] * 0.05
                        Decay = round(Decay)
                        Player_copy -= Decay
                        print("Decay does {Decay} damage")
                else:
                    print("\nThe enemy does not have enough mana\n")
            if  Spell_Caster == False:
                if (Enemy2["Stamina"] > 50 or Enemy2_Category == "Undead"):
                    Damage = int( 25 * Enemy2["Attack"])/ ( Player_copy["Defense"])
                    Damage = round(Damage)
                    Enemy2["Stamina"] -= 50
                    Player_copy["Health"] -= Damage
                    print(f"\n",Enemy2["Type"],f" strikes {name}\n")
                    print(f"\n\n",Damage,"Damage done\n")
                    if Enemy2["Attribute"] == "Decay":
                        Decay = Player_copy["Health"] * 0.05
                        Decay = round(Decay)
                        Player_copy -= Decay
                        print("Decay does {Decay} damage")
                else:
                    print("\nThe enemy does not have enough stamina\n")
        elif Action == Defense_Weight:
            Turn_Time -= Turn_Time
            if Enemy2["Mana"] > 10:
                Heal = (1+ (Enemy2["Max Health"]* 0.05))
                Heal = round(Heal)
                Enemy2["Mana"] -= 10
                Enemy2["Health"] += Heal
                print(f"\n",Enemy2["Type"],f" casts a heal spell\n")
                print(f"\n+{Heal} health\n")
            else:
                print(f"\n",Enemy2["Type"]," does not have enough mana to cast a heal spell\n")
                print(f"\n",Enemy2["Type"]," braces to withstand your next attack\n")
                Enemy2["Defense"] += 10
                Defense2_Stopper = True
        elif Action == Evasion_Weight:
            Turn_Time -= Turn_Time
            Enemy2["Evasion"] += 10
            print(f"\n",Enemy2["Type"]," moves away growing wary\n")
            print("+ 10 Evasion") 
            Evasion2_Stopper = True
        return Enemy2,Player_copy,Evasion2_Stopper,Defense2_Stopper,Turn_Time,Player_Skip

    def Enemy3_Battle(Enemy3,Player,Player_copy,Evasion3_Stopper,Defense3_Stopper,name,Game,Turn_Time,Player_Skip,typewriters):
        
        global typewriter
        typewriter = typewriters
        Attack_Weight = 0
        Defense_Weight = 0
        Evasion_Weight = 0
        Spell_Caster = False
        target = Enemy3

        
        if Enemy3["Category"] == "Undead":
            Attack_Weight += 3
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.3):
                Defense_Weight += 2
                Evasion_Weight += 2
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy3["Category"] == "Humanoid":
            Attack_Weight += 3
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.5):
                Defense_Weight += 3
                Evasion_Weight += 2
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy3["Category"] == "Demon":
            Attack_Weight += 4
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.5):
                Defense_Weight += 2
                Evasion_Weight += 2
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy3["Category"] == "Beast":
            Attack_Weight += 3
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.25):
                Defense_Weight += 2
                Evasion_Weight += 3
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
                
        if Enemy3["Category"] == "Abberation":
            Attack_Weight += 2
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.4):
                Defense_Weight += 3
                Evasion_Weight += 2
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
        if Enemy3["Category"] == "Construct":
            Attack_Weight += 3
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.6):
                Defense_Weight += 4
                Evasion_Weight += 2
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
        if Enemy3["Category"] == "Elemental":
            Attack_Weight += 4
            if Enemy3["Health"] < (Enemy3["Max Health"] * 0.5):
                Defense_Weight += 2
                Evasion_Weight += 2
            if Enemy3["Stamina"] <= 0:
                Attack_Weight = -100
        if Enemy3["Behaviour"] == "Aggressive":
            Attack_Weight += 2
        if Enemy3["Behaviour"] == "Defensive":
            Defense_Weight +=2
        if Enemy3["Behaviour"] == "Evasive":
            Evasion_Weight += 3
        if Enemy3["Spell Caster"] == True:
            Spell_Caster = random.choice([False,True])


        if "Venom" in Enemy3["Type"] or "Swamp" in Enemy3["Type"] or "Bog" in Enemy3["Type"] or "Acid" in Enemy3["Type"] or "Toxic" in Enemy3["Type"]:
            print("Poison Activated")
            Enemy3["Attribute"] = "Poison"
        if "Rot" in Enemy3["Type"] or "Plague" in Enemy3["Type"] or "Disease" in Enemy3["Type"] or "Ruin" in Enemy3["Type"] or "Bone" in Enemy3["Type"]:
            print("Rot Activated")
            Enemy3["Attribute"] = "Decay"
        if "Ice" in Enemy3["Type"] or "Frost" in Enemy3["Type"] or "Frozen" in Enemy3["Type"] or "Snow" in Enemy3["Type"]:
            print("Ice Activated")
            Enemy3["Attribute"] = "Ice"
        if "Lightning" in Enemy3["Type"] or "Storm" in Enemy3["Type"] or "Tempest" in Enemy3["Type"] or "Thunder" in Enemy3["Type"] or "Charged" in Enemy3["Type"]:
            print("Lightning Activated")
            Enemy3["Attribute"] = "Lightning"
        if "Shadow" in Enemy3["Type"] or "Void" in Enemy3["Type"] or "Dark" in Enemy3["Type"] or "Night" in Enemy3["Type"] or "Phantom" in Enemy3["Type"] or "Lich" in Enemy3["Type"] or "Abyss" in Enemy3["Type"] or "Nightmare" in Enemy3["Type"] or "Demon Lord" in Enemy3["Type"] or "Cursed" in Enemy3["Type"]:
            print("Dark Activated")
            Enemy3["Attribute"] = "Dark"
        if "Alchemical" in Enemy3["Type"] or "Mutant" in Enemy3["Type"] or "Experiment" in Enemy3["Type"] or "Potion" in Enemy3["Type"] or "Mutation" in Enemy3["Type"] or "Living" in Enemy3["Type"] or "Mad Alchemist" in Enemy3["Type"] or "Tiny" in Enemy3["Type"] or "Chemical" in Enemy3["Type"]:
            print("Chemical Activated")
            Enemy3["Attribute"] = "Chemical"
        if "Fire" in Enemy3["Type"] or "Flame" in Enemy3["Type"] or "Burning" in Enemy3["Type"] or "Molten" in Enemy3["Type"] or "Inferno" in Enemy3["Type"] or  "Demon" in Enemy3["Type"] or "Ash" in Enemy3["Type"]:
            print("Fire Activated")
            Enemy3["Attribute"] = "Fire"
        if "Shield" in Enemy3["Type"] or "Stone" in Enemy3["Type"] or "Heavy" in Enemy3["Type"] or "Rust" in Enemy3["Type"] or "Steel" in Enemy3["Type"]:
            print("Defense Buff Activated")
            Enemy3["Defense"] += round(Enemy3["Defense"] * 0.01)
        if "Ritual" in Enemy3["Type"] or "Ancient" in Enemy3["Type"] or "Tomb" in Enemy3["Type"]:
            print("Cursed Activated")
            Enemy3["Attribute"] = "Cursed"
        if "Bridge" in Enemy3["Type"]:
            print("Bridge Attribute Activated")
            Enemy3["Attribute"] = "Bridge"
        if "Armory" in Enemy3["Type"]:
            print("Armor Activated")
            Enemy3["Activated"] = "Armory"
        if "Arena" in Enemy3["Type"]:
            print("Crowd Bonus")
            Enemy3["Attribute"] = "Crowd"

        if "Rogue" in Enemy3["Type"] or "Wind" in Enemy3["Type"] or "Dust" in Enemy3["Type"]:
            print("Agility Bonus")
            Enemy3["Attribute "] = "Agile"
            Enemy3["Speed"] += round(Enemy3["Speed"] * 0.01)
        if "War" in Enemy3["Type"]:
            Attack_Weight += 2
            Enemy3["Attack"] += round(Enemy3["Attack"] * 0.05)
            
            
        variance = random.choice(["Attack","Defense","Evasion"])
        if variance == "Attack":
            Attack_Weight += 3
        if variance == "Defense":
            Defense_Weight +=1
        if variance == "Evasion":
            Evasion_Weight +=1
        Action = max(Evasion_Weight,Attack_Weight,Defense_Weight)

        if Action == Attack_Weight:
            Turn_Time -= 0.5
            if  Spell_Caster == True:
                if Enemy3["Mana"] > 50:
                    Damage = int( 25   * Enemy3["Magic Damage"]   / ( Player_copy["Defense"]))    * (1 + Enemy3["Magic Density"] / 100)
                    Damage = round(Damage)
                    Enemy3["Mana"] -= 50
                    Player_copy["Health"] -= Damage
                    print(f"",Enemy3["Type"],f" casts mana blast at  {name}\n")
                    print(f"\n\n",Damage,"Damage done")
                    if Enemy3["Attribute"] == "Decay":
                        Decay = Player_copy["Health"] * 0.05
                        Decay = round(Decay)
                        Player_copy -= Decay
                        print("Decay does {Decay} damage")
                else:
                    print("\nThe enemy does not have enough mana\n")
                
            if  Spell_Caster == False:
                if (Enemy3["Stamina"] > 50 or Enemy3_Category == "Undead") :
                    Damage = int( 25   * Enemy3["Attack"]   / (Player_copy["Defense"]))
                    Damage = round(Damage)
                    Enemy3["Stamina"] -= 50
                    Player_copy["Health"] -= Damage
                    print(f"\n",Enemy3["Type"],f" strikes {name}\n")
                    print(f"\n\n",Damage,"Damage done\n")
                    if Enemy3["Attribute"] == "Decay":
                        Decay = Player_copy["Health"] * 0.05
                        Decay = round(Decay)
                        Player_copy["Health"] -= Decay
                        print("Decay does {Decay} damage")
                else:
                    print("\nThe enemy does not have enough stamina\n")
        elif Action == Defense_Weight:
            Turn_Time -= Turn_Time
            if Enemy3["Mana"] >= 10:
                Heal = (1+ (Enemy3["Max Health"]* 0.05))
                Heal = round(Heal)
                Enemy3["Mana"] -= 10
                Enemy3["Health"] += Heal
                print(f"",Enemy3["Type"]," casts a heal spell\n")
                print(f"+{Heal} health\n")       
            else:
                print(f"\n",Enemy3["Type"]," does not have enough mana to cast a heal spell\n")
                print(f"\n",Enemy3["Type"]," braces to withstand your next attack\n")
                Enemy3["Defense"] += 10
                Defense3_Stopper = True
        elif Action == Evasion_Weight:
            Turn_Time -= Turn_Time
            Enemy3["Evasion"] += 10
            print(f"",Enzemy3["Type"]," moves away growing wary\n")
            print("+ 10 Evasion")
            Evasion3_Stopper = True
        return Enemy3,Player_copy,Evasion3_Stopper,Defense3_Stopper,Turn_Time,Player_Skip 
