from typing import List
from ....infra.db.settings.connection import DBConnectionHandler
from ....infra.db.entities.users import Users as UsersEntity
from ....data.interfaces.users_repository_interface import UsersRepositoryInterface
from ....domain.models.users import Users

class UsersRepository(UsersRepositoryInterface):
    '''
        Classe de repositório de ações da tabela de User.
        Deve conter os métodos de crud da tabela.
        Utiliza DBConnectionHandler e Users (entities).

        Exemplo de uso está em users_repository_test.py
    '''
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name = first_name,
                    last_name = last_name,
                    age = age
                )
                print(new_registry)
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                print('Erro')
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.first_name == first_name)
                        .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception
