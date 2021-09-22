# Alex Moore 
# git hub alexmoore77
# Beginning Chess:  2-Player Edition is designed to allow two players to enjoy the wonderful game of chess!

#initilizing board globally so it does not need to be passed among functions
player1=""
player2=""
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
  counter=8
  for (x) in board:
    print(x)
  print('\n\n\n\n\n\n\n\n\n\n');

def getUserInfo():
  print('Please enter the name of player 1:')
  player1=input()
  print('Welcome, '+ player1 +'!  Now enter the name of player 2.')
  player2=input();
  


drawBoard()
getUserInfo()