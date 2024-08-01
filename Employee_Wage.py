"""
@Author: Manoj KR

@Date: 2024-08-01 11:10:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-08-01 10:35:11

@Title : Calculate Daily Employee Wage .
"""

   
import random
def display_welcome():
    print("Welcome To Wage Computation")

def give_attendance():
    """
     description:
        This function is used to give random Absent or Present by returning 0 and 1 .

    parameters:
               None.
    return:
           1 -> if employee Present.
           0 -> if employee Absent.
    """
    return random.randint(0 , 1)

def calculate_wage_of_employee():
    """
     description:
        This function is used to give Wage of Employee based on Present and Absent.
        Wage per Hour is 20 and Full Day Hour is 8  

    parameters:
               None.
    return:
           160 -> if employee Present Full time 8 hour * 20 per hour.
           0 -> if employee Absent.
    """
    if give_attendance() == 1:
        print("Employee Present For Full Day")
        return 20*8
    else:
        print("Employee NOT Present")
        return 0

def main():
    total_wage=0
    display_welcome()
    total_wage=calculate_wage_of_employee()
    print("Today Wage=",total_wage)

        

if __name__ =="__main__":
    main()