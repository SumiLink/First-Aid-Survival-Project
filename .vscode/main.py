def mountains_adventure():
    print("Welcome to the mountains!")
    print("Your friend has taken a rough fall a bit further up the slope, you need to help them! You call out their name, however they seem unresponsive.")
    print("You need to decide what to do next")

    print("1. Check your surroundings for further danger")
    print("2. Immediately call for help")
    print("3. Act quick and approach your friend")

    choice = input("What will you choose? 1,2 or 3?")
    
    health_change = 0

    if choice == "2":
        print("Poor connection quality doesnt let you get through to emergency services. Time was wasted.")
        health_change -=20
    elif choice == "3":
        print("An approaching skier gently crashed into you, delaying your approach and putting yourself in danger.")
        health_change -=20
    elif choice == "1":
        print("Seems pretty busy on the slope, various skiers speed past you. You find a good time to run over to your friend")
    else:
        print ("Invalid choice. You hesitated whilst your friend is getting colder...")
        health_change -=20

    return health_change
#def rainforest_adventure():
    #5 rounds of rainforest survival

#def desert_adventure():
    #5 rounds of desert survival

health = 60

while True:
    scenario = input("Which scenario would you like?: ")

    if scenario == ("1"):
        print ("Welcome to the mountains!")
        health += mountains_adventure()
        break
    elif scenario == ("2"):
        print ("Welcome to the rainforest!")
        break
    elif scenario == "3":
        print ("Welcome to the desert!")
        break
    else:
        print ("Incorrect input, please try again!")

