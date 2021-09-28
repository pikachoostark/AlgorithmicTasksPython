import random


def rock_paper_scissors():
    print("=== ROCK PAPER SCISSORS ===")
    input("== TO BEGIN PRESS ENTER  ==")
    comp_num = random.randint(1, 3)
    if comp_num == 1:
        comp_turn = "Rock"
    elif comp_num == 2:
        comp_turn = "Paper"
    else:
        comp_turn = "Scissors"
    player_turn = input("YOUR TURN: ")
    print("COMPUTER TURN: {0}".format(comp_turn))
    if (comp_turn == "Rock" and player_turn == "Paper") or \
            (comp_turn == "Paper" and player_turn == "Scissors") or \
            (comp_turn == "Scissors" and player_turn == "Rock"):
        print("=== YOU WIN! ===")
    elif comp_turn == player_turn:
        print("=== DRAW! ===")
    else:
        print("=== YOU LOOSE! ===")
