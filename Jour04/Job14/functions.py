from Class.whiteshield import WShield

def CutSmallWords(charsMin, anString):
    result = ""

    if WShield.IsInt(charsMin, 1) and WShield.IsString(anString):
        words = anString.split()
        i = 0

        while i < len(words):
            if len(words[i]) <= charsMin:
                del words[i]
            else:
                i += 1

        if len(words) > 0:
            if len(words) == 1:
                result = words[0]
            else:
                result = " ".join(words)

    return result