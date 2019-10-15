"""
COMS W4705 - Natural Language Processing - Fall 2019
Homework 2 - Parsing with Context Free Grammars 
Yassine Benajiba
"""
import math
import sys
from collections import defaultdict
import itertools
from grammar import Pcfg

### Use the following two functions to check the format of your data structures in part 3 ###
def check_table_format(table):
    """
    Return true if the backpointer table object is formatted correctly.
    Otherwise return False and print an error.  
    """
    if not isinstance(table, dict): 
        sys.stderr.write("Backpointer table is not a dict.\n")
        return False
    for split in table: 
        if not isinstance(split, tuple) and len(split) ==2 and \
          isinstance(split[0], int)  and isinstance(split[1], int):
            sys.stderr.write("Keys of the backpointer table must be tuples (i,j) representing spans.\n")
            return False
        if not isinstance(table[split], dict):
            sys.stderr.write("Value of backpointer table (for each span) is not a dict.\n")
            return False
        for nt in table[split]:
            if not isinstance(nt, str): 
                sys.stderr.write("Keys of the inner dictionary (for each span) must be strings representing nonterminals.\n")
                return False
            bps = table[split][nt]
            if isinstance(bps, str): # Leaf nodes may be strings
                continue 
            if not isinstance(bps, tuple):
                sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Incorrect type: {}\n".format(bps))
                return False
            if len(bps) != 2:
                sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Found more than two backpointers: {}\n".format(bps))
                return False
            for bp in bps: 
                if not isinstance(bp, tuple) or len(bp)!=3:
                    sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Backpointer has length != 3.\n".format(bp))
                    return False
                if not (isinstance(bp[0], str) and isinstance(bp[1], int) and isinstance(bp[2], int)):
                    print(bp)
                    sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a pair ((i,k,A),(k,j,B)) of backpointers. Backpointer has incorrect type.\n".format(bp))
                    return False
    return True

def check_probs_format(table):
    """
    Return true if the probability table object is formatted correctly.
    Otherwise return False and print an error.  
    """
    if not isinstance(table, dict): 
        sys.stderr.write("Probability table is not a dict.\n")
        return False
    for split in table: 
        if not isinstance(split, tuple) and len(split) ==2 and isinstance(split[0], int) and isinstance(split[1], int):
            sys.stderr.write("Keys of the probability must be tuples (i,j) representing spans.\n")
            return False
        if not isinstance(table[split], dict):
            sys.stderr.write("Value of probability table (for each span) is not a dict.\n")
            return False
        for nt in table[split]:
            if not isinstance(nt, str): 
                sys.stderr.write("Keys of the inner dictionary (for each span) must be strings representing nonterminals.\n")
                return False
            prob = table[split][nt]
            if not isinstance(prob, float):
                sys.stderr.write("Values of the inner dictionary (for each span and nonterminal) must be a float.{}\n".format(prob))
                return False
            if prob > 0:
                sys.stderr.write("Log probability may not be > 0.  {}\n".format(prob))
                return False
    return True



