//# /*
//#  * Un anagrama es una palabra creada a partir de la reordenación de las letras de otra palabra. Ej: saco - caso
//#  * Dado un array de strings, devuelve los anagramas agrupados. Cualquier orden es válido.
//#  *
//#  * Ejemplo:
//#  *  Input: words = ["saco", "arresto", "programa", "rastreo", "caso"].
//#  *  Output: [["saco", "caso"], ["arresto", "rastreo"], ["programa"]].
//#  */


namespace GroupAnagrams;

class Anagram()
{
    static void Main(string[] args)
    {
        List<string> wordList = new List<string> { "saco", "arresto", "programa", "rastreo", "caso" };
        Solution sol = new Solution();
        List<List<string>> result = sol.SolutionAnagram(wordList);
    }
}