class StationInfo:
    '''Class used to store information relating a stations position.'''

    def __init__(self, name, lat, long, total, available):
        self.name = name
        self.lat = lat
        self.long = long
        self.total = int(total)
        self.available = int(available)
        self.bikes = self.total - self.available