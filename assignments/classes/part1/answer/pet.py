from datetime import datetime
from datetime import date

class pet:
    def __init__(self, name, category, subcategory, birthdate=None, colors=None, has_tail=False, has_wings=False, num_of_legs=4, last_fed=None):
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.birthdate = birthdate
        self.colors = colors
        self.has_tail = has_tail
        self.has_wings = has_wings
        self.num_of_legs = num_of_legs
        self.last_fed = last_fed

    def __days_diff(self, start_date, end_date):
        d1 = datetime.strptime(start_date, "%Y-%m-%d")
        d2 = datetime.strptime(end_date, "%Y-%m-%d")
        return abs((d2 - d1).days)

    # Return the age of the pet in years if a birthdate was given
    def age(self):
        if self.birthdate is None:
            return 0
        now = str(date.today())
        return self.__days_diff(self.birthdate, now) / 365

    # Return if the pet is fed or not (True/False)
    # Based on the last_fed date.
    def is_fed(self):
        if self.last_fed is None:
            return False

        now = str(date.today())
        return self.__days_diff(self.last_fed, now) < 1

