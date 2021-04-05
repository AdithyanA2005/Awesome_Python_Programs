import argparse as ap
import sys


def main():

    cmd = ap.ArgumentParser()

    cmd.add_argument('--x', type=float, default=1.0,
                     help="Enter The First Number")

    cmd.add_argument('--y', type=float, default=1.0,
                     help="Enter The Second Number")

    cmd.add_argument('--o', type=str, default='add',
                     help="Enter Prefered operation")

    args = cmd.parse_args()

    return args


def do_operation(args):

    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'div':
        return args.x / args.y


if __name__ == '__main__':
    args = main()
    sys.stdout.write(str(do_operation(args)))
