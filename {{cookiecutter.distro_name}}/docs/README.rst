{{cookiecutter.package_name}}
=============================

FIXME: provide a two paragraphs summary of this package


Developer notes
---------------

Installation and Setup
......................

Please use a virtualenv to maintain this package, but I should not need to say that.

Grab the source from the SCM repository:

.. code:: console

  $ git clone git@git.ivxs.uk:{{cookiecutter.distro_name}}
  $ cd {{cookiecutter.distro_name}}
  $ python3.7 -m virtualenv .venv
  $ source .venv/bin/activate
  $ pip install -e '.[dev]'

Remember, you'll need to activate the virtual environment every time you want to work with your project, in every
console.

Useful Commands
...............

Run unit tests:

.. code:: console

  $ make test-unit

Run integration tests:

.. code:: console

  $ make test-integration

Run all tests:

.. code:: console

  $ make tests

Lint the code (using pylint):

.. code:: console

  $ make lint

Run typecheck:

.. code:: console

  $ make typecheck

Check code with ``black``:

.. code:: console

  $ make black-check

Fix code formatting with ``black``:

.. code:: console

  $ make black-fix

Run code coverage:

.. code:: console

  $ make coverage

Generate HTML documentation (in docs/_build):

.. code:: console

  $ make docs

Links
-----

Project home page

  https://git.ivxs.uk/{{cookiecutter.distro_name}}

Issues tracker

  https://git.ivxs.uk/{{cookiecutter.distro_name}}/issues
