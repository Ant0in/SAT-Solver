

from core.expression import Expression
from core.tree import TreeNode
from core.literal import Literal
from core.and_expression import AND_Expression
from core.or_expression import OR_Expression
from core.not_expression import NOT_Expression


class ExpressionTreeHelper:

    def __init__(self, expression: list[Expression]) -> None:
        
        self.expression: list[Expression] = expression
        self.expression_tree: TreeNode = self.build_tree(expression=expression)

    @staticmethod
    def build_tree(expression):
        
        node = TreeNode(expression)
        
        if isinstance(expression, OR_Expression):
            node.left = ExpressionTreeHelper.build_tree(expression.first)
            node.right = ExpressionTreeHelper.build_tree(expression.second)

        elif isinstance(expression, AND_Expression):
            node.left = ExpressionTreeHelper.build_tree(expression.first)
            node.right = ExpressionTreeHelper.build_tree(expression.second)

        elif isinstance(expression, NOT_Expression):
            node.left = ExpressionTreeHelper.build_tree(expression.first)

        return node




