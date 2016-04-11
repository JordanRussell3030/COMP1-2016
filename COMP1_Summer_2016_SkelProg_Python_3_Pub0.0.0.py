#Skeleton Program for the AQA COMP1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA COMP1 Programmer Team
#developed in a Python 3.4 programming environment

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!Read all comments every time I open this file!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import random

def SetUpGameBoard(Board, Boardsize):
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if (Row == (BoardSize + 1) // 2 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2 + 1):
        Board[Row][Column] = "C"
      elif (Row == (BoardSize + 1) // 2 + 1 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2):
        Board[Row][Column] = "H"
      else:
        Board[Row][Column] = " "

def ChangeBoardSize():
  BoardSize = int(input("Enter a board size (between 4 and 9): "))
  while not(BoardSize >= 4 and BoardSize <= 9):
    BoardSize = int(input("Enter a board size (between 4 and 9): "))
  return BoardSize

def GetHumanPlayerMove(PlayerName, BoardSize):
  #Use while loop for input validation
  valid = False
  while not valid:
    print(PlayerName, "enter the coodinates of the square where you want to place your piece: ", end="")
    #Put error exception after while loop start and print statement
    try:
      Coordinates = int(input())
      #Use & 10 to get the first coordinate (row) and // 10 to get the second coordinate (column)
      #Always use BoardSize never put a hard-coded value for assumed BoardSize
      if Coordinates % 10 != 0 and Coordinates // 10 != 0 and Coordinates % 10 <= BoardSize and Coordinates // 10 <= BoardSize:
        valid = True
    #Exception goes after the whole process
    except ValueError:
      valid = False
  return Coordinates

def GetComputerPlayerMove(BoardSize):
  return random.randint(1, BoardSize) * 10 + random.randint(1, BoardSize)

def GameOver(Board, BoardSize):
  for Row in range(1 , BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == " ":
        return False
  return True

def GetPlayersName():
  PlayerName = input("What is your name? ")
  return PlayerName

#Change so a move is invalid if no pieces are flipped
def CheckIfMoveIsValid(Board, Move):
  Row = Move % 10
  Column = Move // 10
  MoveIsValid = False
  if Board[Row][Column] == " ":
    MoveIsValid = True
  return MoveIsValid

def GetPlayerScore(Board, BoardSize, Piece):
  Score = 0
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == Piece:
        Score = Score + 1
  return Score

def CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  RowCount = StartRow + RowDirection
  ColumnCount = StartColumn + ColumnDirection
  FlipStillPossible = True
  FlipFound = False
  OpponentPieceFound = False
  while RowCount <= BoardSize and RowCount >= 1 and ColumnCount >= 1 and ColumnCount <= BoardSize and FlipStillPossible and not FlipFound:
    if Board[RowCount][ColumnCount] == " ":
      FlipStillPossible = False
    elif Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      OpponentPieceFound = True
    elif Board[RowCount][ColumnCount] == Board[StartRow][StartColumn] and not OpponentPieceFound:
      FlipStillPossible = False
    else:
      FlipFound = True
    RowCount = RowCount + RowDirection
    ColumnCount = ColumnCount + ColumnDirection
  return FlipFound

def FlipOpponentPiecesInOneDirection(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  FlipFound = CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection)
  if FlipFound:
    RowCount = StartRow + RowDirection
    ColumnCount = StartColumn + ColumnDirection
    while Board[RowCount][ColumnCount] != " " and Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      if Board[RowCount][ColumnCount] == "H":
        Board[RowCount][ColumnCount] = "C"
      else:
        Board[RowCount][ColumnCount] = "H"
      RowCount = RowCount + RowDirection
      ColumnCount = ColumnCount + ColumnDirection

def MakeMove(Board, BoardSize, Move, HumanPlayersTurn):
  Row = Move % 10
  Column = Move // 10
  if HumanPlayersTurn:
    Board[Row][Column] = "H"
  else:
    Board[Row][Column] = "C"
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, -1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, 1)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, -1)
    

def PrintLine(BoardSize):
  print("   ", end="") #The spaces before each line
  for Count in range(1, BoardSize * 2):
    print("-", end="") #The lines
  print()

def DisplayGameBoard(Board, BoardSize):
  print() #Just the gap at the top of the board between the text
  print("  ", end="") #The space in front of each column number at the top
  for Column in range(1, BoardSize + 1):
    print(" ", end="") #These are the spaces between the numbers
    print(Column, end="") #These are the column numbers along the top
  print() #An important space needed for alignment at the top of the board
  PrintLine(BoardSize) #The top line
  for Row in range(1, BoardSize + 1):
    print(Row, end="") #This is the column numbers down the left side of the board
    print(" ", end="") #This is the gap between the numbers and the pipes down the columns
    for Column in range(1, BoardSize + 1):
      print("|", end="") #This is pretty much all the pipes
      print(Board[Row][Column], end="") #All the spaces between the columns on each row
    print("|") #This aligns the pipes and dashes
    PrintLine(BoardSize) #All the rest of the lines
    print() #This is the large gaps between the rows which are probably unnecessary

def DisplayMenu():
  print("(p)lay game")
  print("(e)nter name")
  print("(c)hange board size")
  print("(q)uit")
  print()

def GetMenuChoice(PlayerName):
  print(PlayerName, "enter the letter of your chosen option: ", end="")
  Choice = input()
  return Choice

def CreateBoard():
  Board = []
  for Count in range(BoardSize + 1):
    Board.append([])
    for Count2 in range(BoardSize + 1):
      Board[Count].append("")
  return Board

def PlayGame(PlayerName, BoardSize):
  Board = CreateBoard()
  SetUpGameBoard(Board, BoardSize)
  HumanPlayersTurn = False
  while not GameOver(Board, BoardSize):
    HumanPlayersTurn = not HumanPlayersTurn
    DisplayGameBoard(Board, BoardSize)
    MoveIsValid = False
    while not MoveIsValid:
      if HumanPlayersTurn:
        Move = GetHumanPlayerMove(PlayerName, BoardSize)
      else:
        Move = GetComputerPlayerMove(BoardSize)
      MoveIsValid = CheckIfMoveIsValid(Board, Move)
    if not HumanPlayersTurn:
      print("Press the Enter key and the computer will make its move")
      input()
    MakeMove(Board, BoardSize, Move, HumanPlayersTurn)
  DisplayGameBoard(Board, BoardSize)
  HumanPlayerScore = GetPlayerScore(Board, BoardSize, "H")
  ComputerPlayerScore = GetPlayerScore(Board, BoardSize, "C")
  if HumanPlayerScore > ComputerPlayerScore:
    print("Well done", PlayerName, ", you have won the game!")
  elif HumanPlayerScore == ComputerPlayerScore:
    print("That was a draw!")
  else:
    print("The computer has won the game!")
  print()


random.seed()
BoardSize = 6
PlayerName = ""
Choice = ""
while Choice != "q" and Choice != "Q":
  DisplayMenu()
  Choice = GetMenuChoice(PlayerName)
  #.lower or .upper followed by ()[number of characters in] in this case will always be 0 probably
  if Choice.lower()[0] == "p":
    PlayGame(PlayerName, BoardSize)
  elif Choice.lower()[0] == "e":
    PlayerName = GetPlayersName()
  elif Choice.lower()[0] == "c":
    BoardSize = ChangeBoardSize()
