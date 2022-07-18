class Destination:
    def __init__(self, _traveller, _city, _country, _duration, _checked_off = False, id = None):
        self.traveller = _traveller
        self.city = _city
        self.country = _country
        self.duration = _duration
        self.checked_off = _checked_off
        self.id = id


    def mark_checked_off(self):
        self.checked_off = True
