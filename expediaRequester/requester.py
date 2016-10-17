import requests

class ExpediaRequester(object):
 
    apiKey = ""
    base_url = "http://terminal2.expedia.com:80/x/"

    def __init__(self, key):
        self.apikey = key

    def get(self, URL, parameter = None):
        response = requests.get(URL, params = parameter)
        return response.status_code, response.text

    """
    Start activities API
    """

    def activities(self, cityName, startDate, endDate):
        payload = {}
        url = "http://terminal2.expedia.com/x/activities/search"
        payload['location'] = cityName
        if startDate is not None:
            payload['startDate'] = startDate
        if endDate is not None:
            payload['endDate'] = endDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
  
    def activity_details(self, activityId, startDate, endDate):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/activities/details"
        payload['activityId'] = str(activityId)
        if startDate is not None:
            payload['startDate'] = startDate
        if endDate is not None:
            payload['endDate'] = endDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End activities API
    """
    """
    Start hotels API
    """

    def hotels(self, cityName, checkinDate, checkoutDate, room1):
        payload = {}
        url = "http://terminal2.expedia.com/x/mhotels/search"
        payload['city'] = cityName
        payload['checkinDate'] = checkinDate
        payload['checkoutDate'] = checkoutDate
        payload['room1'] = str(room1)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
  
    def hotel_reviews(self, hotelId, summary, sortBy, start, items, categoryFilter):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/reviews/hotels"
        payload['hotelId'] = str(hotelId)
        if summary is not None:
            payload['summary'] = str(summary)
        if sortBy is not None:
            payload['sortBy'] = sortBy
        if start is not None:
            payload['start'] = str(start)
        if items is not None:
            payload['items'] = str(items)
        if categoryFilter is not None:
            payload['categoryFilter'] = categoryFilter
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End hotels API
    """
    """
    Start cars API
    """

    def cars_search(self, pickupDate, dropoffDate, pickupLocation, dropoffLocation, sort, limit, suppliers, classes):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/cars/search"
        if pickupDate is not None:
            payload['pickupdate'] = pickupdate
        if dropoffDate is not None:
            payload['dropoffdate'] = dropoffDate
        if pickupLocation is not None:
            payload['pickuplocation'] = pickuplocation
        if dropoffLocation is not None:
            payload['dropofflocation'] = dropofflocation
        if sort is not None:
            payload['sort'] = sort
        if limit is not None:
            payload['limit'] = str(limit)
        if suppliers is not None:
            payload['suppliers'] = suppliers
        if classes is not None:
            payload['classes'] = classes
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End cars API
    """
    """
    Start cruise API
    """

    def cruise_search_sailings(self, cruiseLines, ships, destinations, departureLocations, earliestDepartureDates, latestDepartureDate, minLength, maxLength, minPrice, maxPrice, sortBy, sortOrder, limit, offset):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailing/search"
        payload['cruiseLines'] = cruiseLines
        if ships is not None:
            payload['ships'] = ships
        if destinations is not None:
            payload['destinations'] = destinations
        if departureLocations is not None:
            payload['ships'] = departureLocations
        if earliestDepartureDates is not None:
            payload['earliestDeptDate'] = earliestDepartureDates
        if latestDepartureDate is not None:
            payload['latestDeptDate'] = latestDepartureDate
        if minLength is not None:
            payload['minLength'] = str(minLength)
        if maxLength is not None:
            payload['maxLength'] = str(maxLength)
        if minPrice is not None:
            payload['minPrice'] = str(minPrice)
        if maxPrice is not None:
            payload['maxPrice'] = str(maxPrice)
        if sortBy is not None:
            payload['sortBy'] = sortBy
        if sortOrder is not None:
            payload['sortOrder'] = sortOrder
        if limit is not None:
            payload['limit'] = str(limit)
        if offset is not None:
            payload['offset'] = str(offset)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def cruise_offer_availability(self, offerToken, adultPassengerCount, childPassengerCount, childPassengerAges):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/cruise/offer/availability"
        payload['offerToken'] = offerToken
        if adultPassengerCount is not None:
            payload['adultPassengerCount'] = str(adultPassengerCount)
        if childPassengerCount is not None:
            payload['childPassengerCount'] = str(childPassengerCount)
        if childPassengerAges is not None:
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

    def flights_search(self, departureDate, returnDate, departureAirport, arrivalAirport, prettyPrint, numberOfAdultTravelers, childTravelerAge, infantSeatingInLap, lccAndMerchantFareCheckoutAllowed, correlationId, maxOfferCount):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/mflights/search"
        payload['departureDate'] = departureDate
        if returnDate is not None:
            payload['returnDate'] = returnDate
        if departureAirport is not None:
            payload['departureAirport'] = departureAirport
        if arrivalAirport is not None:
            payload['arrivalAirport'] = arrivalAirport
        if prettyPrint is not None:
            payload['prettyPrint'] = str(prettyPrint).lower()
        if numberOfAdultTravelers is not None:
            payload['numberOfAdultTravelers'] = str(numberOfAdultTravelers)
        if childTravelerAge is not None:
            payload['childTravelerAge'] = childTravelerAge
        if infantSeatingInLap is not None:
            payload['infantSeatingInLap'] = str(infantSeatingInLap).lower()
        if lccAndMerchantFareCheckoutAllowed is not None:
            payload['lccAndMerchantFareCheckoutAllowed'] = str(lccAndMerchantFareCheckoutAllowed).lower()
        if correlationId is not None:
            payload['correlationId'] = correlationId
        if maxOfferCount is not None:
            payload['maxOfferCount'] = str(maxOfferCount)
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def flights_price_range_search(self, fromAirport, toAirport, departDate):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/flights/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def flights_trends_and_predictions(self, fromAirport, toAirport, departDate):
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
    
    def geography_features(self, gaiaId, verbose, lcid):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/geo/features/"
        url += gaiaId 
        if verbose is not None:
            payload['verbose'] = verbose 
        if lcId is not None:
            payload['lcid'] = lcid
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    def geography_features_by_latlong(self, within, lat, lng, atLeast, expandby, type_val, verbose, lcid):
        payload = {}
        url = "http://terminal2.expedia.com:80/x/geo/features?"
        url += within
        payload['lat'] = lat
        payload['lng'] = lng
        if atLeast is not None:
            payload['atLeast'] = str(atLeast)
        if expandBy is not None:
            payload['expandBy'] = expandBy
        if type_val is not None:
            payload['type'] = type_val
        if verbose is not None:
            payload['verbose'] = verbose
        if lcid is not None:
            payload['lcid'] = lcid
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)
   
    """
    End Goegraphy API
    """
    """
    Start Package Search API
    """
    def packages(self, originalAirport, destinationAirport, departureDate, returnDate, regionid, hotelids, adults, childages, infantinseat, limit, cabinClass, nonstop):
        payload = {}
        url = self.base_url + "packages"
        payload['originAirport'] = originAirport
        payload['destinationAirport'] = destinationAirport
        payload['departureDate'] = departureDate
        payload['returnDate'] = returnDate
        if regionid is not None:
            payload['regionid'] = str(regionid)
        if hotelids is not None:
            payload['hotelids'] = hotelids
        if adults is not None:
            payload['adults'] = str(adults)
        if childages is not None:
            payload['childages'] = childages
        if infantinseat is not None:
            payload['infantinseat'] = str(infantinseat).lower()
        if limit is not None:
            payload['limit'] = str(limit)
        if cabinClass is not None:
            payload['class'] = cabinClass
        if nonstop is not None:
            payload['nonstop'] = str(nonstop).lower()
        payload['apikey'] = self.apikey
        return self.get(url, parameter = payload)

    """
    End Package Search API
    """
    """
    Start suggestions and resolutons API
    """

    def suggestions(self, api, query, maxresults):
        header = {'Authorization' : self.apiKey }

        payload = {}
        url = "http://terminal2.expedia.com/x/suggestions/" + api
        payload['query'] = query
        if maxresults is not None:
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
