import hashlib

input_string = 'yzbqklnj'
search_string1 = '00000'
search_string2 = '000000'

previous_range = 0
for i in range(10_000_000):
    current_string = (input_string + str(i)).encode('utf-8')
    digest = hashlib.md5(current_string).hexdigest()
    if digest.startswith(search_string1):
        print(i)
        previous_range = i
        break

for i in range(previous_range + 1, 10_000_000):
    current_string = (input_string + str(i)).encode('utf-8')
    digest = hashlib.md5(current_string).hexdigest()
    if digest.startswith(search_string2):
        print(i)
        break
