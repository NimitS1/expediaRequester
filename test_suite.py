import unittest
import datetime
import expediaRequester

"""
The data returned will be different at different times.
Hence we just validate if we are getting a OK response.
"""

apiKey = "API_KEY"

class TestActivities(unittest.TestCase):
    """
    Unit test activities API
    """
    def setUp(self):
        self.client = expediaRequester.ExpediaRequester(apiKey)
    
    def test_activities(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.activities("London",
                                            datetime.datetime.strftime(tomorrow, "%Y-%m-%d"),
                                            datetime.datetime.strftime(nextDay, "%Y-%m-%d"))
        self.assertEqual(code, 200)

class testHotels(TestActivities):
    """
    Unit test hotesls API
    """
    def test_hotels(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.hotels("London", 
                                        datetime.datetime.strftime(tomorrow, "%Y-%m-%d"),
                                        datetime.datetime.strftime(nextDay, "%Y-%m-%d"), 3)
        self.assertEqual(code, 200)

    def test_hotel_reviews(self):
        code, json = self.client.hotel_reviews( 234, True, "DATEASC", 0, 10, "Everyone")
        self.assertEqual(code, 200)

class testCars(TestActivities):
    """
    Unit test cars API
    """
    def test_cars(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.cars_search(datetime.datetime.strftime(tomorrow, "%Y-%m-%d")                                           , datetime.datetime.strftime(nextDay, "%Y-%m-%d"),
                                             "SFO", "LAX", "price", 10, "All-American", "economy")
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()
    
