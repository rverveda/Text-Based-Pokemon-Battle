import  os
import random

from pokemon import pokemon

# Clear the terminal
clear = lambda: os.system('cls')

def gameStart():
    clear()
    # Have user select their pokemon
    print('Welcome Trainer! Select your pokemon:\n')
    p1Input = input('1. Bulbasaur\n2. Charmander\n3. Squirtle\nEnter your chosen pokemon\'s number: ')
    if p1Input == '1':
        p1Pokemon = 'Bulbasaur'
    elif p1Input == '2':
        p1Pokemon = 'Charmander'
    elif p1Input == '3':
        p1Pokemon = 'Squirtle'
    else:
        battleStart = False
        p1Pokemon = 0
        p2Pokemon = 0
    
    # Confirm the pokemon selection
    if p1Pokemon != 0:
        clear()
        print('Ah yes. You chose ' + p1Pokemon + '! What a good choice.')
        userInput = input('\nAre you ready to battle? yes(y) or no(n):')
        if userInput.lower() == 'yes' or userInput.lower() == 'y':
            p1Pokemon = pokemon(p1Pokemon)
            p1Pokemon.isComputer = False
            p1Pokemon.playerName = 'Trainer'
            validOpponent = False
            while validOpponent == False:
                clear()
                print('Who are you battling?\n')
                opponent = int(input('1. Your rival\n2. Computer\nEnter your choice\'s number: '))
                if opponent == 1 or opponent == 2:
                    p2Pokemon = pickOppPokemon(opponent)
                    if p2Pokemon != 0:
                        p2Pokemon = pokemon(p2Pokemon)
                        if opponent == 1:
                            p2Pokemon.isComputer = False
                            p2Pokemon.playerName = 'Rival'
                            clear()
                        else:
                            p2Pokemon.isComputer = True
                            p2Pokemon.playerName = 'Computer'
                        battleStart = True
                        validOpponent = True
            battleStart = True
        else:
            battleStart = False
            p2Pokemon = 0

    return battleStart, p1Pokemon, p2Pokemon

# Select opponent's pokemon
def pickOppPokemon(opponent):
    clear()
    if opponent == 1:
        print('Hello Rival! Select your pokemon:\n')
        p2Input = input('1. Bulbasaur\n2. Charmander\n3. Squirtle\nEnter your chosen pokemon\'s number: ')
        if p2Input == '1':
            p2Pokemon = 'Bulbasaur'
        elif p2Input == '2':
            p2Pokemon = 'Charmander'
        elif p2Input == '3':
            p2Pokemon = 'Squirtle'
        else:
            p2Pokemon = 0
    else:
        p2Pokemon = random.choice(['Bulbasaur', 'Charmander', 'Squirtle'])
    return p2Pokemon

# Get a move
def selectMove(currPlayer):
    if currPlayer.isComputer == False:
        currMoves = currPlayer.moves
        print('\n\n' + currPlayer.playerName + '\'s turn. Select ' + currPlayer.name + '\'s move:\n')
        index = 1
        for x in currMoves:
            print('  ' + str(index) + '. ' + x)
            index += 1
        selectedMove = int(input('\nSelect the move number: '))
        if selectedMove <= len(currMoves):
            validMove = True
            move = currMoves[selectedMove - 1]
            moveDamage = currPlayer.moveDamage[selectedMove - 1]
            moveText = currPlayer.moveText[selectedMove - 1]
        else:
            validMove = False
            move = 'Illegal'
            moveDamage = 0
            moveText = 'Illegal'
    else:
        validMove = True
        move = random.choice(currPlayer.moves)
        moveDamage = currPlayer.moveDamage[currPlayer.moves.index(move)]
        moveText = currPlayer.moveText[currPlayer.moves.index(move)]
    return validMove, move, moveDamage, moveText

def doDamage(currPlayer, otherPlayer, move, moveDamage, moveText):
    clear()
    # If move is > 2 it is a normal attack
    if moveDamage > 2:
        modifiedMoveDamage = round(moveDamage * (1 + currPlayer.attMod - otherPlayer.defMod))
        otherPlayer.health -= modifiedMoveDamage
        print(currPlayer.name + ' used ' + move + '.\n' + currPlayer.name + moveText + '\nIt did ' + str(modifiedMoveDamage) + ' damage.\n')
    # If moveDamage fits in this category it is modifier to pokemon's attack modifier
    elif moveDamage <= 2 and moveDamage > 1:
        if currPlayer.attMod < 2:
            currPlayer.attMod += (moveDamage - 1)
            if currPlayer.attMod > 2:
                currPlayer.attMod = 2
            print(currPlayer.name + ' used ' + move + '.\n' + currPlayer.name + moveText + '\n')
        else:
            print('** ' + currPlayer.name + '\'s attack cannot go any higher **')
    # If move damage fits in this category it is a modifier to pokemon's defense modifier
    elif moveDamage <= 1 and moveDamage > 0:
        if currPlayer.defMod < 2:
            currPlayer.defMod += (moveDamage)
            if currPlayer.defMod > 2:
                currPlayer.defMod = 2
            print(currPlayer.name + ' used ' + move + '.\n' + currPlayer.name + moveText + '\n')
        else:
            print('** ' + currPlayer.name + '\'s defense cannot go any higher **')
    # If move damage fits in this category it is a modifier to opponent's defense modifier
    elif moveDamage <= 0 and moveDamage > -1:
        if otherPlayer.defMod > 0:
            otherPlayer.defMod += (moveDamage)
            if otherPlayer.defMod < 0:
                otherPlayer.defMod = 0
            print(currPlayer.name + ' used ' + move + '.\n' + currPlayer.name + moveText + '\n')
        else:
            print('** ' + otherPlayer.name + '\'s defense cannot go any lower **')
    # If move damage fits in this category it is a modifier to opponent's attack modifier
    elif moveDamage <= -1 and moveDamage > -2:
        if otherPlayer.attMod > 0:
            otherPlayer.attMod += (moveDamage + 1)
            if otherPlayer.attMod < 0:
                otherPlayer.attMod = 0
            print(currPlayer.name + ' used ' + move + '.\n' + currPlayer.name + moveText + '\n')
        else:
            print('** ' + otherPlayer.name + '\'s attack cannot go any higher **')

def checkHealth(currPlayer, otherPlayer):
    if currPlayer.health <= 0:
        print(currPlayer.name + ' has fainted. ' + otherPlayer.playerName + ' is the winner!')
        gameOver = True
    elif otherPlayer.health <= 0:
        print(otherPlayer.name + ' has fainted. ' + currPlayer.playerName + ' is the winner!')
        gameOver = True
    else:
        gameOver = False
    return gameOver

def endTurn(currPlayer, otherPlayer):
    input('Input anything to continue to the next turn: ')
    clear()
    tempVar1 = currPlayer
    tempVar2 = otherPlayer
    currPlayer = tempVar2
    otherPlayer = tempVar1
    return currPlayer, otherPlayer




        
    
        
