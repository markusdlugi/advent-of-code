import re


def in_list(sub, str_list):
    return next((s for s in str_list if sub in s), None) is not None


abba_pattern = r'(\w)((?!\1).)\2\1'
aba_pattern = r'(?=(.)((?!\1).)\1)'
hypernet_pattern = r'\[([^\]]*)\]'
supernet_pattern1 = r'([a-z]*)(?:$|\[)'
tls_ips = set()
ssl_ips = set()
for line in open("input/07.txt"):
    line = line.strip()

    hypernets = re.findall(hypernet_pattern, line)
    supernets = re.findall(supernet_pattern1, line)

    # TLS
    abba_list = re.findall(abba_pattern, line)
    abba_in_hypernet = False
    for a, b in abba_list:
        abba = a + b + b + a
        if in_list(abba, hypernets):
            abba_in_hypernet = True
            break
    if len(abba_list) > 0 and not abba_in_hypernet:
        tls_ips.add(line)

    # SSL
    aba_list = re.findall(aba_pattern, line)
    ssl = False
    for a, b in aba_list:
        if not (b, a) in aba_list:
            continue
        aba = a + b + a
        bab = b + a + b
        if in_list(aba, hypernets) and in_list(bab, supernets) or in_list(aba, supernets) and in_list(bab, hypernets):
            ssl_ips.add(line)

print(len(tls_ips))
print(len(ssl_ips))
