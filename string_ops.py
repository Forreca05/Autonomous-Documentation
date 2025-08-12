def reverse_string(s: str) -> str:
    """Inverte a string."""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Conta o número de vogais na string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
