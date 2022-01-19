# OBSOLETE expediaRequestor
THIS PROJECT IS OBSOLETE AS EXPEDIA HAS REMOVED THE APIS.

A python wrapper for [Expedia APIs](http://developer.expedia.com/directory)
The goal is to write a developer friendly client that can used to interact with the Expedia API. Once the wrapper is ready, I will publish it as a package in the [Python package index](https://pypi.python.org/pypi)

[![Build Status](https://travis-ci.org/NimitS1/expediaRequester.svg?branch=master)](https://travis-ci.org/NimitS1/expediaRequester)

### Current to-do
- [X] Create a setup.py file
- [X] Complete the API implementation  
- [X] Populate test cases  
- [X] Integrate with travis CI  

### Current State of APIs

|API                         | Implemented | Testcases added |
|----------------------------|-------------|-----------------|
| Cars                       |   [X]       |   [X]           |
| Cruise                     |   [X]       |   [ ]           |
| Flight Search              |   [X]       |   [X]           |
| Flights prices and trends  |   [X]       |   [X]           |
| Geography                  |   [X]       |   [X]           |
| Hotel Reviews              |   [X]       |   [X]           |
| Hotel Search Offers        |   [X]       |   [X]           |
| Package Search             |   [X]       |   [X]           |
| Suggestions and Resolutions|   [X]       |   [X]           |
| Things To Do!              |   [X]       |   [X]           |

The cruise APIs by Expedia are currently down and cannot be tested till they are back up.  

### Testing
You first need to get an API key from [Expedia](http://developer.expedia.com/).  
Running the test cases is very simple:
```
python test_suite.py
```
