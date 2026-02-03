import random
import time

try:
    import winsound
    sound=True
except ImportError:
    sound=False

def beeb(freq,dur):
    if sound:
        winsound.beep(freq,dur)

def win_sound():
    winsound.Beep(1000, 300)

def lose_sound():
    winsound.Beep(400, 500)

def tie_sound():
    winsound.Beep(700, 300) 

options = ["rock", "paper", "scissors"]      
emoji={"rock":"⛰️","paper":"📄","scissors":"✂️"}
shortcuts={"r":"rock","p":"paper","s":"scissors"}

def get_user_choice():
    choice = input("Enter rock/paper/scissors(r/p/s): ").lower().strip()
    return shortcuts.get(choice, choice)

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice :
        return "tie"
    elif((user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper")):
        return "win"
    else:
        return "lose"    

def play_game():
    print(f"\n🎮 WELCOME TO CONSOLE-BASED ADVANCED ROCK-PAPER-SCISSORS GAME IN PYTHON 🎮!")  
    player_name=input("\n ✍️ Enter your name:")
    rounds=int(input("\n 🔢 How many rounds?(Best of):"))
    wins=losses=ties=0
    history=[]
    print("\nType 'quit' to stop playing.\n")

    for round_no in range(1,rounds+1):
        print(f"\n🔄 round{round_no}")
        user_choice=get_user_choice()
        if user_choice == "quit":
            break
        if user_choice not in options:            
            print("❌Invalid choice!. Try again!")          
            continue 

        computer_choice = random.choice(options) 
        print(f"\n{player_name} chose:{emoji[user_choice]} {user_choice}")    
        print(f"Computer chose: {emoji[computer_choice]}{computer_choice}")

        result=decide_winner(user_choice, computer_choice)

        if result == "win":
            print("🎊 You win!") 
            win_sound()           
            wins += 1 
        elif result == "lose":
            print("💔 You lose!")  
            lose_sound()          
            losses += 1
        else:
             print("🤝 It's a ties!") 
             tie_sound()         
             ties += 1   

        history.append((user_choice,computer_choice,result)) 
        time.sleep(0.5) 

    print("\n🏁 Final Results:") 
    print(f"👤 player:{player_name}")   
    print(f"🏆 Wins: {wins}")
    print(f"❌ Losses: {losses}")  
    print(f"🤝 ties:{ties}")

    if wins>losses:
        print("👨‍💻 overall winer:you!")
    elif losses>wins:
        print("💻 overall winner:computer!")  
    else:
        print("⚖️ match draw!") 

    print("\n📝 match history:")   
    for i, h in enumerate(history,1):
        print(f"round {i}:you({h[0]}) vs CPU({h[1]})→{h[2].upper()}")

    print("\n✌️ Thanks for playing!")   

while True:
    play_game()  

    replay=input("\n♻️ do you want to play again? (y/n):") .lower().strip()
    if replay != "y" :
        print(" Exiting game.Goodbye!👋")   
        break