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
        return user
    
    def keep_going(self):
        '''This function will decide if the user want to continue or not'''
        choice = True
        while choice:
            working = input('Do you want to continue?(Y/N): ')
            if working.lower() == 'y':
                choice = False
                return True
            elif working.lower() == 'n':
                print('Thank you for using me')
                choice = False
                return False
            else:
                print('Your choice is invalid, please try again')
            
    def display(self):
        '''This function will display everything and ask if user want to continue or not'''
        while True:
            self.menu()
            option = self.option()
            if option == 1:
                print(f'Your result in Fahrenheit is {self.ctof()}')
                if not self.keep_going():
                    break
            elif option == 2:
                print(f'Your result in Celsiust is {self.ftoc()}')
                if not self.keep_going():
                    break
            elif option == 3:
                print('Thank you for using me.')
                break

        
cvtemp = Converter()
cvtemp.display()
