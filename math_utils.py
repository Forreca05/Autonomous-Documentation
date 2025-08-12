def factorial(n: int) -> int:
    """Calcula o fatorial de n."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(num: int) -> bool:
    """Verifica se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
