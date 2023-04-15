"""
@Author  : GUETTE Steven
@Class   : WShield
@Version : 1.0.0
@Since   : 2023
"""


class WShield:
    NumericTypes = (int, float)

    """
    Vérifie qu'une valeur de type numérique respecte un interval
    
    """

    def RangeOk(value, minimum=False, maximum=False):
        if type(value) in WShield.NumericTypes:
            if type(minimum) in WShield.NumericTypes and type(maximum) in WShield.NumericTypes:
                return minimum <= value <= maximum
            elif type(minimum) in WShield.NumericTypes:
                return value >= minimum
            elif type(maximum) in WShield.NumericTypes:
                return value <= maximum
            else:
                return True

        return False

    RangeOk = staticmethod(RangeOk)

    """
    Vérifie qu'une valeur de type String, Liste, Tuple, Dict ne soit pas vide

    """

    def IsNotEmpty(var):
        return len(var) > 0

    IsNotEmpty = staticmethod(IsNotEmpty)

    """ 
    Vérifie qu'une variable soit de type String.
    Si notEmptyCheck est sur True, vérifie également si elle est vide.

    """

    def IsString(anString, notEmptyCheck=True):
        if notEmptyCheck:
            return type(anString) == str and WShield.IsNotEmpty(anString)
        else:
            return type(anString) == str

    IsString = staticmethod(IsString)

    """
    Vérifie qu'une variable soit de type Int.
    Si min et/ou max est renseigné, vérifie également l'intervalle.

    """

    def IsInt(anInt, minimum=False, maximum=False):
        if type(anInt) == int:
            if type(minimum) in WShield.NumericTypes or type(maximum) in WShield.NumericTypes:
                return WShield.RangeOk(anInt, minimum, maximum)
            else:
                return True

        return False

    IsInt = staticmethod(IsInt)

    """
    Vérifie qu'une variable soit de type Numeric.
    Si min et/ou max est renseigné, vérifie également l'intervalle.

    """

    def IsNumeric(anNumeric, minimum=False, maximum=False):
        if type(anNumeric) in WShield.NumericTypes:
            if type(minimum) in WShield.NumericTypes or type(maximum) in WShield.NumericTypes:
                return WShield.RangeOk(anNumeric, minimum, maximum)
            else:
                return True

        return False

    IsNumeric = staticmethod(IsNumeric)

    """
    Vérifie qu'une variable soit de type List.
    Si notEmptyCheck est sur True, vérifie également si elle est vide.

    """

    def IsList(anList, notEmptyCheck=True):
        if notEmptyCheck:
            return type(anList) == list and WShield.IsNotEmpty(anList)
        else:
            return type(anList) == list

    IsList = staticmethod(IsList)

    def IsDict(value, notEmptyCheck=True):
        if notEmptyCheck:
            return type(value) == dict and WShield.IsNotEmpty(value)
        else:
            return type(value) == dict

    IsDict = staticmethod(IsDict)

    def IsBool(value):
        return type(value) == bool

    IsBool = staticmethod(IsBool)
