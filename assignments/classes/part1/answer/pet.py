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
        self.deathdate = None

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
        return self.days_since_last_fed() < 1

    def days_since_last_fed(self):
        if self.last_fed is None:
            return 99999

        now = str(date.today())
        return self.__days_diff(self.last_fed, now)

    # Sets the ped as dead if the last fed jumps more than 3 days
    # Returns True if the pet is alive and we were able to update the last_fed variable
    # Returns False if the pet was killed because it was not fed in 3 days
    def feed(self, date_fed):
        if not self.is_alive():
            return False  # Can't feed a dead cat !
        elif self.is_fed():
            return True  # Cat already ate, don't believe her lies
        elif self.__days_diff(self.last_fed, str(date_fed)) > 3:
            self.died(date_fed)
            return False
        else:
            self.last_fed = str(date_fed)
            return True

    # Record the pets death
    def died(self, date_died):
        self.deathdate = str(date_died)

    # Simple helper method to make if statements more readable
    def is_alive(self):
        return self.deathdate is None

