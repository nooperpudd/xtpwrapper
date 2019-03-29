import os
import unittest

from xtpwrapper import QuoteAPI
from xtpwrapper.xtp_enum import XTP_LOG_LEVEL


class QuoteCase(unittest.TestCase):

    def setUp(self):
        self.quote = QuoteAPI()
        self.quote.CreateQuote(1, os.getcwd(), XTP_LOG_LEVEL.XTP_LOG_LEVEL_TRACE)

    def tearDown(self):
        self.quote.Release()

    def test_version(self):
        print(self.quote.GetApiVersion())
