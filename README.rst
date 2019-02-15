###############################################
Human-Friendly Pedantic ``timedelta`` formatter
###############################################

A Python ``timedelta`` wrapper.

.. image :: assets/hfpt-logo-lrg.png

Install with ``pip``::

    pip3 install human-friendly_pedantic-timedelta

For more installation options, read `docs/installation.rst`.

Simple example::

    $ python3
    >>> from pedantic_timedelta import PedanticTimedelta
    >>> PedanticTimedelta(days=0.33).time_format_scaled()
    # OUTPUT
    # ('7.92 hours', 3600.0, 'hour')


