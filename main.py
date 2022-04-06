from people import get_employees
from salary  import calculate_salary
from datetime import datetime

d = datetime.today()

def main_function():
    print('main function is started')
    get_employees()
    calculate_salary()
    print('main function is finished')

if __name__ == '__main__':
    main_function()
    print(f' datetime function - {d}')