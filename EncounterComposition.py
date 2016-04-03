class EncounterInfo(object):
    def __init__(self, Type, SubType, PR, BasicMembers, HeavyMembers, MageMembers, AdeptMembers):
        self.Type = Type
        self.SubType = SubType
        self.PR = PR
        self.BasicAmount = BasicMembers
        self.HeavyAmount = HeavyMembers
        self.MageAmount = MageMembers
        self.AdeptAmount = AdeptMembers

def GatherEncounterInfo():
    ## First get the type of encounter.
    ## Loop used to get a new input if first is incorrect.
    CorrectAnswer = False
    while CorrectAnswer == False:
        try:
            Type = int(input("Select encounter type:\n 1: Gang\n 2: Corporate Security\n 3: KnightErrant Team\n 4: Opposing Team\n 5: Custom\n Selection:"))

            if 0 < Type <= 5:
                CorrectAnswer = True

        except ValueError:
            print("Requires Number")

    ## Second, get subtype of ecnounter.
    CorrectAnswer = False
    if Type == 1:
        while CorrectAnswer == False:
            try:
                SubType = int(input("Select type of gang:\n 1: Wizgang\n 2: Policlub\n 3: Organized crime group\n 4: Generic\n Selection:"))

                if 0 < SubType <=4:
                    CorrectAnswer = True

            except ValueError:
                print("Requires Number")

    elif Type == 2:
         while CorrectAnswer == False:
            try:
                SubType = int(input("Select level of team:\n 1: Light guards\n 2: Heavy guards\n 3: Armed response team\n 4: HRT\n Selection:"))

                if 0 < SubType <=4:
                    CorrectAnswer = True

            except ValueError:
                print("Requires Number")

    elif Type == 3:
         while CorrectAnswer == False:
            try:
                SubType = int(input("Select level of team:\n 1: Standard Patrol\n 2: Armed response team\n 3: HRT\n Selection:"))

                if 0 < SubType <=4:
                    CorrectAnswer = True

            except ValueError:
                print("Requires Number")

    else:
        SubType = 0
    ## PR determined based on encounter types. Otherwise takes user input.
    if Type == 1 and SubType == 1:
        PR = 2

    elif Type == 1 and SubType == 2:
        PR = 1

    elif Type == 1 and SubType == 3:
        PR = 4

    elif Type == 1 and SubType == 4:
        PR = 1

    elif Type == 2 and SubType == 1:
        PR = 2

    elif Type == 2 and SubType == 2:
        PR = 3

    elif Type == 2 and SubType == 3:
        PR = 4

    elif Type == 2 and SubType == 4:
        PR = 5

    elif Type == 3 and SubType == 1:
        PR = 3

    elif Type == 3 and SubType == 2:
        PR = 4

    elif Type == 3 and SubType == 3:
        PR = 5

    elif Type == 4:
        PR = 6

    else:
        CorrectAnswer = False
        while CorrectAnswer == False:
            try:
                temp = int(input("Input PR between 1 and 6: "))
                if 0 < temp <= 6:
                    CorrectAnswer = True
                    PR = temp
            except ValueError:
                print("Requires Number")

    ## Print recommended amounts based on types.
    if Type == 1 and SubType == 1:
        print("Wizgang squad. \n Recommended composition: 1-2 Mage, 0-1 Adept, 4-7 Basic ganger.\n")

    elif Type == 1 and SubType == 2:
        print("Humanis/Policlub mob. \n Recommended composition: 0-1 Mage, 1 Heavy, 6-10 Basic ganger.\n")

    elif Type == 1 and SubType == 3:
        print("Organized crime group (Mafia, Yakuza, etc). \n Recommended composition: 0-1 Mage. 0-1 Adept, 1 Heavy, 4-6 Basic ganger.\n")

    elif Type == 1 and SubType == 4:
        print("Generic gang. \n Recommended composition: 0-1 Adept, 0-1 Heavy, 7-10 Basic ganger\n")

    elif Type == 2 and SubType == 1:
        print("Corporate security patrol. \n Recommended composition: 0-1 Mage, 4-5 Basic guard.\n")

    elif Type == 2 and SubType == 2:
        print("Corporate heavy patrol. \n Recommended composition: 1 Mage, 0 Adept, 1 Heavy, 2-3 Basic guard.\n")

    elif Type == 2 and SubType == 3:
        print("Corporate armed response team. \n Recommended composition: 1 Mage, 0-1 Adept, 1 Heavy, 4-7 Basic guard.\n")

    elif Type == 2 and SubType == 4:
        print("Corporate high threat response. \n Recommended composition: 1-2 Mage, 0-2 Adept, 1-2 Heavy, 3-6 Basic soldier.\n")

    elif Type == 3 and SubType == 1:
        print("Knight Errant patrol. \n Recommended composition: 0-1 Mage, 3-5 Generic officer. \n")

    elif Type == 3 and SubType == 2:
        print("Knight Errant armed response team. \n Recommended composition: 1 Mage, 0-1 Adept, 0-1 Heavy, 3-5 Generic Officer. \n")

    elif Type == 3 and SubType == 3:
        print("Knight Errant High Threat Response. \n Recommended composition: 1-2 Mage, 1-2 Heavy, 5-7 Generic officer. \n")

    elif Type == 4:
        print("Opposing Team. \n Recommended composition: 1-2 Mage, 0-1 Adept, 1-2 Heavy, 1-3 Basic.\n")

    else:
        print("Untyped Encounter. No recommendations. \n")

    ## Take inputs for amounts.
    for x in range(0,4):
        CorrectAnswer = False
        while CorrectAnswer == False:
            if x == 0:
                try:
                    BasicMembers = abs(int(input("\n Select amount of basic members: ")))
                    CorrectAnswer = True
                except ValueError:
                    print("Requires Number.\n")

            elif x == 1:
                try:
                    HeavyMembers = abs(int(input("\n Select amount of heavy weapons members: ")))
                    CorrectAnswer = True
                except ValueError:
                    print("Requires Number.\n")

            elif x == 2:
                try:
                    MageMembers = abs(int(input("\n Select amount of mages: ")))
                    CorrectAnswer = True
                except ValueError:
                    print("Requires Number.\n")

            elif x == 3:
                try:
                    AdeptMembers = abs(int(input("\n Select amount of adepts: ")))
                    CorrectAnswer = True
                except ValueError:
                    print("Requires Number:\n")


    ##Generate statblock object and return.
    GeneratedEncounter = EncounterInfo(Type, SubType, PR, BasicMembers, HeavyMembers, MageMembers, AdeptMembers)
    return GeneratedEncounter
