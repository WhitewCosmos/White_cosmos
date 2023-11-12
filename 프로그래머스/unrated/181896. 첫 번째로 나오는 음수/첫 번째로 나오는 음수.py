def solution(num_list):
    for index, minus in enumerate(num_list):
        if minus < 0 :
            return index
    return -1