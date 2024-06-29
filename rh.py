#!/usr/bin/env python3

# A Small but Useful(tm) script to send you to a page for a random
# date in Hackaday's glorious history.

from datetime import datetime, timedelta
from random import randint

# Hackaday's first post was
# https://hackaday.com/2004/09/05/radioshack-phone-dialer-red-box/ --
# September 5th, 2004.

FRIST_POST = datetime(year=2004, month=9, day=5)


def main():
    """
    Main entry point
    """
    today = datetime.now()
    interval = (today - FRIST_POST).days
    rhday = FRIST_POST + timedelta(days=randint(0, interval))
    print(f"https://hackaday.com/{rhday.year}/{rhday.month}/{rhday.day}")


if __name__ == "__main__":
    main()
