# É o equivalente a uma interface. Quem HERDAR precisa implementar o método a seguir

from abc import ABC, abstractmethod
from typing import Dict

class UserFinder(ABC):

    @abstractmethod
    def find(self, first_name: str) -> Dict: pass