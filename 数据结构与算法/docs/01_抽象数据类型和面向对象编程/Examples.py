class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, year, month, day):
        self._julianDay = 0
        assert self._isValidGregorian(year, month, day), \
                "Invalid Gregorian date."

        # Gredorian data --> julian day formula:
        # T = (M - 14) / 12
        # jday = D - 32075 + (1461 * (Y + 4800 + T) / 4) +
        #                    (367 * (M - 2 - T * 12) / 12) -
        #                    (3 * ((Y + 4900 + T) / 100) / 4)
        #
        # This first line of the equation, T = (M-14)/12, has to be changed
        # since Python's implementation of integer division is not the same
        # as mathematical definition
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
                (1461 * (year + 4800 + tmp) // 4) + \
                (367 * (month -2 - tmp * 12) // 12) - \
                (3 * ((year + 4900 + tmp) // 100) // 4)

    # 一月（31天），二月（平年28天，闰年29天），三月（31天），
    # 四月（30天），五月（31 天），六月（30天），七月（31天），
    # 八月（31天），九月（30天），十月（31天），十一月（30天），
    # 十二月（31天）。

    def _isValidGregorian(self, year, month, day):
        if month > 12 or month < 1:
            return False

        if day < 1 or day > 31:
            return False

        # months_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_30_days = [4, 6, 9, 11]

        if month in months_30_days and day > 30:
            return False

        if month == 2:
            if self._leapYear(year):
                if day > 29:
                    return False
            if day > 28:
                return False

        return True
    # Extracts the appropriate Gregorian date component.
    def year(self):
        return (self._toGregorian())[0] # returing Y from (Y, M, D)

    def month(self):
        return (self._toGregorian())[1] # returing M from (Y, M, D)

    def day(self):
        return (self._toGregorian())[2] # returing D from (Y, M, D)

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        year, month, day = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400 ) % 7

    # Returns the date as a string in Gregorian format.
    def __str__(self):
        year, month, day = self._toGregorian()
        return "%04d/%02d/%02d" % (year, month, day)

    # Returns the date as a string in Gregorian format.
    def __repr__(self):
        return str(self)

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay


    # Returns the Gregorian date as a tuple: (year, month, day).
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return year, month, day

    def monthName(self):
        months = ["Jan", "Feb", "Mar", "Apr", "may", "Jun",
                "Jul", "Aug", "Sept", "Oct", "Nov", "Dec",]
        return months[self.month()]

    def _leapYear(self, year):
        if year % 400 == 0 or \
                (year % 4 == 0 and year % 100 != 0):
                return True
        return False

    def isLeapYear(self):
        return self._leapYear(self.year)


    def numDays(self, otherDate):
        if self._julianDay > otherDate._julianDay:
            return self._julianDay - otherDate._julianDay
        else:
            return otherDate._julianDay - self._julianDay

    def advanceBy(self, days):
        self._julianDay += days
        if self._julianDay < 0:
            self._julianDay = 0