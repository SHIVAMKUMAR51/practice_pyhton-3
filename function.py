string=input("enter the string:")
dict={}
l1=[]
for i in string:
    dict[i] = string.count(i)
print(dict)

dict2 = {}
while(1):
    for i in dict.keys():
        max = i
        for j in dict.keys():
            if j not in dict2.keys():
                if(dict[max] <= dict[j]):
                    max=j
        dict2[max]=dict[max]
    if(len(dict2) == len(dict)):
        break

print(dict2)
