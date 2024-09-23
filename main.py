
from core.literal import Literal
from core.and_expression import AND_Expression
from core.not_expression import NOT_Expression
from core.or_expression import OR_Expression
from core.expression import Expression



e: list = [OR_Expression(Literal('a'), AND_Expression(Literal('b'), Literal('c')))]