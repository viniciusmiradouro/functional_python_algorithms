def is_palindrome(x: int) -> bool:
    return (s := str(x)) == s[::-1]
