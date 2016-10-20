import requests

class ExpediaRequester(object):
 
    apiKey = ""
    base_url = "http://terminal2.expedia.com:80/x/"

    def __init__(self, key):
        self.apikey = key

    def get(self, URL, parameter = None):
        url_params = {}
        for key, value in parameter.items():
            if value is not None:
                url_params[key] = value
        response = requests.get(URL, params = url_params)
        return response.status_code, response.text    

    """
    Start activities API
    """

    def activities(self, cityName = None, startDate = None, endDate = None):
        payload = {}
        url = "http://terminal2.expedia.com/x/activities/search"
        payload['location'] = cityName
        payload['startDate'] = startDate
        payload['endDate'] = endDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
  
    def activity_details(self, activityId = None, startDate = None, endDate = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/activities/details"
        payload['activityId'] = str(activityId)
        payload['startDate'] = startDate
        payload['endDate'] = endDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End activities API
    """
    """
    Start hotels API
    """

    def hotels(self, cityName = None, checkinDate = None, checkoutDate = None, room1 = None):
        payload = {}
        url = "http://terminal2.expedia.com/x/mhotels/search"
        payload['city'] = cityName
        payload['checkinDate'] = checkinDate
        payload['checkoutDate'] = checkoutDate
        payload['room1'] = str(room1)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
  
    def hotel_reviews(self, hotelId, summary = None, sortBy = None, start = None, items = None, categoryFilter = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/reviews/hotels"
        payload['hotelId'] = str(hotelId)
        payload['summary'] = str(summary)
        payload['sortBy'] = sortBy
        payload['start'] = str(start)
        payload['items'] = str(items)
        payload['categoryFilter'] = categoryFilter
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End hotels API
    """
    """
    Start cars API
    """

    def cars_search(self, pickupDate = None, dropoffDate = None, pickupLocation = None, dropoffLocation = None, sort = None, limit = None, suppliers = None, classes = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/cars/search"
        payload['pickupdate'] = pickupDate
        payload['dropoffdate'] = dropoffDate
        payload['pickuplocation'] = pickupLocation
        payload['dropofflocation'] = dropoffLocation
        payload['sort'] = sort
        payload['limit'] = str(limit)
        payload['suppliers'] = suppliers
        payload['classes'] = classes
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End cars API
    """
    """
    Start cruise API
    """

    def cruise_search_sailings(self, cruiseLines = None, ships = None, destinations = None, departureLocations = None, earliestDepartureDates = None, latestDepartureDate = None, minLength = None, maxLength = None, minPrice = None, maxPrice = None, sortBy = None, sortOrder = None, limit = None, offset = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailing/search"
        payload['cruiseLines'] = cruiseLines
        payload['ships'] = ships
        payload['destinations'] = destinations
        payload['ships'] = departureLocations
        payload['earliestDeptDate'] = earliestDepartureDates
        payload['latestDeptDate'] = latestDepartureDate
        payload['minLength'] = str(minLength)
        payload['maxLength'] = str(maxLength)
        payload['minPrice'] = str(minPrice)
        payload['maxPrice'] = str(maxPrice)
        payload['sortBy'] = sortBy
        payload['sortOrder'] = sortOrder
        payload['limit'] = str(limit)
        payload['offset'] = str(offset)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def cruise_offer_availability(self, offerToken = None, adultPassengerCount = None, childPassengerCount = None, childPassengerAges = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/cruise/offer/availability"
        payload['offerToken'] = offerToken
        payload['adultPassengerCount'] = str(adultPassengerCount)
        payload['childPassengerCount'] = str(childPassengerCount)
        payload['childPassengerAges'] = childPassengerAges
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def cruise_search_sailings_filters(self):
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailings/filters"
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End cruise API
    """
    """
    Start flights API
    """

    def flights_search(self, departureDate = None, returnDate = None, departureAirport = None, arrivalAirport = None, prettyPrint = None, numberOfAdultTravelers = None, childTravelerAge = None, infantSeatingInLap = None, lccAndMerchantFareCheckoutAllowed = None, correlationId = None, maxOfferCount = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/mflights/search"
        payload['departureDate'] = departureDate
        payload['returnDate'] = returnDate
        payload['departureAirport'] = departureAirport
        payload['arrivalAirport'] = arrivalAirport
        payload['prettyPrint'] = str(prettyPrint).lower()
        payload['numberOfAdultTravelers'] = str(numberOfAdultTravelers)
        payload['childTravelerAge'] = childTravelerAge
        payload['infantSeatingInLap'] = str(infantSeatingInLap).lower()
        payload['lccAndMerchantFareCheckoutAllowed'] = str(lccAndMerchantFareCheckoutAllowed).lower()
        payload['correlationId'] = correlationId
        payload['maxOfferCount'] = str(maxOfferCount)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def flights_price_range_search(self, fromAirport = None, toAirport = None, departDate = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/flights/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def flights_trends_and_predictions(self, fromAirport = None, toAirport = None, departDate = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/flights/v3/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
    
    """
    End flights API
    """
    """
    Start Geography API
    """
    
    def geography_features(self, gaiaId = None, verbose = None, lcid = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/geo/features/"
        url += gaiaId
        payload['verbose'] = verbose
        payload['lcid'] = lcid
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def geography_features_by_latlong(self, within = None, lat = None, lng = None, atLeast = None, expandby = None, type_val = None, verbose = None, lcid = None):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/geo/features?"
        url += within
        payload['lat'] = lat
        payload['lng'] = lng
        payload['atLeast'] = str(atLeast)
        payload['expandBy'] = expandBy
        payload['type'] = type_val
        payload['verbose'] = verbose
        payload['lcid'] = lcid
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
   
    """
    End Goegraphy API
    """
    """
    Start Package Search API
    """
    def packages(self, originalAirport = None, destinationAirport = None, departureDate = None, returnDate = None, regionid = None, hotelids = None, adults = None, childages = None, infantinseat = None, limit = None, cabinClass = None, nonstop = None):
        payload = {}
        url = self.base_url + "packages"
        payload['originAirport'] = originAirport
        payload['destinationAirport'] = destinationAirport
        payload['departureDate'] = departureDate
        payload['returnDate'] = returnDate
        payload['regionid'] = str(regionid)
        payload['hotelids'] = hotelids
        payload['adults'] = str(adults)
        payload['childages'] = childages
        payload['infantinseat'] = str(infantinseat).lower()
        payload['limit'] = str(limit)
        payload['class'] = cabinClass
        payload['nonstop'] = str(nonstop).lower()
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End Package Search API
    """
    """
    Start suggestions and resolutons API
    """

    def suggestions(self, api = None, query = None, maxresults = None):
        header = {'Authorization' : self.apiKey }

        payload = {}
        url = "http://terminal2.expedia.com/x/suggestions/" + api
        payload['query'] = query
        payload['maxresults'] = str(maxresults)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def suggest_cars(self, query, maxResults):
        return self.suggestions("cars", query, maxResults)

    def suggest_flights(self, query, maxresults):
        return self.suggestions("flights", query, maxresults)

    def suggest_hotels(self, query, maxresults):
        return self.suggestions("hotels", query, maxresults)

    def suggest_packages(self, query, maxresults):
        return self.suggestions("packages", query, maxresults)

    def suggest_regions(self, query):
        return self.suggestions("regions", query, None)

    """
    End suggestions and resolutions API
    """
