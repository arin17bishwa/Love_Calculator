import xlrd #to read the spreadsheet
import time #to calculate the time consumed 

f=open("Love_Calc_All_Year.txt","w+")

def actual_to_req(s):#since there might be some formatting discrepencies(like unwanted endline characters,spaces,etc)
                      #so this program takes the name and converts it into the required name format.
    k=s.split(' ')
    s=''
    for i in k:
        s+=i
    #print('name to str is',s)
    return (s.lstrip().rstrip())

def calculator(s):#main calculator function
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

print()
t1=time.time()
loc=("")#Enter the location of the spreadsheet file to be read.
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
actual_name_list=[]
for i in range(sheet.nrows):
    s=str(sheet.cell_value(i,1))
    if s=="":
        continue
    if s[0]!='1':
        continue
    name=str(sheet.cell_value(i,2))
    if name[0]=='1':
        name = str(sheet.cell_value(i,3))
    k=name.split('\n')
    name=''
    for j in k:
        name+=j+' '
    actual_name_list.append(name.upper().lstrip().rstrip())
st=''
s='Written and Compiled by Arin\n\n\n\n'
f.write(s)
n=len(actual_name_list)
k=1
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        namestr=actual_to_req(actual_name_list[i])+'LOVES'+actual_to_req(actual_name_list[j])
        f.write(str(str(k)+')'+actual_name_list[i]+' LOVES '+actual_name_list[j]+' : '+str(calculator(namestr))+'%'))
        f.write('\n')
        k+=1
t2=time.time()
k-=1
s='Produced '+str(k)+' results in '+str(t2-t1)+' seconds \n'
print(s)
f.write(s)
s='Written and Compiled by Arin\n\n\n\n'
print(s)
f.write(s)
f.close()

