def solution(code):
    ret = ""
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 - mode
        else:
            if mode == 0:
                if i % 2 == 0:
                    ret += code[i]
            else:
                if i % 2 != 0:
                    ret += code[i]
    if len(ret) == 0:
        return "EMPTY"
    return ret
                