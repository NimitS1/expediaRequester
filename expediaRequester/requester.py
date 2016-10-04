import requests

class ExpediaRequestor(object):
    apiKey = ""
    def __init__(self, key):
        self.apiKey = key

    def py2java(self, boolValue):
        if(boolValue):
            return "true"
        else:
            return "false"

    def GET(self, URL):
        response = requests.get(URL)
        return response.status_code, response.text

    """
    Start activities API
    """

    def activities(self, cityName, startDate, endDate):
        url = "http://terminal2.expedia.com/x/activities/search?location="
        url +=  cityName 
        if(startDate != None):
            url += "&startDate=" + startDate
        if(endDate != None):
            url += "&endDate=" + endDate
        url += "&apikey=" + self.apiKey
        return self.GET(url)
  
    def activityDetails(self, activityId, startDate, endDate):
        url = "http://terminal2.expedia.com:80/x/activities/details?activityId="
        url += str(activityId)
        if(startDate != None):
            url += "&startDate=" + startDate
        if(endDate != None):
            url += "&endDate=" + endDate
        url += "&apikey=" + self.apiKey
        return self.GET(url)

    """
    End activities API
    """
    """
    Start hotels API
    """

    def hotels(self, cityName, checkinDate, checkoutDate):
        url = "http://terminal2.expedia.com/x/mhotels/search?city="
        url += cityName
        url += "&checkInDate=" + checkinDate 
        url += "&checkOutDate=" + checkoutDate 
        url += "&room1=2&apikey=" + self.apiKey
        return self.GET(url)
  
    def hotelReviews(self, hotelId, summary, sortBy, start, items, categoryFilter):
        url = "http://terminal2.expedia.com:80/x/reviews/hotels?hotelId=" + str(hotelId)
        if( summary != None):
            url += "&summary=" + str(summary)
        if(sortBy != None):
            url += "&sortBy=" + sortBy
        if(start != None):
            url += "&start=" + str(start)
        if(items != None):
            url += "&items=" + str(items)
        if(categoryFilter != None):
            url += "&categoryFilter=" + categoryFilter
        url = url + "&apikey=" + self.apiKey
        return self.GET(url)

    """
    End hotels API
    """
    """
    Start cars API
    """

    def carsSearch(self, pickupDate, dropoffDate, pickupLocation, dropoffLocation, sort, limit, suppliers, classes):
        url = "http://terminal2.expedia.com:80/x/cars/search?"
        if(pickupDate != None):
            url += "&pickupdate=" + pickupDate
        if(dropoffDate != None):
            url += "&dropoffdate=" + dropoffDate
        if(pickupLocation != None):
            url += "&pickuplocation=" + pickupLocation
        if(dropoffLocation != None):
            url += "&dropofflocation=" + dropoffLocation
        if(sort != None):
            url += "&sort=" + sort
        if(limit != None):
            url += "&limit=" + str(limit)
        if(suppliers != None):
            url += "&suppliers=" + suppliers
        if(classes != None):
            url += "&classes=" + classes
        url = url + "&apikey=" + self.apiKey
        return self.GET(url)

    """
    End cars API
    """
    """
    Start cruise API
    """

    def cruiseSearchSailings(self, cruiseLines, ships, destinations, departureLocations, earliestDepartureDates, latestDepartureDate, minLength, maxLength, minPrice, maxPrice, sortBy, sortOrder, limit, offset):
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailing/search?cruiseLines=" +cruiseLines
        if(ships != None):
            url += "&ships=" + ships
        if(destinations != None):
            url += "&destinations=" + destinations
        if(departureLocations != None):
            url += "&ships=" + departureLocations
        if(earliestDepartureDates != None):
            url += "&earliestDeptDate=" + earliestDepartureDates
        if(latestDepartureDate != None):
            url += "&latestDeptDate=" + latestDepartureDate
        if(minLength != None):
            url += "&minLength=" + str(minLength)
        if(maxLength != None):
            url += "&maxLength=" + str(maxLength)
        if(minPrice != None):
            url += "&minPrice=" + str(minPrice)
        if(maxPrice != None):
            url += "&maxPrice=" + str(maxPrice)
        if(sortBy != None):
            url += "&sortBy=" + sortBy
        if(sortOrder != None):
            url += "&sortOrder=" + sortOrder
        if(limit != None):
            url += "&limit=" + str(limit)
        if(offset != None):
            url += "&offset=" + str(offset)
        url +=  "&apikey=" + self.apiKey
        return self.GET(url)

    def cruiseOfferAvailability(self, offerToken, adultPassengerCount, childPassengerCount, childPassengerAges):
        url = "http://terminal2.expedia.com:80/x/cruise/offer/availability?offerToken=" + offerToken
        if(adultPassengerCount != None):
            url += "&adultPassengerCount=" + str(adultPassengerCount)
        if(childPassengerCount != None):
            url += "&childPassengerCount=" + str(childPassengerCount)
        if(childPassengerAges != None):
            url += "&childPassengerAges=" + childPassengerAges
        url +=  "&apikey=" + self.apiKey
        return self.GET(url)

    def cruiseSearchSailingsFilters(self):
        url = "http://terminal2.expedia.com:80/x/cruise/search/sailings/filters"
        url +=  "&apikey=" + self.apiKey
        return self.GET(url)

    """
    End cruise API
    """
    """
    Start flights API
    """

    def flightsSearch(self, departureDate, returnDate, departureAirport, arrivalAirport, prettyPrint, numberOfAdultTravelers, childTravelerAge, infantSeatingInLap, lccAndMerchantFareCheckoutAllowed, correlationId, maxOfferCount):
        url = "http://terminal2.expedia.com:80/x/mflights/search?departureDate=" + departureDate
        if(returnDate != None):
            url += "&returnDate=" + returnDate
        if(departureAirport != None):
            url += "&departureAirport=" + departureAirport
        if(arrivalAirport != None):
            url += "&arrivalAirport=" + arrivalAirport
        if(prettyPrint != None):
            url += "&prettyPrint=" + self.py2java(prettyPrint)
        if(numberOfAdultTravelers != None):
            url += "&numberOfAdultTravelers" + str(numberOfAdultTravelers)
        if(childTravelerAge != None):
            url += "&childTravelerAge" + childTravelerAge
        if(infantSeatingInLap != None):
            url += "&infantSeatingInLap=" + self.py2java(infantSeatingInLap)
        if(lccAndMerchantFareCheckoutAllowed != None):
            url += "&lccAndMerchantFareCheckoutAllowed=" + self.py2java(lccAndMerchantFareCheckoutAllowed)
        if(correlationId != None):
            url += "&correlationId=" + correlationId
        if(maxOfferCount != None):
            url += "&maxOfferCount=" + str(maxOfferCount)
        url += "&apikey=" + self.apiKey
        return self.GET(url)

    def flightsPriceRangeSearch(self, fromAirport, toAirport, departDate):
        url = "http://terminal2.expedia.com:80/x/flights/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        url += "?apikey=" + self.apiKey
        return self.GET(url)

    def flightsTrendsAndPredictions(self, fromAirport, toAirport, departDate):
        url = "http://terminal2.expedia.com:80/x/flights/v3/search/1/"
        url += fromAirport
        url += "/" + toAirport
        url += "/" + departDate
        url += "?apikey=" + self.apiKey
        return self.GET(url)
    
    """
    End flights API
    """
    """
    Start Geography API
    """
    def getPrefix(self, firstValue):
        if(firstValue):
            return "?"
        return "&"

    def geographyFeatures(self, gaiaId, verbose, lcid):
        firstValue = True
        url = "http://terminal2.expedia.com:80/x/geo/features/"
        url += gaiaId 
        if(verbose != None):
            url += self.getPrefix(firstValue) + "verbose=" + verbose
            firstValue = False
        if(lcId != None):
            url += self.getPrefix(firstValue) + "lcid=" + lcid
            firstValue = False
        url += self.getPrefix(firstValue) + "apiKey=" + self.apiKey
        return self.GET(url)

    def geographyFeaturesByLatLong(self, within, lat, lng, atLeast, expandby, type_val, verbose, lcid):
        url = "http://terminal2.expedia.com:80/x/geo/features?"
        url += within
        url += "&lat=" + lat
        url += "&lng=" + lng
        if(atLeast != None):
            url += "&atLeast=" + str(atLeast)
        if(expandBy != None):
            url += "&expandBy=" + expandBy
        if(type_val != None):
            url += "&type=" + type_val
        if(verbose != None):
            url += "&verbose=" + verbose
        if(lcid != None):
            url += "&lcid=" + lcid
        url += "&apiKey=" + self.apiKey
        return self.GET(url)
   
    """
    End Goegraphy API
    """
