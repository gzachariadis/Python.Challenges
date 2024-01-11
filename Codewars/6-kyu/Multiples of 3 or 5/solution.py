def solution(number):
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)