import random
import sys

"""
    According to some calculations:
    The sum of all possible moves (the number of tree edges) is O(3/2*n^2)
    where n is the "length" of a single list
"""

length = 5000

def create_random_list(length):
    random_list=list()
    for x in range(length):
        seed = random.random()
        if seed <= 0.5:
            random_list.append(False)
        else:
            random_list.append(True)
    return random_list

firstList =  create_random_list(length)   
secondList = create_random_list(length)

class Node:

    def __init__(self):
        self.left = None
        self.right = None

    def addRightSon(self):
        self.right= Node()

    def addLeftSon(self):
        self.left= Node()

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}Node")
        if self.left:
            print(f"{indent}  Left:", self.left)
            self.left.display(level + 1)
        if self.right:
            print(f"{indent}  Right:", self.right)
            self.right.display(level + 1)

def false_decision(levelFirst, levelSecond, moves, node):
    if firstList[levelFirst]==False and secondList[levelSecond]==False and levelFirst != length-1 and levelSecond != length-1:
        node.addLeftSon() 
        moves=moves.copy()
        moves.append(False)
        return solve(levelFirst+1, levelSecond+1, moves, node=node.left)
    elif secondList[levelSecond]==False and levelSecond != length-1:
        node.addLeftSon() 
        moves=moves.copy()
        moves.append(False)
        return solve(levelFirst, levelSecond+1, moves, node=node.left)
    elif firstList[levelFirst]==False and levelFirst != length-1:
        node.addLeftSon() 
        moves=moves.copy()
        moves.append(False)
        return solve(levelFirst+1, levelSecond, moves, node=node.left)
    return None
    
def true_decision(levelFirst, levelSecond, moves, node):
    if firstList[levelFirst]==True and secondList[levelSecond]==True and levelFirst != length-1 and levelSecond != length-1:
        node.addRightSon() 
        moves=moves.copy()
        moves.append(True)
        return solve(levelFirst+1, levelSecond+1, moves, node=node.right)
    elif secondList[levelSecond]==True and levelSecond != length-1:
        node.addRightSon() 
        moves=moves.copy()
        moves.append(True)
        return solve(levelFirst, levelSecond+1, moves, node=node.right)
    elif firstList[levelFirst]==True and levelFirst != length-1:
        node.addRightSon() 
        moves=moves.copy()
        moves.append(True)
        return solve(levelFirst+1, levelSecond, moves, node=node.right)
    return None
                                                                                                                        
def solve(levelFirst=0, levelSecond=0, moves=list(), node=Node()):     

    if levelFirst > length-1 or levelSecond > length-1:
        return None
    elif levelFirst == length -1 and levelSecond==length-1:
        print("Solution: ", moves)
        return moves
  
    seed = random.random()
    
    if seed <= 0.5:     #false decision
        decision = False
        res = false_decision(levelFirst, levelSecond, moves.copy(), node)
    else:               #true decision
        decision = True
        res = true_decision(levelFirst, levelSecond, moves.copy(), node)
    if res == None:
        if decision == False:   
            res = true_decision(levelFirst, levelSecond, moves.copy(), node)
        else:
            res = false_decision(levelFirst, levelSecond, moves.copy(), node)
    return res
    
def main():
    
    root = Node()

    # set recursion limit
    sys.setrecursionlimit(15000)
    recursion_limit = sys.getrecursionlimit()
     
    #print initial data
    print("INITIAL DATA:")
    print(f"First list:\n\t{firstList}")
    print(f"Second list:\n\t{secondList}")
   
    check = True    #check if the program terminates correctly
    note = " - "
    try:
        solution = solve(node=root)
        if solution == None:
            check = False
            note = "It did not find any solution"
    except RecursionError:
        check = False
        note = "Recursion limit exceeded"

    #root.display()
    print(f"Program successfully completed: {check}\tRecursion limit: {recursion_limit}\tNote: {note}")

if __name__ == "__main__":
    main()