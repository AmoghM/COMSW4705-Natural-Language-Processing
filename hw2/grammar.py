"""
COMS W4705 - Natural Language Processing - Fall 2019
Homework 2 - Parsing with Context Free Grammars 
Yassine Benajiba
"""

import sys
from collections import defaultdict
from math import fsum

class Pcfg(object): 
    """
    Represent a probabilistic context free grammar. 
    """

    def __init__(self, grammar_file): 
        self.rhs_to_rules = defaultdict(list)
        self.lhs_to_rules = defaultdict(list)
        self.startsymbol = None 
        self.read_rules(grammar_file)      
 
    def read_rules(self,grammar_file):
        for line in grammar_file: 
            line = line.strip()
            if line and not line.startswith("#"):
                if "->" in line: 
                    rule = self.parse_rule(line.strip())
                    lhs, rhs, prob = rule
                    self.rhs_to_rules[rhs].append(rule)
                    self.lhs_to_rules[lhs].append(rule)
                else: 
                    startsymbol, prob = line.rsplit(";")
                    self.startsymbol = startsymbol.strip()
                    
     
    def parse_rule(self,rule_s):
        lhs, other = rule_s.split("->")
        lhs = lhs.strip()
        rhs_s, prob_s = other.rsplit(";",1) 
        prob = float(prob_s)
        rhs = tuple(rhs_s.strip().split())
        return (lhs, rhs, prob)

    def verify_grammar(self,key):
        """
        Return True if the grammar is a valid PCFG in CNF.
        Otherwise return False. 
        """
        # TODO, Part 1
        try:
            lhs_rule = self.lhs_to_rules[key]
            sum_prob = []
            for lhs in lhs_rule:
                sum_prob.append(lhs[2])
                print("LHS IS: ", lhs)
                rhs = lhs[1]
                if rhs[0].isupper() and rhs[1].isupper():
                    pass
                elif rhs[0].islower() and len(rhs)==1:
                    pass
                else:
                    return False
        except KeyError:
            return False
        if round(fsum(sum_prob),2) == 1.0:
            print(sum_prob)
            return True

        return False 


if __name__ == "__main__":
    with open(sys.argv[1],'r') as grammar_file:
        grammar = Pcfg(grammar_file)
        # print(grammar.lhs_to_rules['FLIGHTS'])
        # print(grammar.verify_grammar('FLIGHTS'))
        # print(grammar.rhs_to_rules[('ABOUT','NP')])