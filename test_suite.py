import unittest
import datetime
import expediaRequester

"""
The data returned will be different at different times.
Hence we just validate if we are getting a OK response.
"""

apiKey = ""

class TestCases(unittest.TestCase):
    """
    Base class for test cases
    """
    def setUp(self):
        self.client = expediaRequester.ExpediaRequester(apiKey)

class TestActivities(TestCases):
    """
    Unit test activities API
    """
    
    def test_activities(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.activities("London",
                                            datetime.datetime.strftime(tomorrow, "%Y-%m-%d"),
                                            datetime.datetime.strftime(nextDay, "%Y-%m-%d"))
        self.assertEqual(code, 200)

class testHotels(TestCases):
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

class testCars(TestCases):
    """
    Unit test cars API
    """
    def test_cars(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.cars_search(datetime.datetime.strftime(tomorrow, "%Y-%m-%d")                                           , datetime.datetime.strftime(nextDay, "%Y-%m-%d"),
                                             "SFO", "LAX", "price", 10, "All-American", "economy")
        self.assertEqual(code, 200)


class testFlightsSearch(TestCases):
    """
    Unit test flights search API
    """
    def test_flights_search(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.flights_search(datetime.datetime.strftime(tomorrow, "%Y-%m-%d")                                           , datetime.datetime.strftime(nextDay, "%Y-%m-%d"), "SFO", "LAX", True, 2, "12", False, False, None, 15)
        self.assertEqual(code, 200)

    def test_flights_price_range_search(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        code, json = self.client.flights_price_range_search("SFO","LAX",datetime.datetime.strftime(tomorrow, "%Y-%m-%d"))
        self.assertEqual(code, 200)

    def test_flights_trends(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        code, json = self.client.flights_trends_and_predictions("SFO","LAX",datetime.datetime.strftime(tomorrow, "%Y-%m-%d"))
        self.assertEqual(code, 200)

class testPackages(TestCases):
    """
    Unit test packages
    """
    def test_packages(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.packages("SFO", "ORL",
                                          datetime.datetime.strftime(tomorrow, "%Y-%m-%d"),
                                          datetime.datetime.strftime(nextDay, "%Y-%m-%d"),
                                          178294, None, 2, "5", False, 10, "coach", False)
        self.assertEqual(code, 200)

class testHotelSearch(TestCases):
    """
    Unit test hotels search
    """
    def test_hotels_search(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.hotel_search("SFO", None, None, None, False, "Inn", "0, 5, 1", None, False, 100, "mobileweb", datetime.datetime.strftime(tomorrow, "%Y-%m-%d"), 
                                  datetime.datetime.strftime(nextDay, "%Y-%m-%d"), "2", "2")
        self.assertEqual(code, 200)


    def test_hotels_offers(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        nextDay = tomorrow + datetime.timedelta(days=1)
        code, json = self.client.hotel_offers(15490, "TOTAL_PRICE", "mobileweb",
                                            datetime.datetime.strftime(tomorrow, "%Y-%m-%d"),
                                            datetime.datetime.strftime(nextDay, "%Y-%m-%d"),
                                            "2", "3, 4")
        self.assertEqual(code, 200) 

    def test_hotels_info(self):
        code, json = self.client.hotel_info(15490)
        self.assertEqual(code, 200)

if __name__ == '__main__':
    unittest.main()
    
