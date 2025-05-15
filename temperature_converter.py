class Converter:
    def menu(self):
        '''This function print out the menu of the application'''
        print('Welcome to the temperature converter application\nHere are our services')
        print('1. Convert from Celsius to Fahrenheit')
        print('2. Convert from Fahrenheit to Celsius')
        print('3. Exit')
        
    def ctof(self):
        '''This function will take the user input in Celsius and then return the temperature in Fahrenheit'''
        while True: #This part will take user input, raise value if user made a wrong input format and make user choose again
            try:
                temp = float(input('Please enter the Celsius temperature: '))
                break
            except ValueError:
                print('Your input must be number only')
        return temp*1.8 + 32
    
    def ftoc(self):
        '''This function will take the user input in Fahrenheit and then return the temperature in Celsius'''
        while True: #This part will take user input, raise value if user made a wrong input format and make user choose again
            try:
                temp = float(input('Please enter the Fahrenheit temperature: '))
                break
            except ValueError:
                print('Your input must be number only')
        return (temp-32)/1.8
    
    def option(self):
        '''This function will get user choice input and process it'''
        while True:
            try:
                user = int(input('What is your choice: '))
                if user in range(1,4):
                    break
                else:
                    print('You must choose option from 1-3')
            except ValueError:
                print('Your choice is invalid, please try again')
        if user == 1:
            result_ctof = self.ctof()
            print(f'The temperature in Fahrenheit is: {result_ctof:.2f}')
                
        elif user == 2:
            result_ftoc = self.ftoc()
            print(f'The temperature in Celsius is: {result_ftoc:.2f}')
        else:
            print('Thank you for choosing our service. Goodbye.')
            
    def display(self):
        '''This function will display everything and ask if user want to continue or not'''
        self.menu()
        self.option()
        while True:
            keep_going = input('Do you want to continue?(Y/N): ')
            if keep_going == 'N':
                break
            elif keep_going == 'Y':
                self.option()
            else:
                print('Your choice is invalid, please try again')
        
cvtemp = Converter()
cvtemp.display()