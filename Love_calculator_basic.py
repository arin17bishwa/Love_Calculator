name=input('ENTER FIRST NAME:').upper().rstrip().lstrip()
name1=''
for i in name.split():
    name1+=i
name2=''
name=input('ENTER SECOND NAME:').upper().lstrip().rstrip()
for i in name.split():
    name2+=i
p=[]
print()
if name1.isalpha() and name2.isalpha():
    st=[name1+'LOVES'+name2,name2+'LOVES'+name1]
    for s in st:
        l1=[]
        c=''
        for i in s:
            if i not in l1:
                l1.append(i)
                c+=str(s.count(i))
        num_str1=c
        num_str2=''
        while len(num_str1)>2:
            len1=len(num_str1)
            mid=len1//2
            i=0

            if len1%2==0:
                for i in range(0, mid-1):
                    num_str2 += str(int(num_str1[i]) + int(num_str1[len1 - i - 1]))
                num_str2+=str(int(num_str1[mid])+int(num_str1[mid+1]))
            else:
                for i in range(0, mid):
                    num_str2 += str(int(num_str1[i]) + int(num_str1[len1 - i - 1]))
                num_str2+=str(num_str1[mid])
            num_str1=num_str2
            #print(num_str1)
            num_str2=''

        print(s.split('LOVES')[0]+' '+'LOVES'+' '+s.split('LOVES')[1],':',num_str1,'%')


else:
    print('INVALID INPUT!!MAKE SURE THE INPUT CONSISTS ONLY OF ALPHABETS!!')
