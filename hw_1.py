def caching_fibonacci():
    """
    Повертає функцію fibonacci(n) з кешуванням результатів.
    """
    cache = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        """
        Обчислює n-те число Фібоначчі з використанням кешу.
        """
        if not isinstance(n, int):
            raise TypeError("n має бути цілим числом")

        if n < 0:
            raise ValueError("n має бути невід'ємним")

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610