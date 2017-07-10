#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import pickle
from ddquery import ddquery

__author__ = '@elinaldosoft'


class TestSqlFormatter(unittest.TestCase):

    def test_load_object(self):

        with open("data.p", "rb") as d:
            model = pickle.load(d)
        d.close()

        print(model)


