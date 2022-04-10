#Project 1 : Basic School Administration Program

import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "E-mail Id"])
        
        writer.writerow(info_list)

if __name__=='__main__':
    condition=1
    student_num=1


while(condition):

    student_info=input("Enter students information for student #{} in the format of (Name Age Contact_Number E-mail_Id): " .format(student_num))
    print("Entered information: " + student_info)

    #split
    student_info_list=student_info.split(' ')
    print("Entered splitted information : " + str(student_info_list))

    print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail Id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

    choice_check=input("Is this entered information correct? (yes/no): ")

    if choice_check=="yes":
        write_into_csv(student_info_list)
        

        condition_check=input("Enter(yes/no) if you want to add information of another student: ")
        if condition_check=="yes":
           condition=1
           student_num=student_num
           +1
        elif condition_check=="no":
           condition=0
        
    elif choice_check=="no":
        print("\nPlease write the information again: ")
