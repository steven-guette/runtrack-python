# coding: utf-8

import maskpass
import datetime
import os

from classes.jsonfile import JSONFile
from classes.securepassword import SecurePassword
from classes.tablebox import TableBox
from classes.textbox import TextBox
from classes.whiteshield import WShield

UserAccountsFile = JSONFile("resources/user_accounts.csv", True)

"""
    Centre de l'application.
"""


# Démarre et maintient l'application en fonctionnement tant que l'utilisateur souhaite l'utiliser. #
def RunApp(result=False):
    DisplayMenuApp()

    if WShield.IsString(result):
        print(f"\n{result}\n")

    userSelect = GetMenuIdSelected()

    if userSelect == 4:
        AppClose()
    else:
        match userSelect:
            case 1:
                DisplayMenuApp()
                result = AddUserAccount()
            case 2:
                result = DisplayAccounts()
            case 3:
                result = RemoveAccountsFile()

        RunApp(result)


# Prépare / formate les données de l'utilisateur pour l'enregistrement. #
def AddUserAccount():
    username = GetUsername()

    Rules = TextBox(GetRules(), "Consignes à respecter")
    print(Rules.GetBox())

    password = GetUserPassword()
    d = datetime.date.today()

    accountDatas = {
        "date": "{}/{}/{}".format(d.day, d.month, d.year),
        "username": username,
        "password": password
    }

    return SetAccountsFile(accountDatas)


""" END """

"""
    Affichage.
"""


# Indique à l'utilisateur que l'application a été fermée. #
def AppClose():
    os.system("cls")
    print("\n--- Password Generator :: Close ---")


# Récupère et affiche les options du menu de l'application. #
def DisplayMenuApp():
    os.system("cls")

    Menu = TextBox(GetMenuList(), "Menu Principal")
    DisplayAppName("Password Generator", Menu.MaxLength + 4)
    print(Menu.GetBox())


# Affiche le nom de l'application. #
def DisplayAppName(appName, length):
    print(("#" * (length - 2)).center(length))
    print(f" {appName} ".center(length, "#"))
    print(("#" * (length - 2)).center(length))


def DisplayAccounts():
    accountsList = GetAccountsList()

    if WShield.IsNotEmpty(accountsList):
        Accounts = TableBox(accountsList)
        return Accounts.GetBox()
    else:
        return GetErrorMessage("user_account_display")


""" END """

"""
    Stockage de données diverses.
"""


# Contient la liste des consignes obligatoires pour le mot de passe. #
def GetRules():
    return [
        "Votre mot de passe doit contenir au moins :",
        "• Huit caractères ;",
        "• Une lettre majuscule ;",
        "• Une lettre minuscule ;",
        "• Un chiffre ;",
        "• L'un des caractères spéciaux suivants : (!, @, #, $, %, ^, &, *)."
    ]


# Contient la liste des options du menu principal. #
def GetMenuList():
    return [
        "Saisissez 1 pour ajouter un compte utilisateur.",
        "Saisissez 2 pour consulter les mots de passes enregistrés.",
        "Saisissez 3 pour supprimer les mots de passes enregistrés.",
        "Saisissez 4 pour quitter le programme"
    ]


def GetErrorMessage(error):
    messages = {
        "invalid_password": "Le mot de passe saisi ne respecte pas les consignes.",
        "lowercase": "Veuillez ajouter une ou plusieurs lettres minuscules à votre mot de passe.",
        "uppercase": "Veuillez ajouter une ou plusieurs lettres majuscules à votre mot de passe.",
        "specialchar": "Veuillez ajouter un ou plusieurs caractères spéciaux indiqués à votre mot de passe.",
        "number": "Veuillez ajouter un ou plusieurs chiffres à votre mot de passe.",
        "length": "Votre mot de passe est trop court.",
        "user_account_display": "Aucun compte utilisateur à afficher.",
        "user_account_remove": "Aucun compte utilisateur à supprimer.",
        "password_record": "Une erreur s'est produite lors de l'enregistrement du mot de passe.",
        "username_already_exists": "Le nom d'utilisateur saisi est déjà utilisé.",
        "password_already_exists": "Le mot de passe saisi est déjà utilisé."
    }

    if error in messages:
        return messages[error]
    else:
        return ""


