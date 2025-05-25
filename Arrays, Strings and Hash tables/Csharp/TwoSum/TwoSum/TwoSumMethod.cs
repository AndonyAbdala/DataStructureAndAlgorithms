//# /*
//#  * Dado un array de números enteros y un target, retorna los índices de dos
//#  * números para los que la suma de ambos sea igual al target.
//#  *
//#  * Puedes asumir que hay solamente una solución.
//#  *
//#  * Ejemplo 1:
//#  *  Input: nums = [9,2,5,6], target = 7
//#  *  Output: [1,2]
//#  *  Explicación: nums[1] + nums[2] == 7, devolvemos [1, 2].
//#  *
//#  * Ejemplo 2:
//#  *  Input: nums = [9,2,5,6], target = 100
//#  *  Output: null
//#  */

namespace TwoSum
{
    class TwoSumMethod
    {
        static public int[] TwoSum(int[] nums, int targetValue)
        { 
            if (nums == null || nums.Length < 2) return new int[] { };

            Dictionary<int, int> complements = new Dictionary<int, int>();

            for (int i = 0; i < nums.Length; i++)
            {
                if (complements.ContainsKey(nums[i]))
                {
                    return new int[] { complements[nums[i]], i };
                }

                int complement = targetValue - nums[i];

                complements.Add(complement, i);
            }

            int[] result = new int[2];
            return result;
        }
    }
}
