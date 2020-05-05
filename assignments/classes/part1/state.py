from datetime import datetime, timedelta, timezone

class State:
    def __init__(self, name, capital, population = None, gmt_offset = -9):
        self.name = name
        self.capital = capital
        self.population = population
        self.gmt_offset = gmt_offset
    
    def display(self):
        print('The capital of ' + self.name + ' is ' + self.capital)
    
    def get_local_time(self):
        return datetime.now(timezone.utc) + timedelta(hours=self.gmt_offset)
    
    def record_births(self, total_births):
        self.population += total_births
    
    def record_deaths(self, total_deaths):
        self.population += total_deaths
        
        # Can't have a negative population
        if self.population < 0:
            self.population = 0