
#login
from FileReadWrite import *
import sys
import linecache
import re
validation="False"
id_loop="False"
student_file="studentinfo.txt"
student_files=readFile(student_file)
new_student_list=[]
print ("_"*140)
print("(A)dmin  (S)tudent")
people='B'
while people!='A'and people!='S':
    people=input("Please enter your identity: ").upper()
    #ADMIN VIEW
    if people=='A':
        import sys
        course_codeandname ={"FHCT1012":"COMPUTING TECHNOLOGY","FHCT1014":"INTRODUCTION TO DATA ANALYTICS","FHCT1022":"PROGRAMMING CONCEPTS","FHCT1024":"PROGRAMMING CONCEPTS AND DESIGN",
                   "FHEL1012":"ENGLISH FOR ACADEMIC STUDY","FHHM1022":"EFFECTIVE COMMUNICATION SKILLS", 
                   "FHMM1014":"MATHEMATICS I","FHMM1024":"MATHEMATICS II","FHMM1034":"MATHEMATICS III",
                   "FHSB1214":"BIOLOGY I","FHSB1224":"BIOLOGY II",
                   "FHSC1014":"MECHANICS","FHSC1024":"THERMODYNAMICS AND ELECTROMAGNETISM", "FHSC1034":"WAVES AND MODERN PHYSICS",
                   "FHSC1114":"PHYSICAL CHEMISTRY","FHSC1124":"ORGANIC CHEMISTRY"}
        course_list=["FHCT1012","FHCT1014","FHCT1022","FHCT1024","FHEL1012","FHHM1022","FHMM1014","FHMM1024","FHMM1034","FHSB1214","FHSB1224","FHSC1014","FHSC1024","FHSC1034","FHSC1114","FHSC1124"]
        course_name_list=[]
        num=len(course_list)
        print ("-"*140)
        print ("UTAR CFS STUDENT CGPA Calculator")
        print ("-"*140)
        #Action
        print ("""1.Courses\n2.Student's Biodata\n3.Student CGPA calculator\n\n\n\nQ.Quit""")
        print ("-"*140)
        action=input("Action:").upper()
        print ("-"*140)
        condition="False"
        while condition == "False":
            if action == "Q":
                f=open
                print("")
                print ("Thank you!")
                sys.exit()
            #Course
            if action =="1":
                for i in range (len(course_codeandname)):
                    course_name=course_codeandname.get(course_list[i])
                    course_name_list.append(course_name)
                for code in range(len(course_list)):
                    print (code+1,"\t",end="")
                    print (course_list[code],"\t",end="")
                    print (course_name_list[code])
                print ("")
                print ("(A)dd\t(D)elete\t(Q)uit")
                print ("-"*140)
                option=input("Option:").upper()
                print ("-"*140)
                if option == "A":
                    course=input("PLease enter course code:").upper()
                    name=input("Please enter course name with'_': ").upper()
                    course_list.append(course)
                    course_name_list.append(name)
                    create="True"
                    while create == "True":
                        choice=input("Continue to (A)dd or (E)nd?:").upper()
                        if choice == "A":
                            course=input("PLease enter course code:").upper()
                            name=input("Please  enter course name:").upper()
                            course_list.append(course)
                            course_name_list.append(name)
                            create="True"
                        elif choice == "E":
                            create="False"
                        else:
                           create="True"
                           print ("Error! Please select valid option!")
                           print ("")
                elif option == "D":
                    for i in range (len(course_codeandname)):
                        course_name=course_codeandname.get(course_list[i])
                        course_name_list.append(course_name)
                    for code in range(len(course_list)):
                        print (code+1,"\t",end="")
                        print (course_list[code],"\t",end="")
                        print (course_name_list[code])
                    print ("")
                    delete_course=input("Please enter the course code you want to delete:").upper()
                    if delete_course in course_list:
                        delete_course_position=course_list.index(delete_course)
                        delete=input("Are you sure?\n(Y)es\t(N)o:").upper()
                        if delete == "Y":
                            course_list.pop(delete_course_position)
                            course_name_list.pop(delete_course_position)
                            print ("The changes have been saved!")
                            for i in range (len(course_codeandname)):
                                course_name=course_codeandname.get(course_list[i])
                                course_name_list.append(course_name)
                        elif delete == "N":
                            print ("The changes have not been saved!")
                            print ("")
                        else:
                            print ("Error! Please select valid option!")
                            print ("")
                elif option=='Q':
                    print ("Thank you!")
                    sys.exit()
                print ("")
                print ("-"*140)

            #2 Student Biodata
            elif action=="2":
                f=open("studentinfo.txt","r")
                print(f.read())
                f.close()
                condition='True'
                print ("(A)dd\t(E)dit\t\t(Q)uit")
                option=input("Option:").upper()
                if option=='A':
                    new_student_id=input("Press (0) to quit\nPlease enter new student ID (only number required):")
                    if new_student_id =="0":
                        print ("Thank you!")
                        sys.exit()
                    elif new_student_id in student_files and 999999<int(new_student_id)<=9999999:
                        print ("This student id had been registered!")
                        print ("")
                    elif new_student_id not in student_file and 999999<int(new_student_id)<=9999999:
                        stu_name=input("Please enter student name:").upper()
                        stu_NRIC=input("Please enter NRIC:").upper()
                        stu_stream=input("Please enter stream:").upper()
                        stu_ussdc=input("Please enter USSDC points (Enter NO if this student do not have participate in USSDC event):").upper()
                        YorN=input("Are you sure?\n(Y)es\t(N)o:").upper()
                        if YorN == "Y":
                            new_student_id=str(new_student_id)
                            new_student_list.append(new_student_id)
                            new_student_list.append(stu_name)
                            new_student_list.append(stu_NRIC)
                            new_student_list.append(stu_stream)
                            new_student_list.append(stu_ussdc)
                            with open("studentinfo.txt","a") as f:
                                wStr=" ".join(new_student_list)+"\n"
                                f.write(wStr)
                            new_student_list.remove(new_student_id)
                            new_student_list.remove(stu_name)
                            new_student_list.remove(stu_NRIC)
                            new_student_list.remove(stu_stream)
                            new_student_list.remove(stu_ussdc)
                            with open("coursecode.txt","a") as f:
                                new=[""]
                                new_lines=" ".join(new)+"\n"
                                f.write(new_lines)
                            with open("coursename.txt","a") as f:
                                new=[""]
                                new_lines=" ".join(new)+"\n"
                                f.write(new_lines)
                            with open("specgrade.txt","a") as f:
                                new=[""]
                                new_lines=" ".join(new)+"\n"
                                f.write(new_lines)
                            print ("New student ID have been created!")
                            print ("")
                elif option=='E':
                    cc_list=[]
                    cn_list=[]
                    cg_list=[]
                    gp_list=[]
                    stu_list=[]
                    file = open("studentinfo.txt","r")
                    course_C=open("coursecode.txt","r")
                    course_N=open("coursename.txt","r")
                    course_G=open("specgrade.txt","r")
                    course_S=open("studentinfo.txt","r")
                    student_id=input("Please insert the the student id you want to edit: ")
                    phrase = student_id
                    #find the line number of student id
                    for number, line in enumerate(file):
                      if phrase in line:
                        line_number = number
                    file.close()
                    linetoread=[line_number]
                    with open("studentinfo.txt", "r") as search:
                        for line in search:
                            if student_id in line:
                                print (line)
                    for s,line in enumerate(course_S):
                        if s in linetoread:
                            stu_list.append(line[:-1])
                            for u in range(len(stu_list)):
                                splited_info_list=(stu_list[u].split())
                    stu_info=splited_info_list
                    updatestudent=input("Student (I)D ; Student (N)ame ; N(R)IC ;(S)tream ; (U)SSDC \nPlease enter the info you want to update:").upper()
                    if updatestudent == "I":
                        print ("")
                        updateid=stu_info[0]
                        print ("Your student ID:",updateid)
                        need_to_update_id=input("Please enter the student id you prefer:").upper()
                        if updateid in stu_info:
                            updateid_position=stu_info.index(updateid)
                            print ("%s---->%s"%(updateid,need_to_update_id))
                            update_id=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_id == "Y":
                                student_id=need_to_update_id
                                stu_info.pop(updateid_position)
                                stu_info.insert(updateid_position,need_to_update_id)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("Student ID have been updated!")
                            elif update_id == "N":
                                print ("Student ID have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updateid not in stu_info:
                            print ("")
                            print ("Error! Please enter valid student ID!")

                    if updatestudent == "N":
                        print ("")
                        updatename=stu_info[1]
                        print ("Your name:",updatename)
                        need_to_update_name=input("Please enter the new name:").upper()
                        if updatename in stu_info:
                            updatename_position=stu_info.index(updatename)
                            print ("%s---->%s"%(updatename,need_to_update_name))
                            update_name=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_name == "Y":
                                stu_info.pop(updatename_position)
                                stu_info.insert(updatename_position,need_to_update_name)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("Name have been updated!")
                            elif update_name == "N":
                                print ("Name have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updatename not in stu_info:
                            print ("")
                            print ("Error! Please enter valid name!")
                    if updatestudent == "S":
                        print ("")
                        updatestream=stu_info[3]
                        print ("Your stream:",updatestream)
                        need_to_update_stream=input("Please enter the new stream:").upper()
                        if updatestream in stu_info:
                            updatestream_position=stu_info.index(updatestream)
                            print ("%s---->%s"%(updatestream,need_to_update_stream))
                            update_stream=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_stream == "Y":
                                stu_info.pop(updatestream_position)
                                stu_info.insert(updatestream_position,need_to_update_stream)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("Stream have been updated!")
                            elif update_stream == "N":
                                print ("Stream have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updatestream not in stu_info:
                            print ("")
                            print ("Error! Please enter valid stream!")
                    if updatestudent == "U":
                        print ("")
                        updateUSSDC=stu_info[4]
                        print ("Your USSDC points:",updateUSSDC)
                        need_to_update_USSDC=input("Please enter the new USSDC:").upper()
                        if updateUSSDC in stu_info:
                            updateUSSDC_position=stu_info.index(updateUSSDC)
                            print ("%s---->%s"%(updateUSSDC,need_to_update_USSDC))
                            update_USSDC=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_USSDC == "Y":
                                stu_info.pop(updateUSSDC_position)
                                stu_info.insert(updateUSSDC_position,need_to_update_USSDC)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("USSDC points have been updated!")
                            elif update_NRIC == "N":
                                print ("USSDC points  have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updateUSSDC not in stu_info:
                            print ("")
                            print ("Error! Please enter valid USSDC points!")
                elif option=='Q':
                    print ("Thank you!")
                    sys.exit()
                    
        print ("")
        print ("-"*140)
                

    #STUDENT VIEW
    elif people=='S':
        old_or_new=input("Press (0) to quit\nAre you an (E)xisting student or (N)ew student?:").upper()
        if old_or_new == "0":
            print ("Thank you!")
            sys.exit()
        while old_or_new == 1:
            old_or_new=input("Press (0) to quit\nAre you an (E)xisting student or (N)ew student?:").upper()
        while id_loop == "False":
            if old_or_new == "0":
                print ("Thank you!")
                sys.exit()
            if old_or_new != "0":
                if old_or_new == "E":
                    while old_or_new == "E":
                        student_id=input("Press (1) to back\nPlease enter valid student ID to continue (only number required):")
                        print ("")
                        validation="False"
                        if validation == "False":
                                if 999999<int(student_id)<=9999999:
                                    f=open("studentinfo.txt","r")
                                    for line in f:
                                       if student_id in line:
                                            print ("Valid student ID!")
                                            validation="True"
                                            old_or_new="Next"
                                elif student_id not in student_files and 999999<int(student_id)<=9999999:
                                    print ("Your ID is not registered in system!")
                                    print ("")
                                    validation="False"
                                elif student_id == "0":

                                    print ("Thank you!")
                                    sys.exit()
                                elif student_id == "1":
                                    old_or_new="1"
                                else:
                                    print ("Error! Please try again")
                                    print ("")
                                    validation="False"

                elif old_or_new == "N":
                    while old_or_new == "N":
                        new_student_id=input("Press (1) to back\nPlease enter new student ID (only number required):")
                        if new_student_id =="0":
                            print ("Thank you!")
                            sys.exit()
                        elif new_student_id in student_files and 999999<int(new_student_id)<=9999999:
                            print ("This student id had been registered!")
                            print ("")
                        elif new_student_id not in student_file and 999999<int(new_student_id)<=9999999:
                            stu_name=input("Please enter your name:").upper()
                            stu_NRIC=input("Please enter NRIC:").upper()
                            stu_stream=input("Please enter stream:").upper()
                            stu_ussdc=input("Please enter USSDC points (Enter NO if you do not have participate in USSDC event):").upper()
                            YorN=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if YorN == "Y":
                                new_student_id=str(new_student_id)
                                new_student_list.append(new_student_id)
                                new_student_list.append(stu_name)
                                new_student_list.append(stu_NRIC)
                                new_student_list.append(stu_stream)
                                new_student_list.append(stu_ussdc)
                                with open("studentinfo.txt","a") as f:
                                    wStr=" ".join(new_student_list)+"\n"
                                    f.write(wStr)
                                new_student_list.remove(new_student_id)
                                new_student_list.remove(stu_name)
                                new_student_list.remove(stu_NRIC)
                                new_student_list.remove(stu_stream)
                                new_student_list.remove(stu_ussdc)
                                with open("coursecode.txt","a") as f:
                                    new=[""]
                                    new_lines=" ".join(new)+"\n"
                                    f.write(new_lines)
                                with open("coursename.txt","a") as f:
                                    new=[""]
                                    new_lines=" ".join(new)+"\n"
                                    f.write(new_lines)
                                with open("specgrade.txt","a") as f:
                                    new=[""]
                                    new_lines=" ".join(new)+"\n"
                                    f.write(new_lines)
                                print ("New student ID have been created!")
                                print ("")
                                old_or_new=input("Press (0) to quit\nAre you an (E)xisting student or (N)ew student?:").upper()
                            elif YorN == "N":
                                print ("New student ID have not been created!")
                                print ("")
                            elif new_student_id == "1":
                                old_or_new=1
                            else:
                                print ("Error! Please select valid option!")
                                print("")

                        elif new_student_id == "1":
                            old_or_new=1     
                        else:
                            print ("Please enter valid ID")
                            print ("")
                elif old_or_new == "Next":
                    id_loop="True"
                elif old_or_new == "1":
                    print ("")
                    old_or_new=input("Press (0) to quit\nAre you an (E)xisting student or (N)ew student?:").upper()
                else:
                    print ("Error! Please select valid option!")
                    print("")

                    old_or_new=input("Press (0) to quit\nAre you a (E)xisting student or (N)ew student?:").upper()

        print ("-"*140)
        countline=0
        with open("studentinfo.txt", "r") as search:
            for line in search:
                if student_id in line:
                    print (line)
                countline+=1
        linenum=[]
        for s in range(countline):
            countline-=1
            linenum.append(countline)
        linenum.sort()
        phrase = student_id
        file = open("studentinfo.txt","r")
        #find the line number of student id
        for number, line in enumerate(file):
          if phrase in line:
            line_number = number
        file.close()

        print ("-"*140)

        #course
        all_grades_list={"A+":4.0,"A":4.0,"A-":3.6667,"B+":3.3333,"B":3.0,"B-":2.6667,"C+":2.3333,"C":2.0,"F":0.0}
        condition="True" 
        #Create
        print ("UTAR CFS STUDENTs' CGPA Calculator")
        print ("-"*140)
        while condition == "True":
            print ("-"*140)
            totalcp=0
            totalch=0
            cc_list=[]
            cn_list=[]
            cg_list=[]
            gp_list=[]
            linetoread=[line_number]
            course_C=open("coursecode.txt","r")
            course_N=open("coursename.txt","r")
            course_G=open("specgrade.txt","r")
            for u,line in enumerate(course_C):
                if u in linetoread:
                    cc_list.append(line[:-1])
                    for y in range(len(cc_list)):
                        splited_code=(cc_list[y].split())
            for u,line in enumerate(course_N):
                if u in linetoread:
                    cn_list.append(line[:-1])
                    for m in range(len(cn_list)):
                        splited_name=(cn_list[m].split())
            for u,line in enumerate(course_G):
                if u in linetoread:
                    cg_list.append(line[:-1])
                    for n in range(len(cg_list)):
                        splited_grade=(cg_list[n].split())
                        for w in range (len(splited_grade)):
                            print (w+1,"\t",end="")
                            print(splited_code[w],end='')
                            print('\t',end='')
                            print(splited_name[w],end='')
                            print(' >>>',end='')
                            print(splited_grade[w],end='')
                            print(' ',end='')
                            grade_point=(all_grades_list.get(splited_grade[w]))#get grade point
                            gp_list.append(grade_point)
                            print("%.4f"%grade_point)
                            credithour=(splited_code[w][-1])#get credit hour
                            gp_course=grade_point*int(credithour)
                            totalcp+=gp_course
                            totalch+=int(credithour)
                            if grade_point==max(gp_list):
                                bestcode=splited_code[w]
                                bestname=splited_name[w]                          
            cgpa=totalcp/totalch
            print("")
            print("TOTAL GRADE POINT=%.4f"%totalcp,'\t',end='')
            print("TOTAL CREDIT HOUR=%d"%totalch,'\t',end='')
            print("TOTAL CGPA=%.4f"%cgpa,'\t',end='')
            leftch=50-(totalch)
            if leftch>0:
                print("You have left %d CREDIT HOURS hours to graduate"%leftch)
            elif leftch<=0:
                print("You had gained enough CREDIT HOUR to graduate!")
            print("BEST PERFORMANCE COURSE= %s %s"%(bestcode,bestname))
            if cgpa>=3.6:
                print("*ACADEMIC ACHIEVEMENT*: DEAN'S LIST")
            elif cgpa==4.0:
                print("*ACADEMIC ACHIEVEMENT*: PRESIDENT'S LIST")
            else:
                print("*ACADEMIC ACHIEVEMENT*: NONE")
            course_N.close()
            course_C.close()
            course_G.close()
            print('')
            action=input("(C)reate (U)pdate (D)elete (Q)uit\nPlease select an action:").upper()
            condition="True"
            if action == "C":
                print ("-"*140)
                course=input("PLease enter course code:").upper()
                name=input("Please enter course name with '_':").upper()
                grade=input("Please enter course grade:").upper()
                YesorNo=input("Are you sure?\n(Y)es\t(N)o:").upper()
                if YesorNo == "Y":
                    with open("coursecode.txt","r") as course_C:
                        lines1=course_C.readlines()
                    with open("coursename.txt","r") as course_N:
                        lines2=course_N.readlines()
                    with open("specgrade.txt","r") as course_G:
                        lines3=course_G.readlines()
                    writetoendofline(lines1,line_number, " ")
                    writetoendofline(lines2,line_number, " ")
                    writetoendofline(lines3,line_number, " ")
                    with open("coursecode.txt","w") as course_C:
                        course_C.writelines(lines1)
                    with open("coursename.txt","w") as course_N:
                        course_N.writelines(lines2)
                    with open("specgrade.txt","w") as course_G:
                        course_G.writelines(lines3)
                    writetoendofline(lines1,line_number, course)
                    writetoendofline(lines2,line_number, name)
                    writetoendofline(lines3,line_number, grade)
                    with open("coursecode.txt","w") as course_C:
                        course_C.writelines(lines1)
                    with open("coursename.txt","w") as course_N:
                        course_N.writelines(lines2)
                    with open("specgrade.txt","w") as course_G:
                        course_G.writelines(lines3)
                    print ("New course have been registered!")
                    print ("")
                elif YesorNo == "N":
                    print ("Course have not been registered!")
                    print ("")
                elif YesorNo == "1":
                    condition="True"
                else:
                    print ("Error! Please select valid option!")
                    print("")
                create="True"
                while create == "True":
                    option=input("Continue to (A)dd or (E)nd?:").upper()
                    if option == "A":
                        course=input("PLease enter course code:").upper()
                        name=input("Please enter course name with '_':").upper()
                        grade=input("Please enter course grade:").upper()
                        YesorNo=input("Are you sure?\n(Y)es\t(N)o:").upper()
                        if YesorNo == "Y":
                            with open("coursecode.txt","r") as course_C:
                                lines1=course_C.readlines()
                            with open("coursename.txt","r") as course_N:
                                lines2=course_N.readlines()
                            with open("specgrade.txt","r") as course_G:
                                lines3=course_G.readlines()
                            writetoendofline(lines1,line_number, " ")
                            writetoendofline(lines2,line_number, " ")
                            writetoendofline(lines3,line_number, " ")
                            with open("coursecode.txt","w") as course_C:
                                course_C.writelines(lines1)
                            with open("coursename.txt","w") as course_N:
                                course_N.writelines(lines2)
                            with open("specgrade.txt","w") as course_G:
                                course_G.writelines(lines3)
                            writetoendofline(lines1,line_number, course)
                            writetoendofline(lines2,line_number, name)
                            writetoendofline(lines3,line_number, grade)
                            with open("coursecode.txt","w") as course_C:
                                course_C.writelines(lines1)
                            with open("coursename.txt","w") as course_N:
                                course_N.writelines(lines2)
                            with open("specgrade.txt","w") as course_G:
                                course_G.writelines(lines3)
                            print ("Course have been registered!")
                            print ("")
                        elif YesorNo == "N":
                            print ("Course have not been registered!")
                            print ("")
                        else:
                            print ("Error! Please select valid option!")
                            print("")
                    elif option == "E":
                        YesorNo=input("Are you sure?\n(Y)es\t(N)o:").upper()
                        if YesorNo == "Y":
                            print ("Thank you!")
                            create="False"
                        elif YesorNo == "N":
                            print ("")
                            create="True"
                        else:
                            print ("Error! Please select valid option!")
                            print("")
                    else:
                       create="True"
                       print ("Error! Please select valid option!")
                       print ("")
        #Update
            elif action == "U":
                f=open("coursecode.txt","r")
                read=f.readlines()
                if read[line_number] == "\n":
                    print ("Error!You does not have any registered course!")
                    print ("")
                else:
                    print ("-"*140)
                    totalcp=0
                    totalch=0
                    cc_list=[]
                    cn_list=[]
                    cg_list=[]
                    gp_list=[]
                    stu_list=[]
                    linetoread=[line_number]
                    course_C=open("coursecode.txt","r")
                    course_N=open("coursename.txt","r")
                    course_G=open("specgrade.txt","r")
                    course_S=open("studentinfo.txt","r")
                    for u,line in enumerate(course_C):
                        if u in linetoread:
                            cc_list.append(line[:-1])
                            for y in range(len(cc_list)):
                                splited_code=(cc_list[y].split())
                    for u,line in enumerate(course_N):
                        if u in linetoread:
                            cn_list.append(line[:-1])
                            for m in range(len(cn_list)):
                                splited_name=(cn_list[m].split())
                    for u,line in enumerate(course_G):
                        if u in linetoread:
                            cg_list.append(line[:-1])
                            for n in range(len(cg_list)):
                                splited_grade=(cg_list[n].split())
                                for w in range (len(splited_grade)):
                                    print (w+1,"\t",end="")
                                    print(splited_code[w],end='')
                                    print('\t',end='')
                                    print(splited_name[w],end='')
                                    print(' >>>',end='')
                                    print(splited_grade[w],end='')
                                    print(' ',end='')
                                    grade_point=(all_grades_list.get(splited_grade[w]))#get grade point
                                    gp_list.append(grade_point)
                                    print("%.4f"%grade_point)
                                    credithour=(splited_code[w][-1])#get credit hour
                                    gp_course=grade_point*int(credithour)
                                    totalcp+=gp_course
                                    totalch+=int(credithour)
                                    if grade_point==max(gp_list):
                                        bestcode=splited_code[w]
                                        bestname=splited_name[w]                          
                    cgpa=totalcp/totalch
                    print("")
                    print("TOTAL GRADE POINT=%.4f"%totalcp,'\t',end='')
                    print("TOTAL CREDIT HOUR=%d"%totalch,'\t',end='')
                    print("TOTAL CGPA=%.4f"%cgpa,'\t',end='')
                    leftch=50-(totalch)
                    if leftch>0:
                        print("You have left %d CREDIT HOURS hours to graduate"%leftch)
                    elif leftch<=0:
                        print("You had gained enough CREDIT HOUR to graduate!")
                    print("BEST PERFORMANCE COURSE= %s %s"%(bestcode,bestname))
                    if cgpa>=3.6:
                        print("*ACADEMIC ACHIEVEMENT*: DEAN'S LIST")
                    elif cgpa==4.0:
                        print("*ACADEMIC ACHIEVEMENT*: PRESIDENT'S LIST")
                    else:
                        print("*ACADEMIC ACHIEVEMENT*: NONE")
                    course_N.close()
                    course_C.close()
                    course_G.close()
                    print('')
                update=input("(C)ourse  (S)tudent\nPlease enter the info you want to update:").upper()
                if update == "C":
                    for cc in range(len(cc_list)):
                        c_code=(cc_list[cc].split(" "))
                    for cn in range(len(cn_list)):
                        c_name=(cn_list[cn].split(" "))
                    for cg in range(len(cg_list)):
                        c_grade=(cg_list[cg].split(" "))
                    print ("")
                    updatecourse=input("Course (C)ode;Course (N)ame;Course (G)rade\nPlease enter the info you want to update:").upper()
                    if updatecourse == "C":
                        print ("")
                        updatecode=input("Please enter the course code you want to update:").upper()
                        need_to_update_code=input("Please enter the course code you prefer:").upper()
                        if updatecode in c_code:
                            updatecode_position=c_code.index(updatecode)
                            print ("%s---->%s"%(updatecode,need_to_update_code))
                            update_code=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_code == "Y":
                                c_code.pop(updatecode_position)
                                c_code.insert(updatecode_position,need_to_update_code)
                                with open('coursecode.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('coursecode.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(c_code)):
                                    with open("coursecode.txt","r") as course_C:
                                        lines1=course_C.readlines()
                                    writetoendofline(lines1,line_number, c_code[i])
                                    with open("coursecode.txt","w") as course_C:
                                        course_C.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("coursecode.txt","w") as course_C:
                                        course_C.writelines(lines1)
                            if update_code == "N":
                                print ("Course code have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updatecode not in c_code:
                            print ("")
                            print ("Error! Please enter valid course code!")
                    
                    elif updatecourse == "N":
                        print ("")
                        updatename=input("Please enter the course name with '_' that you want to update:").upper()
                        need_to_update_name=input("Please enter the course name you prefer:").upper()
                        if updatename in c_name:
                            updatename_position=c_name.index(updatename)
                            print ("%s---->%s"%(updatename,need_to_update_name))
                            update_name=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_name == "Y":
                                c_name.pop(updatename_position)
                                c_name.insert(updatename_position,need_to_update_name)
                                with open('coursename.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('coursename.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(c_name)):
                                    with open("coursename.txt","r") as course_N:
                                        lines1=course_N.readlines()
                                    writetoendofline(lines1,line_number, c_name[i])
                                    with open("coursename.txt","w") as course_N:
                                        course_N.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("coursename.txt","w") as course_N:
                                        course_N.writelines(lines1)
                            if update_name == "N":
                                print ("Course name have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updatename not in c_name:
                            print ("")
                            print ("Error! Please enter valid course name!")
                    
                    elif updatecourse == "G":
                        print ("")
                        updategrade=input("Please enter the course grade you want to update:").upper()
                        need_to_update_grade=input("Please enter the course grade you prefer:").upper()
                        if updategrade in c_grade:
                            updategrade_position=c_grade.index(updategrade)
                            print ("%s---->%s"%(updategrade,need_to_update_grade))
                            update_grade=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_grade == "Y":
                                c_grade.pop(updategrade_position)
                                c_grade.insert(updategrade_position,need_to_update_grade)
                                with open('coursegrade.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('coursegrade.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(c_grade)):
                                    with open("coursegrade.txt","r") as course_G:
                                        lines1=course_G.readlines()
                                    writetoendofline(lines1,line_number, c_grade[i])
                                    with open("coursegrade.txt","w") as course_G:
                                        course_G.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("coursegrade.txt","w") as course_G:
                                        course_G.writelines(lines1)
                            if update_grade == "N":
                                print ("Course grade have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updategrade not in c_grade:
                            print ("")
                            print ("Error! Please enter valid course grade!")
            
                    else:
                        print ("")
                        print ("Error! Please enter valid option!")
                
                if update == "S":
                    print ("")
                    with open("studentinfo.txt", "r") as search:
                        for line in search:
                            if student_id in line:
                                print (line)
                    for s,line in enumerate(course_S):
                        if s in linetoread:
                            stu_list.append(line[:-1])
                            for u in range(len(stu_list)):
                                splited_info_list=(stu_list[u].split())
                    stu_info=splited_info_list
                    updatestudent=input("Student (I)D ; Student (N)ame ; N(R)IC ;(S)tream ; (U)SSDC \nPlease enter the info you want to update:").upper()
                    if updatestudent == "I":
                        print ("")
                        updateid=stu_info[0]
                        print ("Your student ID:",updateid)
                        need_to_update_id=input("Please enter the student id you prefer:").upper()
                        if updateid in stu_info:
                            updateid_position=stu_info.index(updateid)
                            print ("%s---->%s"%(updateid,need_to_update_id))
                            update_id=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_id == "Y":
                                student_id=need_to_update_id
                                stu_info.pop(updateid_position)
                                stu_info.insert(updateid_position,need_to_update_id)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("Student ID have been updated!")
                            elif update_id == "N":
                                print ("Student ID have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updateid not in stu_info:
                            print ("")
                            print ("Error! Please enter valid student ID!")

                    if updatestudent == "N":
                        print ("")
                        updatename=stu_info[1]
                        print ("Your name:",updatename)
                        need_to_update_name=input("Please enter the new name:").upper()
                        if updatename in stu_info:
                            updatename_position=stu_info.index(updatename)
                            print ("%s---->%s"%(updatename,need_to_update_name))
                            update_name=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_name == "Y":
                                stu_info.pop(updatename_position)
                                stu_info.insert(updatename_position,need_to_update_name)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("Name have been updated!")
                            elif update_name == "N":
                                print ("Name have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updatename not in stu_info:
                            print ("")
                            print ("Error! Please enter valid name!")
                    if updatestudent == "S":
                        print ("")
                        updatestream=stu_info[3]
                        print ("Your stream:",updatestream)
                        need_to_update_stream=input("Please enter the new stream:").upper()
                        if updatestream in stu_info:
                            updatestream_position=stu_info.index(updatestream)
                            print ("%s---->%s"%(updatestream,need_to_update_stream))
                            update_stream=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_stream == "Y":
                                stu_info.pop(updatestream_position)
                                stu_info.insert(updatestream_position,need_to_update_stream)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("Stream have been updated!")
                            elif update_stream == "N":
                                print ("Stream have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updatestream not in stu_info:
                            print ("")
                            print ("Error! Please enter valid stream!")
                    if updatestudent == "U":
                        print ("")
                        updateUSSDC=stu_info[4]
                        print ("Your USSDC points:",updateUSSDC)
                        need_to_update_USSDC=input("Please enter the new USSDC:").upper()
                        if updateUSSDC in stu_info:
                            updateUSSDC_position=stu_info.index(updateUSSDC)
                            print ("%s---->%s"%(updateUSSDC,need_to_update_USSDC))
                            update_USSDC=input("Are you sure?\n(Y)es\t(N)o:").upper()
                            if update_USSDC == "Y":
                                stu_info.pop(updateUSSDC_position)
                                stu_info.insert(updateUSSDC_position,need_to_update_USSDC)
                                with open('studentinfo.txt', 'r') as file:
                                    data = file.readlines()
                                data[line_number] ='\n'
                                with open('studentinfo.txt', 'w') as file:
                                    file.writelines(data)
                                for i in range (len(stu_info)):
                                    with open("studentinfo.txt","r") as course_S:
                                        lines1=course_S.readlines()
                                    writetoendofline(lines1,line_number, stu_info[i])
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                    writetoendofline(lines1,line_number," ")
                                    with open("studentinfo.txt","w") as course_S:
                                        course_S.writelines(lines1)
                                print ("USSDC points have been updated!")
                            elif update_NRIC == "N":
                                print ("USSDC points  have not been updated!")
                            else:
                                print ("Error! Please select valid option!")
                        elif updateUSSDC not in stu_info:
                            print ("")
                            print ("Error! Please enter valid USSDC points!")
            

            
        #Delete           
            elif action == "D":
                f=open("coursecode.txt","r")
                read=f.readlines()
                if read[line_number] == "\n":
                    print ("Error!You does not have any registered course!")
                    print ("")
                else:
                    print ("-"*140)
                    totalcp=0
                    totalch=0
                    cc_list=[]
                    cn_list=[]
                    cg_list=[]
                    gp_list=[]
                    linetoread=[line_number]
                    course_C=open("coursecode.txt","r")
                    course_N=open("coursename.txt","r")
                    course_G=open("specgrade.txt","r")
                    for u,line in enumerate(course_C):
                        if u in linetoread:
                            cc_list.append(line[:-1])
                            for y in range(len(cc_list)):
                                splited_code=(cc_list[y].split())
                    for u,line in enumerate(course_N):
                        if u in linetoread:
                            cn_list.append(line[:-1])
                            for m in range(len(cn_list)):
                                splited_name=(cn_list[m].split())
                    for u,line in enumerate(course_G):
                        if u in linetoread:
                            cg_list.append(line[:-1])
                            for n in range(len(cg_list)):
                                splited_grade=(cg_list[n].split())
                                for w in range (len(splited_grade)):
                                    print (w+1,"\t",end="")
                                    print(splited_code[w],end='')
                                    print('\t',end='')
                                    print(splited_name[w],end='')
                                    print(' >>>',end='')
                                    print(splited_grade[w],end='')
                                    print(' ',end='')
                                    grade_point=(all_grades_list.get(splited_grade[w]))#get grade point
                                    gp_list.append(grade_point)
                                    print("%.4f"%grade_point)
                                    credithour=(splited_code[w][-1])#get credit hour
                                    gp_course=grade_point*int(credithour)
                                    totalcp+=gp_course
                                    totalch+=int(credithour)
                                    if grade_point==max(gp_list):
                                        bestcode=splited_code[w]
                                        bestname=splited_name[w]                          
                    cgpa=totalcp/totalch
                    print("")
                    print("TOTAL GRADE POINT=%.4f"%totalcp,'\t',end='')
                    print("TOTAL CREDIT HOUR=%d"%totalch,'\t',end='')
                    print("TOTAL CGPA=%.4f"%cgpa,'\t',end='')
                    leftch=50-(totalch)
                    if leftch>0:
                        print("You have left %d CREDIT HOURS hours to graduate"%leftch)
                    elif leftch<=0:
                        print("You had gained enough CREDIT HOUR to graduate!")
                    print("BEST PERFORMANCE COURSE= %s %s"%(bestcode,bestname))
                    if cgpa>=3.6:
                        print("*ACADEMIC ACHIEVEMENT*: DEAN'S LIST")
                    elif cgpa==4.0:
                        print("*ACADEMIC ACHIEVEMENT*: PRESIDENT'S LIST")
                    else:
                        print("*ACADEMIC ACHIEVEMENT*: NONE")
                    course_N.close()
                    course_C.close()
                    course_G.close()
                    print('')
                    delete_course=input("Press (1) to back\nPlease enter the course code you want to delete:").upper()
                    for cc in range(len(cc_list)):
                        c_code=(cc_list[cc].split(" "))
                    for cn in range(len(cn_list)):
                        c_name=(cn_list[cn].split(" "))
                    for cg in range(len(cg_list)):
                        c_grade=(cg_list[cg].split(" "))
                    if delete_course in c_code:
                        delete_course_position=c_code.index(delete_course)
                        delete=input("Are you sure?\n(Y)es\t(N)o:").upper()
                        if delete == "Y":
                            c_code.pop(delete_course_position)
                            c_name.pop(delete_course_position)
                            c_grade.pop(delete_course_position)
                            # with is like your try .. finally block in this case
                            with open('coursecode.txt', 'r') as file:
                            # read a list of lines into data
                                data = file.readlines()
                            data[line_number] ='\n'
                            # and write everything back
                            with open('coursecode.txt', 'w') as file:
                                file.writelines(data)
                            for i in range (len(c_code)):
                                with open("coursecode.txt","r") as course_C:
                                    lines1=course_C.readlines()
                                writetoendofline(lines1,line_number, c_code[i])
                                with open("coursecode.txt","w") as course_C:
                                    course_C.writelines(lines1)
                                writetoendofline(lines1,line_number," ")
                                with open("coursecode.txt","w") as course_C:
                                    course_C.writelines(lines1)
                            # with is like your try .. finally block in this case
                            with open('coursename.txt', 'r') as file:
                            # read a list of lines into data
                                data2 = file.readlines()
                            data2[line_number] ='\n'
                            # and write everything back
                            with open('coursename.txt', 'w') as file:
                                file.writelines(data2)
                            for i in range (len(c_name)):
                                with open("coursename.txt","r") as course_N:
                                    lines2=course_N.readlines()
                                writetoendofline(lines2,line_number, c_name[i])
                                with open("coursename.txt","w") as course_N:
                                    course_N.writelines(lines2)
                                writetoendofline(lines2,line_number," ")
                                with open("coursename.txt","w") as course_N:
                                    course_N.writelines(lines2)
                            # with is like your try .. finally block in this case
                            with open('specgrade.txt', 'r') as file:
                            # read a list of lines into data
                                data3 = file.readlines()
                            data3[line_number] ='\n'
                            # and write everything back
                            with open('specgrade.txt', 'w') as file:
                                file.writelines(data3)
                            for i in range (len(c_grade)):
                                with open("specgrade.txt","r") as course_G:
                            
                                    lines3=course_G.readlines()
                                writetoendofline(lines3,line_number, c_grade[i])
                                with open("specgrade.txt","w") as course_G:
                                    course_G.writelines(lines3)
                                writetoendofline(lines3,line_number," ")
                                with open("specgrade.txt","w") as course_G:
                                    course_G.writelines(lines3)
                            print ("")
                        elif delete == "N":
                            print ("The changes have not been saved!")
                            print ("")
                        else:
                            print ("Error! Please select valid option!")
                            print ("")
                    elif delete_course == "1":
                        condition="True"
                        print ("")
                
                    else:
                        print ("Error! Please enter valid course!")
                        print( "")

        #Quit
    
            elif action == "Q":
                condition="False"
                print ("Thank you!")
                sys.exit()

        #Error
            elif option == "E":
                print ("")
            else:
                print ("Error! Please select valid action!")
                print ("")
    else:
        print("ERROR! Please enter valid option")
        
    
  
        
       
    
    

