import random as rd

print("Welcom to Chan Ken Pon! ._.")

listChankenpon =["Rock", "Paper", "Scissors"]
computerWin = 0
humanWin = 0
tie = 0

running = True

while running:
    user_Choice = input("Enter 'Rock', 'Paper' or 'Scissors' (or 'quit' to stop playing): ")
    chan_ken_pon = rd.choice(listChankenpon)
    print(f"Computer choose {chan_ken_pon}")
    if user_Choice == "quit":
        break
    elif user_Choice == chan_ken_pon:
        print("Draw for you guys")
        tie +=1
    else:
        if (user_Choice == "Rock" and chan_ken_pon == "Paper") or (user_Choice == 'Scissors' and chan_ken_pon == "Rock") or (user_Choice == "Paper" and chan_ken_pon == "Scissors"):
            print("Computer win")
            print("You lose this round")
            computerWin += 1            
        elif (user_Choice == "Rock" and chan_ken_pon == "Scissors") or (user_Choice == 'Scissors' and chan_ken_pon == "Paper") or (user_Choice == "Paper" and chan_ken_pon == "Rock"):
            print("Human win")
            print("You win this round")            
            humanWin += 1   
    print(f"Score - Win: {humanWin} Losses: {computerWin} Ties: {tie}")
    playMore = input("Do you want to play again(yes/no)._. " )
    if playMore == "yes":
        continue
    else:
        print(f"Thanks for playing! Final Scores - Wins: {humanWin}, Losses: {computerWin}, Ties: {tie}")
        running = False


