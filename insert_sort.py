#coding=utf-8
#插入排序

list = input("请输入要排序的数组：")
list = list.split(" ")
# print(list)
tem = 0
num_list=[]
for con in list:
    tem = int(con)
    num_list.append(tem)

for j in range(1,len(num_list)):
    key = num_list[j]
    i = j - 1
    while i >= 0:
        if num_list[i] < key:
            num_list[i + 1] = num_list[i]
            i -= 1
        else:
            break
    num_list[i+1] = key

print(num_list)