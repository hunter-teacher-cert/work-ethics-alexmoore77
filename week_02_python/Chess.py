# Alex Moore 
# git hub alexmoore77
# Beginning Chess:  2-Player Edition is designed to allow two players to enjoy the wonderful game of chess!

#initilizing board globally so it does not need to be passed among functions
#my plan for later is possibly to create classes for these and corresponding global objects with getter and setter functions to minimize global variable issues.
annotation=""
player1=""
player2=""
board=[
  ['[ R ]','[ N ]','[ B ]','[ Q ]','[ K ]','[ B ]','[ N ]','[ R ]'],
  ['[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]'],
  ['[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]'],
 ['[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]'],
  ['[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]'],
  ['[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]'],
  ['[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]'],
  ['[_R_]','[_N_]','[_B_]','[_Q_]','[_K_]','[_B_]','[_N_]','[_R_]']
]

#return the value at the entered square of the board
def pieceReturn(myLetter, myNumber)
  return piece

#return an updated annotatation string that includes the most recent move
def annotationAdd(myAnnotation, myPiece, myFrom, myTo, myTurn)
  return myAnnotation+' '+ myPiece+myFrom+'-'+myTo

#draw the board by traversing the multidimensional array with nested while loops
def drawBoard(  ):
  print('\n\n\n\n\n\n\n\n\n\nBeginning Chess!\n')
  print('            '+player1+'               ')
  print('   A    B    C    D    E    F    G    H')
  counter=8
  myRow=7
  myCol=0
  while myRow >= 0:
    print (str(counter), end='')
    while myCol < 8:
      print (str(board[myRow][myCol]), end='')
      myCol=myCol+1
    print('') 
    myRow=myRow-1
    counter=counter-1
    myCol=0
  #for (x) in board:
  #  print(str(counter)+' '+str(x))
  #  counter=counter+1
  print('            '+player2+'               ')
  print('\n\n\n\n\n\n\n\n\n\n');

#Change any square by altering the value it holds.  This is used when a piece moves off of a square and when it moves on to a new square.
def modifySquare(myLetter, myNumber, myChar ):
  if myLetter=='A' or myLetter=='a':
    myLetterConverted=0
  if myLetter=='B' or myLetter=='b':
    myLetterConverted=1
  if myLetter=='C' or myLetter=='c':
    myLetterConverted=2
  if myLetter=='D' or myLetter=='d':
    myLetterConverted=3
  if myLetter=='E' or myLetter=='e':
    myLetterConverted=4
  if myLetter=='F' or myLetter=='f':
    myLetterConverted=5
  if myLetter=='G' or myLetter=='g':
    myLetterConverted=6
  if myLetter=='H' or myLetter=='h':
    myLetterConverted=7
  myNumberConverted=(int(myNumber)-1)

  print ('myLetterConvered is equal to '+str(myLetterConverted))
  print (' myNumberConvered is equal to '+str(myNumberConverted))
#store the board charater
  tempBoardChar=  board[myNumberConverted][myLetterConverted]
  board[myNumberConverted][myLetterConverted]=myChar
  return tempBoardChar

drawBoard()

print('Please enter the name of player 1:')
player1=input()
print('Welcome, '+ player1 +'!  Now enter the name of player 2.')
player2=input()
print('\n\n\n\n\n\n\n\n\n\nWelcome to Beginning Chess!\n')

drawBoard()


turn=0

#take turns
while (1==1):
  
  #Identify whose turn it is
  turn=turn+1
  if turn % 2 == 0:
    thisPlayer=player1
  if turn %2 ==1:
     thisPlayer=player2
  print ('The turn is '+str(turn)+'.  The player is '+thisPlayer)
  drawBoard();
annotationAdd()
  print (thisPlayer+ ', from what square will you move your piece?')
  start=input()
  print (thisPlayer+ ', to what square would you like to move this piece?')
  destination=input()
  print('Move: '+start+' to '+destination)
  startLetterFrom=start[:1]
  startNumberFrom=start[1:2]
  destinationLetterTo=destination[:1]
  destinationNumberTo=destination[1:2]
  print('startLetterFrom: '+startLetterFrom)
  print('startNumberFrom: '+startNumberFrom)
  print('destinationLetterTo: '+destinationLetterTo)
  print('destinationNumberTo: '+destinationNumberTo)
  
  modifySquare(destinationLetterTo, destinationNumberTo, modifySquare(startLetterFrom, startNumberFrom, '[___]')
  )
  #The modifySquare() for the destination square empties that square and returns the character of the piece that was there.  The modfifySquare for the destination square places that piece at that square
  #modifySquare(destinationLetterTo, destinationNumberTo, 'P')