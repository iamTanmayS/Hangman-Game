import random
from Hangman_ascii_designs import *
from Hangman_random_words import *

word_list = random_word
print(hangman_logo)
chosen_word = list(random.choice(word_list))
blank = []
for i in chosen_word:
    blank.append(" ")  
wrong = 0  

while blank != chosen_word:
    guess = input("\nEnter your guessed letter :  ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                blank[i] = guess
    else: 
        wrong = wrong+1
        print("incorrect Guess")
        if wrong == 0 :
            print(wrong_guess1)
        elif wrong == 1:
            print(wrong_guess2)
        elif wrong == 2:
            print(wrong_guess3)
        elif wrong == 3:
            print(wrong_guess4)
        elif wrong == 4:
            print(wrong_guess5)
        if wrong == 6:
                print(f'''{Hangman_died}
                           {lose} ''')  
                break

if blank == chosen_word:
    print(won)
    print("The Correct Word is : ")
    for i in chosen_word:
        print(i,end= "" )
        
else:
    print("The Correct Word is : ")
    for i in chosen_word:
        print(i,end= "" )
  
            
  
    
