def countSeq(num) -> str:


    result = ''
    previews = ''
    count = 1

    for i in range(len(num)+1):

        if previews == '':

            previews = num[i]

        else:

            try:
                
                if previews == num[i]:

                    count += 1

                else:

                    result += str(count)
                    result += previews
                    count = 1

                previews = num[i]

            except:

                result += str(count)
                result += previews


    return result


teste1 = countSeq('5526844')
teste2 = countSeq('11895142')


print(teste1)
print(teste2)