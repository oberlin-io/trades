import argparse
from app import capital
from app import caprisk
from app import trade

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--u_cap', action='store', type=int, help='Update latest capital amount.')
    parser.add_argument('--u_caprisk', action='store', type=float, help='Update latest capital risk, eg .01.')
    parser.add_argument('--mk_trade', action='store', nargs='+',
        help='Make a trade study, starting with symbol, entry, and stop loss.')
    return parser.parse_args()

def run_args(args):
    if args.u_cap is not None:
        capital.update(args.u_cap)
    if args.u_caprisk is not None:
        caprisk.update(args.u_caprisk)
    if args.mk_trade is not None:
        t=trade.Trade(args.mk_trade[0], args.mk_trade[1], args.mk_trade[2])
        t.set_capital()
        t.set_caprisk()
        t.get_pos_size()
        t.save_data()
