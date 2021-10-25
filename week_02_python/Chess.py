# Alex Moore 
# git hub alexmoore77
# Beginning Chess:  2-Player Edition is designed to allow two players to enjoy the wonderful game of chess!

#KEY NOTE:  Due to the moat of ?, the annotations in the main functions are off.  Whenever the coordinates are passed in as arguments the functions, they are passed in with the offset so that little to no modification needs to take place in the functions themselves.

#initilizing board globally so it does not need to be passed among functions
#my plan for later is possibly to create classes for these and corresponding global objects with getter and setter functions to minimize global variable issues.
annotation=""
player1=""
player2=""
#note the mote of ?? to avoid array out of bounds errors
board=[
  ['[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]', '[ ? ]', '[ ? ]', '[ ? ]' ],
['[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]', '[ ? ]', '[ ? ]', '[ ? ]' ],

  ['[ ? ]','[ ? ]','[ R ]','[ N ]','[ B ]','[ Q ]','[ K ]','[ B ]','[ N ]','[ R ]','[ ? ]','[ ? ]'],
  ['[ ? ]','[ ? ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ P ]','[ ? ]','[ ? ]'],
  ['[ ? ]','[ ? ]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[ ? ]','[ ? ]'],
 ['[ ? ]','[ ? ]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[ ? ]','[ ? ]'],
  ['[ ? ]','[ ? ]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[ ? ]','[ ? ]'],
  ['[ ? ]','[ ? ]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[___]','[ ? ]','[ ? ]'],
  ['[ ? ]','[ ? ]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[_P_]','[ ? ]','[ ? ]'],
  ['[ ? ]','[ ? ]','[_R_]','[_N_]','[_B_]','[_Q_]','[_K_]','[_B_]','[_N_]','[_R_]','[ ? ]','[ ? ]'],
['[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]', '[ ? ]', '[ ? ]', '[ ? ]' ],
['[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]','[ ? ]', '[ ? ]', '[ ? ]', '[ ? ]' ]

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
  counter=10
  myRow=9
  myCol=2
  while myRow >= 2:
    print (str(counter-2), end='')
    while myCol < 10:
      print (str(board[myRow][myCol]), end='')
      myCol=myCol+1
    print('') 
    myRow=myRow-1
    counter=counter-1
    myCol=2
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




#convert chess annotation letter to a 0-index list value.
def convertLetter(myLetter):
  if myLetter=='A' or myLetter=='a':
    return 2
  if myLetter=='B' or myLetter=='b':
    return 3
  if myLetter=='C' or myLetter=='c':
    return 4
  if myLetter=='D' or myLetter=='d':
    return 5
  if myLetter=='E' or myLetter=='e':
    return 6
  if myLetter=='F' or myLetter=='f':
    return 7
  if myLetter=='G' or myLetter=='g':
    return 8
  if myLetter=='H' or myLetter=='h':
    return 9

#convert chess annotation number to a 0-index list value
def convertNumber(myNumber):
  return (int(myNumber)-1)

def pieceAtSquare(myLetterFrom, myNumberFrom):
  myLetterConverted=convertLetter(myLetterFrom)
  myNumberConverted=convertNumber(myNumberFrom)
  return board[myNumberConverted][myLetterConverted]

#Find the piece at the square passed in, and isolate the letter.  Follow that with the letter and the number.
def updateAnnotation(myLetterFrom, myNumberFrom, myLetterTo,myNumberTo, annotation, turn):
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
    annotation+='\n'+str(turn)+'. '+myPiece+mySymbol+myLetterTo+str(int(myNumberTo)-2)
  if turn%2==0:
    print('It is turn 2!')
    annotation+='    ' +str(turn)+'. '+myPiece+mySymbol+myLetterTo+str(int(myNumberTo)-2)  
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

def returnAvailableMoves(myLetter,myNumber,myChar):
  if myChar=='[_P_]':
    return blackPawnValidMoves(myLetter,myNumber)
  if myChar=='[_R_]':
    return 'You are trying to move a black rook.'
  if myChar=='[_N_]':
    return 'You are trying to move a black knight.'
  if myChar=='[_B_]':
    return 'You are trying to move a black bishop.'
  if myChar=='[_Q_]':
    return 'You are trying to move a black queen.'
  if myChar=='[_K_]':
    return 'You are trying to move a black king.'
  if myChar=='[ P ]':
    return whitePawnValidMoves(myLetter,myNumber)
  if myChar=='[ R ]':
    return 'You are trying to move a white rook.'
  if myChar=='[ N ]':
    return 'You are trying to move a white knight.'
  if myChar=='[ B ]':
    return 'You are trying to move a white bishop.'
  if myChar=='[ Q ]':
    return 'You are trying to move a white queen.'
  if myChar=='[ K ]':
    return 'You are trying to move a white king.'
  else:
     return ''

def convertToLetter(myLetterAsNumber):
  if myLetterAsNumber==2:
    return 'A'
  if myLetterAsNumber==3:
    return 'B'
  if myLetterAsNumber==4:
    return 'C'
  if myLetterAsNumber==5:
    return 'D'
  if myLetterAsNumber==6:
    return 'E'
  if myLetterAsNumber==7:
    return 'F'
  if myLetterAsNumber==8:
    return 'G'
  if myLetterAsNumber==9:
    return 'H'
    

def whitePawnValidMoves(myLetter,myNumber):
  validMoves=[]
  sampleReturn="it works but not with a list!"
  myLetterConverted=convertLetter(myLetter)
  myNumberConverted=convertNumber(myNumber)

  print('myLetterConverted='+str(myLetterConverted))
  print('myNumberConverted='+str(myNumberConverted))

  print('board[myNumberCoverted+1][myLetterConverted]='+str(board[myNumberConverted+1][myLetterConverted]))

  print('board[myNumberCoverted+2][myLetterConverted]='+str(board[myNumberConverted+2][myLetterConverted]))
  
  #If the white pawn is on rank 2 and can move 2 spaces
  if str(myNumberConverted)=='3' and board[myNumberConverted+1][myLetterConverted]=='[___]' and board[myNumberConverted+2][myLetterConverted]=='[___]':
    validMoves.append("Two spaces possible with pawn!")
    validMoves.append(str(myLetter)+str(int(myNumber)+2-2))
  
  #If the white pawn can move 1 space
  if board[myNumberConverted+1][myLetterConverted]=='[___]':
    validMoves.append("One space possible with pawn!")
    validMoves.append(str(myLetter)+str(int(myNumber)+1-2))
  
  #If the white pawn can capture left
  if board[myNumberConverted+1][myLetterConverted-1]!='[___]' and board[myNumberConverted+1][myLetterConverted-1][1:2]=='_':
    validMoves.append("Capture left possible with pawn!")
    
 #now convert myLetter and move to the left for that
    validMoves.append(convertToLetter(myLetterCoverted-1)+str(int(myNumber)+1-2))

  #If the white pawn can capture right
  if board[myNumberConverted+1][myLetterConverted+1]!='[___]' and board[myNumberConverted+1][myLetterConverted+1][1:2]=='_':

    validMoves.append("Capture right possible with pawn!")
 
  #now convert myLetter and move to the right for that
    validMoves.append(convertToLetter(myLetterConverted+1)+str(int(myNumber)+1-2))
  return validMoves

def blackPawnValidMoves(myLetter,myNumber):
  validMoves=[]
  sampleReturn="it works but not with a list!"
  myLetterConverted=convertLetter(myLetter)
  myNumberConverted=convertNumber(myNumber)

  print('myLetterConverted='+str(myLetterConverted))
  print('myNumberConverted='+str(myNumberConverted))

  print('board[myNumberCoverted+1][myLetterConverted]='+str(board[myNumberConverted+1][myLetterConverted]))

  print('board[myNumberCoverted+2][myLetterConverted]='+str(board[myNumberConverted+2][myLetterConverted]))
  
  #If the black pawn is on rank 2 and can move 2 spaces
  if str(myNumberConverted)=='8' and board[myNumberConverted-1][myLetterConverted]=='[___]' and board[myNumberConverted-2][myLetterConverted]=='[___]':
    validMoves.append("Two spaces possible with pawn!")
    validMoves.append(str(myLetter)+str(int(myNumber)-2-2))
  
  #If the black pawn can move 1 space
  if board[myNumberConverted-1][myLetterConverted]=='[___]':
    validMoves.append("One space possible with pawn!")
    validMoves.append(str(myLetter)+str(int(myNumber)-1-2))
  
  #If the black pawn can capture left
  if board[myNumberConverted-1][myLetterConverted-1]!='[___]' and board[myNumberConverted-1][myLetterConverted-1][1:2]==' ':
    validMoves.append("Capture left possible with pawn!")
    
 #now convert myLetter and move to the left for that
    validMoves.append(convertToLetter(myLetterCoverted-1)+str(int(myNumber)-1-2))

  #If the white pawn can capture right
  if board[myNumberConverted-1][myLetterConverted+1]!='[___]' and board[myNumberConverted-1][myLetterConverted+1][1:2]==' ':

    validMoves.append("Capture right possible with pawn!")
 
  #now convert myLetter and move to the right for that
    validMoves.append(convertToLetter(myLetterConverted+1)+str(int(myNumber)-1-2))
  return validMoves

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

  annotation=updateAnnotation(startLetterFrom, str(int(startNumberFrom)+2), destinationLetterTo, str(int(destinationNumberTo)+2), annotation, turn)
  print('Annotation:\n'+annotation)

  print('Available moves for '+pieceAtSquare(startLetterFrom,str(int(startNumberFrom)+2))+ ' at square '+startLetterFrom+str(int(startNumberFrom)+2))
  
  print(returnAvailableMoves(startLetterFrom, str(int(startNumberFrom)+2), pieceAtSquare(startLetterFrom,str(int(startNumberFrom)+2))))

  modifySquare(destinationLetterTo, str(int(destinationNumberTo)+2), modifySquare(startLetterFrom, str(int(startNumberFrom)+2), '[___]')
  )
  #The modifySquare() for the destination square empties that square and returns the character of the piece that was there.  The modfifySquare for the destination square places that piece at that square
  #modifySquare(destinationLetterTo, destinationNumberTo, 'P')