from models.comportement import Comportement

class Ennemi:

    def __init__(self, nom: str, hp: int, attaque: int, comportement: Comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self._comportement = comportement

    def agir(self) -> str:
        return self._comportement.agir(self) 

    def set_comportement(self, comportement: Comportement):
        self._comportement = comportement 


    def get_comportement(self):
        return self._comportement

    def recevoir_degats(self, degats: int):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.nom} (HP: {self.hp}/{self.hp_max})"