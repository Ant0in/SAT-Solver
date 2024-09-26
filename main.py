

from core.literal import Literal
from core.and_expression import AND_Expression
from core.not_expression import NOT_Expression
from core.or_expression import OR_Expression

from scripts.process_expression import ProcessHelper



if __name__ == '__main__':
    
    # Création des littéraux
    literal_A = Literal('A')
    literal_B = Literal('B')
    literal_C = Literal('C')
    literal_D = Literal('D')

    e = OR_Expression(AND_Expression(literal_A, literal_B), AND_Expression(NOT_Expression(literal_A), NOT_Expression(literal_B)))

    print(ProcessHelper.process_expression(e))
