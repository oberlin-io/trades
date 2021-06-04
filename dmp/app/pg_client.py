from sqlalchemy import create_engine

class PGClient():

    def __init__(self, db_name):
        self.engine = create_engine(
            f'postgresql://postgres:postgres@localhost:5432/{db_name}')

    def get_engine(self):
        return self.engine

    def select(self, select_stmnt):
        with self.engine.connect() as connection:
            data=connection.execute(select_stmnt)
            return (data, data.keys())
