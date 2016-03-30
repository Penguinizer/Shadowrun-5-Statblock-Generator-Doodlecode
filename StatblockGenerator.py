import random
import math
class StatBlock(object):
    def __init__(self, Body, Agility, Reaction, Strength, Charisma, Intuition, Logic, Will, Magic, Edge,
                Name, Metatype, PhysLimit, MentalLimit, SocialLimit, Equipment, Skills, ArmorValue, Iniative, Dicepool):

        self.Body = Body
        self.Agility = Agility
        self.Reaction = Reaction
        self.Strength = Strength
        self.Charisma = Charisma
        self.Intuition = Intuition
        self.Logic = Logic
        self.Will = Will
        self.Magic = Magic
        self.Edge = Edge
        self.Name = Name
        self.Metatype = Metatype
        self.PhysicalLimit = PhysLimit
        self.MentalLimit = MentalLimit
        self.SocialLimit = SocialLimit
        self.Equipment = Equipment
        self.Skills = Skills
        self.ArmorValue = ArmorValue
        self.Iniative = Iniative
        self.Dicepool = Dicepool

def GenerateStatblocks(EncounterInfo):
    EncounterStatblocks = []

    ## Call the function to generate an individual statblock for each instance of an enemy of a type.
    for x in range(0, EncounterInfo.BasicAmount):
        EncounterStatblocks.append(GenerateIndividualStatblock(EncounterInfo.PR, 1))

    for x in range(0, EncounterInfo.HeavyAmount):
        EncounterStatblocks.append(GenerateIndividualStatblock(EncounterInfo.PR, 2))

    for x in range(0, EncounterInfo.MageAmount):
        EncounterStatblocks.append(GenerateIndividualStatblock(EncounterInfo.PR, 3))

    for x in range(0, EncounterInfo.AdeptAmount):
        EncounterStatblocks.append(GenerateIndividualStatblock(EncounterInfo.PR, 4))

    return EncounterStatblocks

