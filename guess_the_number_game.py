logo="""

 _____                       _____ _            _   _                 _                
|  __ \                     |_   _| |          | \ | |               | |               
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|    
                                                                                       
                                                                                       

"""
import random
def checker(my_guess, your_guess,):
    if my_guess > your_guess :
        print("Too Low")
        return False

    elif my_guess < your_guess:
        print("Too High")
        return False

    elif my_guess == your_guess:
        print(f"Yeahh you got it , The guess is {my_guess}")
        return True

p=-1
attempts =0
game_isover=True
print(logo)
print("Welcome to The Number Guessing Game:")
print("I'm thinking of a number between 0 and 100")
pd=input("Choose the difficulty of the game (easy or hard):").strip().lower()
while game_isover:
    if pd =="easy":
        attempts=10
        my_guess=random.randint(0,100)
        while attempts:
            your_guess=int(input("Make a guess"))
            if checker(my_guess,your_guess,):
                break
            attempts=attempts-1
            print(f"you have {attempts} attempts left")
        if attempts==0:
            print("all attempts are over you losse the game ")
        game_isover=False
    if pd =="hard":
        attempts=5
        my_guess = random.randint(0, 100)
        while attempts:
            your_guess = int(input("Make a guess"))
            if checker(my_guess, your_guess, ):
                break
            attempts = attempts - 1
            print(f"you have {attempts} attempts left")
        if attempts == 0:
            print("all attempts are over you losse the game ")
        game_isover = False
