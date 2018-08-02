places = []
minX, maxX = 0, 0
minY, maxY = 0, 0


def setup():
    size(800,800)
    noLoop()
    readData()
    
def draw():
    background(255)
    for place in places:
        # print place
        place.draw()
    
def readData():
    global minX, maxX, minY, maxY
    lines = loadStrings("http://www.infres.enst.fr/~eagan/class/igr204/data/population.tsv")
    print "Loaded", len(lines), "lines" # for debugging
    
    # First line contains metadata
    # Second line contains column labels
    # Third line and onward constains data cases
    
    for line in lines[2:]:
        print line
        columns = line.split("\t")
        place = Place()
        place.postalCode = int(columns[0])
        place.longitude = float(columns[1])
        place.latitude = float(columns[2])
        place.name = columns[4]
        place.population = int(columns[5])
        place.density = float(columns[6])
        places.append(place)
        
    Place.minX = min(places, key=lambda place: place.longitude).longitude
    Place.maxX = max(places, key=lambda place: place.longitude).longitude
    Place.minY = min(places, key=lambda place: place.latitude).latitude
    Place.maxY = max(places, key=lambda place: place.latitude).latitude
    
class Place(object):
    minX, maxX = (0, 0)
    minY, maxY = (0, 0)
    
    longitude = 0
    latitude = 0
    name = ""
    postalCode = 0
    population = -1
    density = -1
    
    @property
    def x(self):
        return map(self.longitude, self.minX, self.maxX, 0, width)
    
    @property
    def y(self):
        return map(self.latitude, self.minY, self.maxY, height, 0)
    
    def draw(self):
        black = color(0)
        
        # refactored into properties
        # print self.longitude, self.latitude
        # x, y = self.longitude, self.latitude
        # x = map(x, self.minX, self.maxX, 0, width)
        # y = map(y, self.minY, self.maxY, height, 0)
        
        try:
            set(self.x, self.y, black)
        except Exception, e:
            print "Error drawing place at ({}, {}): {}".format(self.x, self.y, e)
        
    
