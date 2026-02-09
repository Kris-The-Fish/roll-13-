
error = "please enter an integer more than ? equal to 13."

while True:
    try:
        Game_goal = int(input("what is the game goal?"))

        if Game_goal < 13:
            print(error)
        else:
            print(f"Game goal: {Game_goal}")
            break

    except ValueError:
        print(error)

