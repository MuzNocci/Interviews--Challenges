def ArrayJumping(arr:list) -> int:


    arrOrdered = sorted(arr)
    count = 0

    for i in range(len(arr)):
        if arr[i] != arrOrdered[i]:
            count += 1
  
  
    return count



print('Testing...')

assert (ArrayJumping([1,2,3,4,2])) == 3, 'Não passou no teste 1'
assert (ArrayJumping([1,7,1,1,1,1])) == 2, 'Não passou no teste 2'

print('Passou em todos os testes. Parabéns!')