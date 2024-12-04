def solve(s):
    string_list = s.split(" ")
    final = ""
    for i in string_list:
        final += i.capitalize() + ' '
    return final
