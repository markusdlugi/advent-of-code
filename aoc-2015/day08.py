code_len = 0
str_len = 0
coded_code_len = 0
for line in open("input/08.txt"):
    line = line.strip()
    code_len += len(line)
    string = line[1:-1].encode("utf-8").decode("unicode_escape")
    str_len += len(string)
    code = "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
    coded_code_len += len(code)
    # print(line, len(line), string, len(string), code, len(code))

print(code_len - str_len)
print(coded_code_len - code_len)
