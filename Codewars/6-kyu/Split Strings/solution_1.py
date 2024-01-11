def solution(s):
    result = []
    for i in range(0, len(s), 2):
        try:
            result.append("".join([s[i], s[i + 1]]))
        except IndexError:
            result.append("".join([s[-1:], "_"]))
    return result