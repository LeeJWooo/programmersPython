def solution(my_string, overwrite_string, s):
    n = s + len(overwrite_string)
    answer = my_string[:s] + overwrite_string + my_string[n:]

    return answer
result = solution("hello world", "test", 6)
print(result)