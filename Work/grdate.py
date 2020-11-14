import datetime

class grdate(datetime.date):
    
    # Used with `str()`
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.day},{self.month},{self.year})'


