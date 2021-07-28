from datetime import date

from .forecast_type import ForecastType

class Forecast:
    def __init__(self,
                 current_temp,
                 humidity,
                 wind,
                 high_temp=None,
                 low_temp=None,
                 description="",
                 forecast_date=None,
                 forecast_type=ForecastType.TODAY):
        self._current_temp=current_temp
        self._high_temp=high_temp
        self._low_temp=low_temp
        self._humidity=humidity
        self._wind=wind
        self._desciption=description
        self._forecast_type=forecast_type
        if forecast_date is None:
            self.forecaste_date=date.today()
        else:
            self._forecast_date=forecast_date

@property
def forecast_date(self):
    return self._forecast_date

@forecast_date.setter
def forecast_date(self, forecaste_date):
    self._forecast_date=forecast_date.strftime("%a %b %c")

@property
def current_temp(self):
    retuen self._current_temp

@property
def humiduty(self):
    return self._humidity

