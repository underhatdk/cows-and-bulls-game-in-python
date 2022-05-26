import random

def num_generator():
    num = random.randint(0,9999)
    num_str = str(num)
    com_num = num_str.zfill(4)
    return com_num
def player_input():
    while(True):
        try:
            global player_num
            z=player_num=input("Enter your  Number:")
            z=int(z)
            if(len(player_num)!=4):
                print("Enter a 4 digit number")
                continue
        except ValueError:
                 print("The input you entered is not a number")
        else:
            x=0
            for i in range(0,4):
                 x=x+1
            if(x!=4):
                 print("Enter a number with different digits")
                 continue
            else:
                 return

def num_comparison(a,b):
    a=str(a)
    b=str(b)
    for i in range(0,4):
        for j in range(0,4):
            if(i==j)and(a[i]==b[j]):
                global bull_count
                bull_count+=1
            elif(i!=j)and(a[i]==b[j]):
                global cow_count
                cow_count+=1
            else:
                pass
player_num=0
user_choice=True
while(user_choice):
    cow_count=0
    bull_count=0
    game_num=num_generator()
    score_counter=0
    while(True):
        player_input()
        score_counter=score_counter+1
        num_comparison(game_num,player_num)
        if(bull_count==4):
            print("Yes You Won")
            print("You have completed the game in",str(score_counter),"Moves")
            print("Do you want to play again")
            print("Enter \"y\" to play again")
            print("Enter anything to exit")
            choice=input("Enter your choice: ")
            if (choice=="y"):
                user_choice=True
            else:
                user_choice=False
                print("Bye Bye!!")
            break
        else:
            print("cow_count",cow_count)
            print("bull_count",bull_count)
            cow_count=0
            bull_count=0
