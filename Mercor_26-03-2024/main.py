def countSeq(num) -> str:


    num += ' '
    previews = ''
    count = 1
    result = ''

    for i in num:

        if previews == '':
            
            previews = i

        else:

            if previews == i:

                count += 1

            else:

                result += str(count)
                result += previews
                count = 1

        previews = i


    return result



teste1 = countSeq('1255487')
teste2 = countSeq('2259973')
teste3 = countSeq('6698742')



print(teste1)
print(teste2)
print(teste3)