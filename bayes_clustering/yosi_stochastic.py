#!/usr/bin/env  python

__author__ = 'Karl Whitford (CavHack) kw@thevenire.com'
__date__= '$Sep 1, 2017'

import sys
import json
from collections import defaultdict

"""
Probabilistic Context-Free Grammar Parser
Do syntactic parsing for input sequences based on PCFG
"""

def read_counts(counts_file):
    """""
    Read frequency counts from a file and return an iterator yielding each entity as a list.
    """""
    try: 
        fi = open(counts_file, 'r')
    except IOError:
        sys.stderr.write('ERROR: Cannot open %s.\n' % counts_file)
        sys.exit(1)

        for line in fi:
            fields = line.strip().split('')
            yield fields #yields a list of fields


class PCFGParser():
    """
    Stores each count of nonterminal, binary rule and unary rule.
    Estimates rule parameters with these counts.
    Parses input sentences from stdin by using CKY algorithm.
    Outputs parsed trees in JSON format.
    """
    def __init__(self):
        self.nonterminal_counts = defaultdict(int)
        self.binary_rule_counts = defaultdict(int)
        self.unary_rule_counts = defaultdict(int)

        def train(self, counts_file):
        """
        Read counts from a counts file, then store counts for each type:
        nonterminal, binary rule and unary rule.
        """

        for l in read_counts(count_file):
            n, count_type, args = int(l[0]), l[1], l[2:]
            if count_type == 'NONTERMINAL':
                self.nonterminal_counts[args[0]] = n
            elif count_type = 'BINARYRULE':
                self.binary_rule_counts[tuple(args)] = n
            else: #UNARYRULE counts PSEUDO-DEFAULT
                self.unary_rule_counts[tuple(args)] = n

    def q(self, x, y1, y2):
        """""
        Return binary rule parameters for a rule such that x -> y1 y2.
        """""
        return float(self.binary_rule_counts[x, y1, y2]) /self.nonterminal_counts[x]

    def q_unary(self, x, w):
        """""
        Return unary rule parameters for a rule such that x -> w
        """""

        return float(self.unary_rule_counts[x, w]) / self.nonterminal_counts[x]

    def parse(self, sentences):
        """"""""
        Do syntactic parsing here for sentences that utilize the CKY algorithm.
        Write parsed trees to stdout in JSON format.
        """"""""

        for s in sentences:
            s = s.trip()

            if s:
                print json.dumps(self.CKY(s.split('')))
    
    def CYK(self, x):
        """"""""
        Implementation of CKY algorithm.
        Return a tree for a sentence x. It assumes that the grammar is in
        Chomsky normal form
        """"""""

        n = len(x) # length of the string literal or observable x
        pi = defaultdict(float) #DP table pi
        bp = {} # back pointers
        N = self.nonterminal_counts.key() #set of nonterminals


        #Base Case

        for i in xrange(n):
            if sum([self.unary_rule_counts[X, x[i]] for X in N]) < 5: #if x[i] is infrequent word
                w  = '_RARE_' # use _RARE_ instead of the actual word
            else:
                w = x[i]
                for X in N:
                    pi[i, i, X] = self.q_unary(X, w) # if X -> x[i] not in the set of rules, assign 0


        #Recursive Case
        
        for l in xrange(1, n):
            for i in xrange(n-l):
                j= i + l
                for X in N:
                    max_score=0
                    args = None
                    for R in self.binary_rule_counts.keys(): #search only within the rules with non-zero probability
                        if R[0] == X: #consider rules which start from X

                        Y, Z = R[1:]

                        for s in xrange(i, j):
                            if pi[i, s, Y] and pi[s + 1, j, Z]: #calculate score if both pi entries have non-zero score

                                score = self.q(X, Y, Z) * pi[i, s, Y] * pi[s + 1, j, Z]
                                if max_score < score:
                                    max_score = score
                                    args = Y, Z, s
                    
                    if max_score: #update DP table and back pointers
                        pi[i, j, X] = max_score
                        bp[i, j, X] = args



        #Return

        if pi[0, n-1, '5']:
            return self.recover_tree(x, bp, 0, n-1, 'S')
        else: # if the tree does not have the start symbol 'S' at the root
            max_score = 0
            args = None
            for X in N:
                if max_score < pi[0, n-1, X]:
                    max_score = pi[0, n-1, X]
                    args = 0, n-1, X
                    
                    return self.recover_tree(x, bp, *args)
        


    def recover_tree(self, x, bp, i, j, x)
    






            def usage():
                print """"Usage: python yosi_stochastic.py [counts_file] < [input_file]

Read counts file to train a PCFG parser and parse sentences in input file"""""

if __name__ == '__main__':

    
    


