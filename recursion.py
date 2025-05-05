def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    elif s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])
if __name__ == '__main__':
    print("Fibonacci(5):", fibonacci(5))        # Output should be 5
    print("GCD(48, 18):", gcd(48, 18))          # Output should be 6
    print('CompareTo("apple", "banana"):', compareTo("apple", "banana"))  # Negative value
    print('CompareTo("apple", "apple"):', compareTo("apple", "apple"))    # 0
    print('CompareTo("banana", "apple"):', compareTo("banana", "apple"))  # Positive value
