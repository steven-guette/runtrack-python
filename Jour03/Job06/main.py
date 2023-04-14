def WriteInPyramid(text):
    endPos = 1

    while len(text) > endPos:
        print(text[0:endPos:])

        text = text[endPos::]
        endPos += 1

text = "abcdefghijklmnopqrstuvwxyz" * 10

WriteInPyramid(text)