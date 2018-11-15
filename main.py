#Wilder Umana 5/29/2018
#https://www.tutorialspoint.com/sqlite/sqlite_python.htm
#https://www.pythoncentral.io/introduction-to-sqlite-in-python/

from Cases import Cases
from Investigator import Investigator
import sqlite3
import time
def main():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == 'Will' and PassWord == '911':
            time.sleep(1)
            print ("Login successful!")
            time.sleep(2)
            print('\t\tWelcome'+'\t'+str(UserName))
            break

        else:
            print ("Password did not match! or Username Did not match")


main()
#if the program gives an Error, please restart it againg
case=Cases()
investigator=Investigator()

print('Welcome to The Forensic Lab\n','\tWhat Would you like to do?')
print()
inside=1
while(inside==1):
    print("A. View Cases\n")
    print("B. View Investigators\n")
    option=input("Select from the options(A/B):").upper()
    if (option=='A'):
        optionA='Y'
        while(optionA=='Y'):
            case.viewCases()
            print('\tWould your like to do something else')
            print("\t\tC. View Case By ID")
            print("\t\tD. Add a Case")
            print("\t\tE. Edit A Case")
            print("\t\tF. Add/view/Edit Evidence")
            print("\t\tQ. Quit")
            option1=input("Select from the options(C/D/E/F/Q):").upper()
            if (option1=='C'):
                optionC='Y'
                while(optionC=='Y'):
                    ID=input(str("Enter the ID of the Case\n")).upper()
                    try:
                        case.viewCaseByID(ID)
                        optionC=input('Do you want Enter Another ID? (Y/N)\n').upper()
                    except:
                        print("\t\tYou must Enter a Number\t\t")
                        print()
                        optionC=input('Do you want to try Again (Y/N)\n').upper()
            elif (option1=='D'):
                optionD='Y'
                while(optionD=='Y'):
                     print('Please Have the Case ID,Name,Date, and Description avaliable')
                     print()
                     caseID=input(str('Enter The Case ID:\n')).upper()
                     if caseID=="":
                        print('You did not Input Information')
                        caseID=input(str('Enter The Case ID:\n')).upper()
                     name=input(str('Enter The Name:\n')).upper()
                     if name=="":
                        print('You did not Input Information')
                        name=input(str('Enter The Name:\n')).upper()
                     date=input(str('Enter The Case Date:\n')).upper()
                     if date=="":
                        print('You did not Input Information')
                        date=input(str('Enter The Case Date:\n')).upper()
                     description=input(str('Enter The Description:\n')).upper()
                     if description=="":
                        print('You did not Input Information')
                        description=input(str('Enter The Description:\n')).upper()
                        if description=="":
                            print("You made too many mistakes, you will be logged off")
                            time.sleep(5)
                            
                            exit()
                     case.addCase(name,description,date,caseID)
                     optionD=input('Would you like to add Aother Case?(N/Y)\n').upper()
            elif (option1=='E'):
              optionE='Y'
              while(optionE=='Y'):
                     print('You are about to Edit a Case \n\t\tPlease Have the Case ID,Name,Date, and Description avaliable')
                     print()
                     caseID=input(str('Enter The Case ID:\n')).upper()
                     if caseID=="":
                        print('You did not Input Information')
                        caseID=input(str('Enter The Case ID:\n')).upper()
                     name=input(str('Enter The Name:\n')).upper()
                     if name=="":
                        print('You did not Input Information')
                        name=input(str('Enter The Name:\n')).upper()
                     date=input(str('Enter The Case Date:\n')).upper()
                     if date=="":
                        print('You did not Input Information')
                        date=input(str('Enter The Case Date:\n')).upper()
                     description=input(str('Enter The Description:\n')).upper()
                     if description=="":
                        print('You did not Input Information')
                        description=input(str('Enter The Description:\n')).upper()
                        if description=="":
                            print("You made too many mistakes, you will be logged off")
                            time.sleep(5)
                            exit
                     case.editCase(name,description,date,caseID)
                     optionF=input('\t\tWould you like to Edit Another Case?(Y/N):\n').upper()
            elif(option1=='F'):
                optionF='Y'
                while(optionF=='Y'):
                    print('\tWhat Woud you liek to do?')
                    print("\t\tA. Add Evidence")
                    print("\t\tE. Edit Evidence")
                    print("\t\tV. View all Evidence by Case ID")
                    print("\t\tQ. Quit")
                    option2=input("Select From the options (A/E/V/Q)").upper()
                    
                    if (option2=='A'):
                        optionA='Y'
                        while (optionA=='Y'):
                            print('Your Are about to aDD Evidence, \n\t\tplease have your Cases ID, Name, and Description avaliable')
                            caseID=input(str('Enter the Case ID:\n')).upper()
                            if caseID=="":
                                print('\t\tYou did not Input Information')
                                caseID=input(str('Enter the Case ID:\n'))
                            name=input(str('Enter the name:\n'))
                            if name=="":
                                print('\t\tYou did not Input Information')
                                name=input(str('Enter The Name:\n')).upper()
                            description=input(str('Enter a Description:\n'))
                            if description=="":
                                print('\t\tYou did not Input Information')
                                description=input(str('Enter The Description:\n')).upper()
                                if description=="":
                                    print("You made too many mistakes, you will be logged off")
                                    time.sleep(5)
                                    exit()
                            try:
                               case.addEvidence(name,description,caseID)
                            except:
                              print('\t\tYour must Enter a Number')
                              print()
                              optionA=input('Do you want to try againg: (Y/N)\n').upper()
                    if(option2=='E'):
                      optionE='Y'
                      while (optionE=='Y'):
                         print('Your Are about to EDIT Evidence, \n\t\tplease have your Cases ID, Name, and Description avaliable')
                         caseID=input(str('Enter the Case ID:\n')).upper()
                         if caseID=="":
                            print('\t\tYou did not Input Information')
                            caseID=input(str('Enter the Case ID:\n')).upper()
                         name=input(str('Enter the name:\n'))
                         if name=="":
                            print('\t\tYou did not Input Information')
                            name=input(str('Enter The Name:\n')).upper()
                         description=input(str('Enter a Description:\n'))
                         if description=="":
                            print('\t\tYou did not Input Information')
                            description=input(str('Enter The Description:\n')).upper()
                            if description=="":
                                print("You made too many mistakes, you will be logged off")
                                time.sleep(5)
                                exit()
                         try:
                           case.editEvidence(name,description,caseID)
                         except:
                          print('\t\tYour must Enter a Number')
                          print()
                          optionE=input(str('Do you want to try againg: (Y/N)\n')).upper()
                      optionE=input('\t\tdo you want to Edit more Evidence: (Y/N)\n').upper()
                    if(option2=='V'):
                      optionV='Y'
                      while (optionV=='Y'):
                        ID=input("Enter the ID of the Case\n").upper()
                        try:
                            case.viewAllEvidenceByCaseID(ID)
                            optionV=input('Do you want Enter Another ID? (Y/N)\n').upper()
                        except:
                            print("\t\tYou must Enter a Number\t\t")
                            print()
                            optionV=input('Do you want to try Again (Y/N)\n').upper()
                    if (option2=='Q'):
                        optionF='N'
            elif(option1=='Q'):
              optionA='N'
    #the following code is to add investigators, I had trouble inserting the investigator to a case
    # Wish I had more time to perfect that. besides everything works
    # Only regret I would of like assinging Investigator to a case by case_id, like i did with evidence.
    
    elif(option=='B'):
        optionB='Y'
        while (optionB=='Y'):
            investigator.viewInvestigators()
            print('\t\tWould You Like to do Something Else?:')
            print('V. view Investigator by ID:')
            print('A. add an Investigator:')
            print('E. edit an Investigator:')
            print('Q. Quit:')
            option3=input('select from the options(V/A/E/Q):').upper()
            if (option3=='V'):
                option3='Y'
                while (option3=='Y'):
                    ID=input(str('Enter the ID of the Investigator:\n')).upper()
                    try:
                        investigator.viewInvestigatorByID(ID)
                        optionV=input('Do you want to Enter Another ID? (Y/N)\n').upper()
                    except:
                            print("\t\tYou must Enter a Number\t\t")
                            print()
                            optionV=input('Do you want to try Again (Y/N)\n').upper()
            elif(option3=='A'):
                optionA='Y'
                while(optionA=='Y'):
                    print('you are about to add An investigator,\n Please have the ID, Name, Rank,Agency and Precint Avaliable')
                    ID=input(str('Enter the ID:\n')).upper()
                    if ID=="":
                            print('\t\tYou did not Input Information')
                            ID=input(str('Enter the  ID:\n')).upper()
                    name=input(str('Enter the name:\n'))
                    if name=="":
                        print('\t\tYou did not Input Information')
                        name=input(str('Enter The Name:\n')).upper()
                    rank=input(str('Enter the Rank:\n'))
                    if rank=="":
                       print('\t\tYou did not Input Information')
                       rank=input(str('Enter The rank:\n')).upper()
                    agency=input(str('Enter the Agency:\n')).upper()
                    if agency=="":
                       print('\t\tYou did not Input Information')
                       agency=input(str("Enter the Agency:\n")).upper()
                    precinct=input(str('Enter the Precinct:\n')).upper()
                    if precinct=="":
                       print('\t\tYou did not INput Information')
                       precinct=input(str('Enter the Precinct:\n')).upper()
                       if precinct=="":
                          print("You made too many mistakes, you will be logged off")
                          time.sleep(5)
                          exit()
                    try:
                        investigator.addInvestigator(ID,name,rank,agency,precinct)
                        optionA=input('Would you like to add another Investigator(Y/N)\n').upper()  
                    except:
                        print('\t\tYour must Enter a Number')
                        print()
                        optionA=input(str('Do you want to try againg: (Y/N)\n')).upper()
            elif(option3=='E'):
               optionE='Y'
               while(optionE=='Y'):
                    print('you are about to edit An investigator,\n Please have the ID, Name, Rank,Agency and Precint Avaliable')
                    ID=input(str('Enter the ID:\n')).upper()
                    if ID=="":
                            print('\t\tYou did not Input Information')
                            ID=input(str('Enter the  ID:\n')).upper()
                    name=input(str('Enter the name:\n')).upper()
                    if name=="":
                        print('\t\tYou did not Input Information')
                        name=input(str('Enter The Name:\n')).upper()
                    rank=input(str('Enter the Rank:\n'))
                    if rank=="":
                       print('\t\tYou did not Input Information')
                       rank=input(str('Enter The rank:\n')).upper()
                    agency=input(str('Enter the Agency:\n')).upper()
                    if agency=="":
                       print('\t\tYou did not Input Information')
                       agency=input(str("Enter the Agency:\n")).upper()
                    precinct=input(str('Enter the Precinct:\n')).upper()
                    if precinct=="":
                       print('\t\tYou did not INput Information')
                       precinct=input(str('Enter the Precinct:\n')).upper()
                       if precinct=="":
                          print("You made too many mistakes, you will be logged off")
                          time.sleep(5)
                          exit()
                    try:
                        investigator.editInvestigator(ID,name,rank,agency,precinct)
                        optionA=input('Would you like to edit another Investigator(Y/N)\n').upper()  
                    except:
                        print('\t\tYour must Enter a Number')
                        print()
                        optionA=input(str('Do you want to try againg: (Y/N)\n')).upper()
        
            elif(option3=='Q'):
                optionB='N'
                                

