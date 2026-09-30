from abc import ABC, abstractmethod

class Comportement(ABC):
    @abstractmethod
    def agir(self, ennemi):
        pass