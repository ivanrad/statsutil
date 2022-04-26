#!/usr/bin/env python3
"""k-th percentile

Read a sequence of newline delimited decimal numbers from file(s) (or standard
input), and print k-th percentile (95th by default) to standard output.
"""
import argparse
import fileinput
from collections import defaultdict
from decimal import Decimal
from typing import DefaultDict, Iterable, Optional, Union


def percentile(iterable: Iterable[Union[Decimal, str]], p: int = 95) -> Optional[Decimal]:
    """Return k-th percentile for a sequence of Decimal values"""
    vals: DefaultDict[Decimal, int] = defaultdict(int)
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


def main() -> None:
    """Entry point"""

    def valid_percentile(p):
        p = int(p)
        if p < 1 or p > 99:
            raise argparse.ArgumentTypeError('percentile should be between 1 and 99')
        return p

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=__doc__
    )
    parser.add_argument(
        '-p',
        type=valid_percentile,
        default=95,
        help='percentile (default: %(default)d)',
    )
    parser.add_argument('file', nargs='*', help='file to be read')
    args = parser.parse_args()

    with fileinput.input(files=args.file) as fi:
        p = percentile(fi, p=args.p)  # type: ignore
        print(p)


if __name__ == '__main__':
    main()
