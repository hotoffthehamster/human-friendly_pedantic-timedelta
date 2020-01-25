# This file exists within 'human-friendly_pedantic-timedelta' aka 'pedantic_timedelta':
#
#   https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta
#
# Copyright © 2018-2020 Landon Bouma. All rights reserved.
#
# Permission is hereby granted,  free of charge,  to any person obtaining a
# copy of this software and associated documentation files (the ),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge,  publish,  distribute, sublicense,
# and/or  sell copies  of the Software,  and to permit persons  to whom the
# Software  is  furnished  to do so,  subject  to the following conditions:
#
# The  above  copyright  notice  and  this  permission  notice  shall  be
# included  in  all  copies  or  substantial  portions  of  the  Software.
#
# THE  SOFTWARE  IS  PROVIDED  ,  WITHOUT  WARRANTY  OF ANY KIND,
# EXPRESS OR IMPLIED,  INCLUDING  BUT NOT LIMITED  TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE  FOR ANY
# CLAIM,  DAMAGES OR OTHER LIABILITY,  WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE,  ARISING FROM,  OUT OF  OR IN  CONNECTION WITH THE
# SOFTWARE   OR   THE   USE   OR   OTHER   DEALINGS  IN   THE  SOFTWARE.

"""A Human-friendly Pedantic `timedelta` formatter."""

from __future__ import absolute_import, unicode_literals

from gettext import gettext as _

import time
from datetime import timedelta
from inflector import Inflector, English

import logging
log = logging.getLogger('timedelta_wrap')


