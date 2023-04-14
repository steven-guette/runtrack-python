from classes.whiteshield import WShield

def GetStudentMarkRounded(mark):
    if WShield.IsNumeric(mark, 0, 100):
        if (mark+1) % 5 == 0:
            mark += 1
        elif (mark+2) % 5 == 0:
            mark += 2

    return mark