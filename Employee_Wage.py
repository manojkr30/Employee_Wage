"""
@Author: Manoj KR

@Date: 2024-08-01 12:40:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-08-01 13:38:11

@Title : Calculate Daily Employee Wage  .
"""  
import random
def display_welcome():
    """
     description:
        This function is used to Print welcome message .

    parameters:
               None.
    return:
           None.
    """
    print("Welcome To Wage Computation")

def check_attendance():
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

def check_full_or_part_time():
    """
     description:
        This function is used to give random Full time or Part time Employee by returning 0 and 1 .

    parameters:
               None.
    return:
           1 -> if employee Full Time.
           0 -> if employee Part Time.
    """
    return random.randint(0 , 1)

def calculate_wage_of_employee():
    """
     description:
        This function is used to give Calculate Daily Employee Wage for both Full Time and Part time Employee.
        Wage per Hour is 20
        Full Day Hour is 8
        Part time Hour is 8

    parameters:
               None.
    return:
            By calling switch_statment by sending attendence and fulltime or partime by o and 1. 
           160 -> if employee Present and Full Time.
           80 -> if employe Present and Part Time.
           0 -> if employee Absent.
    """
    return swith_statment([check_attendance(),check_full_or_part_time()])
def swith_statment(match_values):
    """
     description:
        This function is used to give Calculate Daily Employee Wage for both Full Time and Part time Employee by using Switch Statment.
    parameters:
            list : having attendance and parttime or fulltime.
    return: 
           160 -> if employee Present and Full Time.
           80 -> if employe Present and Part Time.
           0 -> if employee Absent.
    """
    match match_values:
        case [1,1] : 
            print("Employee Present Today")
            return 8*20
        case [1,0] :
            print("for Part time")
            return 4*20
        case _:
            print("Employee Absent Today")
            return 0
            
if __name__ =="__main__":
    display_welcome()
    empoyee_wage=0
    empoyee_wage=calculate_wage_of_employee()
    print("Today Employee Wage =",empoyee_wage)