
'''
given an int car_capacity and array of rides start_time, end_time, passenger_count.
return true if it's possible to complete all the rides without exceeding car capacity.
'''


def can_complete_rides(car_capacity, rides):
    current_passengers = 0

    for ride in rides:
        start_time, end_time, passenger_count = ride
        # Check if adding the passenger count of the current ride exceeds the car capacity
        if current_passengers + passenger_count > car_capacity:
            return False
        # Update the current passenger count
        current_passengers += passenger_count

    return True


# Example usage
car_capacity = 5
rides = [(0, 5, 2), (3, 7, 3), (8, 10, 1)]
print(can_complete_rides(car_capacity, rides))  # Output: True
