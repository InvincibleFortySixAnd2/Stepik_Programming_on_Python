str = input()
i = 0
cnt = 1
n_str = ''

for ltr in str:
    print(ltr)
    if ltr[i] == ltr[i + 1]:
        cnt = cnt + 1
        i += 1
    print(cnt)






#for ltr in str:
