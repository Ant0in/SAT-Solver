

from core.expression import Expression
from core.literal import Literal
from core.and_expression import AND_Expression
from core.or_expression import OR_Expression
from core.not_expression import NOT_Expression


class TreeNode:

    def __init__(self, expression: Expression):
        self.expression = expression
        self.left = None  # Pour les sous-expressions
        self.right = None  # Pour les sous-expressions

    def decompose(self):
        if isinstance(self.expression, Literal):
            return [[self.expression]]
        
        # Pour OR et AND, décomposer récursivement
        if isinstance(self.expression, OR_Expression):
            left_decomp = TreeNode(self.left).decompose()  # Decomposition gauche
            right_decomp = TreeNode(self.right).decompose()  # Decomposition droite
            return left_decomp + right_decomp  # Combiner les deux décompositions

        elif isinstance(self.expression, AND_Expression):
            return [[self.left.expression, self.right.expression]]  # Tout doit être ensemble

        elif isinstance(self.expression, NOT_Expression):
            return [[self.expression.first]]  # Pour NOT, on peut le traiter comme une clause

        return []