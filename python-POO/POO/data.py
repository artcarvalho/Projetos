class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def formatada(self):
        print("%02d/%02d/%02d" % (self.day, self.month, self.year))