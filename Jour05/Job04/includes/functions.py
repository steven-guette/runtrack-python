import string
from classes.whiteshield import WShield

def CaesarEncode(message):
    if WShield.IsString(message, False):
        abc = string.ascii_lowercase
        abcLength = len(abc)

        message = message.lower()
        encryptedMsg = ""

        for char in message:
            if char not in abc:
                encryptedMsg += char
            else:
                charFromReplace = abc.index(char) + 3

                if charFromReplace > abcLength:
                    charFromReplace = charFromReplace - abcLength

                encryptedMsg += abc[charFromReplace]

        print("Le message de base :{}".format(message))
        print("\nLe message crypté :{}".format(encryptedMsg))

    elif len(message) == 0:
        print("\nAucun message à crypter.")
    else:
        print("\nCaesarEncode() ->")
        print("\nLe paramètre `message`doit être une chaine de caractères.")


    
