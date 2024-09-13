import re
class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        
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
    
    def add_trips(self, value):
        if not isinstance(value, Trip):
            raise Exception('trip must be an instance of Trip')
        self._trips.append(value)
    
    def trips(self):
        return self._trips
    
    def visitors(self):
        visitors_welcomed = set()
        for trip in self._trips:
            if isinstance(trip.visitor, Visitor):
                visitors_welcomed.add(trip.visitor)
        return list(visitors_welcomed)
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        visit_count = {}
        for trip in self._trips:
            visitor = trip.visitor
            if visitor in visit_count:
                visit_count[visitor] += 1
            else:
                visit_count[visitor] = 1
        
        if not visit_count:
            return None
        return max(visit_count, key=visit_count.get)


class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        
        Trip.all.append(self)
        visitor.add_trips(self)
        national_park.add_trips(self)
        
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
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise Exception('visitor must be an instance of Visitor')
        self._visitor = value
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise Exception('national park must be an instance of NationalPark')
        self._national_park = value

class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = []
    
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
    
    def add_trips(self,value):
        if not isinstance(value, Trip):
            raise Exception('result not an instance of Result')
        self._trips.append(value)
    
    def trips(self):
        return self._trips
    
    def national_parks(self):
        parks_visited = set()
        for trip in self._trips:
            if isinstance(trip.national_park, NationalPark):
                parks_visited.add(trip.national_park)
        return list(parks_visited)
    
    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise Exception('Park doesn\'t exist')
        return sum(1 for trip in self._trips if trip.national_park == park)