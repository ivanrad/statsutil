#!/usr/bin/env python3
"""Population standard deviation

Read a sequence of newline delimited decimal numbers from file(s) (or standard
input), and print standard deviation to standard out.
"""
import argparse
import fileinput
import sys
from decimal import Decimal
from typing import Iterable, Union


def stddev(iterable: Iterable[Union[Decimal, str]]) -> Decimal:
    """Population standard deviation for a sequence of Decimal values"""
    m, m2 = Decimal(0), Decimal(0)
    n = 0
    for line in iterable:
        v = Decimal(line)
        m += v
        m2 += v**2
        n += 1
    return (m2 / n - (m / n) ** 2).sqrt() if n > 0 else Decimal(0)


def main() -> None:
    """Entry point"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=__doc__
    )
    parser.parse_args()

    with fileinput.input(files=sys.argv[1:]) as fi:
        std = stddev(fi)  # type: ignore
        print(f'{std:.3f}')


if __name__ == '__main__':
    main()
