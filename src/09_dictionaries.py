"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

fourth = dict([('lat',10),('long',29),('name','a fourth place')])
waypoints.append(fourth)

print(waypoints)



# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
waypoints[0]["name"] = "not a real place"
waypoints[0]["lon"] = -130

print(waypoints[0])

# Write a loop that prints out all the field values for all the waypoints
print("\n")
for counter,wp in enumerate(waypoints):
    print(f"Waypoint {counter+1}")
    keyval = wp.items()
    
    for kv in keyval:
        print(f"{kv[0]}: {kv[1]}")
    print("\n")
    
    
    
    # for val in values:
    #     print(val)
    # keys = wp.keys()
    # values = wp.values()






