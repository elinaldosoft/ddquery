Django Debug Query (ddquery)
-------------------------------
Ddquery is one lib in python for beautiful colored SQL statements, for database relational in Django

Requirements
------------------
- Python ≥ 3.3
- Django ≥ 1.8

How it looks like?
------------------

.. code-block:: console

    python manage.py runserver

.. image:: https://raw.githubusercontent.com/elinaldosoft/ddquery/master/imgs/shell-01.png
    :alt: Shell

.. code-block:: console

    python manage.py shell

.. image:: https://raw.githubusercontent.com/elinaldosoft/ddquery/master/imgs/shell-02.png
    :alt: Shell 02

.. code-block:: console

    python manage.py migration

.. image:: https://raw.githubusercontent.com/elinaldosoft/ddquery/master/imgs/migration.png
    :alt: Migration


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
