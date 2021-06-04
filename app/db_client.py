from sqlalchemy import create_engine

class PGClient():

    def __init__(self, db_name):
        self.engine = create_engine(
            f'postgresql://postgres:postgres@localhost:5432/{db_name}')
