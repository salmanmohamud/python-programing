# Choose some good hangman words for your program. You can go to this website and create a list of words for your game.
# At the start of the game, use the random library to choose a random word from your hangman words and display the word's letters as dashes rather than letters.
# Now, apply the input function to allow the user to make letter guesses. Use try... except and if statements to make sure that only valid inputs work with your script i.e. a user can only choose one letter at a time, and a user cannot choose letters that have been chosen before.
# If the letter is in the word then it is printed in place of the corresponding dash. If the letter is not in the word, that is counted as a failed attempt, Limit the number of failed attempts for the user to 6 such that on the 6th fail, the game ends and the script prints the actual word and "You Lost". Make sure to tell the user they won if they guess all the correct letters in under 6 failed attempts.
# If you want to take the project a notch higher, you can use the Python Turtle Library to visualize the hanging like in this website. This is optional!

# naming, choosing the list and number of fails
name= "nairobi"
letters=[]
fail=0

# for loop choosing any greater range and comparing the number of fails and then braking the loop
for i in range(20):
    if fail== 5:
        print("failed")
        break 
# choosing the lenght of the dash(hangman) and putting it as a variable   
    Blank= "-"*len(name)
    #[1,2,2,3,4,5]
# creating another loop with a character in the letter variable to play with
    for y in letters:
 #choosing the same character in the name of the hangman
        if y in name:
 # choosing the position of the letter in the actual hangman name
            index=name.index(y)
 # creating a list for the dashes of the hangman to be filled
            split=list(Blank)
 #replacing the dashes with actual hangman letters correct ones
            split[index]=y
 # now adding or joining the actual name into the empty dashes 
            Blank=''.join(split)
 # creating a condition of when the user finshes filling in the dahes   
    if "-" not in Blank:
        print("DONE")
        break
#user will be able to the the blank or dashes
    print(Blank)
    Enter = input("Fill in The Dashes ")
# this is for conditioning when the user writes a wrong letter or else add the right letter into the dash
    if Enter not in name:
        print("fail")
        fail=fail+1
    else:
        letters.append(Enter)
        





    


            























