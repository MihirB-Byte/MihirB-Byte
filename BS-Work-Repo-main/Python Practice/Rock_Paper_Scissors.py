""" import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + '  guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))  """


import random,sys

print(" Let play Rock Paper Scissors")



wins=0
loss=0
tie=0
random_num=0
gen_choice=0
Ch='y'



def rpsgen():
    random_num = random.randrange(1,3)
    ##print ("Working")
    return random_num


if __name__ == "__main__": 


    while Ch=='y':
        playerChoice= input("Please choose from 'R' 'P' and 'S' or 'q' to exit :")
        
        ##print(playerChoice)
        ##print(rpsgen())

        if playerChoice == "R":
            gen_choice= rpsgen()
            ##print("if condition R Main")
            if gen_choice==1:
                tie+=1
                print(" \n The match was tied")
            elif gen_choice==2:
                loss+=1
                print(" \n You lost this round")
            elif gen_choice==3:
                wins+=1
                print(" \n You won this round")
        elif playerChoice== "P":
            gen_choice= rpsgen()
            if gen_choice==1:
                wins+=1
                print(" \n You won this round")
            elif gen_choice==2:
                tie+=1
                print(" \n The match was tied")
            elif gen_choice==3:
                loss+=1
                print(" \n You lost this round")
        elif playerChoice=="S":
            gen_choice= rpsgen()
            if gen_choice==1:
                loss+=1
                print(" \n You lost this round")
            elif gen_choice==2:
                wins+=1
                print(" \n You won this round")
            elif gen_choice==3:
                tie+=1
                print(" \n The match was tied")
        elif playerChoice=="q":
            sys.exit()

        ##print(" \n Gen_choice = " + str(gen_choice))

        

        if gen_choice==1:
            gen_choice='Rock'
            ##print("R last condition ")
        elif gen_choice==2:
            gen_choice='Paper'
            ##print("P last condition ")
        elif gen_choice==3:
            gen_choice='Scissor'
            ##print("S last condition ") 
        
        
        if playerChoice=='R':
            playerChoice='Rock'
            ##print("R last condition ")
        elif playerChoice=='P':
            playerChoice='Paper'
            ##print("P last condition ")
        elif playerChoice=='S':
            playerChoice='Scissor'
            ##print("S last condition ")
        

        

        print(" For this round" + "\n player choice : " + str(playerChoice) + "\n Computer Generated : " + str(gen_choice) )    
        print('\n wins =' + str(wins) + ' Loss = ' + str(loss) + ' Tie = ' + str(tie))  

        Ch=input("Do you want to play again? Prss 'y' or 'n' :")


            

