from models.comportement import Comportement

class ComportementFurtif (Comportement):
    def __init__(self):
        self._tour_furtif = 0

    def agir(self, ennemi):
        if self._tour_furtif % 2 == 0:
            return "defend" 
        else: 
            return "attaque"