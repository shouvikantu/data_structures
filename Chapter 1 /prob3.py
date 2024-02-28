class Bounce:
    def __init__(self, initial_height, numof_bounce):
        self._initial_height = initial_height
        self._numof_bounce = numof_bounce

    @property
    def initial_height(self):
        return self._initial_height
    
    @initial_height.setter
    def initial_height(self, value):
        self._initial_height = value

    @property
    def numof_bounce(self):
        return self._numof_bounce
    
    @numof_bounce.setter
    def numof_bounce(self, value):
        self._numof_bounce = value

    def get_total_distance(self, bounce_index = 0.6):
        total_distance = self.initial_height
        for x in range(1,self._numof_bounce):
            total_distance+= 2* (self._initial_height * (bounce_index**x))
        
        total_distance +=  self._initial_height * bounce_index**self._numof_bounce
        return total_distance
    
