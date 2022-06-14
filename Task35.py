def get_data_from_file(num):
    f = open(num, 'r')
    flist = f.read() + ' '
    flist = list(map(int, flist.split()))
    f.close()
    return flist

def find_number(num):
    for i in range(len(num)-1):
        if num[i+1] - num[i] > 1:
            return num[i] + 1


fnum = '35_Add_number.txt'
num_list = get_data_from_file(fnum)

print(num_list)
print(find_number(num_list))


def get_full_num(num):
    for i in range(len(num)-1):
        if num[i+1] - num[i] > 1:
            num.insert(i+1, num[i] + 1)
    return num

num = get_data_from_file(fnum)

print(get_full_num(num_list)) 