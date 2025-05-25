namespace TwoSum;

class TwoSum()
{
    static void Main(string[] args)
    {
        int[] array = { 1, 2, 3, 5, 8 };
        int targetValue = 4;
        int[] result = TwoSumMethod.TwoSum(array, targetValue);

        string resultString = $"The index to sum {targetValue} are: ";
        int i = 0 ;
        foreach (int resultItem in result)
        {
            if (i == 1)
                resultString += resultItem.ToString();
            else
                resultString += resultItem.ToString() + ", ";
            i++;
        }
        Console.WriteLine(resultString);
    }
}