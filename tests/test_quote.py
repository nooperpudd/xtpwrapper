import unittest

from xtpwrapper.quote import Quote

class QuoteCase(unittest.TestCase):

    def test_version(self):
        print(Quote().GetApiVersion())

