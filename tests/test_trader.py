import os
import unittest

from xtpwrapper import TraderApi
from xtpwrapper.xtp_enum import XTP_LOG_LEVEL


class TraderTestCase(unittest.TestCase):

    def setUp(self):
        self.trader = TraderApi()
        self.trader.CreateTrader(1, os.getcwd(), XTP_LOG_LEVEL.XTP_LOG_LEVEL_TRACE)

    def tearDown(self):
        self.trader.Release()

    def test_version(self):
        print(self.trader.GetApiVersion())