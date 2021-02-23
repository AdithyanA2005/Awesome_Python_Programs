import argparse as ap
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'mult':
        return args.x * args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        return "apps command was not recognised"


def start():
    cmd = ap.ArgumentParser()
    cmd.add_argument('--x', type=float, default=1.0, help="Enter The First Number")
    cmd.add_argument('--y', type=float, default=1.0, help="Enter The Second Number")
    cmd.add_argument('--o', type=str, default=1.0, help="Enter Prefered operation")
    args = cmd.parse_args()
    return args

if __name__ == '__main__':
    args = start()
    sys.stdout.write(str(calc(args)))
