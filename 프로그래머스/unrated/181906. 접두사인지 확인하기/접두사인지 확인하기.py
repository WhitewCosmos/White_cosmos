def solution(my_string, is_prefix):
    answer = 0
    for i, k in enumerate(is_prefix):
        if i < len(my_string):
            if k != my_string[i]:
                return answer
        else:
            return answer
    return 1       