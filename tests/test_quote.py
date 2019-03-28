import os
import unittest

from xtpwrapper.xtp_enum import XTP_LOG_LEVEL
from xtpwrapper.quote import QuoteAPI


class QuoteCase(unittest.TestCase):

    def setUp(self):
        self.quote = QuoteAPI()
        abs_path = os.path.abspath(os.path.curdir)
        self.quote.CreateQuote(1, abs_path, XTP_LOG_LEVEL.XTP_LOG_LEVEL_TRACE)

    def tearDown(self):
        self.quote.Release()

    def test_version(self):
        print(self.quote.GetApiVersion())
