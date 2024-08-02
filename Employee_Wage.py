"""
@Author: Manoj KR

@Date: 2024-08-02 10:25:12

@Last Modified by: Manoj KR

@Last Modified time: 2024-08-02 11:33:01

@Title : Calculating Wages for a Month.
"""  
import random
FULL_TIME = 8
PART_TIME = 4
WAGE_HOUR = 20
ABSENT = 0
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
            return ABSENT
        
def calculate_wage_for_month():
    """
    description:
        This function is used to give Calculate Montly Employee Wage (20 days in a month) 
    parameters:
             None
    return: 
           total_month_wage : Total Mnth wage of Employee.
           full_time : Nuber of days Employee Wark for Full Time
           part_time : Nuber of days Employee Wark for Part Time
           absent : Number of days Employee Absent in a Month
           present : Number of days Employee Present in a Month
    
    """
    
    total_month_wage=full_time=part_time=absent=present=0
    
    for i in range(DAYS_MONTH):
        wage=calculate_wage_for_day()
        if wage > 0 :
            present+=1
            if wage == FULL_TIME_WAGE_DAY:
                full_time +=1
                total_month_wage += wage
            else :
                part_time +=1
                total_month_wage += wage
        else :
            absent +=1
    
    return total_month_wage,present,absent,full_time,part_time
        


  
     
            
if __name__ =="__main__":
    display_welcome()
    total_month_wage,present,absent,full_time,part_time=calculate_wage_for_month()
    print("The Employee in Month (20 days)")
    print("---------------------------------")
    print(f"Present :{present}",f"Absent :{absent}",sep="\t | \t")
    print("---------------------------------")
    print(f"{full_time} Days Work Full Time",f"{part_time} Days Work Part Time",sep="   |   ")
    print("---------------------------------")
    print(f"Total Wage Per Month = {total_month_wage}")
    