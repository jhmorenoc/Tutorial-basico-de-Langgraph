"""
Herramientas matemáticas para el agente con memoria.

Este módulo contiene las funciones de herramientas que el agente puede utilizar
para realizar operaciones matemáticas básicas como suma, multiplicación y división.
"""


def multiply(a: int, b: int) -> int:
    """
    Multiplica dos números enteros y retorna el resultado.

    Esta función toma dos argumentos de tipo entero, 'a' y 'b', y retorna el producto de ambos.
    Es útil cuando se requiere realizar operaciones de multiplicación en flujos de trabajo matemáticos
    o como parte de herramientas de cálculo para agentes conversacionales.

    Args:
        a: Primer número entero a multiplicar.
        b: Segundo número entero a multiplicar.

    Returns:
        El resultado de multiplicar 'a' por 'b' como un entero.

    Example:
        >>> multiply(3, 4)
        12
    """
    return a * b


def add(a: int, b: int) -> int:
    """
    Suma dos números enteros y retorna el resultado.

    Esta función recibe dos argumentos de tipo entero, 'a' y 'b', y retorna la suma de ambos.
    Es útil para realizar operaciones aritméticas básicas, como sumar cantidades, totales o valores
    en diferentes contextos dentro de un agente conversacional.

    Args:
        a: Primer número entero a sumar.
        b: Segundo número entero a sumar.

    Returns:
        La suma de 'a' y 'b' como un entero.

    Example:
        >>> add(3, 4)
        7
    """
    return a + b


def divide(a: int, b: int) -> float:
    """
    Divide el primer número entero por el segundo y retorna el resultado como flotante.

    Esta función toma dos argumentos de tipo entero, 'a' y 'b', y retorna el cociente de la división de 'a' entre 'b'.
    Es importante asegurarse de que 'b' no sea cero para evitar errores de división.
    Es útil para calcular proporciones, promedios u otras operaciones que requieran división en agentes conversacionales.

    Args:
        a: Número entero que será el dividendo.
        b: Número entero que será el divisor (no debe ser cero).

    Returns:
        El resultado de dividir 'a' entre 'b' como un número flotante.

    Raises:
        ZeroDivisionError: Si b es igual a cero.

    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


# Lista de todas las herramientas disponibles
AVAILABLE_TOOLS = [add, multiply, divide]