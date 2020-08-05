# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:49:14 2020

@author: Angshuman
"""


winningComb= [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)];
gameSymbols= ('X','O');

board= ['#','1', '2', '3', '4', '5', '6', '7', '8', '9' ];
        
def showBoard():
    print(board[1] + ' | ' + board[2] + ' | ' + board[3]);
    print('---------');
    print(board[4] + ' | ' + board[5] + ' | ' + board[6]);
    print('---------');
    print(board[7] + ' | ' + board[8] + ' | ' + board[9]);
    

def takePlayerInfo():
    pl1Name  = input("Provide player-1 name: ");
    pl1Symbol = input("Please choose your game symbol [X, O]: ");
    while  pl1Symbol not in (gameSymbols):
        print("You have given wrong input!. Please select a symbol from [X, O]");
        pl1Symbol = input("Please choose your game symbol [X, O]: ");
    player1=(pl1Name, pl1Symbol); 
    
    pl2Name = input("Provide player-2 name: ");
    pl2Symbol = '';
    if pl1Symbol == 'X':
        pl2Symbol = 'O';
    else:
        pl2Symbol = 'X';
    player2=(pl2Name, pl2Symbol);
    playerInfo= [player1,player2];
    print(f"Welcome player {pl1Name} and {pl2Name} in TIC TAC TOE \n{pl1Name} will go first\n\n");
    showBoard();
    takeUserInput(playerInfo,0);

def takeUserInput(playerInfo, currPlayerIndex):
    currentPlayerName = playerInfo[currPlayerIndex][0];
    currentPlayerSymbol = playerInfo[currPlayerIndex][1];
    print('Taking user input');
    currentPos = input(f"{currentPlayerName} please choose your index position for symbol {currentPlayerSymbol}: ");
    while currentPos not in board:
        print("Invalid input");
        currentPos = input(f"{currentPlayerName} please choose your index position for symbol {currentPlayerSymbol}: ");
    
    currentPos = int(currentPos);
    board[currentPos] = currentPlayerSymbol;
    showBoard();
    
    decideWinner(playerInfo, currPlayerIndex);
    

def continueGame(playerInfo, currPlayerIndex):
    answers = ['Y', 'YES', 'N', 'NO'];
    answer = input("Do you want to continue[Y/N, yes/no]? ");
    answer = answer.upper();
    while answer not in answers:
        print("I do not understant. Please provide valid input[Y/N, yes/no]:  ")
        answer = input("Do you want to continue[Y/N, yes/no]? ");
        answer = answer.upper();
    
    if answer == 'Y' or answer== 'YES':
        takeUserInput(playerInfo, currPlayerIndex);
    else:
        pass;

def decideWinner(playerInfo, currPlayerIndex):
    winnerDecided =False;
    for a,b,c in winningComb:
        if playerInfo[currPlayerIndex][1] == board[a] == board[b] == board[c]:
            winnerName = playerInfo[currPlayerIndex][0];
            winnerDecided =True;
            print(f"**************************** {winnerName} IS THE WINNER ****************************");
            break;
            
    if  not winnerDecided:        
        if currPlayerIndex == 0:
            currPlayerIndex=1;
        else:
            currPlayerIndex =0;
        continueGame(playerInfo, currPlayerIndex)
    else:
        answers = ['Y', 'YES', 'N', 'NO'];
        answer = input("Do you want to restart the game[Y/N, yes/no]? ");
        answer = answer.upper();
        while answer not in answers:
            print("I do not understant. Please provide valid input[Y/N, yes/no]:  ")
            answer = input("Do you want to continue[Y/N, yes/no]? ");
            answer = answer.upper();
        
        if answer == 'Y' or answer== 'YES':
            for index in range(1,10):
                board[index] = str(index);
            showBoard();
            if currPlayerIndex == 0:
                currPlayerIndex=1;
            else:
                currPlayerIndex =0;
            takeUserInput(playerInfo, currPlayerIndex);
        else:
            pass;
  

takePlayerInfo();


