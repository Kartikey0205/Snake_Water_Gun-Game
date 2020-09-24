import random

characterOfGame = ["s", "w", "g"]
total_Chance = 10
no_of_chance = 0
computer_Score = 0
your_score = 0

print("Welcome to Snake Water Gun Game ")
print("You have Total 10 Chances to play this Game in one time \n BEST OF LUCK ")
# print("Press \n s for Snake \n w for water \n g for gun")
while no_of_chance < total_Chance:
    takeCharacterFrom_User = input("Press \n s for Snake \n w for water \n g for gun\n")
    computer_Charcter = random.choice(characterOfGame)

    # Draw Case
    if takeCharacterFrom_User == computer_Charcter:
        print("Match draw you and computer both played the same character")
        print("Both will gain 0 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances  \n ")

    # First Case
    elif takeCharacterFrom_User == 's' and computer_Charcter == 'w':
        print("Wow you had win this chance ")
        print("You  will gain 1 points and computer gain 0 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances  \n ")
        your_score = your_score + 1


    # second Case
    elif takeCharacterFrom_User == 's' and computer_Charcter == 'g':
        print("Oooopppss  you had lost this chance and Computer wins this time ")
        print("You  will gain 0 points and computer gain 1 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances  \n ")
        computer_Score = computer_Score + 1

    # third Case
    elif takeCharacterFrom_User == 'w' and computer_Charcter == 's':
        print("Oooopppss  you had lost this chance and Computer wins this time ")
        print("You  will gain 0 points and computer gain 1 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances \n ")
        computer_Score = computer_Score + 1

    # Fourth Case
    elif takeCharacterFrom_User == 'w' and computer_Charcter == 'g':
        print("Wow you had win this chance ")
        print("You  will gain 1 points and computer gain 0 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances \n ")
        your_score = your_score + 1

        # Fifth Case
    elif takeCharacterFrom_User == 'g' and computer_Charcter == 'w':
        print("Oooopppss  you had lost this chance and Computer wins this time ")
        print("You  will gain 0 points and computer gain 1 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances \n ")
        computer_Score = computer_Score + 1

        # sixth Case
    elif takeCharacterFrom_User == 'g' and computer_Charcter == 's':
        print("Wow you had win this chance ")
        print("You  will gain 1 points and computer gain 0 points ")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if (remainingChances > 1):
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances \n ")
        your_score = your_score + 1

        # Last Case

    else:
        print("Enter Invalid Character")
        no_of_chance = no_of_chance + 1
        remainingChances = total_Chance - no_of_chance
        if remainingChances > 1:
            print(f"Play Again because you have {remainingChances} more chances\n ")
        else:
            print(f"Ooopss !! you have {remainingChances}  chances \n ")

print("GAME OVER !!! ")

if your_score > computer_Score:
    print(
        f"Congratulations !! You have won this Game \n Your score is {your_score} \nAnd\n Computer score is {computer_Score}")

elif computer_Score > your_score:
    print(
        f"Oooopssss !! You have lost this Game \n Your score is {your_score} \nAnd\n Computer score is {computer_Score}\nCongratulations Computer for winning "
        f"this Game")
else:
    print(
        f"Wow !! I am surprised You both had Score equally \n Your score is {your_score} \nAnd\n Computer score is {computer_Score}")

print("Thank you for Playing The game hope you had enjoyed  !! ")



"""
My SCORE ---

Welcome to Snake Water Gun Game 
You have Total 10 Chances to play this Game in one time 
 BEST OF LUCK 
Press 
 s for Snake 
 w for water 
 g for gun
s
Oooopppss  you had lost this chance and Computer wins this time 
You  will gain 0 points and computer gain 1 points 
Play Again because you have 9 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
w
Match draw you and computer both played the same character
Both will gain 0 points 
Play Again because you have 8 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
g
Wow you had win this chance 
You  will gain 1 points and computer gain 0 points 
Play Again because you have 7 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
w
Wow you had win this chance 
You  will gain 1 points and computer gain 0 points 
Play Again because you have 6 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
g
Match draw you and computer both played the same character
Both will gain 0 points 
Play Again because you have 5 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
s
Match draw you and computer both played the same character
Both will gain 0 points 
Play Again because you have 4 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
s
Match draw you and computer both played the same character
Both will gain 0 points 
Play Again because you have 3 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
w
Oooopppss  you had lost this chance and Computer wins this time 
You  will gain 0 points and computer gain 1 points 
Play Again because you have 2 more chances
 
Press 
 s for Snake 
 w for water 
 g for gun
g
Match draw you and computer both played the same character
Both will gain 0 points 
Ooopss !! you have 1  chances 
 
Press 
 s for Snake 
 w for water 
 g for gun
s
Wow you had win this chance 
You  will gain 1 points and computer gain 0 points 
Ooopss !! you have 0  chances 
 
GAME OVER !!! 
Congratulations !! You have won this Game 
 Your score is 3 
And
 Computer score is 2
Thank you for Playing The game hope you had enjoyed  !! 

"""