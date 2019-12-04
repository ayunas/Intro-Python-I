# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
import ast

# YOUR CODE HERE
class LatLon:
    def __init__(self,city,lat,lon):
        self.city = city
        self.lat = lat
        self.lon = lon
    
    def __repr__(self):
        return str(dict([("city", self.city),("lat",self.lat),("lon", self.lon)]))


tokyo = LatLon('tokyo',35.68,139.65)
mecca = LatLon('mecca',21.39,39.86)
medina = LatLon('medina',24.52,39.57)
# print(mecca)
# print(medina)

# Make a class Waypoint that can be passed parameters `city`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self,city,lat,lon,spot):
        super().__init__(city,lat,lon)
        self.spot = spot
    
    def __repr__(self):
        return f"At waypoint: {self.spot}.  lat,long: {self.lat,self.lon}, city: {self.city}"


kaaba = Waypoint("mecca",21.39,39.86,"kaaba")
eiffel_tower = Waypoint("paris", 48.86,2.29, "eiffel_tower")

# print(eiffel_tower)
# print(kaaba)
# eiffel_tower


# Make a class Geocache that can be passed parameters `city`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(LatLon):
    def __init__(self,city,difficulty,size,lat,lon):
        super().__init__(city,lat,lon)
        self.difficulty = difficulty
        self.size = size
    
    def __repr__(self):
        superobj = super().__repr__()
        geo = str({"difficulty": self.difficulty, "size": self.size})
        geodict = ast.literal_eval(geo)
        superobjdict = ast.literal_eval(superobj)
        obj = {**geodict,**superobjdict}
        return "Geocache: " + str(obj)

game = Geocache('athens','hard','1 gb',58,43)
print(game)


# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint("paris", 41.70505, -121.51521, "catacombs" )
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache)

# Print it--also make this print more nicely
# print(geocache)
