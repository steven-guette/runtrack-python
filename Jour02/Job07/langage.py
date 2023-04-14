def ChooseYourLanguage(langage):
    langage = langage.lower()
    outputText = "Tu est un developpeur "

    if langage == "javascript":
        outputText += "web"
    elif langage == "python":
        outputText += "IA"
    elif langage == "java":
        outputText += "logiciel"
    elif langage == "reactjs":
        outputText += "mobile"
    else:
        outputText = "Un jour, je serais le meilleurdeveloppeur..."

    print(outputText)

languages = ["javascript", "python", "java", "reactjs", "html"]

for lang in languages:
    ChooseYourLanguage(lang)