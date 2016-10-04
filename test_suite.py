import unittest
import expediaRequester

"""
The data returned will be different at different times.
Hence we just validate if we are getting a OK response.
"""

apiKey = "Cw7BldtcUbgDLWM1hrTGneo8xM0rz4bW"

class TestActivities(unittest.TestCase):
    """
    Unit test activities API
    """
    def setUp(self):
        self.client = expediaRequester.ExpediaRequester(apiKey)
    
    def testActivities(self):
        code, json = self.client.activities("London", None, None)
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()
    
