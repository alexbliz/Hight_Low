from game_data import data 
import random 
from art import logo 
from art import vs 
from replit import clear 

score=0

def getindex():
  index=random.randint(0, len(data)-1)
  return index







def game(score):
 
  lets_start = True
  while lets_start == True:
    a=getindex()
    b=getindex()
    print(logo)
    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
    print(vs)
    print(f"Compare B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")
    guess=input("who has more followers? Type 'A' or 'B': ").lower()
    
    if guess =='a' and data[a]['follower_count'] > data[b]['follower_count']:
      score += 1
      clear()
      print(f"You are right! Corrent score: {score} ")
    else:
      lets_start = False
  return score









while True:
  score = game(score)
  print(f"Sorry that's wrong. final score: {score}")
  
  if input("start again? Type 'y' or 'n': ") != 'y':
    break
  else:
    score=0
    clear()
