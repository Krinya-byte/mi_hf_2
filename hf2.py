import sys
import re


class Node:
    def __init__(self, line: str, nodes: list) -> None:
        line.split('\t')
        self.cdom = int(line.pop(0))
        self.pnum = int(line.pop(0))
        self.parentindexes = []
        self.parents = []
        self.values = [[]]
        if self.pnum is not 0:
            for num in range(0,self.pnum):
                self.parentindexes.append(line.pop(0))
            
        for num in nodes:
            self.parents.append(nodes[self.parentindexes[nodes]])
        else:
            for value in line:
                self.values.append(value)


class BayesianNet:
    def __init__(self) -> None:
        self.nnum = int(input())
        self.nodes = []
        for line in range(0, self.nnum):
            self.nodes.append(
            line
            )
                #Node(re.findall("\d+(?:\.\d+)?", sys.stdin.readline()), self.nodes))


net = BayesianNet()
