def get_unic(my_list):
    unic = []
    for i in range(len(my_list)):
        if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
            unic.append(my_list[i])
    return unic

x = int(input('Введите длину списка: '))
my_list = [i for i in range(0, x)]
print('Заполните список: ')
for i in range(0, x):
    my_list[i] = int(input())

print(get_unic(my_list))