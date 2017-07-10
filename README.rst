Django Debug Query (ddquery)
-------------------------------
Ddquery is one lib in python for beautiful colored SQL statements, for database relational in Django

How it looks like?
------------------

.. image:: https://raw.githubusercontent.com/elinaldosoft/ddquery/master/imgs/shell-01.png
    :alt: Shell

How to use
-----------

.. code-block:: console

    pip install ddquery


Add it to your Django Logging settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add it to yout Django LOGGING settings:

.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'sqlhandler': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'sqlformatter'
            }
        },
        'formatters': {
            'sqlformatter': {
                '()': 'ddquery.SqlFormatter',
                'format': '%(levelname)s %(message)s',
            },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['sqlhandler'],
                'level': 'DEBUG',
            },
        }
    }
