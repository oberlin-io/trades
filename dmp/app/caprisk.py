from datetime import datetime as dt

def update(percent):
    with open('db/caprisk.csv', 'a') as f:
        dt_stamp=dt.now().strftime('%Y-%m-%d %H:%M:%S')
        record=f'{dt_stamp},{percent}\n'
        f.write(record)
        print(f'Capital risk updated to {percent}.')
