from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:
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

