def merge_the_tools(string, k):
    
    n = len(string) // k
    aux = 0
    var = ''
    
    for i in range(len(string)):
        
        if aux == k:
            aux = 0
            var = set(list(var))
            print(''.join(var))
            var = ''
        aux += 1
        var += string[i]
    if aux == k:
        var = set(list(var))
        print(''.join(var))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
