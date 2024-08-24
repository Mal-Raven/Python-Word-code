import json 
import random as r
from word_check import word_check_1 as chk_wrd

with open("dict.json") as dictionary: # opens the "dictionary.json" file and names it "Dictionary"
    py_dict = json.load(dictionary) # converts the json file to a python file and assigns it to a variable 
sorted_dict = dict(sorted(py_dict.items())) # sorts the py_dict dictionary based on its keys and converts them to a python dictionary
words_list = []

for sd in sorted_dict.keys(): # loops through the dictionary keys
    words_list.append(sd) # appends the keys to the "words_list" list
ask = input("play word guess?:y/n \n")
if "y" in ask:
    print("hint: '#' = letter is not in word, '_' = letter is in word but in wrong place")
    word_len = 3 # The starting lenght of word
    game_over = False
    score = 0
    while word_len < 13 and game_over == False:  # condition for the loop to keep flowing
        
        pick_words = []
        for word in words_list: #loops through the words in the word_list
            if len(word) == word_len and word[0:word_len] != "-": 
                pick_words.append(word) # appends words whose lenght is equal to the word_len variable and the word does start with a "-" to the pick_words list
        com_word = str(r.choice(pick_words)) # picks a word from the pick_words list at random and converts it to a string 
        print(com_word)
        mean_word = f"word meaning: {sorted_dict[com_word]}" # prints the value of the word which is the meaning of the word from the sorted_dict dictionary
        print(mean_word)
        print(f"hint:The word is a {word_len} letter word \n") # gives a clue of the lenght of the word picked at random from the pick_words list
        
        tries = 4 # number of tries to guess the com_word
        while tries > 0:
            user_word = input("Guess the word:") # Asks the user to guess the word based on the meaning of the word
            if len(user_word) != word_len or user_word.islower(): # Checks if the user_word is the same lenght and capitalized as the picked word 
                print("wrong input: check word length or capitalize input")
            else:
                hint, signal = chk_wrd(com_word, user_word) # checks the user_word against the com_word and gives hint based on how related both are

                if signal == word_len: # compares the signal against the lenght of the word
                    print("You are correct!!!")
                    score += 10
                    break
                else:
                    print(hint)
                    print(f"you have {tries-1} tries left \n{mean_word}")
                    tries -= 1
            
        else:
            game_over = True # if user doesn't guess the right word within the given number of tries, game_over is made True inorder to terminate the outer loop
            print(f"The word is {com_word}")        
            print(f"GAME OVER! \nYour score is {score}" )
        word_len += 1
    else:
        if game_over == True: # checks why the outer loop ended, if it is because game_over was made True or because the loop finished without being interrupted    
            pass
        else:
            print("You won the game !!!")       
elif "n" in ask:
    print("GAME OVER!")
else:
    print("wrong input") 