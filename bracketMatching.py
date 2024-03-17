def bracket_matching(input_str):
    stack = []
    result = ""
    unmatched_left = set()
    unmatched_right = set()

    for i, char in enumerate(input_str):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                unmatched_right.add(i)

    for i in stack:
        unmatched_left.add(i)

    for i, char in enumerate(input_str):
        if i in unmatched_left:
            result += 'x'
        elif i in unmatched_right:
            result += '?'
        else:
            result += ' '

    return input_str + '\n' + result

# 读取输入并处理每个测试用例
while True:
    try:
        test_case = input().strip()
        print(bracket_matching(test_case))
    except EOFError:
        break
