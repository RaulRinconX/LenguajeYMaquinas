#
#   LECTURA Y LIMPIEZA DEL PROGRAMA
#
def addSpaces(cad: str):
    """
    Añade espacios a los operadores para poder separarlos

    Args:
        cad (str): programa
    """
    operators = ['(', ')', '{', '}', ';', ':=']
    for op in operators:
        cad = cad.replace(op, ' ' + op + ' ')

    return


def cleanProgram(cad: str):
    """
    Limpia el código para que pueda ser tokenizado

    Args:
        cad (str): programa
    Returns:
        list : programa partido
    """

    # separa los operadores
    addSpaces(cad)

    # separa por whitespaces
    broken_prog = cad.split(None)

    return broken_prog


def readProgram(testname: str)->list:
    """
    Lee el programa y lo limpia para ser evaluado

    Args:
        testname (str): nombre del archivo (incluye .txt)

    Returns:
        list : programa partido
    """
    arch = open("" + testname, "r")

    inicial = arch.read()

    return cleanProgram(inicial)


print(readProgram("test1_in.txt"))

