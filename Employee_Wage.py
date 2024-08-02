"""
@Author: Manoj KR

@Date: 2024-08-02 14:02:23

@Last Modified by: Manoj KR

@Last Modified time: 2024-08-02 14:50:01

@Title : Refactor the Code to write a Class Method to Compute Employee Wage.
"""  
import random

class EmployeeWageComputation:
    FULL_TIME_HOURS = 8
    PART_TIME_HOURS = 4
    WAGE_PER_HOUR = 20
    MAX_HOURS = 100
    MAX_DAYS = 20

    @classmethod
    def display_welcome(cls):
        """Prints a welcome message."""
        print("Welcome To Wage Computation")

    @classmethod
    def check_attendance(cls):
        """
        Randomly determines if the employee is present or absent.
        
        Returns:
            int: 1 if employee is present, 0 if absent.
        """
        return random.randint(0, 1)

    @classmethod
    def check_full_or_part_time(cls):
        """
       Description: Randomly determines if the employee works full-time or part-time.
        
        Returns:
            int: 1 if employee is full-time, 0 if part-time.
        """
        return random.randint(0, 1)

    @classmethod
    def calculate_wage_for_day(cls, attendance, work_type):
        """
        Description : Calculates the daily wage based on attendance and work type.
        
        Parameters:
            attendance (int): 1 if employee is present, 0 if absent.
            work_type (int): 1 if full-time, 0 if part-time.
        
        Returns:
            int: Daily wage based on attendance and work type.
        """
        if attendance == 1:
            hours = cls.FULL_TIME_HOURS if work_type == 1 else cls.PART_TIME_HOURS
            return hours * cls.WAGE_PER_HOUR
        return 0

    @classmethod
    def calculate_wage_till_condition(cls):
        """
        Description: Calculates wages until the total working hours or days for the month are reached.
        Parameters:
                None
        Returns:
            list: Employee daily wages.
        """
        wages = []
        total_hours = 0
        total_days = 0

        while total_hours < cls.MAX_HOURS and total_days < cls.MAX_DAYS:
            total_days += 1
            attendance = cls.check_attendance()
            work_type = cls.check_full_or_part_time()
            daily_wage = cls.calculate_wage_for_day(attendance, work_type)

            wages.append(daily_wage)
            total_hours += cls.FULL_TIME_HOURS if work_type == 1 else cls.PART_TIME_HOURS if attendance == 1 else 0

        return wages

if __name__ == "__main__":
    EmployeeWageComputation.display_welcome()
    employee_wage_list = EmployeeWageComputation.calculate_wage_till_condition()
    print(f"Employee Wage List: {employee_wage_list}")
    print(f"Total Wage of Employee: {sum(employee_wage_list)}")
