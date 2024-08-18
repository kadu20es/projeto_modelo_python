# implementa a "interface" criada em domain/use_cases/user_finder.py
from typing import Dict
from ...domain.use_cases.user_finder import UserFinder as UserFinderInterface
from ...data.interfaces.users_repository_interface import UsersRepositoryInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None: # users_repository é uma injeção de dependência
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        return super().find(first_name)