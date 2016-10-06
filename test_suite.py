import unittest
import datetime
import expediaRequester

"""
The data returned will be different at different times.
Hence we just validate if we are getting a OK response.
"""

apiKey = "api_key"

class TestActivities(unittest.TestCase):
    """
    Unit test activities API
    """
    def setUp(self):
        self.client = expediaRequester.ExpediaRequester(apiKey)
    
    def testActivities(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.activities("London",
                                            datetime.datetime.strftime(tomorrow, "%Y-%m-%d"),
                                            datetime.datetime.strftime(nextDay, "%Y-%m-%d"))
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()
    
