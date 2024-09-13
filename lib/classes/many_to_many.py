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
        if not 3<= len(value):
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