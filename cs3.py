#python program to make a area calculator
print('''
1 for circle
2 for square
3 for triangle
4 for rectangle''')
choice = input('enter the no : ')
if choice in ('1','2','3','4'):
    if choice == '1':
        r = int(input('enter radius : '))
        circle = 3.14*r**2
        print('area =',circle)

    elif choice == '2':
        s = int(input('enter side : '))
        square = s*s
        print('area =',square)

    elif choice == '3':
        h = int(input('enter height : '))
        b = int(input('enter base length : '))
        triangle = 0.5*h*b
        print('area =',triangle)

    elif choice == '4':
        l = int(input('enter length : '))
        b = int(input('enter base length : '))
        rectangle = l*b
        print('area =',rectangle)
    
