#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import pickle
from ddquery import SqlFormatter
import sqlparse
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import Terminal256Formatter

__author__ = '@elinaldosoft'


class TestSqlFormatter(unittest.TestCase):

    def setUp(self):
        with open("data.p", "rb") as d:
            self.model = pickle.load(d)
        d.close()

    def test_sqlformatter(self):
        sqlformatter = SqlFormatter().format(self.model)
        sql_compare = 'SELECT "django_migrations"."app","django_migrations"."name" FROM "django_migrations"'
        sql_compare = sqlparse.format(sql_compare, reindent=True, keyword_case='upper')
        sql_compare = "(0.005ms) {0}".format(sql_compare)

        sql_compare = highlight(
            sql_compare,
            SqlLexer(),
            Terminal256Formatter(style='default')
        )

        self.assertEqual(sql_compare, sqlformatter)
