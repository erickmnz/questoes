def anagrama(entrada):
    subs, total, new = [], [], []

    p = entrada.split(' ')
    palavra = ''.join(p)

    s_ubs=[subs.append(palavra[i:k]) for k in range(1,len(palavra)+1)for i in range(len(palavra)) if palavra[i:k] != '']
    t_otal = [total.append(subs[n]) for j in range(1,len(subs)) for n in range(len(subs)) if sorted(subs[n]) == sorted(subs[j]) and len(subs[n])<len(palavra) ]
    #return len(subs), len(total), total

    for i in range(len(total)-1):
        if sorted(total[i]) == sorted(total[i+1]) and new.count([total[i], total[i+1]]) < 1:
            n= new.extend([[total[i], total[i+1]]])

    #return new, len(new)
    return len(new)

print(anagrama(input('digite: ')))
#print(anagrama('aab'))
#print(anagrama('abc'))
#print(anagrama('abcd'))
#print(anagrama('abcde'))
#print(anagrama('aabb'))
#print(anagrama('col o   mb o'))
#print(anagrama('ovo'))
#print(anagrama('ifailuhkqq'))
#print(anagrama('aaabbaabb'))
#print(anagrama('tamborbolha'))


