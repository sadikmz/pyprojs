# Let's see how we can add some debugging into to our class object

from datetime import datetime, timezone


def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))

    return results

def debug_info(cls):
    cls.debug = info
    return cls


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._spead = 0 # private variable

    @property
    def spead(self):
        return self._spead

    @spead.setter
    def spead(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('speed must be lower than top speed')
        else:
            self._spead = new_speed

# run
favorite = Automobile('Ford', 'Model T', 1989, 45)
print(favorite.debug())
# favorite.spead = 100
favorite.spead = 20
print(favorite.debug())

#

