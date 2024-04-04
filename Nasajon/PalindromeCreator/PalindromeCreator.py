def PalindromeCreator(strParam:str) -> str:  # Palindromo ou Not possible


    result = ''
    rest = ''
    strParamInvert = strParam[::-1]

    while len(strParam) > 0:

        if not strParam[0] == strParamInvert[0]:
            result += strParam[0]
            strParam = strParam[1::]
            strParamInvert = strParamInvert[:-1:]
        else:
            rest += strParam[0]
            strParam = strParam[1::][:-1:]
            strParamInvert = strParamInvert[1::][:-1:]


    return 'Not possible' if result == '' or len(rest) < 3 else result



print('Testing...')

assert (PalindromeCreator(str('abjchba'))) == 'jc', 'Não passou no teste 1'
assert (PalindromeCreator(str('mmop'))) == 'Not possible', 'Não passou no teste 2'
assert (PalindromeCreator(str('kjjjhjjj'))) == 'k', 'Não passou no teste 3'

print('Passou em todos os testes. Parabéns!')