Array_1 = []
Array_2 = []
Array_3 = []

while(True):

    x0 = input('Enter your request\n')
    
    if x0=='vote':
    
        while(True):
    
            print('Welcome to our voting software')
            print('''Press 1 for candidate-1
Press 2 for candidate-2
Press 3 for candidate-3''')
            x1 = input('Press your vote according to instructions\n')

            if x1=='1':
                        Array_1.append('v')

            elif x1=='2':
                        Array_2.append('v')

            elif x1=='3':
                        Array_3.append('v')

            elif x1=='q':
                        break

    elif x0=='show results':
        gnome = '4563'
        x2 = input('Enter the code\n')

        if x2==gnome:

            print(len(Array_1))
            print(len(Array_2))
            print(len(Array_3))

    elif x0=='purpose over':

        break
        


    








