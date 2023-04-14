class WShield:
    NumericTypes = (int, float)

    """
    Vérifie qu'une valeur de type Numéric respecte un interval
    
    """
    def RangeOk(value, min = False, max = False):
        if type(value) in WShield.NumericTypes:
            if type(min) in WShield.NumericTypes and type(max) in WShield.NumericTypes:
                return (min <= value <= max)
            elif type(min) in WShield.NumericTypes:
                return (value >= min)
            elif type(max) in WShield.NumericTypes:
                return (value <= max)
            else:
                return True
            
        return False    
    RangeOk = staticmethod(RangeOk)

    """
    Vérifie qu'une valeur de type String, Liste, Tuple, Dict ne soit pas vide

    """
    def IsNotEmpty(var):
        return (len(var) > 0)    
    IsNotEmpty = staticmethod(IsNotEmpty)
    
    """ 
    Vérifie qu'une variable soit de type String.
    Si notEmptyCheck est sur True, vérifie également si elle est vide.

    """
    def IsString(anString, notEmptyCheck = True):
        if notEmptyCheck:
            return (type(anString) == str and WShield.IsNotEmpty(anString))
        else:
            return (type(anString) == str)        
    IsString = staticmethod(IsString)
        
    """
    Vérifie qu'une variable soit de type Int.
    Si min et/ou max est renseigné, vérifie également l'interval.

    """
    def IsInt(anInt, min = False, max = False):
        if type(anInt) == int:
            if type(min) in WShield.NumericTypes or type(max) in WShield.NumericTypes:
                return (WShield.RangeOk(min, max)) 
            else:
                return True

        return False      
    IsInt = staticmethod(IsInt)

    """
    Vérifie qu'une variable soit de type Numeric.
    Si min et/ou max est renseigné, vérifie également l'interval.

    """
    def IsNumeric(anNumeric, min = False, max = False):
        if (type(anNumeric) in WShield.NumericTypes):
            if type(min) in WShield.NumericTypes or type(max) in WShield.NumericTypes:
                return (WShield.RangeOk(min, max))  
            else:
                return True
            
        return False      
    IsNumeric = staticmethod(IsNumeric)

    """
    Vérifie qu'une variable soit de type List.
    Si notEmptyCheck est sur True, vérifie également si elle est vide.

    """
    def IsList(anList, notEmptyCheck = True):
        if notEmptyCheck:
            return (type(anList) == list and WShield.IsNotEmpty(anList))
        else:
            return (type(anList) == list)        
    IsList = staticmethod(IsList)