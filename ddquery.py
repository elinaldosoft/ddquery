#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import sqlparse
from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import Terminal256Formatter

__author__ = '@elinaldosoft'


class SqlFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        self.highlight = kwargs.pop('highlight', True)
        self.style = kwargs.pop('style', 'default')

        self.parse = kwargs.pop('parse', True)
        self.reindent = kwargs.pop('reindent', True)
        self.keyword_case = kwargs.pop('keyword_case', 'upper')

        self._lexer = SqlLexer()
        self._formatter = Terminal256Formatter(style=self.style)

        super(SqlFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        super(SqlFormatter, self).format(record)
        sql = record.sql.strip()

        if self.parse:
            sql = sqlparse.format(sql, reindent=self.reindent, keyword_case=self.keyword_case)
            if hasattr(record, 'duration'):
                sql = "({0:.3f}ms) {1}".format(record.duration, sql)

        if self.highlight:
            sql = highlight(
                    sql,
                    self._lexer,
                    self._formatter
                )

        return sql
