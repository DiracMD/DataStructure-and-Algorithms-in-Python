from enum import Enum

class BaseEnum(Enum):
    def _generate_next_value(name,start,count,last_value):
        return name 
# the baseENUM is a very simple class inheritigng from the Enum
# the only thing we need ton here is override the method _generate_next_balue 
# o that every enumeration that inherits from BaseEnum and has properties with the value set to auto()  
# will automatically get thesame value as the property name


