f1=open("D:\\Pythonworks\\datasets\\all_student.txt")

f2=open("D:\\Pythonworks\\datasets\\failed_students.txt")

all_students=set()

failed_students=set()

for line in f1:
    
    line=line.rstrip("\n")
    
    all_students.add(line)
    
print(all_students)

for line in f2:
    
    line=line.rstrip("\n")
    
    failed_students.add(line)
    
print(failed_students)

pass_studentts=all_students.difference(failed_students)

print(f"pass students{pass_studentts}")


f1.close()

f2.close()
