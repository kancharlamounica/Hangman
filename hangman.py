import random
import time
import os
os.system('clear')
def hangman(fail):
     if fail == 0:
         print("__________\n|         \n|         \n|         \n|         \n|         \n|         \n|         ")
     if fail == 1:
         print("__________\n|        |\n|         \n|         \n|         \n|         \n|         \n|         ")
     if fail == 2:
         print("__________\n|        |\n|        O\n|         \n|         \n|         \n|         \n|         ")
     if fail == 3:
         print("__________\n|        |\n|        O\n|        |\n|         \n|         \n|         \n|         ")
     if fail == 4:
         print("__________\n|        |\n|        O\n|       _|_\n|       \n|         \n|         \n| ")
     if fail == 5:
         print("__________\n|        |\n|        O\n|       _|_\n|        | \n|          \n|          \n|          ")
     if fail == 6:
         print("__________\n|        |\n|        O\n|       _|_\n|       /| \n|          \n|          \n|          ")
     if fail == 7:
         print("__________\n|        |\n|        O\n|       _|_\n|       /|\ \n|         \n|         \n|          ")
     if fail == 8:
         print("__________\n|        |\n|        O\n|       _|_\n|       /|\ \n|        | \n|       \n|          ")
     if fail == 9:
         print("__________\n|        |\n|        O\n|       _|_\n|       /|\ \n|        | \n|      _/ \n|  ")
     if fail == 10:
         print("__________\n|        |\n|        O\n|       _|_\n|       /|\ \n|        |\n|      _/ \_\n|    ")
def hangman_check(alpha):
     fail, chances = 0, 10
     while fail <= chances:
         if dash == list(word):
             print("Congratulations! You won!")
             break
         elif fail == chances:
             print("Game Over! \n The word which made you to lose your lives is",word.upper())
             break
         alpha = input("Guess a letter: ")
         if alpha in guesses:
             print("You've already entered this letter:")
         else:
             guesses.append(alpha)
             if  alpha in word:
			     dash[word.index(alpha)] = alpha
             else:
  			     fail += 1
                 print("Ohhh! It's wrong \n You lost", fail ,"lives")
                 time.sleep(0.3)
                 hangman(fail)
                 time.sleep(0.3)
           print(' '.join(dash))
         print("Guessed letter:",guesses)
def run(choice):
     if (choice.lower()) == 'yes':
         print(("_ "*len(word)) ,len(word), "letters")
         return(hangman_check(choice))
     else:
         print("Bye Bye!")
words = ['flux','quiz', 'crazy', 'ready','working', 'game', 'friends', 'computer', 'wise', 'talent', 'life', 'smile', 'beauty', 'sock', 'nature', 'love', 'joy', 'waltz', 'brick','hungry    ', 'isograms', 'handsome', 'film', 'music', 'heart', 'cigar', 'magic', 'tiger', 'liar', 'dog', 'donkey', 'monkey', 'browse', 'joker', 'road','throne','superman','spiderman', 'compile']
print("                                  Welcome to Hangman!")
word, guesses, name = random.choice(words), [], input("\n        Your name please:")
dash = list("_" * len(word))
print(" Hello", name, "!")
print("Let's see if you can guess the word!")
time.sleep(0.5)
print("\n  You just have 10 lives \n  whenever you guess the word wrong you lose one \n  Guess the word to survive \n          All the best!")
time.sleep(3)
choice = input("  Dare to die? say yes/no:")
run(choice)
        