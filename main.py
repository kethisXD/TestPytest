def lenString(string):
    return len(string)

def StringInFile(string):
    with open("text.txt", 'w') as f:
        f.writelines(string)
        

