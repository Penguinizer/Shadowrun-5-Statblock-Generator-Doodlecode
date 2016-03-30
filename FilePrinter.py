def PrintStatblocks(Statblocks):
    correctanswer = False
    while correctanswer == False:
        tempinput = input("Name of file statblocks will be stored in:  ")
        if tempinput:
            correctanswer = True

    filename = tempinput+".txt"
    file = open(filename, 'w')

    for unit in Statblocks:
        file.write("Name: " + unit.Name + '\n' + "Statline: Bod: " + str(unit.Body) + ", Agi: " +
                   str(unit.Agility) + ", Rea: " + str(unit.Reaction) + ", Str: " + str(unit.Strength) +
                   ", Cha: " + str(unit.Charisma) + ", Int: " + str(unit.Intuition) + ", Log: " +
                   str(unit.Logic) + ", Wil: " + str(unit.Will) + ", Mag: " + str(unit.Magic) +
                   ", Edg: " + str(unit.Edge) + '\n' + "Limits: Physical Limit: " + str(unit.PhysicalLimit) +
                   ", Mental Limit: " + str(unit.MentalLimit) + ", Social Limit: " + str(unit.SocialLimit) +
                   '\n' + "Equipment: " + unit.Equipment + '\n' + "Soak Pool: " + str(unit.ArmorValue) +
                   ", Iniative: " + unit.Iniative + ", Offensive Dicepool: " + str(unit.Dicepool) +'\n' + "Skills: " + unit.Skills + '\n' +
                   "Adept Powers and Ware as wished, but assume to be included in statlines. Add more if you wish.\n\n")

    file.close()

    return