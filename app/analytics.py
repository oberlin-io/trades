import pandas as pd

def get_top_setups(db):
    s='select * from setups s left join symbols b on (s.symbol_id=b.symbol_id);'
    # add 's full outer join bots b where s.setup_id=b.setup_id;'
    # need to drop setups that are not active. and/or do a date filter two last
    # three days
    df=pd.read_sql(s, db.engine)
    # add drop na on bot_id
    df['pot_profit']=(df.setup_min_tp-df.setup_entry)*df.setup_pos_size
    df.setup_created=df.setup_created.dt.date
    df.sort_values(
        by=['setup_min_tp_realistic', 'pot_profit'],
        ascending=[False, False],
        inplace=True,
        )
    if df.shape[0]>30:
        df=df.iloc[:30,:].copy()
    sel=['symbol', 'setup_created', 'pot_profit', 'setup_entry', 'setup_stoploss', 'setup_min_tp_realistic']
    return df[sel].to_string(index=False)
