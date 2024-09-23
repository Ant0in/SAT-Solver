

from core.expression import Expression
from core.literal import Literal



class Node:

    def __init__(self, expression) -> None:
        
        self.expression: list[Expression | Literal] = expression
        self.childrens: list['Node'] = []

    def is_literal(self) -> bool:

        for p in self.expression:
            if isinstance(p, Expression): return False
        return True
    
    def add_children(self, n: 'Node') -> None:
        assert isinstance(n, Node)
        self.childrens.append(n)



class Tree:

    def __init__(self, root: Node) -> None:
        self.root: Node = root

    def get_leaves(self) -> list[Node]:

        stack: list = [self.root]
        visited: set = set()
        ret: list = list()

        while stack:
            
            current: Node = stack.pop()
            if current not in visited:
                visited.add(current)

                if not c.childrens:
                    ret.append(current)
                    continue

                for c in current.childrens:
                    stack.append(c)

        return ret