# /*
#  * Crea una función que encuentre todas las combinaciones de los números
#  * de una lista que suman el valor objetivo.
#  * - La función recibirá una lista de números enteros positivos
#  *   y un valor objetivo.
#  * - Para obtener las combinaciones sólo se puede usar
#  *   una vez cada elemento de la lista (pero pueden existir
#  *   elementos repetidos en ella).
#  * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#  *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#  *   (Si no existen combinaciones, retornar una lista vacía)
#  */

def find_combinations(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            combinations.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(nums)):
            backtrack(i + 1, target - nums[i], path + [nums[i]])

    combinations = []
    nums.sort() 
    backtrack(0, target, [])
    return combinations

lst = [1, 5, 3, 2]
objective = 6
result = find_combinations(lst, objective)
print(f"Lista: {lst}\nObjetivo: {objective}")
print("\nSoluciones:", result)









