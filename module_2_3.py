my_list = [42, 69, 322, 13, 1, 99, -5, 9, 8, 7, -6, 5]
dl_my_list = (len(my_list))
print(type(dl_my_list), dl_my_list)
ind = 0
my_list[ind]
print(type(my_list[ind]), my_list[ind])
while my_list[ind] > 0:
    print(ind)
    print(my_list[ind], " - Число положительное")
    ind = ind + 1
    if ind > 11:
        break







