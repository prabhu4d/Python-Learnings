# Travel

## Scenario

lets say you have pulsar (top speed: 200kmph), and your are in Coimbatore and you want to go Bangalore.
you will travel path is

1. Coimbatore
2. Salem
3. Dharmapuri
4. Hosur
5. Bangalore

you need to know how long it is, how much time it takes, and how much petrol you need

## implementation details

- there is no persistant storage for this simulation
- class Map

  - where places are located
  - places are object of Place Class
  - it should have class variable

    ```python
    grid = {
      lat1: {lon1 : place_object, lon2: place_object}
      lat2: {lon1: place_object, lon2: place_object}
    }

    ```

  - it must have show_map function which will display all the places

    ```txt
    # show_map output example

    (lat1, long1) -> place_1
    (lat2, long2) -> place_2

    ```

  - it also have distance_calculator function
    - accepts source address, destination address
    - calculate the distance between lat1, long1, lat2, long2

- class Place

  - it accepts place name, lat & long
  - after place instantiation it must store in Map class variable called grid
  - lat, long must be unique for each place, if duplicate provided ask user to update the lat, long via terminal

- class Vehicle

  - here you will store vechile information

    - Name
    - RC No
    - Mileage (kmph)
    - Top speed (kmph)
    - Petrol level (l)
    - current location (place object or string)

  - while print the vechile object it must display the attributes
  - create a ride_details function
    - it takes the average_speed and path as argument, where path is a list of place_objects
      - example
        - cbe_bge = [coimbatore, salem, dharmapuri, hosur, bangalore]
    - the function must calculate the travel time based on the average speed given by the user
    - need to calculate the petrol needed to travel
  - create a start_ride function

    - it take path as argument
    - it will check petrol status, if it is enough go to ride else ask user to fill the petrol via terminal
    - every 10 minutes the bike should print current location, assume 10m as 1s for quick simulation purpose
    - output must be

    ```bash
    Ride Started from Coimbatore to Bangalore

    0min : Coimbatore to Salem, location: Coimbatore+{distance_cross_per_10min}
    10min : Coimbatore to Salem, location: Coimbatore+24
    20min : Coimbatore to Salem, location: Coimbatore+48
    30min : Coimbatore to Salem, location: Coimbatore+72
    ...
    ...
    1hr : Salem to Dharmapuri, location: Salem+0
    1hr10min: Salem to Dharmapuri, location: Salem+24
    ...
    ...
    ...
    4hr10min: Hosur to Bangalore, location: Hosur+48

    Bangalore Arrived    
    ```
