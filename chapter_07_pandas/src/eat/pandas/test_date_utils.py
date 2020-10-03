import unittest
import datetime
import pandas

import pypigenhole.simpleutils.date_utils as date_utils
import pypigenhole.simpleutils.simple_timer as simple_timer


class DateUtilsTest(unittest.TestCase):
    def test_parser(self):
        dates = [f'{y}{m}{d}' for y in range(2010, 2021) for m in range(1, 13) for d in range(1, 29)]
        print(f'number of dates parsed: {len(dates)}')

        parser = date_utils.CachedDateParser('%Y%m%d')
        pbm = simple_timer.PerfBenchmark('date_parser')
        with pbm:
            for d in dates:
                parser.parse(d)
        dur1 = pbm.dur

        pbm = simple_timer.PerfBenchmark('datetime parser')
        with pbm:
            for d in dates:
                datetime.datetime.strptime(d, '%Y%m%d')
        dur2 = pbm.dur
        print(abs(dur1 - dur2) / dur1)
        self.assertTrue(abs(dur1 - dur2) / dur1 < 0.1)

        # This proves that strptime() is not slow.
