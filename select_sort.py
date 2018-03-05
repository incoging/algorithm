#coding=utf-8
#选择排序

str = input("请输入要排序的数组：")
str = str.split(" ")
list = []
for con in str:
    tem = int(con)
    list.append(tem)

def searchMin(n):       #寻找从下标n开始的最小值
    min = list[n]
    j = n
    for i in range(n,len(list)):
        if list[i] < min:
            min = list[i]
            j = i
    return min, j

for i in range(len(list)-1):
    min, index = searchMin(i)
    tem = list[i]
    list[i] = list[index]
    list[index] = tem

print(list)