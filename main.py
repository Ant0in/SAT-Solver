
from core.literal import Literal
from core.and_expression import AND_Expression
from core.not_expression import NOT_Expression
from core.or_expression import OR_Expression
from scripts.create_expression_tree import ExpressionTreeHelper



e: list = AND_Expression(OR_Expression(Literal('x'), Literal('y')), AND_Expression(NOT_Expression(Literal('x')), NOT_Expression(Literal('y'))))
h: ExpressionTreeHelper = ExpressionTreeHelper(expression=e)

print(e)
print(h.expression_tree.decompose())