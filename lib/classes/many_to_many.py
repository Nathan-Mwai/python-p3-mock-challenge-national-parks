import re
class NationalPark:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception('Name must be in string format')
        if len(value) < 3:
            raise Exception('Length of name must be 3 and above')
        if hasattr(self, '_name') and self._name is not None:
            raise Exception('Name cannot be changed once made')
        self._name = value
    
    def trips(self):
        pass
    
    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass


class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self,value):
        if not isinstance(value, str):
            raise Exception('Start date must be in string format')
        if len(value) < 7:
            raise Exception('values must be greater than 7 characters')
        
        #  Using regex to input method
        pattern = r'^[A-z]+ \d{1,2}(st|nd|rd|th)?$'
        if not re.match(pattern, value):
            raise Exception('Start date must be in format of "Month Day(suffix)"')
        self._start_date = value
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self,value):
        if not isinstance(value, str):
            raise Exception('Start date must be in string format')
        if len(value) < 7:
            raise Exception('values must be greater than 7 characters')
        
        #  Using regex to input method
        pattern = r'^[A-z]+ \d{1,2}(st|nd|rd|th)?$'
        if not re.match(pattern, value):
            raise Exception('Start date must be in format of "Month Day(suffix)"')
        self._end_date = value 
        

class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception('name must be in string format')
        if not (1 <= len(value) <= 15):
            raise Exception('Length of name must be between 1 and 15')
        self._name = value
        
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass