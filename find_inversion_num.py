#coding=utf-8
#通过归并排序在nlgn时间内找到逆序数的个数
def merge(list, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    list1 = list[p:q+1]
    list2 = list[q+1: r+1]
    global inversion
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
                inversion += n1 - i     #每次取右边列表中的一次数，左边列表剩下的数的个数，就是对于右边这个数的逆序数
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
    # print(list)


        # del list[-2:]

def merge_sort(list, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(list, p, q)
        merge_sort(list, q+1, r)
        merge(list, p, q, r)


if __name__ == "__main__":

    inversion = 0
    s = 0
    t_list = [5, 2, 4, 6, 1, 3, 8, 9, 12, 7]
    merge_sort(t_list, 0, len(t_list)-1)
    print(t_list)
    print(inversion)

    # inversion = 0
    # testlist = [2, 5, 8, 10, 11, 1, 3, 6, 7]
    # merge(testlist,0, 4, 8)
    # print(inversion)