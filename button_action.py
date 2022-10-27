"""
ButtonAction Module
"""

import re
from main import TransformExpression, Calculator, check_expression
from stack import Stack


class ButtonAction:
    """
    Actions for calculator buttons
    """
    def __init__(self, input_text):
        self.expression = ""
        self.stack = Stack()
        self.rpn = TransformExpression(self.stack)
        self.input_text = input_text

    def bt_click(self, item):
        """
        Presses a button
        """
        self.expression = self.expression + str(item)
        unexpected_combos = ['+-', '+*', '+/', '+^', '-+', '-*', '-/', '-^', '*+', '*-',
                             '*/', '*^', '/+', '/-', '/*', '/^', '^+', '^-', '^*', '^/',
                             '++', '--', '**', '//', '^^', '+.', '-.', '*.', '/.', '^.',
                             '.+', '.-', '.*', './', '.^']
        if self.expression[-2:] in unexpected_combos:
            self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def bt_clear(self):
        """
        Clears input field
        """
        self.expression = ""
        self.input_text.set("")

    def bt_equal(self):
        """
        Outputs the result of expression
        """
        self.expression = check_expression(self.expression)
        rpn_list = self.rpn.to_list(self.expression)
        num1 = Calculator(self.stack)
        rpn_str = self.rpn.transformation(rpn_list)
        result = num1.display_calculation(num1.to_list(rpn_str))
        result_str = str(result)
        if result_str[-2:] == '01':
            result_str = re.sub('[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?[0]?01',
                                '', result_str)
            result = float(result_str)
        self.expression = ""
        self.input_text.set(result)
