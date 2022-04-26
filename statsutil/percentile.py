#!/usr/bin/env python3
"""k-th percentile

Read a sequence of newline delimited decimal numbers from file(s) (or standard
input), and print k-th percentile (95th by default) to standard output.
"""
from collections import defaultdict
from decimal import Decimal
from typing import Iterable, Optional

def percentile(iterable: Iterable[Decimal], p: int = 95) -> Optional[Decimal]:
    """Return k-th percentile for a sequence of Decimal values"""
    vals = defaultdict(int)
    n = 0
    for line in iterable:
        vals[Decimal(line)] += 1
        n += 1
    cutoff = int(n * ((Decimal(p) / 100)))
    c = 0
    for v in sorted(vals.keys()):
        c += vals[v]
        if c > cutoff:
            return v
    return None

if __name__ == '__main__':
    import argparse, sys, fileinput

    def valid_percentile(p):
        p = int(p)
        if not (p >= 1 and p <= 99):
            raise argparse.ArgumentTypeError('percentile should be between 1 and 99')
        return p

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        type=valid_percentile,
        default=95,
        help='percentile (default: %(default)d)',
    )
    parser.add_argument('file', nargs='*', help='file to be read')
    args = parser.parse_args()

    with fileinput.input(files=args.file) as fi:
        p = percentile(fi, p=args.p)
        print(p)
