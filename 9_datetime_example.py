import datetime

class whatIsTime:
    
    # Construct a date from a POSIX timestamp (like time.time())
    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    # Construct a date from time.time()
    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)

    # Construct a date from a proleptic Gregorian ordinal
    @classmethod
    def fromordinal(cls, n):
        # January 1 of year 1 is day 1.
        # Only the year, month and day are non-zero in the result

        y, m, d = _ord2ymd(n)
        


    
