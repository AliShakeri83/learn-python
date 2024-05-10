s1=[8.5 , 'test' , 2.3564 , 49 , 47.3 , 'java' , 71.569 , 63 , 8 , 'c++' , 12.14]
for i in s1:
    if type (i) == float :
        print(f'{i:.2f}')
    if type (i) == str :
        continue
    if type (i) == int :
        print(f'{i:04d}')
