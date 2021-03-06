"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadRespondentData(dct_file='2002FemResp.dct',
                       dat_file='2002FemResp.dat.gz'):
    return nsfg.ReadFemResp(dct_file, dat_file);


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    respondentDf = ReadRespondentData()
    print(respondentDf['pregnum'].value_counts())

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
