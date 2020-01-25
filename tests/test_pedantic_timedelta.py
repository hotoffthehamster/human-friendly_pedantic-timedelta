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

"""Tests for ``human-friendly_pedantic-timedelta``."""

from __future__ import absolute_import, unicode_literals

import datetime

import pytest
from freezegun import freeze_time
from pedantic_timedelta import PedanticTimedelta


@freeze_time('2015-12-10 12:30')
class TestPedanticTimedeltaTimeFormatElapsed(object):
    @pytest.mark.parametrize(('secs_then', 'secs_now', 'expectation'), [
        #  ((datetime.datetime.now() ... # BUGBUG: Set with true now, not freeze_time's!?
        (
            (
                datetime.datetime(2015, 12, 10, 12, 30, 0)
                - datetime.timedelta(days=1)
                - datetime.datetime.utcfromtimestamp(0)
            ).total_seconds(), None, '1.00 day',
        ),
        (
            (
                datetime.datetime(2015, 12, 10, 12, 30, 0)
                - datetime.timedelta(minutes=2.5)
                - datetime.datetime.utcfromtimestamp(0)
            ).total_seconds(),
            (
                datetime.datetime(2015, 12, 10, 12, 30, 0)
                - datetime.datetime.utcfromtimestamp(0)
            ).total_seconds(),
            '2.50 mins.',
        ),
    ])
    def test_time_format_elapsed(self, secs_then, secs_now, expectation):
        """Ensure that output matches expectation."""
        formatted = PedanticTimedelta.time_format_elapsed(secs_then, secs_now)
        assert formatted == expectation


@freeze_time('2015-12-10 12:30')
class TestPedanticTimedeltaTimeFormatScaledSeconds(object):
    @pytest.mark.parametrize(('seconds', 'exp_fmmtd', 'exp_scale', 'exp_units'), [
        (86400 / 2, '12.00 hours', 3600, 'hour'),
        (31556925.1296, '1.00 year', 31556925.1296, 'year'),
        (86400 * 40, '1.31 months', 2629743.7608, 'month'),
        (1.5, '1.50 secs.', 1.0, 'sec'),
    ])
    def test_time_format_elapsed(self, seconds, exp_fmmtd, exp_scale, exp_units):
        """Ensure that output matches expectation."""
        (
            tm_fmttd, tm_scale, tm_units,
        ) = PedanticTimedelta(seconds=seconds).time_format_scaled()
        assert tm_fmttd == exp_fmmtd
        assert tm_scale == exp_scale
        assert tm_units == exp_units


class TestPedanticTimedeltaOverflowError(object):
    @pytest.mark.parametrize(('days'), [
        (1000000000),
    ])
    def test_time_format_elapsed(self, days):
        """Ensure that output matches expectation."""
        with pytest.raises(ValueError):
            PedanticTimedelta(days=days)


class TestPedanticTimedeltaClassless(object):
    def test_time_format_elapsed(self):
        """Ensure that output matches expectation."""
        PedanticTimedelta.__new__(cls=None)

