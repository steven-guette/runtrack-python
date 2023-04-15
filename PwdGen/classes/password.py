import hashlib

class Password:
    PwdPfx = "Wh!t€"
    PwdSfx = "C@t"

    def __init__(self, password):        
        Password.SetSaltValues()
        self._Pwd = Password.GetHashPassword(Password.SetPwd(password))

    #region GETTERS    

    def GetHashPassword(cls, str):
        str = Password.PwdPfx + str + Password.PwdSfx
        pwd = hashlib.sha256()
        pwd.update(str.encode())

        return pwd.hexdigest()
    GetHashPassword = classmethod(GetHashPassword)

    def GetPassword(self):
        return self._Pwd    

    #endregion

    #region SETTERS
    def SetPwd(cls, value):
        pwd = hashlib.sha1()
        pwd.update(value.encode())
        return pwd.hexdigest()
    SetPwd = classmethod(SetPwd)

    def SetSaltValues(cls):
        Password.SetPfx()
        Password.SetSfx()
    SetSaltValues = classmethod(SetSaltValues)

    def SetPfx(cls):
        pfx = hashlib.md5()
        pfx.update(Password.PwdPfx.encode())
        Password.PwdPfx = pfx.hexdigest()
    SetPfx = classmethod(SetPfx)

    def SetSfx(cls):
        sfx = hashlib.md5()
        sfx.update(Password.PwdSfx.encode())
        Password.PwdSfx = sfx.hexdigest()
    SetSfx = classmethod(SetSfx)

    #endregion

    Pwd = property(GetPassword)