class CkyParser(object):
    """
    A CKY parser.
    """

    def __init__(self, grammar): 
        """
        Initialize a new parser instance from a grammar. 
        """
        self.grammar = grammar

    def is_in_language(self,tokens):
        """
        Membership checking. Parse the input tokens and return True if
        the sentence is in the language described by the grammar. Otherwise
        return False
        """
        # TODO, part 2
        n = len(tokens)
        prob_table = {}
        parse_table = {}
        table = [[[] for i in range(0, n)] for j in range(0, n)]
        # print(len(table[0]))

        for i in range(0,len(tokens)):
            rules = grammar.rhs_to_rules[(tokens[i],)]
            for rule in rules:
                table[i][i].append(rule[0])
                # parse_table[(i,i+1)] = {rule[0]:(i,i+1)}
                # prob_table[(i,i+1)] = {rule[0]:rule[2]}

        # print(table)
        # exit()
        for length in range(2,n+1):
            for i in range(0,n-length+1):
                j = i+length
                for k in range(i+1,j):
                    # print(n,length,i,k,j)
                    # print("TABLE[I][K]", i, k-1, table[i][k-1])
                    # print("TABLE[K][J]", k, j-1, table[k][j-1])
                    if len(table[i][k-1]) is not 0 and len(table[k][j-1]) is not 0:
                        import itertools
                        union = list(itertools.product(table[i][k-1],table[k][j-1]))
                        # print("UNION IS: ", union)
                        for un in union:
                            if un in grammar.rhs_to_rules:
                                non_terminal = grammar.rhs_to_rules[un]
                                for nt in non_terminal:
                                    # if (i,j) not in prob_table:
                                    #     prob_table[(i,j)] = {}
                                    #     parse_table[(i, j)] = {}

                                    table[i][j-1].append(nt[0])
                                    # print(prob_table)
                                    # print(i,k,j)
                                    # input()

                                    # try:
                                    #     prob = prob_table[(i,j)][nt[0]]
                                    #     if prob > nt[2]:
                                    #         raise KeyError
                                    #         # prob_table[(i,j)][nt[0]] = max(prob, nt[2])
                                    # except KeyError:
                                    #     prob_table[(i,j)][nt[0]] = nt[2]
                                    #     left_key = list(parse_table[(i,k)].keys())[0]
                                    #     left_child = (left_key,i,k)
                                    #     right_key = list(parse_table[(k,j)].keys())[0]
                                    #     right_child = (right_key,k,j)
                                    #     parse_table[(i,j)][nt[0]] = (left_child, right_child)
        # print("NOW THE TABLE IS")
        # print(table[0])
        # print(parse_table[(0,3)])
        if 'TOP' in table[0][n-1]:
            return True

        return False
       
    def parse_with_backpointers(self, tokens):
        """
        Parse the input tokens and return a parse table and a probability table.
        """
        # TODO, part 3
        table= {}
        probs = {}
        n = len(tokens)

        for tok in range(0,n):
            span = (tok, tok+1)
            if span not in table:
                table[span] = {}
                probs[span] = {}

            non_terminals = grammar.rhs_to_rules[(tokens[tok],)]
            for nt in non_terminals:
                try:
                    if math.log2(nt[2]) > probs[span][nt[0]]:
                        raise KeyError
                        # probs[span][nt[0]] = math.log(nt[2])
                        # table[span][nt[0]] = tokens[tok]
                except KeyError:
                    table[span][nt[0]] = tokens[tok]
                    probs[span][nt[0]] = math.log2(nt[2])

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length
                for k in range(i + 1, j):
                      try:
                          import itertools
                          union = list(itertools.product(table[(i,k)].keys(), table[(k,j-1)].keys()))
                          for un in union:
                              if un in grammar.rhs_to_rules:
                                  non_terminal = grammar.rhs_to_rules[un]
                                  for nt in non_terminal:
                                      if nt[0] not in table[(i,j)]:
                                          table[(i, j)][nt[0]] = ((un[0],i,k),(un[1],k,j))
                                          probs[(i,j)][nt[0]] = math.log2(nt[2]) + probs[(i,k)][un[0]] + probs[(k,j)][un[1]]
                                      else:
                                          if probs[(i,j)][nt[0]] < math.log2(un[2]) + probs[(i,k)][un[0]] + probs[(k,j)][un[1]]:
                                              table[(i, j)][nt[0]] = ((un[0], i, k), (un[1], k + 1, j + 1))
                                              probs[(i, j)][nt[1]] = math.log2(nt[2]) + probs[(i, k + 1)][un[0]] + probs[(k + 1, j + 1)][un[1]]

                      except KeyError:
                          continue
        return table, probs


def get_tree(chart,i,j,nt):
    """
    Return the parse-tree rooted in non-terminal nt and covering span i,j.
    """
    # TODO: Part 4

    if j-i == 1:
        output = (nt, chart[i, j][nt])
        return output

    out1 = get_tree(chart, chart[(i,j)][nt][0][1], chart[(i,j)][nt][0][2], chart[(i,j)][nt][0][0])
    out2 = get_tree(chart, chart[(i,j)][nt][1][1], chart[(i,j)][nt][1][2], chart[(i,j)][nt][1][0])
    return (nt, out1, out2)

       
if __name__ == "__main__":
    
    with open('atis3.pcfg','r') as grammar_file: 
        grammar = Pcfg(grammar_file) 
        parser = CkyParser(grammar)
        toks =['flights', 'from','miami', 'to', 'cleveland','.']
        # toks = ['miami', 'flights', 'cleveland', 'from', 'to', '.']
        print(parser.is_in_language(toks))
        table, probs = parser.parse_with_backpointers(toks)
        assert check_table_format(table)
        assert check_probs_format(probs)
        print(table)
        print(probs)
        get_tree(table, 0, len(toks), grammar.startsymbol)
