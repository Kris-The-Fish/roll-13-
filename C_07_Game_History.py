
# initialise list to hold game history
game_history = []

# get data (base component does this already, code below fore testing purposes)

while True:
    round_played = input("Round? ")
    if round_played == "":
        break

    user_points = int(input("User points? "))
    comp_points = int(input("Computer points? "))
    winner = input("Who won? ")
    user_score = int(input("User Score: "))
    comp_score = int(input("Computer Score: "))

    game_results = (f"Round {round_played}: User Points: {user_points} | "
                    f"Computer Point {comp_points}, {winner} wins "
                    f"{user_score} | {comp_score}")

    game_history.append(game_results)

print("Game History")

for item in game_history:
    print(item)

