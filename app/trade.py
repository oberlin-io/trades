import math
import json
from datetime import datetime as dt

class Trade():
    def __init__(self, symbol, entry, stop_loss):
        self.datetime=dt.now().strftime('%Y%m%d%H%M%S')
        self.symbol=symbol.lower()
        self.fpath=f'db/{self.datetime}_{self.symbol}.json'
        self.entry=float(entry)
        self.stop_loss=float(stop_loss)

    def set_capital(self):
        with open('db/capital.csv') as f:
            self.capital=float(f.read().splitlines()[-1].split(',')[-1])
        print(f'Capital: {self.capital}')
    
    def set_caprisk(self):
        with open('db/caprisk.csv') as f:
            self.caprisk=float(f.read().splitlines()[-1].split(',')[-1])
        print(f'Capital risk percent: {self.caprisk}')
    
    def get_pos_size(self):
        self.trade_risk=self.entry-self.stop_loss
        self.pos_size=math.floor(self.capital*self.caprisk/self.trade_risk)
        self.invest_amount=self.pos_size*self.entry
        print(f'Position size: {self.pos_size}')
        print(f'Invest amount: {self.invest_amount}')
        return (self.pos_size, self.invest_amount)

    def save_data(self):
        j=json.dumps(self.__dict__)
        with open(self.fpath, 'w') as f:
            f.write(j)

    def open_trade(self):
        pass # select from list, then set_data; will have to move attributes set in init
    
    def set_data(self):
        pass # assign the json dict to the self.__dict__?
    
    def set_take_profit(self, take_profit):
        pass

    def set_profit_loss(self, profit_loss):
        pass

    def set_roi(self):
        pass
