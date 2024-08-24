# Using for loop to compare a user_word and a com_word to give an output
# METHOD 1
def word_check_1(com_word, user_word):

                hint = list(user_word) # Turns the user_word to a list inorder to be used as a hint
                signal = 0 # Increases for any letter in the the word and in the right position
                dups = [] # Takes in letters in the right position as elements
                for j, u in enumerate(user_word): # loops through the user_word and it's indexes
               
                    if u in com_word:     
                        if u == com_word[j]: # checks if a letter is in com_word and in the right position
                            signal +=1
                            hint[j] = u
                            dups.append(u)
                    else:
                         hint[j] = "#" # accounts for elements in user_word that are not in com_word 
                for j, u in enumerate(user_word):
                    u_count1 = user_word.count(u) # counts how many times an element u appears in user_word
                    u_count2 = com_word.count(u) # counts how many times an elenment u appears in com_word
                    u_count3 = dups.count(u) # counts how many times an element u appears in dups list
                    u_count4 = user_word[0:j+1].count(u) # counts how many times an element u appears in user_word from the start of user_word to that element
                    if u in com_word:     
                        if u != com_word[j] and u in dups: # accounts for an element u that is not equal to an element in com_word that is in the same index, also the element is present in dups
                            if u_count1 > u_count2 and u_count3 == u_count2: 
                                hint[j] = "#"
                            elif u_count1 > u_count2 and u_count3 < u_count2 and u_count4 <= u_count2:
                                hint[j] = "_"
                                print(u)
                            elif u_count1 > u_count2 and u_count3 < u_count2 and u_count4 > u_count2:
                                 hint[j] ="#"
                            else:
                                hint[j] ="_"
                        elif u != com_word[j] and u not in dups: # accounts for an element u that is not equal to an element in com_word that is in the same index, the element is not present in dups
                            if u_count1 > u_count2 and u_count4 <= u_count2:
                                hint[j] = "_"
                            elif u_count1 > u_count2 and u_count4 > u_count2:
                                hint[j] = "#"
                            else:
                                hint[j] = "_"
                    else:
                        hint[j] = " #"
            
                return hint,signal
'''com_word = 'ACCOMMODATE'
user_word = input("guess the word:")
game = word_check_1(com_word, user_word)
print(game)'''



# METHOD 2 ( Using nested for loop)

def word_check_2(com_word, user_word):
            if len(user_word) != len(com_word) or user_word.islower():
                print("wrong input: check word length or capitalize input")
            else:
                hint = list(user_word)
                dups = ""
                signal = 0
                for j, u in enumerate(user_word):
            
                    for i, c in enumerate(com_word):
                        
                        if u in com_word:   
                            if u == c and j == i:
                                dups += u   

                print(dups)
                for j, u in enumerate(user_word):
                    u_count3 = user_word.count(u)
                    u_count2 = com_word.count(u)
                    for i, c in enumerate(com_word):

                        if u in com_word:
                            if u == c and j == i:
                                signal +=1
                                hint[j] = u
                                break
                                
                            elif u == c and j != i:
                                cu_count = user_word[0:i].count(u)
                                cu_count2 = user_word[0:j+1].count(u)
                                
                                if u in dups:
                                    cu_count1 = dups.count(u)
                                    if u_count3 > u_count2 and cu_count1 == u_count2:
                                        hint[j] = "#"
                                        
                                    elif u_count3 > u_count2 and cu_count1 < u_count2 and cu_count2 <= u_count2:
                                        hint[j] = "_"    
                                        print(u)
                                    elif u_count3 > u_count2 and cu_count1 < u_count2 and cu_count2 > u_count2:
                                        hint[j] = "#"
                                    elif u_count3 <= u_count2:
                                        hint[j] ="_"                  
                                else:
                                    if cu_count2 <= u_count2:
                                        hint[j] = "_"
                                    else:
                                        hint[j] = "#"              
                        else:
                            hint[j] = "#"
                
            return hint,signal
'''com_word = 'APPETITE'
user_word = input("guess the word:")
game = word_check_2(com_word, user_word)
print(game)'''