def GenerateIndividualStatblock(PR, Enemytype):
    ##Semirandom stats based on PR.
    random.seed()

    if PR == 1:
        Body = RandStat(2,2)
        Agility = RandStat(3,2)
        Reaction = RandStat(2,2)
        Strength = RandStat(3,2)
        Charisma = RandStat(2,2)
        Intuition = RandStat(2,2)
        Logic = 3
        Will = RandStat(3,2)
        Edge = PR

        if Enemytype == 3 or Enemytype == 4:
            Magic = RandStat(int(math.ceil(PR/2)), 3)

        else:
            Magic = 0

    elif PR == 2:
        Body = RandStat(3,2)
        Agility = RandStat(3,2)
        Reaction = RandStat(3,2)
        Strength = RandStat(4,2)
        Charisma = RandStat(3,2)
        Intuition = RandStat(3,2)
        Logic = RandStat(3,2)
        Will = RandStat(3,2)
        Edge = PR

        if Enemytype == 3 or Enemytype == 4:
            Magic = RandStat(int(math.ceil(PR/2)), 3)

        else:
            Magic = 0

    elif PR == 3:
        Body = RandStat(3,2)
        Agility = RandStat(4,2)
        Reaction = RandStat(3,2)
        Strength = RandStat(4,2)
        Charisma = RandStat(3,2)
        Intuition = RandStat(3,2)
        Logic = RandStat(3,2)
        Will = RandStat(3,2)
        Edge = PR

        if Enemytype == 3 or Enemytype == 4:
            Magic = RandStat(int(math.ceil(PR/2)), 3)

        else:
            Magic = 0

    elif PR == 4:
        Body = RandStat(3,3)
        Agility = RandStat(4,3)
        Reaction = RandStat(4,2)
        Strength = RandStat(4,2)
        Charisma = RandStat(3,2)
        Intuition = RandStat(3,3)
        Logic = RandStat(3,2)
        Will = RandStat(4,2)
        Edge = PR

        if Enemytype == 3 or Enemytype == 4:
            Magic = RandStat(int(math.ceil(PR/2)), 3)

        else:
            Magic = 0

    elif PR == 5:
        Body = RandStat(4,3)
        Agility = RandStat(5,3)
        Reaction = RandStat(4,3)
        Strength = RandStat(4,3)
        Charisma = RandStat(3,2)
        Intuition = RandStat(4,2)
        Logic = RandStat(4,2)
        Will = RandStat(4,3)
        Edge = PR

        if Enemytype == 3 or Enemytype == 4:
            Magic = RandStat(int(math.ceil(PR/2)), 3)

        else:
            Magic = 0

    elif PR == 6:
        Body = RandStat(5,3)
        Agility = RandStat(6,2)
        Reaction = RandStat(5,3)
        Strength = RandStat(5,5)
        Charisma = RandStat(4,2)
        Intuition = RandStat(4,3)
        Logic = RandStat(4,3)
        Will = RandStat(5,2)
        Edge = PR

        if Enemytype == 3 or Enemytype == 4:
            Magic = RandStat(int(math.ceil(PR/2)), 3)

        else:
            Magic = 0


    MetatypeRandInt = random.randint(0,100)
    ArmorValue = 0
    if MetatypeRandInt <= 40:
        Metatype = "Human"

    elif 40 < MetatypeRandInt <= 62:
        Metatype = "Ork"
        Body += 3
        Strength += 2
        Logic -= 1
        Charisma -= 1

    elif 62 < MetatypeRandInt <= 77:
        Metatype = "Elf"
        Agility += 1
        Charisma += 2

    elif 77 < MetatypeRandInt <= 91:
        Metatype = "Dwarf"
        Body += 2
        Reaction -= 1
        Strength +=2
        Will += 1

    else:
        Metatype = "Troll"
        Body += 4
        Agility -= 1
        Strength += 3
        Charisma -= 2
        Logic -= 1
        Intuition -= 1
        ArmorValue += 1

    ArmorValue += Body

    if Enemytype == 1:
        Name = "%s Generic Enemy" % Metatype

    elif Enemytype == 2:
        Name = "%s Heavy Weapons Specialist" % Metatype

    elif Enemytype == 3:
        Name = "%s Mage" % Metatype

    elif Enemytype == 4:
        Name = "%s Adept" % Metatype

    PhysLimit = round((Strength*2 + Agility + Reaction)/3)
    MentalLimit = round((Logic*2 + Intuition + Charisma)/3)
    SocialLimit = round((Charisma*2 + Will + 4)/3)

    if PR <= 3:
        SkillTempNumber = 3
    else:
        SkillTempNumber = PR

    Skills = "%i ranks in the Firearms, Melee Combat and Spellcasting groups, %i in Perception and other assorted skills." % (SkillTempNumber , (SkillTempNumber-1))

    if PR == 1:
        if Enemytype == 2:
            Equipment = "Knife (S+1, AP -1, Acc 5), Defiance T-250(Acc 4, DV 12P, AP +3), Armor Vest (9)"
            ArmorValue += 9

        elif Enemytype == 4:
            Equipment = "Club (S+3, AP -, Acc 4), Browning Ultra Power (Acc 5, DV 8P, AP-1) or Colt Government (Acc 6, DV 7, AP -1), Armor Vest (9)"
            ArmorValue += 9

        else:
            Equipment = "Knife (S+1, AP -1, Acc 5), Browning Ultra Power (Acc 5, DV 8P, AP-1) or Colt Government (Acc 6, DV 7, AP -1), Armor Vest (9)"
            ArmorValue += 9

    elif PR == 2:
        if Enemytype == 2:
            Equipment = "Knife (S+1, AP -1, Acc 5), Defiance T-250 (Acc 4, DV 12P, AP +3), Armor Vest (9), Ballistic Mask (2)"
            ArmorValue += 11

        elif Enemytype == 4:
            Equipment = "Club (S+3, AP -, Acc 4), Taurus Omni (Acc 5, DV 7P, AP-1) or Ceska Black Scorpion (Acc 5, DV 6p, AP-, burst), Armor Vest (9), Helmet (2)"
            ArmorValue += 11

        else:
            Equipment = "Knife (S+1, AP -1, Acc 5), Taurus Omni (Acc 5, DV 7P, AP-1) or Ceska Black Scorpion (Acc 5, DV 6p, AP-, burst), Armor Vest (9)"
            ArmorValue += 9

    elif PR == 3:
        if Enemytype == 2:
            Equipment = "Combat Knife (S+1, AP -2, Acc 6), Ruger 100 (Acc 6, DV 11P, AP -3) or Defiance T-250 (Acc 4, DV 12P, AP +3), Armor Jacket (12)"
            ArmorValue += 12

        elif Enemytype == 4:
            Equipment = "Sword (S+3, AP -2, Acc 6), Ares Predator (Acc 6, DV 8p, AP -1) or Remington Roomsweeper(Acc 4, 9P, AP +4, shotgun), Colt Cobra TZ-120 (Acc 5, DV 7p, AP-, FA) or HK-227 (Acc 7, Dv 7p, AP-, FA), Armor Jacket (12)"
            ArmorValue += 12

        else:
            Equipment = "Combat Knife (S+1, AP -2, Acc 6), Ares Predator (Acc 6, DV 8p, AP -1) or Remington Roomsweeper(Acc 4, 9P, AP +4, shotgun) ja Colt Cobra TZ-120 (Acc 5, DV 7p, AP-, FA) tai HK-227 (Acc 7, Dv 7p, AP-, FA), Armor Jacket (12)"
            ArmorValue += 12

    elif PR == 4:
        if Enemytype == 2:
            Equipment = "Combat Knife (S+1, AP -2, Acc 6), Ruger 100 (Acc 6, DV 11P, AP -3) or Ingram Valiant (Acc 6, DV 9P, AP -2, Full Auto), Armor Jacket (12), Helmet (2)"
            ArmorValue += 14

        elif Enemytype == 4:
            Equipment = "Sword (S+3, AP -2, Acc 6), Ares Predator (Acc 6, DV 8p, AP -1), Ingram Smartgun X (Acc 6, DV 8p, AP-) or AK-97 (Acc 5, DV 10p, AP -2, Burst/FA), Armor Jacket (12), Ballistic Mask (2)"
            ArmorValue += 14

        else:
            Equipment = "Combat Knife (S+1, AP -2, Acc 6), Ares Predator (Acc 6, DV 8p, AP -1), Ingram Smartgun X (Acc 6, DV 8p, AP-) or AK-97 (Acc 5, DV 10p, AP -2, Burst/FA), Armor Jacket (12)"
            ArmorValue += 12

    elif PR == 5:
        if Enemytype == 2:
            Equipment = "Katana (S+2, AP -3, Acc 6), Crocket EBR (Acc 6, DV 12P, AP -3, BF) or Enfield AS-7 (Acc 5, DV 15P, AP +3, BF, Shotgun), Full Body Armor (18)"
            ArmorValue += 18

        elif Enemytype == 4:
            Equipment = "Combat Axe (S+5, AP -4, Acc 5), Ruger Super Warhawk (Acc 5, Dv 9p, AP -2) or Ares Predator (Acc 6, DV 8p, AP -1), Yamaha Raiden (Acc 7, DV 11p, Ap -2. FA), Full Body Armor (18)"
            ArmorValue += 18

        else:
            Equipment = "Katana (S+2, AP -3, Acc 6), Ruger Super Warhawk (Acc 5, Dv 9p, AP -2) or Ares Predator (Acc 6, DV 8p, AP -1), Yamaha Raiden (Acc 7, DV 11p, Ap -2. FA), Full Body Armor (18)"
            ArmorValue += 18

    elif PR == 6:
        if Enemytype == 2:
            Equipment = "Katana (S+2, AP -3, Acc 6), Ruger Super Warhawk (Acc 5, Dv 9p, AP -2), Crocket EBR (Acc 6, DV 12P, AP -3, BF) or Enfield AS-7 (Acc 5, DV 15P, AP +3, BF, Shotgun), Full Body Armor (18)"
            ArmorValue += 18

        elif Enemytype == 4:
            Equipment = "Monofilament Whip (DV 12P, AP -8, Acc 7), Ruger Super Warhawk (Acc 5, Dv 9p, AP -2), Full Body Armor (18)"
            ArmorValue += 18

        else:
            Equipment = "Katana (S+2, AP -3, Acc 6), Ruger Super Warhawk (Acc 5, Dv 9p, AP -2), Ares Alpha (Acc 8, DV 11p, AP -2, FA. Underbarrel GL), Full Body Armor (18)"
            ArmorValue += 18

    if PR < 3:
        Iniative = "1d6+%i" %(Reaction+Intuition)
    elif 3 < PR < 5:
        Iniative = "2d6+%i" %(Reaction+Intuition)
    else:
        Iniative = "3d6+%i" %(Reaction+Intuition)

    Dicepool = SkillTempNumber + Agility

    ##Kerätään ja luodaan statblock joka palautetaan.
    GeneratedStatblock = StatBlock(Body, Agility, Reaction, Strength, Charisma, Intuition, Logic, Will, Magic, Edge,
                Name, Metatype,PhysLimit, MentalLimit, SocialLimit, Equipment, Skills, ArmorValue, Iniative, Dicepool)
    return GeneratedStatblock

def RandStat(base, added):
    stat = base + random.randint(0, added)
    return stat