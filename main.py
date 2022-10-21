import functions
battleStart = False
gameOver = False
playerOne = 0
playerTwo = 0
currPlayer = 0
otherPlayer = 0

# Start the game
while battleStart == False:
    battleStart, playerOne, playerTwo = functions.gameStart()

# Assign the current player and other player
currPlayer = playerOne
otherPlayer = playerTwo

# Start the battle
while gameOver == False:
    formattedP1 = '{:.0f}'.format(playerOne.health)
    formattedP2 = '{:.0f}'.format(playerTwo.health)
    print(playerOne.name + '\n  Health: ' + formattedP1 + '\n' + playerTwo.name + '\n  Health: ' + formattedP2)
    # Have the current player select a move
    validMove, move, moveDamage, moveText = functions.selectMove(currPlayer)
    # If the move is valid, have it deal damage. If not, ask for move again
    if validMove == True:
        # Deal the damage to the opposing pokemon
        functions.doDamage(currPlayer, otherPlayer, move, moveDamage, moveText)
        # Check if the game is over
        gameOver = functions.checkHealth(currPlayer, otherPlayer)
        # If the game isn't over swap the current player
        if gameOver == False:
            currPlayer, otherPlayer = functions.endTurn(currPlayer, otherPlayer)
