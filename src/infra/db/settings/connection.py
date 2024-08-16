from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

class DBConnectionHandler():

    def __init__(self) -> None:
        '''self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'user',
            'password',
            'address',
            '3306', # port
            'database_name'
        )'''
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'root',
            '270170',
            'localhost',
            '3306', # port
            'clean_database'
        )
        self.__engine = self.__create_database_engine()
        self.session = None
        '''
            Ao executar a classe, o método construtor cria a conexão com a DB
        '''

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        '''
            Cria a sessão ao entrar no contexto
        '''
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, enc_val, exc_tb):
        '''
            Fecha a sessão ao sair
        '''
        self.session.close()

