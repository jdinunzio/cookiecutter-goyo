# -*- coding: utf-8 -*-
"""sum module documentation. It's always nice to have module docs"""


class Sum:  # pylint: disable=too-few-public-methods
    """Sum class. This class implements the sum of two numbers."""

    def sum(self, operand_a: float, operand_b: float) -> float:  # pylint: disable=no-self-use
        """Sum two numbers.

        Args:
            operand_a: First Operand.
            operand_b: Second Operand.

        Returns:
            Sum of a and b.
        """
        return operand_a + operand_b
