###############################################
Human-Friendly Pedantic ``timedelta`` formatter
###############################################

.. image:: https://travis-ci.org/hotoffthehamster/human-friendly_pedantic-timedelta.svg?branch=develop
  :target: https://travis-ci.org/hotoffthehamster/human-friendly_pedantic-timedelta

.. image:: https://codecov.io/gh/hotoffthehamster/human-friendly_pedantic-timedelta/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/hotoffthehamster/human-friendly_pedantic-timedelta

.. image:: https://img.shields.io/github/license/hotoffthehamster/human-friendly_pedantic-timedelta.svg?style=flat

A Python ``timedelta`` wrapper.

.. image:: docs/assets/hfpt-logo-lrg.png
   :align: left

Install with ``pip``::

    pip3 install human-friendly_pedantic-timedelta

For more installation options, read `docs/installation.rst`.

Simple example::

    $ python3
    >>> from pedantic_timedelta import PedanticTimedelta
    >>> PedanticTimedelta(days=0.33).time_format_scaled()
    # OUTPUT
    # ('7.92 hours', 3600.0, 'hour')

