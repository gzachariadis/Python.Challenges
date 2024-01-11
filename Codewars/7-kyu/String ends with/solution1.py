def solution(string, ending):
    return ending in string[-len(ending):]