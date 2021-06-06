from app.acct_status import AcctStatus
from app.symbol import Symbol
from app.db_client import PGClient
import os
import time


os.system('clear')
m='Connecting to trades database...'
print(m)
db=PGClient('trades')
time.sleep(1)

def menu():
    os.system('clear')
    m='''Menu
[1] Get account status
[2] Change account status
[3] New setup
[X] Exit
Select: '''
    ui=input(m)
    os.system('clear')
    run_app(ui)
    enter_to_cont()

def enter_to_cont():
    ui=input()
    del ui

def run_app(ui):
    if ui=='1':
        print('Get account status')
        acct_status=AcctStatus()
        for k, v in acct_status.get_recent_status(db).items():
            print(f'{k}: {v}')

    elif ui=='2':
        print('Change account status')
        acct_status=AcctStatus()
        for k, v in acct_status.get_recent_status(db).items():
            print(f'{k}: {v}')
        acct_status.input_status()
        acct_status.load_status(db)
        for k, v in acct_status.get_recent_status(db).items():
            print(f'{k}: {v}')

    elif ui=='3':
        print('New setup')
        symbol=Symbol()
        symbol.input_symbol()
        symbol.symbol_exists(db)
        symbol.load_symbol(db)
        symbol.query_symbol_info(db)
        for k, v in symbol.get_symbol_info().items():
            print(f'{k}: {v}')

    elif ui.upper()=='X':
        print('Exiting trades...')
        time.sleep(1)
        os.system('clear')
        exit()

    else:
        print('Input not found.')

while True:
    menu()
