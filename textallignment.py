def print_logo(thickness):
    
    c = 'H'
    
    
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    
    
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    
    
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))
    
    
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
    
    
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


if __name__ == "__main__":
    thickness = int(input())  
    if thickness % 2 == 1:
        print_logo(thickness)
    else:
        print("Please enter an odd number.")
