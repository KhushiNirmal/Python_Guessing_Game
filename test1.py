
# import random
# random.randint(1,50)    

# for i in range(10):
#     print(random.randint(1,50))


# Guessing Game
# 1. Python will guess one game in a range of 1 to 50 numbers
# 2. Take users input in UserNum
# 3.If UserNum is near +-10 digits to the actual number give 10 points
# 4. else if UserNum is near +-5 digits to the actual number give 5 points
# 5. else if UserNum is exactly the same give 50 points
# 6. show the output and score


import random

def guessGame():
    playA = 'y'
    score= 0
    while playA == 'y':
        computerNum = random.randint(1,50)
        userNum = int(input("\n Enter a number between 1 to 50 - "))

        diff = computerNum - userNum
        if computerNum == userNum:
            print("Its the same number, wow you get 50 Points ")
            score = score + 50
            print("Your updated score is ",score )
        elif diff >= -5 and   diff <=5:
            print("This number is very close to real number ")  
            print(" userNum = ", userNum)
            print(" computerNum = ", computerNum)
            score = score + 25
            print ("Your updated score is ", score)
        elif diff >= -10 and diff <= 10:
            print("This number is close to real number ")  
            print(" userNum = ", userNum)
            print(" computerNum = ", computerNum)
            score = score + 10
            print ("Your updated score is ", score)
        else:
            print("Sorry your guess didn't make it ")
            print(" userNum = ", userNum)
            print(" computerNum = ", computerNum)
            print ("Your updated score is ", score)

        playA = input("\n\n Do you want to play again 'y/n ")    
    else:
            print("Final Score = ", score)

def playAgain():        #Recursive function
    pg = input("\n\n Do you want to play again 'y/n ")  
    if pg == 'y' or pg == 'n' :
        return pg
    else:
      pg =  playAgain()   
      
guessGame() 
