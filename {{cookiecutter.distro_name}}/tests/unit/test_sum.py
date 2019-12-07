# -*- coding: utf-8 -*-
from {{cookiecutter.package_name}}.sum import Sum

from unittest import TestCase


class TestSum(TestCase):

    @classmethod
    def setupClass(cls):
        cls.sum = Sum()

    def test_sum(self):
        """Sum must return the addition of two numbers"""
        a, b = 2, 3
        self.assertEqual(Sum.sum(a, b), a + b)

