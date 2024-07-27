import random

def snake(score,name):
    snakes_location={51:11,56:15,62:57,92:53,98:9}
    if score in snakes_location:
        score=snakes_location[score]
        print(name, "so sad you are eaten by snake oh....")
    return score
def climber(score,name):
    climber_location={2:38,4:14,9:31,33:85,80:99,52:88}
    if score in climber_location:
        score=climber_location[score]
        print(name, "Hurah you got climber....")
    return score

#execution
print("------Welcome to Snakes and Ladders-----")
print("To Win Reach 100")
print("Enter Player_1 name")
player1_name=input()
print("Enter Player_2 name")
player2_name=input()
print(player1_name,"Press_1 To Roll The Dice")

win=True
player1_score=0
player2_score=0
while(win):
    
    choice=int(input())
    dice_score=random.randint(1,6)
    print("Dice_Score : ",dice_score)
    if choice==1:
        player1_score+=dice_score
        player1_score=snake(player1_score,player1_name)
        player1_score=climber(player1_score,player1_name)
        print(player1_name,"You are at ",player1_score)
        print(player2_name,"Press_2 To Roll The Dice")
    elif choice==2:
        player2_score+=dice_score
        player2_score=snake(player2_score,player2_name)
        player2_score=climber(player2_score,player2_name)
        print(player2_name,"You are at ",player2_score)
        print(player1_name,"Press_1 To Roll The Dice")
    else:
        print("Invalid choice")
    if player1_score==100:
        print(player1_name,"Won The Game Congratulations")
        win=False
    elif player1_score==100:
        print(player2_name,"Won The Game Congratulations")
        win=False



