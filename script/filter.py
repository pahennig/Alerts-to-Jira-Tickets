import time
from datetime import datetime

# Defining filter to get data from last day. 
def definingFilter():
    isItMonday = datetime.today().strftime('%A')
    if isItMonday != 'Monday':
        filters = {
            'date': {'gte_ndays': 7}
        }
        request_data = {
            'filters': filters,
            'isScan': True
        }
    elif isItMonday == 'Tuesday':
        filters = {
            'date': {'gte_ndays': 6}
        }
        request_data = {
            'filters': filters,
            'isScan': True
        }
    else:
        filters = {
            'date': {'gte_ndays': 5}
        }
        request_data = {
            'filters': filters,
            'isScan': True
        }

    return request_data
