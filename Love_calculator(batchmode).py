def calculator(s):
    l1 = []
    c = ''
    for i in s:
        if i not in l1:
            l1.append(i)
            c += str(s.count(i))
    num_str1 = c
    num_str2 = ''
    while len(num_str1) > 2:
        len1 = len(num_str1)
        mid = len1 // 2
        i = 0
        if len1 % 2 == 0:
            for i in range(0, mid - 1):
                num_str2 += str(int(num_str1[i]) + int(num_str1[len1 - i - 1]))
            num_str2 += str(int(num_str1[mid]) + int(num_str1[mid + 1]))
        else:
            for i in range(0, mid):
                num_str2 += str(int(num_str1[i]) + int(num_str1[len1 - i - 1]))
            num_str2 += str(num_str1[mid])
        num_str1 = num_str2
        num_str2 = ''

    return (num_str1)


name_list=[]
actual_name_list=[]
percent_list=[]
n=int(input('ENTER THE NO.OF NAMES:'))
for i in range(n):
    name = input('ENTER NAME '+str(i+1)+':').upper().rstrip().lstrip()
    actual_name_list.append(name)
    name1 = ''
    for i in name.split():
        name1 += i
    name_list.append(name1)
print()
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        namestr=name_list[i]+'LOVES'+name_list[j]
        percent_list.append(calculator(namestr))
k=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        print(actual_name_list[i],'LOVES',actual_name_list[j],':',percent_list[k],'%')
        k+=1
