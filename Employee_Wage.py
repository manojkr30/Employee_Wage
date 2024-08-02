"""
@Author: Manoj KR

@Date: 2024-08-02 10:25:12

@Last Modified by: Manoj KR

@Last Modified time: 2024-08-02 11:33:01

@Title : Calculate Wages till a condition of total working hours or days is reached for a month (100 hours and 20 days).
"""  
import random
FULL_TIME = 8
PART_TIME = 4
WAGE_HOUR = 20
FULL_TIME_WAGE_DAY= FULL_TIME * WAGE_HOUR
PART_TIME_WAGE_DAY= PART_TIME * WAGE_HOUR
DAYS_MONTH = 20

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

def calculate_wage_for_day():
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
            return FULL_TIME*WAGE_HOUR
        case [1,0] :
            return PART_TIME*WAGE_HOUR
        case _:
            return 0
        
def calculate_wage_till_condition():
    """
    description:
        This function is used Calculate Wages till a condition of total working hours or days is reached for a month
        Assume --> 100 hours and 20 days
    parameters:
             None
    return: 
           list = employee daily wages.
    """
    wage_list=[]
    HOURS = 100 
    DAYS = 20
    current_hours=0
    current_days =0
    while current_hours <= HOURS and current_days < DAYS :
        current_days += 1
        wage=calculate_wage_for_day()
        if  wage == FULL_TIME_WAGE_DAY:
            wage_list.append(wage)
            current_hours += FULL_TIME
           
        elif wage == PART_TIME_WAGE_DAY:
            wage_list.append(wage)
            current_hours += PART_TIME
            
        else :
             wage_list.append(0)
        
             
    return wage_list
     
            
if __name__ =="__main__":
    display_welcome()
    employee_wage_list=calculate_wage_till_condition()
    print(f"Employee_Wage_List {employee_wage_list}")
    print(f"Total Wage of Employee : {sum(employee_wage_list)}")
    
  