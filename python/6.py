#Input
subjects=["Mathematics","Physics","Chemistry","Biology","English"]
marks=[]
print("Enter marks for the following subjects:")
for sub in subjects:
    m=float(input(f"{sub}: "))
    marks.append(m)

#Calculation
total_marks=sum(marks)
percentage=(total_marks / 500) * 100

#Pass/Fail    
passed_all=True
for m in marks:
    if m<40:
        passed_all = False
        break
#Grading
if percentage>=90:
    grade="A+(Outstanding)"
elif percentage>=80:
    grade="A(Excellent)"
elif percentage>=70:
    grade="B(Good)"
elif percentage>=60:
    grade="C(Average)"
elif percentage>=50:
    grade="D(Pass)"
else:
    grade="F(Fail)"

#Print result
result = "Pass" if (passed_all and percentage>=50) else "Fail"

#Output
for i in range(len(subjects)):
    print(f"{subjects[i]:<12}:{marks[i]}")
print(f"Total Marks:{total_marks}/500")
print(f"Percentage:{percentage:.2f}%")
print(f"Grade:{grade}")
print(f"Final Result:{result}")
