# /*
#  * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
#  * y retorne lo siguiente:
#  * - "X" si han ganado las "X"
#  * - "O" si han ganado los "O"
#  * - "Empate" si ha habido un empate
#  * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#  *   O si han ganado los 2.
#  * Nota: La matriz puede no estar totalmente cubierta.
#  * Se podría representar con un vacío "", por ejemplo.
#  */

def analyze_tic_tac_toe(matrix):
    # Check rows and columns
    for i in range(3):
        # Rows
        if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != "":
            return matrix[i][0]
        # Columns
        if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != "":
            return matrix[0][i]

    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != "":
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != "":
        return matrix[0][2]

    # Check tie
    tie = True
    for row in matrix:
        for element in row:
            if element == "":
                tie = False
                break

    if tie:
        return "Tie"

    # If none of the above conditions are met
    return "Null"

# Example of use
example_matrix = [
    ["X", "O", "X"],
    ["O", "", "O"],
    ["X", "O", ""]
]

result = analyze_tic_tac_toe(example_matrix)
print("Result:", result)






