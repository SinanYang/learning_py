def fac(x):
    result = 0
    i = 1
    while i < x:
        if x % i == 0:
            result = result + i
        i += 1
    return result


n = int(input(' Please type a number: '))
count = 1
list_of_value = []

while count < n:
    list_of_value.append(fac(count))
    count += 1

num = 0

for value in list_of_value:
    num += 1
    if (value != 0) & (value < n):
        if num < value:
            num_ami = value
            value_ami = list_of_value[num_ami - 1]
            if num == value_ami:
                print("{}-{}".format(num, value))
