# -*- coding: utf-8 -*-
#  vim:tw=0:ts=4:sw=4:et
# Copyright: © 2015-2018 Landon Bouma.
# License: GPLv3. See LICENSE.

import time
from datetime import timedelta
from inflector import Inflector, English

import logging
log = logging.getLogger('timedelta_wrap')


class PedanticTimedelta(timedelta):
    # Contains fcns. cxpx'ed from Cyclopath's pyserver/util_/misc.py

    # CAVEAT: Unlike datetime.timedelta, which accepts weeks but not
    # months or years because not every month nor every year has the
    # same number of days, this script fudges the calculation so we
    # can pretty-print an approximate elapsed time.

    # https://en.wikipedia.org/wiki/Tropical_year
    #  Laskar's expression: Mean tropical year on 1/1/2000 was 365.242189 days.
    #  Gregorian calendar average year is 365.2425 days, matching northward
    #  (March) equinox year of 365.2424 days (as of January 2000).
    # Calculating from rough estimate of 365d 5h 48m 46s per year.
    #  time_in_year = timedelta(days=365, hours=5, minutes=48, seconds=46)
    #  SECS_IN_YEAR = time_in_year.total_seconds() # 31556926
    #  DAYS_IN_YEAR = SECS_IN_YEAR / 24.0 / 60.0 / 60.0 # 365.2421991
    # Calculating from scholarly numbers.
    DAYS_IN_YEAR = 365.242189  # Laskar's expression.
    SECS_IN_DAY = 86400  # 1/86,400 is mean of solar day.
    SECS_IN_YEAR = DAYS_IN_YEAR * SECS_IN_DAY  # 31556925.1296

    # Average number of days in a month.
    # MAGIC_NUMBERS: 7 months are 31 days long, 4 are 40, and one is 28ish.
    #  avg_month_days = (7*31 + 4*30 + 28.25) / 12.0 # 30.4375
    DAYS_IN_MONTH = DAYS_IN_YEAR / 12.0  # 30.436849
    SECS_IN_MONTH = SECS_IN_YEAR / 12.0  # 2629743.7608

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
    def time_format_elapsed(time_then, time_now=None):
        if time_now is None:
            time_now = time.time()
        secs_elapsed = time_now - time_then
        tdw = PedanticTimedelta(seconds=secs_elapsed)
        return tdw.time_format_scaled()[0]

    # FIXME: Move this fcn. into its own class like datetime.timedelta?
    #        Or extend datetime.timedelta?
    #        Note that timedelta converts the difference between two
    #        dates or times into number of days, seconds, and microseconds.
    #        We could extend timedelta and rename this fcn, e.g.,
    #         pretty_print(), or something...

    # FIXME: (lb): I bet there's a better way to do this so that calendar
    #          dates are accounted for, e.g., this function will not report
    #          1/1/2000 00:00 to 1/1/2001 00:00 as exactly 1 year.
    #        We could use library to do date match, and then all we'd
    #          need to calculate here is math for one day, or maybe the
    #          month. But don't calculate anything more than the current
    #          month's worth of days? So, would 2/10 to 3/10 be "1 month",
    #          and 3/10 to 4/10 also be "1 month"? Or should we never use
    #          months, but use weeks and years instead??? Month would work
    #          if we counted elapsed months using day of month, rather than
    #          seconds! There's gotta be a calendar math library to help us
    #          out...
    #        (Considering month math, would, e.g., 1/1/2000 to 4/1/2000
    #          be reported as exactly 3 months? But then 1/28 to 2/28
    #          would be reported as "1 month", but 2/28 to 3/28 would
    #          not be "1 month" (though it would be "4 weeks"...). No
    #          wonder I decided to name this package "pedantic"!)

    def _units_and_scale(self):
        if self.total_seconds() > PedanticTimedelta.SECS_IN_YEAR:
            tm_unit = 'year'
            s_scale = PedanticTimedelta.SECS_IN_YEAR
        elif self.total_seconds() > PedanticTimedelta.SECS_IN_MONTH:
            tm_unit = 'month'
            s_scale = PedanticTimedelta.SECS_IN_MONTH
        elif self.total_seconds() > PedanticTimedelta.SECS_IN_DAY:
            tm_unit = 'day'
            s_scale = PedanticTimedelta.SECS_IN_DAY
        elif self.total_seconds() > (60 * 60):  # secs/min * mins/hour = secs/hour
            tm_unit = 'hour'
            s_scale = 60.0 * 60.0  # secs_in_hour
        elif self.total_seconds() > 60:  # secs/min = secs/min
            tm_unit = 'min.'
            s_scale = 60.0  # secs_in_minute
        else:
            tm_unit = 'sec.'
            s_scale = 1.0  # secs_in_second
        return tm_unit, s_scale

    def time_format_scaled(self):
        tm_unit, s_scale = self._units_and_scale()
        adj_time = self.total_seconds() / s_scale
        pass
        time_fmtd = (
            '{:2} {}'.format(
                # (lb): I timeit'd Inflector().pluralize vs. inflectr=Inflector();
                # inflectr.pluralize. Creating object ahead of time is not faster.
                adj_time, Inflector(English).conditional_plural(
                    adj_time, tm_unit,
                ),
            )
        )
        return time_fmtd, s_scale, tm_unit

    # ***

# ***

