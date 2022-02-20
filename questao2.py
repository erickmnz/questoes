#testes unitarios estao como comentarios
def senha(passw):
    passw = input('digite: ')
    alpha_upper=0
    alpha_lower=0
    character=0
    digit =0
    #is_strong = False
    if len(passw) >= 6:
        for i in passw:
            if i.isupper() == True:
                alpha_upper+=1
            elif i.islower() == True:
                alpha_lower +=1
            elif i.isdigit() == True:
                digit +=1
            elif i in '!@#$%^&*()-+':
                character+=1
        if (alpha_lower >= 1) and (alpha_upper >=1) and (digit >=1) and (character >= 1):
            #is_strong = True
            #print(is_strong, alpha_lower, alpha_upper,digit,character)
            return 'Senha aceita'
        else:
            return 'Senha incompativel'
    else:
        #print(is_strong)
        return 6-len(passw)

#teste1 = senha('AIERHJsjhfduae8123(@((#*')
#teste2= senha('Ya3')
#teste3 = senha('Ya3a')
#teste4 = senha('Ya')
#teste5 = senha('Uhahdhuae*7273((s)')
#print(f'Teste1: {teste1}\nTeste2: {teste2}\nTeste3: {teste3}\nTeste4: {teste4}\nTeste5: {teste5}')
print(senha(input))
