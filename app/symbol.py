from app import conf
from datetime import datetime as dt
import numpy as np
import pandas as pd

class Symbol:

    def __init__(self):
        pass

    def input_symbol(self):
        ui=input('Symbol: ')
        self.symbol=ui.upper()

    def symbol_exists(self, db):
        s=f"select * from symbols where symbol='{self.symbol}';"
        df=pd.read_sql(s, db.engine)
        if df.shape[0]==0:
            self.exists=False
        else:
            self.exists=True
            self.symbol_id=df.iloc[0].symbol_id
            self.symbol_created=df.iloc[0].symbol_created

    def load_symbol(self, db):
        if self.exists==False:
            t=dt.now().strftime(conf.timestamp_fmt)
            s=f'insert into symbols (symbol, symbol_created) values {self.symbol, t};'
            db.engine.execute(s)

    def query_symbol_info(self, db):
        s=f"select * from symbols where symbol='{self.symbol}';"
        df=pd.read_sql(s, db.engine)
        self.symbol_id=df.iloc[0].symbol_id
        self.symbol_created=df.iloc[0].symbol_created

    def get_symbol_info(self):
        return {'Symbol': self.symbol, 'Symbol ID': self.symbol_id,
            'Symbol created': self.symbol_created}
