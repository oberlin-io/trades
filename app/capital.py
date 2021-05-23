from datetime import datetime as dt

def update(amount):
    with open('db/capital.csv', 'a') as f:
        dt_stamp=dt.now().strftime('%Y-%m-%d %H:%M:%S')
        record=f'{dt_stamp},{amount}\n'
        f.write(record)
        print(f'Capital updated to {amount}.')

