import pandas as pd
import math

class Setup:

    def __init__(self, symbol_id):
        self.symbol_id=symbol_id

    def get_entry_stoploss(self):
        ui=input('Entry: ')
        self.entry=float(ui)
        ui=input('Stoploss: ')
        self.stoploss=float(ui)

    def query_acct_status(self, db):
        s='select * from acct_status order by acct_status_created desc limit 1;'
        df=pd.read_sql(s, db.engine)
        self.acct_status_cap=df.iloc[0]['acct_status_cap']
        self.acct_status_cap_risk_pct=df.iloc[0]['acct_status_cap_risk_pct']
        self.acct_status_min_rr_pct=df.iloc[0]['acct_status_min_rr_pct']

    def calc_risk_amounts(self):
        self.cap_risk=self.acct_status_cap*self.acct_status_cap_risk_pct
        self.trade_risk=self.entry-self.stoploss

    def calc_pos_size(self):
        self.pos_size=math.floor(self.cap_risk/self.trade_risk)
        self.price=self.entry*self.pos_size

    def calc_min_tp(self):
        self.min_tp=self.entry+(self.trade_risk*self.acct_status_min_rr_pct)
        # not rounding because not sure how many decimals are relevant for crypto
        #self.min_tp=round(
        #    self.entry+(self.trade_risk*self.acct_status_min_rr_pct), 4)

    def is_min_tp_realistic(self):
        m=f'Is a take-profit of {self.min_tp} realistic? (y/n) '
        ui=input(m)
        if ui.lower()=='y':
            self.min_tp_realistic=True
        elif ui.lower()=='n':
            self.min_tp_realistic=False

    def load_setup(self, db):
        cols=[
              'symbol_id',
              'setup_entry',
              'setup_stoploss',
              'setup_min_tp',
              'setup_min_tp_realistic',
              'setup_pos_size',
              'setup_cap',
              'setup_cap_risk_pct',
              'setup_min_rr_pct',
              ]
        colstxt=', '.join(cols)
        vals=[
            self.symbol_id,
            self.entry,
            self.stoploss,
            self.min_tp,
            self.min_tp_realistic,
            self.pos_size,
            self.acct_status_cap,
            self.acct_status_cap_risk_pct,
            self.acct_status_min_rr_pct,
            ]
        vals_str=[str(v) for v in vals]
        valstxt=', '.join(vals_str).replace('True', 'TRUE')
        s=f'insert into setups ({colstxt}) values ({valstxt});'
        db.engine.execute(s)

    def get_setup_info(self, db):
        s='select * from setups order by setup_id desc limit 1;'
        df=pd.read_sql(s, db.engine)
        self.setup_info=df.iloc[0].to_dict()
        return df.iloc[0].to_dict()
