from time import sleep


i = 1

while i > 0:

    player1 = str(input("Enter name of player: "))
    player2 = str(input("Enter name of opponent: "))
    move1 = str(input("Enter move for player: "))
    move2 = str(input('Enter move for opponent: '))


    if move1 == 'Rock' and move2 == 'Scissors':
        print("Player 1 wins!")
    elif move1 == 'Scissors' and move2 == 'Paper':
        print("Player 1 wins!")
    elif move1 == 'Paper' and move2 == 'Rock':
        print("Player 1 wins!")
    else:
        print("Opponent wins.")

    sleep(2)





    i+=1















