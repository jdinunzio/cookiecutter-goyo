# -*- coding: utf-8 -*-
"""Sum module documentation. It's always nice to have module docs."""


class Sum:  # pylint: disable=too-few-public-methods
    """Sum class. This class implements the sum of two numbers."""

    @staticmethod
    def sum(operand_a: float, operand_b: float) -> float:
        """Sum two numbers.

        Args:
            operand_a: First Operand.
            operand_b: Second Operand.

        Returns:
            Sum of a and b.
        """
        return operand_a + operand_b
