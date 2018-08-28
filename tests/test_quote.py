import unittest

from xtpwrapper.quote import Quote
from xtpwrapper._enum import XTP_LOG_LEVEL
import os

class QuoteCase(unittest.TestCase):

    def setUp(self):
        self.quote = Quote()
        abs_path = os.path.abspath(os.path.curdir)
        self.quote.CreateQuote(1, abs_path, XTP_LOG_LEVEL.XTP_LOG_LEVEL_TRACE.value)
    def tearDown(self):
        self.quote.Release()

    def test_version(self):

        print(self.quote.GetApiVersion())

