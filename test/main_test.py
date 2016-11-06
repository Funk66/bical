import unittest
import datetime

import bical


class TestCalendar(unittest.TestCase):
    def setUp(self):
        self.calendar = bical.Calendar()
        self.date = datetime.datetime(2016, 6, 4)

    def test_quarter(self):
        self.assertEqual(4, self.calendar.quarter(datetime.datetime(2015, 12, 31)))
        self.assertEqual(1, self.calendar.quarter(datetime.datetime(2016, 1, 1)))

    def test_add(self):
        self.assertEqual('2016-01', self.calendar.add(2015, 53, 53, False))
        self.assertEqual('2016-Q1', self.calendar.add(2015, 12, 12, True))

    def test_convert(self):
        self.assertEqual('2016-22', self.calendar.convert(self.date, 'week'))
        self.assertEqual('2016-06', self.calendar.convert(self.date, 'month'))
        self.assertEqual('2016-Q2', self.calendar.convert(self.date, 'quarter'))

    def test_increment(self):
        self.assertEqual('2016-01', self.calendar.increment('2015-53', 'week'))
        self.assertEqual('2016-01', self.calendar.increment('2015-12', 'month'))
        self.assertEqual('2016-Q1', self.calendar.increment('2015-Q4', 'quarter'))

    def test_timeline(self):
        self.assertEqual(['2016-22'], self.calendar.timeline(self.date, self.date, 'week'))


if __name__ == '__main__':
    unittest.main()

