# Interface de users_repository - usada por infra/db/repositories/users_reposotory.py
from typing import List
from abc import ABC, abstractmethod
from ...domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass

    @abstractmethod
    def select_user(self, first_name: str) -> List[Users]: pass