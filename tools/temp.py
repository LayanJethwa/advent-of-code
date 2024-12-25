import math
import g
import re
import functools
from collections import defaultdict
from copy import deepcopy
import networkx as nx

d = defaultdict(int)
ll = open("input.txt",'r').read().splitlines()
ll = open("test.txt",'r').read().splitlines()
a = 0
for l in ll:
    #l = [int(i.group()) for i in re.finditer("-?\d+",l)]
    #l = l.split()
    #l = [int i for i in l]
    #l = l.replace('
    #l = l.split('
print(a)