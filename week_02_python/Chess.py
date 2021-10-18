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
#def pieceReturn(myLetter, myNumber)
#  return piece

#return an updated annotatation string that includes the most recent move
#def annotationAdd(myAnnotation, myPiece, myFrom, myTo, myTurn)
#  return myAnnotation+' '+ myPiece+myFrom+'-'+myTo

#draw the board by traversing the multidimensional array with nested while loops
def drawBoard(annotation):
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
  print('\n\n')
  print(annotation)
  print('\n\n\n\n\n\n\n\n');

#recursively check all possible moves for the rook.  Add each possible move to a list, and return the list.
def rookAvailableMovesListReturn(myLetter, myNumber, myChar):
  myConvertedLetter=convertLetter(myLetter)
  myConvertedNumber=convertNumber(myNumber)

#base case for recursive functions
#how to make recursive function?


#convert chess annotation letter to a 0-index list value.
def convertLetter(myLetter):
  if myLetter=='A' or myLetter=='a':
    return 0
  if myLetter=='B' or myLetter=='b':
    return 1
  if myLetter=='C' or myLetter=='c':
    return 2
  if myLetter=='D' or myLetter=='d':
    return 3
  if myLetter=='E' or myLetter=='e':
    return 4
  if myLetter=='F' or myLetter=='f':
    return 5
  if myLetter=='G' or myLetter=='g':
    return 6
  if myLetter=='H' or myLetter=='h':
    return 7

#convert chess annotation number to a 0-index list value
def convertNumber(myNumber):
  return (int(myNumber)-1)

def pieceAtSquare(myLetterFrom, myNumberFrom):
  myLetterConverted=convertLetter(myLetterFrom)
  myNumberConverted=convertNumber(myNumberFrom)
  return board[myNumberConverted][myLetterConverted]

def updateAnnotation(myLetterFrom, myNumberFrom, myLetterTo,myNumberTo, annotation, turn):
#Find the piece at the square passed in, and isolate the letter.  Follow that with the letter and the number.
  myPiece=pieceAtSquare(myLetterFrom, myNumberFrom)[2:3]
  myDestination=pieceAtSquare(myLetterTo,myNumberTo)[2:3]
  if myDestination=='_':
    mySymbol=''
  elif myDestination!='_':
    mySymbol='x'
  if myPiece=='P' and mySymbol!='x':
    myPiece=''
  elif myPiece=='P' and mySymbol=='x':
    myPiece=myLetterFrom

  if turn%2==1:
    print('It is turn 1!')
    annotation+='\n'+str(turn)+'. '+myPiece+mySymbol+myLetterTo+myNumberTo
  if turn%2==0:
    print('It is turn 2!')
    annotation+='    ' +str(turn)+'. '+myPiece+mySymbol+myLetterTo+myNumberTo
    
  print ('Annotation:'+annotation)
  return annotation

#Change any square by altering the value it holds.  This is used when a piece moves off of a square and when it moves on to a new square.
def modifySquare(myLetter, myNumber, myChar ):
  myLetterConverted=convertLetter(myLetter)
  myNumberConverted=convertNumber(myNumber)

  print ('myLetterConvered is equal to '+str(myLetterConverted))
  print (' myNumberConvered is equal to '+str(myNumberConverted))
  #store the board character
  tempBoardChar=  board[myNumberConverted][myLetterConverted]
  board[myNumberConverted][myLetterConverted]=myChar
  return tempBoardChar

drawBoard(annotation)

print('Please enter the name of player 1:')
player1=input()
print('Welcome, '+ player1 +'!  Now enter the name of player 2.')
player2=input()
print('\n\n\n\n\n\n\n\n\n\nWelcome to Beginning Chess!\n')

drawBoard(annotation)


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
  drawBoard(annotation)
  #annotationAdd()
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

  annotation=updateAnnotation(startLetterFrom, startNumberFrom, destinationLetterTo, destinationNumberTo, annotation, turn)
  print('Annotation:\n'+annotation)


  modifySquare(destinationLetterTo, destinationNumberTo, modifySquare(startLetterFrom, startNumberFrom, '[___]')
  )
  #The modifySquare() for the destination square empties that square and returns the character of the piece that was there.  The modfifySquare for the destination square places that piece at that square
  #modifySquare(destinationLetterTo, destinationNumberTo, 'P')