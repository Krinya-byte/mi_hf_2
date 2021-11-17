import enum
import sys
import re
import copy


class Node:
    def __init__(self, line: list, nodes: list) -> None:
        self.cdom = int(line.pop(0))
        self.pnum = int(line.pop(0))
        self.parents = []
        self.values = {}
        self.index = ''
        if self.pnum != 0:
            for num in range(0,self.pnum):
                self.parents.append(nodes[int(line.pop(0))])
            while(len(line) != 0):
                temp = ''
                templist = []
                for value in range(0,self.pnum):
                    temp += line.pop(0)
                for value in range(0,self.cdom):
                    templist.append(float(line.pop(0)))
                self.values[temp] = templist
        else: 
            for value in range(0,self.cdom):
                self.values[str(value)] = float(line[value])


class BayesianNet:
    def __init__(self) -> None:
        self.nnum = int(input())
        self.nodes = []
        self.enum = 0
        self.evidencenodes = {}
        self.decisions = {}
        for line in range(0, self.nnum):
            debugline = input()
            float_input = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
            rx = re.compile(float_input, re.VERBOSE)
            self.nodes.append(
                Node(rx.findall(debugline), self.nodes))
               #Node(re.findall("\d+(?:\.\d+)?", debugline), self.nodes))
        for node in self.nodes:
            node.index = str(self.nodes.index(node))
        self.enum = int(input())
        for line in range(0,self.enum):
            eline = re.findall("\d+(?:\.\d+)?", input())
            self.evidencenodes[eline[0]] = eline[1]
        self.goalnode = int(input())
        self.decnum = int(input())
        num = len(self.nodes[self.goalnode].values)
        for line in range(0,self.nodes[self.goalnode].cdom*self.decnum):
            decline = input().split()
            tempkey = []
            tempvalue = 0    
            for num in range(0,2):
                tempkey.append(decline.pop(0))
            tempvalue = float(decline.pop(0))
            self.decisions[tuple(tempkey)] = tempvalue
        self.enumeration_ask()
    
    def enumeration_ask(self):
        Q_x = []
        X = self.nodes[self.goalnode]
        E = self.evidencenodes
        tempnodes = copy.deepcopy(self.nodes)        
        for num in range(0,X.cdom):
            E[X.index] = str(num)
            tY = None
            Q_x.append(self.enumerate_all(tempnodes,E,tY))
        sum = 0
        for value in Q_x:
            sum += value
        for value in Q_x:
            print(value/sum,sep='\n')
        desicion = []
        for x in range(0,self.decnum):
            sumdec = 0
            for dom in range(0,self.nodes[self.goalnode].cdom):
                for key, value in self.decisions.items():
                    if int(key[0]) == dom and int(key[1]) == x:
                        sumdec += Q_x[dom] * value
            desicion.append(sumdec)
        maxnum = max(desicion)
        print(desicion.index(maxnum))


    def enumerate_all(self,nodes: list, cE: dict,tY: Node):
        if len(nodes) == 0:
            return 1.0
        Y = nodes.pop(0)
        tY = Y
        if Y.index in cE.keys():
            p = self.P(Y,cE)*self.enumerate_all(nodes,cE,tY) 
            if tY is not None:
                nodes.insert(0,tY)
            return  p
        else:
            tempvalues = 0
            tempE = copy.deepcopy(cE)
            for num in range(0,Y.cdom):
                tempE[Y.index] = str(num)
                tempvalues += self.P(Y,tempE)*self.enumerate_all(nodes,tempE,tY)
            if tY is not None:
                nodes.insert(0,tY)
            return tempvalues


    def P(self,Y: Node,tempE: dict):
        if Y.pnum == 0:
            key = tempE[Y.index]
            return Y.values.get(key)
        else:
            tempstr = ''
            for p in Y.parents:
                tempstr += tempE[p.index]
            p =  Y.values[tempstr]
            return p[int(tempE[Y.index])]
            

net = BayesianNet()
