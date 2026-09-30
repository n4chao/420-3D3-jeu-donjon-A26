from models.comportement import Comportement

class ComportementDefensif(Comportement):
    def agir(self, ennemi):
        if ennemi.hp > ennemi.hp_max * 0.5:
            return "defend" 
        else: 
            return "attaque"