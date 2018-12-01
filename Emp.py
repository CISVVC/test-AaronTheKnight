Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Employee:

    #initialize the attributes
    def __init__(self, name, id, department, title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    #set the attributes
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    #return the attributes
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    #return the objects state as a string

    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nID number: ' + self.__id + \
               '\nDepartment: ' + self.__department + \
               '\nTitle: ' + self.__title
import emp



def main():

    # Create three employee objects
    emp1 = Employee(name='Susan Meyers', employee_id='47899', department='Accounting', title='Vice President')
    emp2 = Employee(name='Mark Jones', employee_id='39119', department='IT', title='Programmer')
    emp3 = Employee(name='Joy Rogersr', employee_id='81774', department='Manufacturing', title='Engineer')

    print(emp1, sep='/n/n')
    print(emp2, sep='/n/n')
    print(emp3, sep='/n/n')
