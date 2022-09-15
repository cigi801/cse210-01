def main(spaces):
  main = (f"{spaces[1]}|{spaces[2]}|{spaces[3]}\n" 
              "-+-+-\n"
              f"{spaces[4]}|{spaces[5]}|{spaces[6]}\n"
              "-+-+-\n"
              f"{spaces[7]}|{spaces[8]}|{spaces[9]}")     
  print(main)

def check_turn(turn):
  if turn % 2 == 0: return 'X'
  else: return 'O'

def win(spaces):
  # check horizontal wins
  if (spaces[1] == spaces[2] == spaces[3]) \
    or (spaces[4] == spaces[5] == spaces[6]) \
    or (spaces[7] == spaces[8] == spaces[9]):
    return True
  # check vertical wins
  elif (spaces[1] == spaces[4] == spaces[7]) \
    or (spaces[2] == spaces[5] == spaces[8]) \
    or (spaces[3] == spaces[6] == spaces[9]):
    return True
  # check diagonal wins
  elif (spaces[1] == spaces[5] == spaces[9]) \
    or (spaces[3] == spaces[5] == spaces[7]):
    return True

  else: return False