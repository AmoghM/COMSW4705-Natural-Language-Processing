`RESULT: Coverage: 67%, Average F-score (parsed sentences): 0.95, Average F-score (all sentences): 0.64`

The PDF version of the question and solution is available in the files `hw2_questions.pdf` and `hw2_solutions.pdf`. <br>
This assignment had 2 sections:
* Programming: Write CYK parsing algorithm along with backpointers on ATIS (Air Travel Information Services) subsection of the Penn Treebank.
Complete question is present in `hw2_questions.pdf`
Commands To Run:
1. Reading Grammar: `python grammar.py atis.pcfg`

2. Parsing using CKY and creating backpointers : `python cky.py`

3. Evaluate F1-score on atis test data : `python evaluate.py`

* Written: <i>Q/A below</i>
### Problem 1 (10 pts) - PCFGs and HMMs
Both PCFGs and HMMs can be seen as generative models that produce a sequence of POS tags 
and words with some probability (of course the PCFG will generate even more structure, 
but it will also generate POS tags and words). <br>
(a) Consider the grammar specified in Problem 2 below, and the sentence <i>"they are baking potatoes"</i>. 
For each sequence of POS tags that is possible for this sentence according to the grammar, 
what is the joint probability P(tags,words) according to the PCFG? 
Hint: consider all parses for the sentence -- you may want to work on problem 2 first. 
<br><br>
(b) Design an HMM that produces the same joint probability P(tags, words) as the PCFG for each of the possible tag sequences for the sentence in part (a). 
Note: Your HMM does not have to assign 0 probabilities to tag sequences that are not possible according to the PCFG. 
<br><br>
(c) In general, is it possible to translate any PCFG into an HMM that produces the identical joint probability P(tags,words) as the PCFG (i.e. not just for a single sentence)? Explain how or why not. 
No formal proof is necessary. Hint: This has nothing to do with probabilities, but with language classes

### Problem 2 (10 pts) - Earley Parser
Earley Parser Consider the following probabilistic context free grammar.

S → NP VP [1.0]<br>
NP → Adj NP [0.3] <br>
NP → PRP [0.1] <br>
NP → N [0.6] <br>
VP → V NP [0.8] <br>
VP → Aux V NP [0.2]<br>
PRP → they [1.0] <br>
N → potatoes [1.0] <br>
Adj → baking [1.0] <br>
V → baking [0.5] <br>
V → are [0.5] <br>
Aux → are [1.0]<br>

(a) Using this grammar, show how the <b>Earley algorithm</b> would parse the following sentence. 
<i>they are baking potatoes</i> <br>
Write down the complete parse chart. The chart should contain n+1 entries where n is the length of the sentence. 
Each entry i should contain all parser items generated by the parser that end in position i. You can ignore the probabilities for part (a).
<br><br>
(b) Write down all parse trees for the sentence and grammar from problem 2 and compute their probabilities according to the PCFG.


### Problem 3 (10 pts) - CKY parsing 
(a) Convert the grammar from problem 2 into an equivalent grammar in Chomsky Normal Form (CNF). Write down the new grammar. 
Also explain what the general rule is for dealing with
<br>
1. Rules of the form A→B (i.e. a single nonterminal on the right hand side).<br>
2. Rules with three or more nonterminals on the right hand side (e.g. A→B C D E).<br>

You do not have to deal with the case in which terminals and non-terminals are mixed in a rule right-hand side. 
You also do not have to convert the probabilities. Hint: Think about adding new nonterminal symbols.
<br>

(b) Using your grammar, fill the CKY parse chart as shown in class and show all parse trees.

### Problem 4 (10 pts) - Transition Based Dependency Parsing Consider the following dependency graph
![Q4 image](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/dep-parse.JPG)
Write down the sequence of transitions that an arc-standard dependency parser would have to take to generate this dependency tree from the initial state. <br>
([root]σ, [he, sent, her, a, funny, meme, today]β, {}A) <br>
Also write down the state resulting from each transition

#### Solution:-
![Solution image 1](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_1.jpg)
![Solution image 2](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_2.jpg)
![Solution image 3](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_3.jpg)
![Solution image 4](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_4.jpg)
![Solution image 5](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_5.jpg)
![Solution image 6](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_6.jpg)
![Solution image 7](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_7.jpg)
![Solution image 8](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_8.jpg)
![Solution image 9](https://github.com/AmoghM/COMSW4705-Natural-Language-Processing/blob/master/hw2-parsing/pic/NLP-HW-2_9.jpg)




