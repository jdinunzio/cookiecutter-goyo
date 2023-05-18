# -*- coding: utf-8 -*-
from unittest import TestCase

from {{cookiecutter.package_name}}.sum import Sum


class TestSum(TestCase):
    """Test case for Sum."""

    @classmethod
    def setUpClass(cls):
        cls.adder = Sum()

    def test_sum(self):
        """Sum must return the addition of two numbers

        Given two numbers
        When Sum.sum() is invoked
        Then it must return their sum.
        """
        operand_a, operand_b = 2, 3
        self.assertEqual(self.adder.sum(operand_a, operand_b), operand_a + operand_b)
