class StandInfo:
    '''Class used to store information relating to station vacancy.'''

    def __init__(self, total, available, time):
        self.total = int(total)
        self.available = int(available)
        self.time = str(time)[0:-3]
        self.bikes = self.total - self.available