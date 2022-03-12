Page Objects Pattern
-------------
Page Objects Pattern introduces page objects to make the project structured.

Installing dependencies
^^^^^^^^
`Python 3.9+`_

Virtual Enviornment

PIP Dependencies

- To install packages::

    $ pip install -r requirements.txt

.. _`Python 3.9+`: https://www.python.org/downloads/

Prerequites
^^^^^^^^
Run the Frontend server first by following instructions in the 'Frontend' directory

Running pytest
^^^^^^^^
Test directory of 'tests' is defined at pytest.ini. Pytest will run if you input 'pytest' in the directory of 'page_objects_pattern'.

Example::

    $ pytest
Logging
^^^^^^^^
Allure plugin creates 'test.log' file as soon as pytest running session is done in the root directory of 'page_objects_pattern'.