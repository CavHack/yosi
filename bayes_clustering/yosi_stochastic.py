#!/usr/bin/env  python

__author__ = 'Karl Whitford (CavHack) kw@thevenire.com'
__date__= '$Sep 1, 2017'

import sys
import json
from collections import defaultdict

"""
Probabilistic Context-Free Grammar Parser
Do syntactic partsing for input sequences based on PCFG
"""

def read_counts(counts_file):
    """""
    Read frequency counts from a file and return an iterator yielding each entity as a list.
    """""
    try: 
        fi = open(counts_file, 'r')
    except IOError:
        sys.stderr.write('ERROR: Cannot open %s.\n' % counts_file):
        sys.exit(1)

        for line in fi:
            fields = line.strip().split('')
            yield fields #yields a list of fields



            def usage():
                print """"Usage: python yosi_stochastic.py [counts_file] < [input_file]

Read counts file to train a PCFG parser and parse sentences in input file"""""

if __name__ == '__main__':

    
    


