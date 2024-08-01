"""
@Author: Manoj KR

@Date: 2024-08-01 10:20:02

@Last Modified by: Manoj KR

@Last Modified time: 2024-08-1 10:45:11

@Title : Check Employee is Present or Absent

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

def attendance():
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

def main():
    display_welcome()
    if attendance() == 1:
        print("Employee Present")
    else :
        print("Employee Absent")

if __name__ =="__main__":
    main()