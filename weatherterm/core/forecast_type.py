from enum import Enum,unique

@unique

class ForecastType(Enum):
    TODAY="today"
    FIVEDAYS="5day"
    TENDAYS="10days"
    WEEKEND="weekend"

# use the enum to create the class


