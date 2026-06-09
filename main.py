import random
from words import word_list
from body import stages
import os

def get_word():
  key = random.choice(list(word_list.keys()))
  word = random.choice(word_list[key])
  return word.upper()


def play(word):
  word_completion = '_'*len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = len(stages)-1
  
  print("Let's play hangman!")
  print("\n")
  while not guessed and tries > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(stages[len(stages) - 1 - tries])
    print(word_completion)
    print(f"Tries left: {tries}")
    guess = input("Please guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      
      if guess in guessed_letters:
        print("You have already guessed this")
        continue
        
      elif guess not in word:
        print(guess,"is not in the word.")
        tries -= 1
        guessed_letters.append(guess)
        
      else:
        print("Good job",word,"is in the word")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        for i,letter in enumerate(word):
          if letter == guess:
            word_as_list[i] = guess
        word_completion = "".join(word_as_list)
        
          
        if '_' not in word_completion:
            guessed = True
        
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed that word")
        continue
      if guess != word:
        print("Wrong ",guess, " is not the word")
        tries -= 1
        guessed_words.append(guess)
      else:
        print("You got it!!", guess, "is in the word.")
        guessed = True
        word_completion = word
      
    else:
      print("Not a valid guess")


word = get_word()
play(word)
