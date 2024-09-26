

from core.expression import Expression
from core.literal import Literal
from core.and_expression import AND_Expression
from core.or_expression import OR_Expression
from core.not_expression import NOT_Expression


class Node:

    def __init__(self, expression: Expression | Literal) -> None:

        self.expression: list[Expression | Literal] = [expression]
        self.children: list[Expression | Literal] = list()
    
    def add_children(self, child: 'Expression | Literal') -> None:
        self.children.append(child)



class ExpressionTree:

    def __init__(self, root: Node) -> None:
        self.root = root

    def split_tree(self) -> list[list[Literal]]:
        return self._split_node(self.root)

    def _split_node(self, node: Node) -> list[list[Literal]]:
        
        # Lets take the first expression of the node.
        expr: Expression = node.expression[0]

        # If it's a literal, then it's already simplified.
        if isinstance(expr, Literal):
            return [[expr]]

        # If it's an AND, we have to combine left and right branches.
        if isinstance(expr, AND_Expression):
            left_branches: list[list[Literal]] = self._split_node(Node(expr.first))
            right_branches: list[list[Literal]] = self._split_node(Node(expr.second))
            # Combine les branches de gauche avec celles de droite.
            return [left_branch + right_branch for left_branch in left_branches for right_branch in right_branches]

        # If it's an OR, we branch.
        elif isinstance(expr, OR_Expression):
            left_branches: list[list[Literal]] = self._split_node(Node(expr.first))
            right_branches: list[list[Literal]] = self._split_node(Node(expr.second))
            # Chaque côté du OR devient une branche.
            return left_branches + right_branches

        # if it's a NOT, we use Morgan's laws.
        elif isinstance(expr, NOT_Expression):
            
            negated_expressions = expr.morgan_laws_split()
            result_branches = []
            for branch in negated_expressions:
                result_branches.extend(self._split_node(Node(branch[0])))
            return result_branches

        else:
            raise ValueError(f"Type d'expression non supporté : {type(expr)}")