class PedanticTimedelta(timedelta):
    """
    Wrapper formats timedelta using least common whole number time unit.

    - A :func:`datetime.timedelta` formatter that uses progressive time unit
      labels to prepare a delta time value for output.

    .. NOTE::

        Unlike :func:`datetime.timedelta`, which accepts weeks but not
        months, nor years, because not every month, nor every year has
        the same number of days, this class fudges the calculation,
        allowing one to specify imprecise time deltas.

    :cvar DAYS_IN_YEAR: Mean tropical year (using Laskar's expression)
                        on January 1, 2000.

    - https://en.wikipedia.org/wiki/Tropical_year

    """

    # https://en.wikipedia.org/wiki/Tropical_year
    #  Laskar's expression: Mean tropical year on 1/1/2000 was 365.242189 days.
    #  Gregorian calendar average year is 365.2425 days, matching northward
    #  (March) equinox year of 365.2424 days (as of January 2000).
    # Calculating from rough estimate of 365d 5h 48m 46s per year.
    #  time_in_year = timedelta(days=365, hours=5, minutes=48, seconds=46)
    #  SECS_IN_YEAR = time_in_year.total_seconds() # 31556926
    #  DAYS_IN_YEAR = SECS_IN_YEAR / 24.0 / 60.0 / 60.0 # 365.2421991
    # Calculating from scholarly numbers.
    DAYS_IN_YEAR = 365.242189
    """
    Mean tropical year (using Laskar's expression) on 1/1/2000.
    - https://en.wikipedia.org/wiki/Tropical_year
    """

    SECS_IN_DAY = 86400
    """1/86,400 is mean of solar day."""

    SECS_IN_YEAR = DAYS_IN_YEAR * SECS_IN_DAY  # 31556925.1296
    """DAYS_IN_YEAR * SECS_IN_DAY"""

    # Average number of days in a month.
    # MAGIC_NUMBERS: 7 months are 31 days long, 4 are 40, and one is 28ish.
    #  avg_month_days = (7*31 + 4*30 + 28.25) / 12.0 # 30.4375
    DAYS_IN_MONTH = DAYS_IN_YEAR / 12.0  # 30.436849
    """DAYS_IN_YEAR / 12.0"""

    SECS_IN_MONTH = SECS_IN_YEAR / 12.0  # 2629743.7608
    """SECS_IN_YEAR / 12.0"""

    # ***

    # We override __new__ and not __init__ because we want to be
    # called before timedelta.__init__.
    def __new__(
        cls=None,
        # Part of timedelta:
        days=0,
        seconds=0,
        microseconds=0,
        milliseconds=0,
        minutes=0,
        hours=0,
        weeks=0,
        # Our additions:
        fortnights=0,
        months=0,
        seasons=0,
        years=0,
        bienniums=0,
        decades=0,
        jubilees=0,
        centuries=0,
        millenniums=0,
        ages=0,
        megaannums=0,
        epochs=0,
        eras=0,
        eons=0,
        gigaannums=0
    ):
        """Create new PedanticTimedelta instance.

        A wrapper around `datetime.timedelta.__new__`
        that recognizes additional time units, including
        'months', 'years', and much, much more.

        In addition to the parent class's parameters -- *days*, *seconds*,
        *microseconds*, *minutes*, *hours*, and *weeks* -- the following
        constructor parameters are recognized.

        (Note that all arguments are optional and default to 0.
        Arguments may be integers or floats, and may be positive or negative.
        Only days, seconds and microseconds are stored internally.
        Other arguments are converted to those units and added together.)

        :param fortnights: 14 days each.
        :param months: Approximated as :py:attr:`DAYS_IN_MONTH`.
        :param seasons: ¼ year each.
        :param years: Approximated as :py:attr:`DAYS_IN_YEAR`.
        :param bienniums: 2 years each.
        :param decades: 10 years each.
        :param jubilees: 50 years each.
        :param centuries: 100 years each.
        :param millenniums: 1000 years each.
        :param ages: 1000000 years each.
        :param megaannums: 1000000 years each.
        :param epochs: 10000000 years each.
        :param eras: 100000000 years each.
        :param eons: 500000000 years each.
        :param gigaannums: 1000000000 years each.

        :type fortnights: float
        :type months: float
        :type seasons: float
        :type years: float
        :type bienniums: float
        :type decades: float
        :type jubilees: float
        :type centuries: float
        :type millenniums: float
        :type ages: float
        :type megaannums: float
        :type epochs: float
        :type eras: float
        :type eons: float
        :type gigaannums: float
        """
        def new_timedelta():
            totaled_days = as_days()
            must_not_be_more_than_2737909_years(totaled_days)
            return new_object(totaled_days)

        def as_days():
            totaled_days = days
            # Ref: https://en.wikipedia.org/wiki/Unit_of_time
            # FIXME: 2015.02.04: Needs testing, especially because overflows
            #        might mean parent class can only represent so many days.
            n_years = 0
            n_years +=   1000000000 * gigaannums    # noqa: E222
            n_years +=    500000000 * eons          # noqa: E222
            n_years +=    100000000 * eras          # noqa: E222
            n_years +=     10000000 * epochs        # noqa: E222
            n_years +=      1000000 * megaannums    # noqa: E222
            n_years +=      1000000 * ages          # noqa: E222
            n_years +=         1000 * millenniums   # noqa: E222
            n_years +=          100 * centuries     # noqa: E222
            n_years +=           50 * jubilees      # noqa: E222
            n_years +=           10 * decades       # noqa: E222
            n_years +=            2 * bienniums     # noqa: E222
            n_years +=            1 * years         # noqa: E222
            n_years +=         0.25 * seasons       # noqa: E222
            n_days = n_years * PedanticTimedelta.DAYS_IN_YEAR
            n_days += PedanticTimedelta.DAYS_IN_MONTH * months
            n_days +=            14 * fortnights    # noqa: E222
            totaled_days += n_days
            return totaled_days

        def must_not_be_more_than_2737909_years(totaled_days):
            # Watch out for OverflowError.
            #   >>> timedelta(math.pow(2,31))
            #   OverflowError: normalized days too large to fit in a C int
            # Also note different (but similar) errors, one being more helpful.
            #   >>> timedelta(math.pow(2,30))
            #   OverflowError: days=1073741824; must have magnitude <= 999999999
            # Checking the more better error message:
            #   >>> timedelta(999999999)
            #   datetime.timedelta(999999999)
            #   >>> timedelta(1000000000)
            #   OverflowError: days=1000000000; must have magnitude <= 999999999
            #
            # BUG nnnn/WONTFIX: Support any int and not just C ints.
            #     999999999/365.242189 = 2737909.3
            #     so we can only support megaannums and nothing more.
            #     (At least total_seconds() works 'til infinity!)
            if totaled_days > 999999999:
                raise ValueError(
                    'pedantic_timedelta:'
                    ' That many days is not supported.'
                    ' Try <= 999999999'
                )

        def new_object(totaled_days):
            td_cls = cls
            if td_cls is None:
                td_cls = timedelta
            return timedelta.__new__(
                td_cls,
                days=totaled_days,
                seconds=seconds,
                microseconds=microseconds,
                milliseconds=milliseconds,
                minutes=minutes,
                hours=hours,
                weeks=weeks
            )

        return new_timedelta()

    # ***

    @staticmethod
    def time_format_elapsed(secs_then, secs_now=None):
        """Format elapsed time pedantically.

        :param secs_then: seconds at time of event (e.g., ``time.time()``).
        :type secs_then: float

        :param secs_now: seconds from which to calculate elapsed time.
             Defaults to now if not specified (in which case `secs_then`
             should be represented as seconds since epoch).
        :type secs_now: float

        :return: elapsed time formatted using single unit of time
        :rtype: string
        """
        if secs_now is None:
            secs_now = time.time()
        secs_elapsed = secs_now - secs_then
        tdw = PedanticTimedelta(seconds=secs_elapsed)
        return tdw.time_format_scaled()[0]

    def _units_and_scale(self):
        """Determine best time unit to use to represent time duration.

        Private method determines the maximum scale that can be used to
        represent a time value as 1 of more of a unit, e.g., 1 second, 59
        minutes, 15 days, but never 61 seconds, 90 minutes, 35 days, etc.
        """
        is_abbrev = False
        if self.total_seconds() >= PedanticTimedelta.SECS_IN_YEAR:
            tm_unit = _('year')
            s_scale = PedanticTimedelta.SECS_IN_YEAR
        elif self.total_seconds() >= PedanticTimedelta.SECS_IN_MONTH:
            tm_unit = _('month')
            s_scale = PedanticTimedelta.SECS_IN_MONTH
        elif self.total_seconds() >= PedanticTimedelta.SECS_IN_DAY:
            tm_unit = _('day')
            s_scale = PedanticTimedelta.SECS_IN_DAY
        elif self.total_seconds() >= (60 * 60):  # secs/min * mins/hour = secs/hour
            tm_unit = _('hour')
            s_scale = 60.0 * 60.0  # secs_in_hour
        elif self.total_seconds() >= 60:  # secs/min = secs/min
            tm_unit = _('min')
            is_abbrev = True
            s_scale = 60.0  # secs_in_minute
        else:
            tm_unit = _('sec')
            is_abbrev = True
            s_scale = 1.0  # secs_in_second
        return tm_unit, is_abbrev, s_scale

    def time_format_scaled(self):
        """Format time duration using appropriate precision and time unit.

        Format the instance's elapsed time using the largest single
        unit of time where value is 1 or more (unless the elapsed time
        is less than a single second, in which case the value will be
        expressed in seconds).

        :return: tuple containing (formatted time, seconds in unit, time unit)
        :rtype: tuple(string, seconds-per-unit, time-unit)

        >>> PedanticTimedelta(days=0.33).time_format_scaled()
        ('7.92 hours', 3600.0, 'hour')
        """
        tm_unit, is_abbrev, s_scale = self._units_and_scale()
        adj_time = self.total_seconds() / s_scale
        # (lb): I timeit'd Inflector().pluralize vs. inflectr=Inflector();
        # inflectr.pluralize. Creating object ahead of time is not faster.
        tm_units = Inflector(English).conditional_plural(adj_time, tm_unit)
        if is_abbrev:
            tm_units += '.'
        time_fmtd = ('{:.02f} {}'.format(adj_time, tm_units))
        return time_fmtd, s_scale, tm_unit

    # ***

# ***

