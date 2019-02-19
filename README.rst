#####################################
Human-Friendly Pedantic ``timedelta``
#####################################

.. image:: https://travis-ci.org/hotoffthehamster/human-friendly_pedantic-timedelta.svg?branch=develop
  :target: https://travis-ci.org/hotoffthehamster/human-friendly_pedantic-timedelta
  :alt: Build Status

.. image:: https://codecov.io/gh/hotoffthehamster/human-friendly_pedantic-timedelta/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/hotoffthehamster/human-friendly_pedantic-timedelta
  :alt: Coverage Status

.. image:: https://readthedocs.org/projects/human-friendly-pedantic-timedelta/badge/?version=latest
  :target: https://human-friendly-pedantic-timedelta.readthedocs.io/en/latest/
  :alt: Documentation Status

.. image:: https://img.shields.io/github/release/hotoffthehamster/human-friendly_pedantic-timedelta.svg?style=flat
  :target: https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta/releases
  :alt: GitHub Release Status

.. image:: https://img.shields.io/pypi/v/human-friendly-pedantic-timedelta.svg
  :target: https://pypi.org/project/human-friendly-pedantic-timedelta/
  :alt: PyPI Release Status

.. image:: https://img.shields.io/github/license/hotoffthehamster/human-friendly_pedantic-timedelta.svg?style=flat
  :target: https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta/blob/develop/LICENSE
  :alt: License Status

A Python ``timedelta`` wrapper which provides pedantic string formatting.

Install with ``pip``::

    pip3 install human-friendly_pedantic-timedelta

For more options, read the
`installation guide
<https://human-friendly-pedantic-timedelta.readthedocs.io/en/latest/installation.html>`__.

Simple example::

    $ python3
    >>> from pedantic_timedelta import PedanticTimedelta
    >>> PedanticTimedelta(days=0.33).time_format_scaled()
    # OUTPUT
    # ('7.92 hours', 3600.0, 'hour')

|

.. image:: https://raw.githubusercontent.com/hotoffthehamster/human-friendly_pedantic-timedelta/master/docs/assets/hfpt-logo-lrg.png
   :target: https://human-friendly-pedantic-timedelta.readthedocs.io/en/develop/authors.html#graphics-shout-out
   :align: center
   :alt: "Penrose Hourglass"

