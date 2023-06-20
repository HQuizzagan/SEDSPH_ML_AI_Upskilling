import math
import numpy as np

def haversine_distance(pickup, dropoff):
    '''
    Calculate the distance using the latitude and longitude of the PICKUP and DROPOFF with the Haversine formula.
    
    Parameters:
        pickup (tuple): A tuple of (latitude, longitude) for the pickup location.
        dropoff (tuple): A tuple of (latitude, longitude) for the dropoff location.
        
    Returns:
        float: The distance between the pickup and dropoff locations in kilometers.
    '''
    
    # Convert coordinates to radians
    pickup_lat, pickup_long = pickup
    dropoff_lat, dropoff_long = dropoff
    pickup_lat, pickup_long, dropoff_lat, dropoff_long = map(np.radians, [pickup_lat, pickup_long, dropoff_lat, dropoff_long])
    
    # Haversine formula
    dlat = dropoff_lat - pickup_lat
    dlong = dropoff_long - pickup_long
    a = np.sin(dlat/2.0)**2 + np.cos(pickup_lat) * np.cos(dropoff_lat) * np.sin(dlong/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    # Radius of earth in kilometers is 6371
    return 6371 * c