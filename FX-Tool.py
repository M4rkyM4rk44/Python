import os

i = 0
while (i != 1):
    os.system('clear')

    print('Please Choose An Option:')
    print('')
    print('1: EXIT')
    print('2: Calculate Risk')
    print('3: Calculate Lot Size')
    print('4: Both')
    print('')
    
    option = int(input('Enter Your Choice: '))
    if option == 1:
        os.system('clear')
        print('Bye!')
        print('')
        i = 1
    elif option == 2:
        os.system('clear')
        print('=====Calculate Risk=====')
        print('')
        bal = float(input('Account Balance: $'))
        ris = int(input('Risk Percentage: %'))
        res = (ris*bal)/100
        print('')
        print("Risk Amount: $"+str(round(res,2)))
        print('')
        i = 2
    elif option == 3:
        os.system('clear')
        print('=====Calculate Lot Size=====')
        print('')
        amt = float(input('Risk Amount: $'))
        slp = float(input('Stop Loss Pips: '))
        res = amt/(10*slp)
        print('')
        print('Lot Size: '+str(round(res,1)))
        print('')
        i = 3
    elif option == 4:
        os.system('clear')
        print('=====Calculate Both=====')
        print('')
        bal = float(input('Account Balance: $'))
        ris = int(input('Risk Percentage: %'))
        amt = (ris*bal)/100
        slp = float(input('Stop Loss Pips: '))
        res2 = amt/(10*slp)
        print('')
        print('Lot Size: '+str(round(res2,1)))
        print('')
        i = 4
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
