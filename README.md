# expediaRequestor
A python wrapper for [Expedia APIs](http://developer.expedia.com/directory)
The goal is to write a developer friendly client that can used to interact with the Expedia API. Once the wrapper is ready, I will publish it as a package in the [Python package index](https://pypi.python.org/pypi)

###Current to-do
- [X] Create a setup.py file
- [ ] Make code completely Pythony [lint, refactor Java style code]
- [ ] Complete the API implementation  
- [ ] Populate test cases  
- [ ] Integrate with travis CI  

###Current State of APIs

|API                         | Implemented | Testcases added |
|----------------------------|-------------|-----------------|
| Cars                       |   [X]       |   [X]           |
| Cruise                     |   [X]       |   [ ]           |
| Flight Search              |   [X]       |   [X]           |
| Flights prices and trends  |   [X]       |   [X]           |
| Geography                  |   [ ]       |   [ ]           |
| Hotel Reviews              |   [X]       |   [X]           |
| Hotel Search Offers        |   [ ]       |   [ ]           |
| Package Search             |   [X]       |   [X]           |
| Suggestions and Resolutions|   [X]       |   [X]           |
| Things To Do!              |   [ ]       |   [ ]           |

The cruise APIs by Expedia are currently down and cannot be tested till they are back up.  
The package search API seems to be buggy so the test for it's wrapper is commented.  
The search resolutions API seems to look for particular headers which I am not able deduce.  


###Note to testers:
Remember that you have to add your own API key for testing
