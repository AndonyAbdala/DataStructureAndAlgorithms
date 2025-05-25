# /*
#  * Un anagrama es una palabra creada a partir de la reordenación de las letras de otra palabra. Ej: saco - caso
#  * Dado un array de strings, devuelve los anagramas agrupados. Cualquier orden es válido.
#  *
#  * Ejemplo:
#  *  Input: words = ["saco", "arresto", "programa", "rastreo", "caso"].
#  *  Output: [["saco", "caso"], ["arresto", "rastreo"], ["programa"]].
#  */


def createAnagramHash(inputString: str):
    letterCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for character in inputString:
        letterCount[ord(character) - ord('a')] = letterCount[ord(character) - ord('a')] + 1
    result = "".join(str(letterCount))
    return result

def buildAnagramMap(stringArray):
    map = {}
    for word in stringArray:
        hash = createAnagramHash(word)
        if not (hash in map.keys()):
            map[hash] = []
        map[hash].append(word)
        
    return map

def groupAnagrams(wordsArray):
    if wordsArray == None or len(wordsArray) == 0:
        return None
    result = {}
    result = buildAnagramMap(wordsArray)
    return list(result.values())

words = ["saco", "arresto", "programa", "rastreo", "caso", "asco"]
result = groupAnagrams(words)
print(result)