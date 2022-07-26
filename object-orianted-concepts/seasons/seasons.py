from datetime import date
import inflect
import sys

""" YYYY-MM-DD """

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Getter(Year)
    @property
    def year(self):
        return self._year

    # Setter(Year)
    @year.setter
    def year(self, year):
        if not year:
            raise ValueError("Missing year")
        self._year = year

    # Getter(Month)
    @property
    def month(self):
        return self._month

    # Setter(Month)
    @month.setter
    def month(self, month):
        if not month:
            raise ValueError("Missing month")
        self._month = month

    # Getter(Day)
    @property
    def day(self):
        return self._day

    # Setter(Day)
    @day.setter
    def day(self, day):
        if not day:
            raise ValueError("Missing day")
        self._day = day

    def __str__(self):
        return f"Birth = {self.year}-{self.month}-{self.day}"


def main():
    try:
        print(calculate(birth_date(input("Date of Birth:"))))
    except ValueError:
        sys.exit("Invalid date")


# returns Date object
def birth_date(date):
    try:
        year, month, day = date.split("-")
        return Date(int(year), int(month), int(day))
    except (ValueError, AttributeError):
        sys.exit("Invalid date")

def calculate(Date):
    p = inflect.engine()

    birth_date = date(int(Date.year), int(Date.month), int(Date.day))
    current_date = date.today()

    diff = (current_date - birth_date)
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword='')

    return f"{output.capitalize()} minutes"


if __name__ == "__main__":
    main()
