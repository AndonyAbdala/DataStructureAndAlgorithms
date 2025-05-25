using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace GroupAnagrams
{
    class Solution()
    {
        public  List<List<string>> SolutionAnagram(List<string> wordsList)
        {
            Dictionary<string, List<string>> result = new Dictionary<string, List<string>>();
            foreach (var word in wordsList)
            {
                string hash = createHash(word);
                if (!result.ContainsKey(hash)) 
                {
                    result[hash] = new List<string>();
                }
                result[hash].Add(word);
            }
            return result.Values.ToList();
        }

        private string createHash(string word)
        {
            int[] arrayHash = new int[26];
            foreach (char c in word) 
            {
                arrayHash[c - 'a']++;
            }
            return string.Join("", arrayHash);
        }
    }
}
