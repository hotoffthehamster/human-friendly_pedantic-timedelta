############
Installation
############

.. |virtualenv| replace:: ``virtualenv``
.. _virtualenv: https://virtualenv.pypa.io/en/latest/

.. |workon| replace:: ``workon``
.. _workon: https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html?highlight=workon#workon

To install system-wide, run as superuser::

    $ pip3 install human-friendly_pedantic-timedelta

To install user-local, simply run::

    $ pip3 install -U human-friendly_pedantic-timedelta

To install within a |virtualenv|_, try::

    $ mkvirtualenv pedantic-timedelta
    (pedantic-timedelta) $ pip install human-friendly_pedantic-timedelta

To develop on the project, link to the source files instead::

    (pedantic-timedelta) $ deactivate
    $ rmvirtualenv pedantic-timedelta
    $ git clone git@github.com:hotoffthehamster/human-friendly_pedantic-timedelta.git
    $ cd human-friendly_pedantic-timedelta
    $ mkvirtualenv -a $(pwd) --python=/usr/bin/python3.7 pedantic-timedelta
    (pedantic-timedelta) $ make develop

After creating the virtual environment,
to start developing from a fresh terminal, run |workon|_::

    $ workon pedantic-timedelta
    (pedantic-timedelta) $ ...

