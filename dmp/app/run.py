import yf_client
import pandas as pd
import pg_client
import json

yfc=yf_client.YFClient()
ssc=pg_client.PGClient('stock_staging')

def get_n_stage(symbol, suffix):
    # Get data
    r=yfc.get_historical(symbol, 'US')

    # Stage data
    df=pd.DataFrame(json.loads(r)['prices'])
    table_name=symbol+suffix
    df.to_sql(table_name,
        con=ssc.get_engine(),
        if_exists='replace',
        index=False,)

    # Query staged data
    select_stmnt=f'select date, open, close, high, low, volume from "{table_name}";'
    result=ssc.select(select_stmnt)
    df=pd.DataFrame(result[0], columns=result[1])

    print(df.head())

    # Prep

    # Analytics


if __name__=='__main__':
    get_n_stage('CRCT', '_daily')
