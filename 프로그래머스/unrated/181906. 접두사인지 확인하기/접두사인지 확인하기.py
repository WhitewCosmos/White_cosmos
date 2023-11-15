def solution(my_string, is_prefix):
    answer = 0
    if len(is_prefix) > len(my_string):
        return 0
    else:
        for i, k in enumerate(is_prefix):
            if k != my_string[i]:
                return answer
        return 1       