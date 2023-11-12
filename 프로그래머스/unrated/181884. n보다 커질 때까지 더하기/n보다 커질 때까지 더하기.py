def solution(numbers, n):
    sum = 0
    for value in numbers:
        sum += value
        if sum > n:
            return sum
            