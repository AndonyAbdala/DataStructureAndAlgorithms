# /*
#  * Dado un método que recibe una String, comprobar si todos los caracteres son únicos o no.
#  *
#  * isUnique("abcde") => true;
#  * isUnique("abcded") => false;
#  */

def isUnique(string: str):
    if len(string) > 26:
        return False
    
    uniqueItems = []
    for item in string:
        if item in uniqueItems:
            return False
        uniqueItems.append(item)
    return True

print(isUnique("abcded"))
print(isUnique("abcde"))