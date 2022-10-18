class pokemon:
    health = 60
    attMod = 1
    defMod = 1
    moves = ['Growl', 'Tackle']
    moveDamage = [-0.2, 20]
    moveText = [' growls. The opponent\'s pokemon\'s defense is lowered.', 
    ' lunges forward and hit\'s the opponent\'s pokemon.']
    def __init__(self, name):
        self.name = name