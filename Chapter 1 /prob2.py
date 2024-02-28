class Wage:
    """Calculates and returns the weekly pay of a worker."""
    def __init__(self, hourly_wage, regular_hours, overtime_hours):
        self._hourly_wage = hourly_wage
        self._regular_hours = regular_hours
        self._overtime_hours = overtime_hours

    @property
    def hourly_wage(self):
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, value):
        if value < 0:
            raise ValueError("Hourly wage cannot be negative.")
        self._hourly_wage = value

    # Similar for regular_hours and overtime_hours...
    @property
    def regular_hours(self):
        return self._regular_hours
    
    @regular_hours.setter
    def regular_hours(self, value):
        self._regular_hours=value

    @property
    def overtime_hours(self):
        return self._overtime_hours

    @overtime_hours.setter
    def overtime_hours(self, value):
        self._overtime_hours  = value  

    def get_pay(self):
        return (self._regular_hours * self._hourly_wage) + (self._overtime_hours * self._hourly_wage * 1.5)