""" END """

"""
    Check et sécurité.
"""


# Vérifie si le mot de passe est conforme aux consignes données. #
def IsValidPassword(password):
    checkList = {
        "length": (len(password) >= 8),
        "uppercase": False,
        "lowercase": False,
        "number": False,
        "specialchar": False
    }

    if WShield.IsString(password):
        for char in password:
            if IsUppercase(char):
                checkList["uppercase"] = True
            elif IsLowercase(char):
                checkList["lowercase"] = True
            elif IsNumber(char):
                checkList["number"] = True
            elif IsSpecialChar(char):
                checkList["specialchar"] = True

        for key in checkList:
            if not checkList[key]:
                print("{}\n{}".format(GetErrorMessage("invalid_password"), GetErrorMessage(key)))
                return False
    else:
        return False

    return True


# Vérifie que le mot de passe possède un ou plusieurs...
# ...caractères minuscules. #
def IsUppercase(char):
    return char.isupper()


# ...caractères majuscules. #
def IsLowercase(char):
    return char.islower()


# ...chiffres. #
def IsNumber(char):
    return char.isnumeric()


# ...caractères spéciaux pré-déterminés. #
def IsSpecialChar(char):
    if "!@#$%^&*".find(char) == -1:
        return False
    else:
        return True


# Récupère les données des utilisateurs et vérifie de potentiels doublons. #  
def AlreadyExistsInAccounts(accountKey, accountValue):
    accounts = GetAccountsList()

    for account in accounts:
        if account[accountKey] == accountValue:
            return True

    return False


""" END """

"""
    Gestion des dossiers / fichiers.
"""


# Supprime le fichier contenant les données des utilisateurs. #
def RemoveAccountsFile():
    if UserAccountsFile.FileExists():
        UserAccountsFile.Remove()
        return "Les comptes utilisateurs ont été supprimés avec succès."
    else:
        return GetErrorMessage("user_account_remove")


# Récupère et retourne les données utilisateur. #
def GetAccountsList():
    return UserAccountsFile.GetContent()


# Génère ou modifie le contenu du fichier contenant les données des utilisateurs. #
def SetAccountsFile(userDatas):
    if UserAccountsFile.SetContent(userDatas):
        return "Le mot de passe a été enregistré."
    else:
        return GetErrorMessage("password_record")


""" END """

"""
    Récupération des saisies de l'utilisateur.
"""


# Récupère l'option du menu sélectionnée. #
def GetMenuIdSelected():
    print("\nSaisissez le chiffre correspondant à votre choix, puis appuyez sur la touche entrée du clavier : ")
    userSelect = input("» ")

    if userSelect.isnumeric():
        userSelect = int(userSelect)
    else:
        print("Veuillez renseigner un chiffre valide.\n")
        return GetMenuIdSelected()

    return userSelect


# Récupère le nom de l'utilisateur. #
def GetUsername():
    username = input("\nSaisissez un nom d'utilisateur : ")
    username = username.strip()

    if len(username) > 0:
        if AlreadyExistsInAccounts("username", username):
            print(GetErrorMessage("username_already_exists"))
            return GetUsername()
        else:
            return username
    else:
        return GetUsername()


# Récupère le mot de passe de l'utilisateur. #
def GetUserPassword():
    password = maskpass.askpass("\nSaisissez votre mot de passe : ", "*")
    password = password.strip()

    if IsValidPassword(password):
        Password = SecurePassword(password)

        if AlreadyExistsInAccounts("password", Password.GetPassword()):
            print(GetErrorMessage("password_already_exists"))
            return GetUserPassword()
        else:
            return Password.GetPassword()
    else:
        return GetUserPassword()


""" END """
