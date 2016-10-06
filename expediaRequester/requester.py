import requests

class ExpediaRequester(object):
    apiKey = ""
    def __init__(self, key):
        self.apiKey = key

    def get(self, URL):
        response = requests.get(URL)
        return response.status_code, response.text

    """
    Start activities API
    """

    def activities(self, cityName, startDate, endDate):
        url = "http://terminal2.expedia.com/x/activities/search?location="
        url +=  cityName 
        if startDate is not None:
            url += "&startDate=" + startDate
        if endDate is not None:
            url += "&endDate=" + endDate
        url += "&apikey=" + self.apiKey
        return self.get(url)
  
    def activity_details(self, activityId, startDate, endDate):
        url = "http://terminal2.expedia.com:80/x/activities/details?activityId="
        url += str(activityId)
        if startDate is not None:
            url += "&startDate=" + startDate
        if endDate is not None:
            url += "&endDate=" + endDate
        url += "&apikey=" + self.apiKey
        return self.get(url)

    """
    End activities API
    """
    """
    Start hotels API
    """

    def hotels(self, cityName, checkinDate, checkoutDate, room1):
        url = "http://terminal2.expedia.com/x/mhotels/search?city="
        url += cityName
        url += "&checkInDate=" + checkinDate 
        url += "&checkOutDate=" + checkoutDate 
        url += "&room1=" + str(room1)
        url += "&apikey=" + self.apiKey
        return self.get(url)
  
    def hotel_reviews(self, hotelId, summary, sortBy, start, items, categoryFilter):
        url = "http://terminal2.expedia.com:80/x/reviews/hotels?hotelId=" + str(hotelId)
        if summary is not None:
            url += "&summary=" + str(summary)
        if sortBy is not None:
            url += "&sortBy=" + sortBy
        if start is not None:
            url += "&start=" + str(start)
        if items is not None:
            url += "&items=" + str(items)
        if categoryFilter is not None:
            url += "&categoryFilter=" + categoryFilter
        url = url + "&apikey=" + self.apiKey
        return self.get(url)

    """
    End hotels API
    """
    """
    Start cars API
    """

    def cars_search(self, pickupDate, dropoffDate, pickupLocation, dropoffLocation, sort, limit, suppliers, classes):
        url = "http://terminal2.expedia.com:80/x/cars/search?"
        if pickupDate is not None:
            url += "pickupdate=" + pickupDate
        if dropoffDate is not None:
            url += "&dropoffdate=" + dropoffDate
        if pickupLocation is not None:
            url += "&pickuplocation=" + pickupLocation
        if dropoffLocation is not None:
            url += "&dropofflocation=" + dropoffLocation
        if sort is not None:
            url += "&sort=" + sort
        if limit is not None:
            url += "&limit=" + str(limit)
        if suppliers is not None:
            url += "&suppliers=" + suppliers
        if classes is not None:
            url += "&classes=" + classes
        url = url + "&apikey=" + self.apiKey
        return self.get(url)

    """
    End cars API
    """
    """
    Start cruise API
    """

    def cruise_search_sailings(self, cruiseLines, ships, destinations, departureLocations, earliestDepartureDates, latestDepartureDate, minLength, maxLength, minPrice, maxPrice, sortBy, sortOrder, limit, offset):
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailing/search?cruiseLines=" +cruiseLines
        if ships is not None:
            url += "&ships=" + ships
        if destinations is not None:
            url += "&destinations=" + destinations
        if departureLocations is not None:
            url += "&ships=" + departureLocations
        if earliestDepartureDates is not None:
            url += "&earliestDeptDate=" + earliestDepartureDates
        if latestDepartureDate is not None:
            url += "&latestDeptDate=" + latestDepartureDate
        if minLength is not None:
            url += "&minLength=" + str(minLength)
        if maxLength is not None:
            url += "&maxLength=" + str(maxLength)
        if minPrice is not None:
            url += "&minPrice=" + str(minPrice)
        if maxPrice is not None:
            url += "&maxPrice=" + str(maxPrice)
        if sortBy is not None:
            url += "&sortBy=" + sortBy
        if sortOrder is not None:
            url += "&sortOrder=" + sortOrder
        if limit is not None:
            url += "&limit=" + str(limit)
        if offset is not None:
            url += "&offset=" + str(offset)
        url +=  "&apikey=" + self.apiKey
        return self.get(url)

    def cruise_offer_availability(self, offerToken, adultPassengerCount, childPassengerCount, childPassengerAges):
        url = "http://terminal2.expedia.com:80/x/cruise/offer/availability?offerToken=" + offerToken
        if adultPassengerCount is not None:
            url += "&adultPassengerCount=" + str(adultPassengerCount)
        if childPassengerCount is not None:
            url += "&childPassengerCount=" + str(childPassengerCount)
        if childPassengerAges is not None:
            url += "&childPassengerAges=" + childPassengerAges
        url +=  "&apikey=" + self.apiKey
        return self.get(url)

    def cruise_search_sailings_filters(self):
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailings/filters"
        url +=  "&apikey=" + self.apiKey
        return self.get(url)

    """
    End cruise API
    """
    """
    Start flights API
    """

    def flights_search(self, departureDate, returnDate, departureAirport, arrivalAirport, prettyPrint, numberOfAdultTravelers, childTravelerAge, infantSeatingInLap, lccAndMerchantFareCheckoutAllowed, correlationId, maxOfferCount):
        url = "http://terminal2.expedia.com:80/x/mflights/search?departureDate=" + departureDate
        if returnDate is not None:
            url += "&returnDate=" + returnDate
        if departureAirport is not None:
            url += "&departureAirport=" + departureAirport
        if arrivalAirport is not None:
            url += "&arrivalAirport=" + arrivalAirport
        if prettyPrint is not None:
            url += "&prettyPrint=" + str(prettyPrint).lower()
        if numberOfAdultTravelers is not None:
            url += "&numberOfAdultTravelers" + str(numberOfAdultTravelers)
        if childTravelerAge is not None:
            url += "&childTravelerAge" + childTravelerAge
        if infantSeatingInLap is not None:
            url += "&infantSeatingInLap=" + str(infantSeatingInLap).lower()
        if lccAndMerchantFareCheckoutAllowed is not None:
            url += "&lccAndMerchantFareCheckoutAllowed=" + str(lccAndMerchantFareCheckoutAllowed).lower()
        if correlationId is not None:
            url += "&correlationId=" + correlationId
        if maxOfferCount is not None:
            url += "&maxOfferCount=" + str(maxOfferCount)
        url += "&apikey=" + self.apiKey
        return self.get(url)

    def flights_price_range_search(self, fromAirport, toAirport, departDate):
        url = "http://terminal2.expedia.com:80/x/flights/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        url += "?apikey=" + self.apiKey
        return self.get(url)

    def flights_trends_and_predictions(self, fromAirport, toAirport, departDate):
        url = "http://terminal2.expedia.com:80/x/flights/v3/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        url += "?apikey=" + self.apiKey
        return self.get(url)
    
    """
    End flights API
    """
    """
    Start Geography API
    """
    def get_prefix(self, firstValue):
        if firstValue:
            return "?"
        return "&"

    def geography_features(self, gaiaId, verbose, lcid):
        firstValue = True
        url = "http://terminal2.expedia.com:80/x/geo/features/"
        url += gaiaId 
        if verbose is not None:
            url += self.getPrefix(firstValue) + "verbose=" + verbose
            firstValue = False
        if lcId is not None:
            url += self.getPrefix(firstValue) + "lcid=" + lcid
            firstValue = False
        url += self.getPrefix(firstValue) + "apiKey=" + self.apiKey
        return self.get(url)

    def geography_features_by_latlong(self, within, lat, lng, atLeast, expandby, type_val, verbose, lcid):
        url = "http://terminal2.expedia.com:80/x/geo/features?"
        url += within
        url += "&lat=" + lat
        url += "&lng=" + lng
        if atLeast is not None:
            url += "&atLeast=" + str(atLeast)
        if expandBy is not None:
            url += "&expandBy=" + expandBy
        if type_val is not None:
            url += "&type=" + type_val
        if verbose is not None:
            url += "&verbose=" + verbose
        if lcid is not None:
            url += "&lcid=" + lcid
        url += "&apiKey=" + self.apiKey
        return self.get(url)
   
    """
    End Goegraphy API
    """
