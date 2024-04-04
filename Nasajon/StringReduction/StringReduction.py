def StringReduction(strParam:str) -> int:


    reductions = {
        'ab':'c',
        'ac':'b',
        'ba':'c',
        'bc':'a',
        'ca':'b',
        'cb':'a',
    }
    string = strParam

    def reduction(string):

        for key, value in reductions.items():
            string = string.replace(key,value,1)

        return string


    while string != reduction(string):

        string = reduction(string)


    return len(string)



print('Testing...')

assert (StringReduction(str('abcabc'))) == 2, 'Não passou no teste 1'
assert (StringReduction(str('cccc'))) == 4, 'Não passou no teste 2'
assert (StringReduction(str('bcab'))) == 1, 'Não passou no teste 3'

print('Passou em todos os testes. Parabéns!')