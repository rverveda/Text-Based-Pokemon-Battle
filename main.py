import functions
battleStart = False
gameOver = False
userPokemon = 0
compPokemon = 0
currPlayer = 'user'

# Start the game
while battleStart == False:
    battleStart, userPokemon, compPokemon = functions.gameStart()

# Start the battle
while gameOver == False:
    print(userPokemon.name + '\n  Health: ' + str(userPokemon.health) + '\n' + compPokemon.name + '\n  Health: ' + str(compPokemon.health))
    # Have the current player select a move
    validMove, move, moveDamage, moveText = functions.selectMove(currPlayer, userPokemon, compPokemon)
    # If the move is valid, have it deal damage. If not, ask for move again
    if validMove == True:
        # Deal the damage to the opposing pokemon
        functions.doDamage(currPlayer, userPokemon, compPokemon, move, moveDamage, moveText)
        # Check if the game is over
        gameOver = functions.checkHealth(userPokemon, compPokemon)
        # If the game isn't over swap the current player
        if gameOver == False:
            currPlayer = functions.endTurn(currPlayer)
