from app.symbol import Symbol
from app.db_client import PGClient
import os

os.system('clear')

m='Connecting to trades database...'
print(m)
db=PGClient('trades')

def menu():
    m='''Menu
  [1] Account status
  [2] New setup
  [X] Exit
  Select: '''
    run_app(input(m))

def run_app(ui):
    if ui=='1':
        pass

    elif ui=='2':
        symbol=Symbol()
        symbol.input_symbol()
        symbol.symbol_exists(db)
        symbol.load_symbol(db)
        symbol.query_symbol_info(db)
        for k, v in symbol.get_symbol_info().items():
            print(f'  {k}: {v}')

    elif ui.upper()=='X':
        print('Exiting trades...')
        exit()
        
    else:
        print('Input not found.')

while True:
    menu()
