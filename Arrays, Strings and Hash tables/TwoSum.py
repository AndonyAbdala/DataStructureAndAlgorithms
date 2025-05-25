# /*
#  * Dado un array de números enteros y un target, retorna los índices de dos
#  * números para los que la suma de ambos sea igual al target.
#  *
#  * Puedes asumir que hay solamente una solución.
#  *
#  * Ejemplo 1:
#  *  Input: nums = [9,2,5,6], target = 7
#  *  Output: [1,2]
#  *  Explicación: nums[1] + nums[2] == 7, devolvemos [1, 2].
#  *
#  * Ejemplo 2:
#  *  Input: nums = [9,2,5,6], target = 100
#  *  Output: null
#  */

def TwoSum(array, targetValue: int):
    if array == None or len(array) < 2:
        return None
    
    complements = {}
    for index, element in enumerate(array):
        if element in complements.keys():
            return [complements.get(element), index]
        
        complement = targetValue - element
        complements[complement] = index

array = [1, 3, 5, 9, 4]
targetValue = 12
result = TwoSum(array, targetValue)

print(result)
 