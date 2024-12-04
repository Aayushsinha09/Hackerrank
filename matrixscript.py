import re

def decode_matrix_script():
    
    rows, cols = map(int, input().split())
    matrix = [input() for _ in range(rows)]

    
    transposed = zip(*matrix)

    
    decoded_script = ''.join(''.join(column) for column in transposed)

    
    result = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_script)


    print(result)


decode_matrix_script()
