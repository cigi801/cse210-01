

from functions import main, check_turn, win


spaces = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
finished = False
turn = 0

while playing:
  main(spaces)
  print(' ')
  print(check_turn(turn) + "'s turn to choose a square (1-9)")
  print(' ')
  # input from player
  choice = input()
  print(' ')
  # checks for valid user input
  if str.isdigit(choice) and int(choice) in spaces:
    # checks if spot has already been taken
      if not spaces[int(choice)] in {"X", "O"}:
      # increment turns
        turn += 1
        spaces[int(choice)] = check_turn(turn)
  
      # check if game has ended
  if win(spaces): playing, finished = False, True
if finished:
  print("Good game. Thanks for playing!")
