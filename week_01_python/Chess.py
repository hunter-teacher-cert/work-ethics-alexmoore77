# Alex Moore 
# git hub alexmoore77
# Beginning Chess:  2-Player Edition is designed to allow two players to enjoy the wonderful game of chess!

#initilizing board globally so it does not need to be passed among functions

board=[
  ['R','N','B','Q','K','B','N','R'],
  ['P','P','P','P','P','P','P','P'],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],
  [' ',' ',' ',' ',' ',' ',' ',' '],  
  ['P','P','P','P','P','P','P','P'],
  ['R','N','B','Q','K','B','N','R']
]

def drawBoard(  ):
  print('\n\n\n\n\n\n\n\n\n\nWelcome to Beginning Chess!\n')
  #print('What is your name?')    # ask for their name
  #myName = input()
  #print('It is good to meet you, ' + myName)
  #print('The length of your name is:')
  #print(len(myName))
  #print('What is your age?')    # ask for their age
  #myAge = input()
  #print('You will be ' + str(int(myAge) + 1) + ' in a year.')
  counter=8
  for (x) in board:
    print(x)
  print('\n\n\n\n\n\n\n\n\n\n');

drawBoard()