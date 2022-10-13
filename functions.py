import  os
import random

from pokemon import pokemon

# Clear the terminal
clear = lambda: os.system('cls')

def gameStart():
    clear()
    # Have user select their pokemon
    print('Welcome Trainer! Select your pokemon:\n')
    userInput = input('1. Bulbasaur\n2. Charmander\n3. Squirtle\nEnter your chosen pokemon\'s number: ')
    if userInput == '1':
        userPokemon = 'Bulbasaur'
    elif userInput == '2':
        userPokemon = 'Charmander'
    elif userInput == '3':
        userPokemon = 'Squirtle'
    else:
        battleStart = False
        userPokemon = 0
        compPokemon = 0
    
    # Confirm the pokemon selection
    if userInput == '1' or userInput == '2' or userInput == '3':
        clear()
        print('Ah yes. You chose ' + userPokemon + '! What a good choice.')
        userInput = input('\nAre you ready to battle? yes(y) or no(n):')
        if userInput.lower() == 'yes' or userInput.lower() == 'y':
            userPokemon, compPokemon = pickCompPokemon(userPokemon)
            battleStart = True
        else:
            battleStart = False
            compPokemon = 0

    return battleStart, userPokemon, compPokemon

# Select opponent's pokemon
def pickCompPokemon(userPokemon):
    clear()
    userPokemon = pokemon(userPokemon)
    if userPokemon.name == 'Bulbasaur':
        compPokemon = random.choice(['Charmander', 'Squirtle'])
    elif userPokemon.name == 'Charmander':
        compPokemon = random.choice(['Bulbasaur', 'Squirtle'])
    else:
        compPokemon = random.choice(['Charmander', 'Bulbasaur'])
    compPokemon = pokemon(compPokemon)
    return userPokemon, compPokemon

# Get a move
def selectMove(currPlayer, userPokemon, compPokemon):
    if currPlayer == 'user':
        currMoves = userPokemon.moves
        print('\n\nSelect ' + userPokemon.name + '\'s move:\n')
        index = 1
        for x in currMoves:
            print('  ' + str(index) + '. ' + x)
            index += 1
        selectedMove = int(input('\nSelect the move number: '))
        if selectedMove <= len(currMoves):
            validMove = True
            move = currMoves[selectedMove - 1]
            moveDamage = userPokemon.moveDamage[selectedMove - 1]
            moveText = userPokemon.moveText[selectedMove - 1]
        else:
            validMove = False
            move = 'Illegal'
            moveDamage = 0
            moveText = 'Illegal'
    else:
        validMove = True
        move = random.choice(compPokemon.moves)
        moveDamage = compPokemon.moveDamage[compPokemon.moves.index(move)]
        moveText = compPokemon.moveText[compPokemon.moves.index(move)]
    return validMove, move, moveDamage, moveText

def doDamage(currPlayer, userPokemon, compPokemon, move, moveDamage, moveText):
    if currPlayer == 'user':
        compPokemon.health -= moveDamage
        clear()
        print(userPokemon.name + ' used ' + move + '.\n' + userPokemon.name + moveText + '\nIt did ' + str(moveDamage) + ' damage.\n')
    else:
        userPokemon.health -= moveDamage
        clear()
        print(compPokemon.name + ' used ' + move + '.\n' + compPokemon.name + moveText + '\nIt did ' + str(moveDamage) + ' damage.\n')

def checkHealth(userPokemon, compPokemon):
    if userPokemon.health == 0:
        print(userPokemon.name + ' has fainted. ' + compPokemon.name + ' is the winner!')
        gameOver = True
    elif compPokemon.health == 0:
        print(compPokemon.name + ' has fainted. ' + userPokemon.name + ' is the winner!')
        gameOver = True
    else:
        gameOver = False
    return gameOver

def endTurn(currPlayer):
    input('Input anything to continue to the next turn: ')
    clear()
    if currPlayer == 'user':
        currPlayer = 'comp'
    else:
        currPlayer = 'user'
    return currPlayer




        
    
        
