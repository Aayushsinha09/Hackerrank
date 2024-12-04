def rangoli(size):
    import string
    

    alphabet = string.ascii_lowercase
    
    
    lines = []
    for i in range(size):
       
        left_part = "-".join(alphabet[size-1:size-i-1:-1])
        
      
        full_line = left_part + "-" + "-".join(alphabet[size-i-1:size]) if i != 0 else alphabet[size-1]
        
       
        lines.append(full_line.center(4*size-3, '-'))

    
    return "\n".join(lines + lines[-2::-1])
