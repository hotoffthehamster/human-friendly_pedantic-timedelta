# -*- coding: utf-8 -*-

# This file is part of 'human-friendly_pedantic-timedelta'.
#
# 'human-friendly_pedantic-timedelta' is free software: you can re-
# distribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# 'human-friendly_pedantic-timedelta' is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with 'human-friendly_pedantic-timedelta'. If not, visit:
#
#   http://www.gnu.org/licenses/

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

