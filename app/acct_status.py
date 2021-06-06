import pandas as pd

class AcctStatus:
    """
    acct_status_cap
    acct_status_cap_risk_pct
    acct_status_min_rr_pct
    """
    def __init__(self):
        pass

    def input_status(self):
        ui=input('Capital: ')
        if ui=='':
            self.acct_status_cap=self.recent_status['acct_status_cap']
        else:
            self.acct_status_cap=float(ui.replace(',', ''))

        ui=input('Capital risk pct (as decimal): ')
        if ui=='':
            self.acct_status_cap_risk_pct=self.recent_status['acct_status_cap_risk_pct']
        else:
            self.acct_status_cap_risk_pct=float(ui)

        ui=input('Minimum reward-risk pct (as decimal): ')
        if ui=='':
            self.acct_status_min_rr_pct=self.recent_status['acct_status_min_rr_pct']
        else:
            self.acct_status_min_rr_pct=float(ui)

    def load_status(self, db):
        cols=['acct_status_cap', 'acct_status_cap_risk_pct', 'acct_status_min_rr_pct']
        colstxt=', '.join(cols)
        vals=list()
        for col in cols:
            vals.append(str(self.__dict__[col]))
        valstxt=', '.join(vals)
        s=f'insert into acct_status ({colstxt}) values ({valstxt});'
        db.engine.execute(s)

    def get_recent_status(self, db):
        s='select * from acct_status order by acct_status_created desc limit 1;'
        df=pd.read_sql(s, db.engine)
        self.recent_status=df.iloc[0].to_dict()
        return df.iloc[0].to_dict()
