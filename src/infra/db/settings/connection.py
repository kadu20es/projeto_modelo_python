from sqlalchemy import create_engine

class DBConnectionHandler():
    
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'user',
            'password',
            'address',
            '3306', # port
            'database_name'
        )
        self.__engine = self.__create_database_engine()
        '''
            Ao executar a classe, o método construtor cria a conexão com a DB
        '''

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine

