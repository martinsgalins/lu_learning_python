from datetime import datetime, timedelta


class DateTime:

    def __init__(self, datumlaiks):
        self.datetime = datumlaiks

    def time_elapsed(self, datumlaiks):
        difference = self.datetime - datumlaiks
        return difference

    def time_after(self, minutes):
        after = self.datetime + timedelta(minutes=minutes)
        return after


now = DateTime(datetime.now())
print(now.time_after(minutes=30))


