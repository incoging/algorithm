#coding=utf-8
#归并排序


#方法一：通过左边右边加最大值无穷大来进行判断
# def merge(list, p, q, r):
#     # n1 = q - p + 1
#     # n2 = r - q
#     list1 = list[p:q+1]
#     list2 = list[q+1: r+1]
#
#     inf = float("inf")
#     list1.append(inf)
#     list2.append(inf)
#
#     i = 0
#     j = 0
#     for k in range(p,r + 1):
#         if list1[i] < list2[j]:
#             list[k] = (list1[i])
#             i += 1
#         else:
#             list[k] = (list2[j])
#             j += 1
#     # del list[-2:]
#
# def merge_sort(list, p, r):
#     if p < r:
#         q = (p + r)//2
#         merge_sort(list, p, q)
#         merge_sort(list, q+1, r)
#         merge(list, p, q, r)
#
#
# if __name__ == "__main__":
#     # str = input("请输入要排序的数组：")
#     # str = str.split(" ")
#     # t_list = []
#     # for con in str:
#     #     tem = int(con)
#     #     t_list.append(tem)
#     s = 0
#
#     t_list = [5, 2, 4, 6, 1, 3, 8, 9, 12, 7]
#     merge_sort(t_list, 0, len(t_list)-1)
#     print(t_list)






#方法二：左边右边一个输入完毕，另一个直接全部接到后面
def merge(list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    list1 = list[p:q+1]
    list2 = list[q+1: r+1]
    i = 0
    j = 0
    left_over = False
    right_over = False
    kk = 0
    for k in range(p,r + 1):
        if i < n1 and j < n2:
            if list1[i] < list2[j]:
                list[k] = (list1[i])
                i += 1
            else:
                list[k] = (list2[j])
                j += 1
        elif j >= n2 :
            right_over = True
            kk = k
            break
        else:
            left_over =True
            kk = k
            break
    if left_over:
        for la in range(kk, r + 1):
            list[la] = list2[j]
            j += 1
    if right_over:
        for la in range(kk, r + 1):
            list[la] = list1[i]
            i += 1

def merge_sort(list, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(list, p, q)
        merge_sort(list, q+1, r)
        merge(list, p, q, r)


if __name__ == "__main__":

    s = 0
    t_list = [5, 2, 4, 6, 1, 3, 8, 9, 12, 7]
    merge_sort(t_list, 0, len(t_list)-1)
    print(t_list)
