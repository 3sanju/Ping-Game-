import random

def roll():
    min=1
    max=6
    roll=random.randint(min,max)
    return roll

while True:
    players=input("Enter the number of players between (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("Number of players should be between (2-4)")
    else:
        print("Invalid Player Number,Try Again!!")

max_score=50
players_score=[0 for _ in range(players)]

while max(players_score)< max_score:
    for player_indx in range(players):
     print("\n Player Number",player_indx+1,"Turn has just started!!\n")
     print("\n Your Total Score",players_score[player_indx])
     current_score=0
     while True:
       should_roll=input("You want to roll the dice (y) ")
       if should_roll.lower() != "y":
         break
       value =roll()
       if value ==1:
        current_score =0
        print("Turn Down!!")
        break
       else:
        current_score +=value
        print("You rolled a number",value)

       print("Your current score is ",current_score)

     players_score[player_indx] +=current_score
     print("Your Total Score will be ", players_score[player_indx])

max_score=max(players_score)
winning_indx =players_score.index(max_score)
print("Player Number",player_indx+1,"is winning with the score of ",max_score)

