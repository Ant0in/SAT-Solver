

from core.expression import Expression
from core.literal import Literal
from core.and_expression import AND_Expression
from core.not_expression import NOT_Expression
from core.or_expression import OR_Expression
from core.tree import ExpressionTree, Node




class ProcessHelper:


    @staticmethod
    def process_expression(expression: Expression) -> dict:
        
        ret: list = list()
        tree: ExpressionTree = ExpressionTree(root=Node(expression=expression))
        simplified: list[list[Literal]] = tree.split_tree()

        print(simplified)
        
        for sp in simplified:

            if not ProcessHelper.has_contradictions(literals=sp):
                ret.append({l.name: (not l.apply_not) for l in sp})

        return ret

    @staticmethod
    def has_contradictions(literals: list[Literal]) -> bool:
        return False