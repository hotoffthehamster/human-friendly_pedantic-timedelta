############
Installation
############

To install system-wide, run as superuser::

    $ pip install human-friendly_pedantic-timedelta

To install user-local, simply run::

    $ pip install -U human-friendly_pedantic-timedelta

To install within a ``virtualenv``, try::

    $ mkvirtualenv pedantic-timedelta
    $ pip install human-friendly_pedantic-timedelta

To develop on the project, link to the source files instead::

    $ deactivate
    $ rmvirtualenv pedantic-timedelta
    $ git clone git@github.com:hotoffthehamster/human-friendly_pedantic-timedelta.git
    $ cd human-friendly_pedantic-timedelta
    $ mkvirtualenv -a $(pwd) --python=/usr/bin/python3.7 pedantic-timedelta
    $ make develop

To start developing from a fresh terminal, run ``workon``::

    $ workon pedantic-timedelta

