print('''
1 for yen
2 for dollar
3 for ruble
4 for yuan ''')
while True:
    choice = input("enter choice'1','2','3','4' : ")
    if choice in ('1','2','3','4'):
        if choice == '1':
            m = int(input('enter money : '))
            money = m*1.8
            print("money in japanese currency =",money)
        elif choice == '2':
            m = int(input('enter money : '))
            money = m*0.012
            print("money in american currency =",money)
        elif choice == '3':
            m = int(input('enter money : '))
            money = m*1.1
            print("money in russian currency =",money)
        elif choice == '4':
            m = int(input('enter money : '))
            money = m*0.086
            print("money in chinese currency =",money)
        
        next_calculation = input("Let's do next conversion? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print('invalid input')
        