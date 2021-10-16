from art import logo
from random import choice
from replit import clear

#function to deal cards to the user
def deal_card():
  deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return choice(deck)

#initialising the card decks for both users
def start_game():
  computer_cards = []
  user_cards = []
  while len(user_cards)<2:
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
  if check_blackjack(computer_cards) or check_blackjack(user_cards):
    return has_blackjack(computer_cards, user_cards)
  else:
    return want_to_play(computer_cards, user_cards)

#check for blackjack
def check_blackjack(cards):
  if 10 in cards and 11 in cards:
    return True
  else:
    return False

#one player has a blackjack
def has_blackjack(computer_cards,user_cards):
  sum_users = sum(user_cards)
  sum_computer = sum(computer_cards)
  if check_blackjack(user_cards):
    sum_users = 0
  else:
    sum_computer = 0
  if sum_users == 0 or sum_computer == 0:
    if sum_users==0:
      result = "You have a blackjack! You win."
    elif sum_computer==0:
      result = "Lose, Opponent has a blackjack."
  print(f"\tYour final hand: {user_cards}, final score: {sum_users}\n\tComputer's final hand: {computer_cards}, final score: {sum_computer}")
  return result

#checking if the user wants to continue playing
def want_to_play(computer_cards,user_cards):
  playing = True
  while playing:
    computer_cards, sum_computer = values(computer_cards)
    user_cards, sum_users = values(user_cards)
    print(f"\tYour cards: {user_cards}, current score: {sum_users}\n\tComputer's first card: {computer_cards[0]}")
    value = values(user_cards)[1]
    if value > 21:
      playing = False
    else:
      option = input("Type 'y' to get another card, type 'n' to pass: ")
      if option=='n':
        playing = False
      elif option=='y':
        user_cards.append(deal_card())
      else:
        option = input("Please enter valid value, either 'y' or 'n': ")
  while sum(computer_cards)<17:
    computer_cards.append(deal_card())
  return winner(computer_cards, user_cards)

#checking the sum of cards for user and computer
def values(cards):
  total = 0
  for card in range(len(cards)):
    if cards[card]==11:
      if total+cards[card]>21:
        total += 1
        cards[card] = 1
      else:
        total += 11
    else:
      total += cards[card]
  return cards, total

#declaring the result of the game
def winner(computer_cards,user_cards):
  computer_cards, sum_computer = values(computer_cards)
  user_cards, sum_users = values(user_cards)
  print(f"\tYour final hand: {user_cards}, final score: {sum_users}\n\tComputer's final hand: {computer_cards}, final score: {sum_computer}")
  result = ""
  if sum_users>21:
    result = "You wentover. You lose."
  elif sum_users<=21:
    if sum_users<sum_computer:
      if sum_computer<=21:
        result = "You lose."
      elif sum_computer>21:
        result = "Opponent went over. You win."
    elif sum_users>sum_computer:
      result = "You win."
    else:
      result = "It's a draw."
  return result

#initiate blackjack game
def play_blackjack():
  clear()
  print(logo)
  game_result = start_game()
  print(game_result)

#asking user if they want to play a game
play = True
while play:
  to_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
  if to_play=='y':
    play_blackjack()
  elif to_play=='n':
    play = False
  else:
    print("Please enter either 'y' or 'n'.")
