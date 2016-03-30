def PrintStatblocks(Statblocks):
    correctanswer = False
    while correctanswer == False:
        tempinput = input("Name of file statblocks will be stored in:  ")
        if tempinput:
            correctanswer = True

    filename = tempinput+".txt"
    file = open(filename, 'w')

    for unit in Statblocks:
        file.write("Name: " + unit.ReturnName() + '\n' + "Statline: Bod: " + str(unit.ReturnBody()) + ", Agi: " +
                   str(unit.ReturnAgility()) + ", Rea: " + str(unit.ReturnReaction()) + ", Str: " + str(unit.ReturnStrength()) +
                   ", Cha: " + str(unit.ReturnCharisma()) + ", Int: " + str(unit.ReturnIntuition()) + ", Log: " +
                   str(unit.ReturnLogic()) + ", Wil: " + str(unit.ReturnWill()) + ", Mag: " + str(unit.ReturnMagic()) +
                   ", Edg: " + str(unit.ReturnEdge()) + '\n' + "Limits: Physical Limit: " + str(unit.ReturnPhysicalLimit()) +
                   ", Mental Limit: " + str(unit.ReturnMentalLimit()) + ", Social Limit: " + str(unit.ReturnSocialLimit()) +
                   '\n' + "Equipment: " + unit.ReturnEquipment() + '\n' + "Soak Pool: " + str(unit.ReturnArmorValue()) +
                   ", Iniative: " + unit.ReturnIniative() + '\n' + "Skills: " + unit.ReturnSkills() + '\n' +
                   "Adept Powers and Ware as wished, but assume to be included in statlines. Add more if you wish.\n\n")

    file.close()

    return