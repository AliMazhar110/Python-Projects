from hangman_art import*
from hangman_words import*
import random
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
index_list=list(range(word_length))
random.shuffle(index_list)
guessed_list=[]
for i in range(word_length):
  guessed_list.append("_")
for i in range((word_length-1)//2):
  ind = index_list.pop()
  guessed_list[ind] = chosen_word[ind]
guessed_word=[]
for word in guessed_list:
    guessed_word.append(word)
print(guessed_list)
trials = len(stages)-1
while "_" in guessed_list:
  if trials<0:
    break
  guess = input("Guess a letter: ").lower()
  
  if guess in guessed_word:
    print("You have already guessed this word.")
  elif guess in chosen_word:
    start=0
    guessed_word.append(guess)
    for letter in chosen_word:
        if letter == guess:
          index = chosen_word.index(letter,start,word_length)
          guessed_list[index] = letter
          start=index+1
  else:
    print(stages[trials])
    trials-=1
  print(guessed_list)
if "_" in guessed_list:
  print("You Lose")
else:
  print("\nThe Word is","".join(guessed_list))
  print("You Win")
