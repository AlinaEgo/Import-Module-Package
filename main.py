from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_date = datetime.date.today()
    print(current_date)