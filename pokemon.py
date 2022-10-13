class pokemon:
    health = 60
    moves = ['Growl', 'Tackle']
    moveDamage = [0, 20]
    moveText = [' growls. The opponent\'s pokemon\'s defense is lowered. Unfortunately, I have not programmed that so nothing happens.', 
    ' lunges forward and hit\'s the opponent\'s pokemon.']
    def __init__(self, name):
        self.name = name