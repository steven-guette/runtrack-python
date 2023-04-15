"""
@Author  : GUETTE Steven
@Class   : SecurePassword
@Version : 1.0.0
@Since   : 2023
"""

import hashlib


class SecurePassword:
    (PwdPfx, PwdSfx) = ("Wh!t€", "C@t")

    def __init__(self, password):
        self.Pwd = ""
        self.SetPwd(password)

    # region GETTERS

    def GetPassword(self):
        return self.Pwd

        # endregion

    # region SETTERS
    def SetPwd(self, password):
        if len(self.Pwd) == 0:
            password = SecurePassword.PwdPfx + password + SecurePassword.PwdSfx

            pwd = hashlib.sha256()
            pwd.update(password.encode())
            self.Pwd = pwd.hexdigest()

    # endregion
