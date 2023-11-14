def solution(myString, pat):
    answer = ''.join(['A' if char == 'B' else 'B' for char in myString])
    return 1 if pat in answer else 0