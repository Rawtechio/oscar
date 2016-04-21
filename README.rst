.. image:: oscar.png

Oscar
==============================

.. image:: https://travis-ci.org/Rawtechio/oscar.svg?branch=master
    :target: https://travis-ci.org/Rawtechio/oscar

.. image:: https://codecov.io/github/Rawtechio/oscar/coverage.svg?branch=master
    :target: https://codecov.io/github/Rawtechio/oscar?branch=master

.. image:: https://requires.io/github/Rawtechio/oscar/requirements.svg?branch=master
     :target: https://requires.io/github/Rawtechio/oscar/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://landscape.io/github/Rawtechio/oscar/master/landscape.svg?style=flat
   :target: https://landscape.io/github/Rawtechio/oscar/master
   :alt: Code Health


About
-----

This is a PoC for the GCC customer first program phase 1.
For travis

Deploy
------

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy

Running tests
-------------

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd oscar
    celery -A oscar.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.