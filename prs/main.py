import random


ops = {
    'r': 'rock', 
    'p': 'paper', 
    's': 'scissors'
    }
cpu = random.choice(list(ops.keys()))


def determine_winner(player, cpu):
    if player == cpu:
        print(f"Both players selected {player}. It's a tie!")
    elif player == 'r':
        if player == 'sc':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == 'p':
        if player == 'r':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == 's':
        if player == 'p':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


while True:
    player = input("Enter a choice (rock[R], paper[P], scissors[S]): ")
    if player.lower() not in ops.keys():
        print("Option does not match")
        continue
    else:
        print("Its now time for CPU choice\n")
        print("==================================")
        print("CPU Choice is (%s)" %cpu)

        print("Player(%s)" % ops[player] + ":" + "CPU(%s)" %cpu)


    determine_winner(player, cpu)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break