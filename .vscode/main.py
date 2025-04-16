def mountains_adventure():
    print("Welcome to the mountains!")
    start_health = 100

    # Round 1
    def mountains_adventure_round_1(current_health):
        print("Your friend has taken a rough fall a bit further up the slope. You call out their name, but they seem unresponsive.")
        print("You need to decide what to do next.")
        print("1. Check your surroundings for further danger")
        print("2. Immediately call for help")
        print("3. Act quick and approach your friend")

        choice = input("What will you choose? 1, 2 or 3? ")
        health_change = 0

        if choice == "2":
            print("Poor connection quality doesn’t let you get through to emergency services. Time was wasted.")
            health_change -= 20
        elif choice == "3":
            print("An approaching skier gently crashed into you, delaying your approach and putting yourself in danger.")
            health_change -= 20
        elif choice == "1":
            print("Seems pretty busy on the slope. You find a good time to run over to your friend.")
        else:
            print("Invalid choice. You hesitated while your friend is getting colder...")
            health_change -= 20

        updated_health = current_health + health_change
        print(f"Your friend's health is now {updated_health}")
        return updated_health

    # Round 2
    def mountains_adventure_round_2(current_health):
        print("\nYou have reached your friend, but they are in a bad state. You need to make a decision on how to proceed.")
        print("1. Ask your friend if they can hear you")
        print("2. Try to pull them onto their feet")
        print("3. Wait and observe a little more")

        choice = input("What will you choose? 1, 2 or 3? ")
        health_change = 0

        if choice == "1":
            print("Your friend is unresponsive.")
        elif choice == "2":
            print("Your friend is now clearly unresponsive and cannot use their legs.")
            health_change -= 20
        elif choice == "3":
            print("Your friend is getting colder.")
            health_change -= 20
        else:
            print("Invalid choice. You hesitated while your friend is getting colder...")
            health_change -= 20

        updated_health = current_health + health_change
        print(f"Your friend's health is now {updated_health}")
        return updated_health

    # Run both rounds in order
    health_after_round1 = mountains_adventure_round_1(start_health)
    health_after_round2 = mountains_adventure_round_2(health_after_round1)

    return health_after_round2


#def rainforest_adventure():
    #5 rounds of rainforest survival

#def desert_adventure():
    #5 rounds of desert survival

#main code
health = 100

while True:
    scenario = input("\nWhich scenario would you like to play?\n1 = Mountains \n2 = Rainforest \n3 = Desert \nYour choice: ")

    if scenario == "1":
        health = mountains_adventure()
        print(f"End of mountain scenario. Final health: {health}")
        break
    elif scenario == "2":
        print("Rainforest scenario coming soon!")
        break
    elif scenario == "3":
        print("Desert scenario coming soon!")
        break
    else:
        print("Invalid input, please try again.")