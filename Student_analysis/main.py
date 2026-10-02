import numpy as np
students = np.array([
    "Sant", "Gourav", 'Tanshiq', 'Happy', 'Aryan', 'jatin', 'Kartik', 'Nirmit', 'Harsh', 'Darshika'
])

subjects = np.array([
    "English", 'Hindi', 'Computer Science', 'Maths', 'Science', 'Sst'
])

marks = np.array([
    [10,50,60,76,76,98],
    [67,87,98,45,12,34],
    [68,47,35,73,67,87],
    [98,65,37,23,78,85],
    [56,36,87,96,43,87],
    [65,78,34,67,80,53],
    [30,14,29,23,27,36],
    [56,45,76,89,38,10],
    [76,46,25,80,24,85],
    [77,45,34,75,35,88]
])

attendance = np.array([
    40,67,54,89,65,89,10,56,87,97
])
print('Students  : \n',students)
print('Subjects : \n',subjects)
print('-'*100)
print('Marks Of Each Student : \n',marks)
print('-'*100)
print(np.shape(marks))
print('Total number Of Students : ',marks.shape[0])
print('Total number of Subjects : ',marks.shape[1])
print('datatype Of marks :',marks.dtype)
print('-'*100)
maxmarks=100
total_marks = np.sum(marks,axis=1)
average_marks=np.mean(marks,axis=1)
print('TOTAL MARKS OF EACH STUDENT : \n ',total_marks)
print('AVERAGE MARKS OF EACH STUDENT : \n ',average_marks)
percentage=(total_marks/(len(subjects) * maxmarks))*100
print("PERCENTAGE OF STUDENT ",percentage)
print('-------- STUDENT ANALYSIS --------')
for i in range(len(students)):
    print(
        f"{students[i]:11} | "
        f"Total : {total_marks[i]:5} | "
        f"Average : {average_marks[i]:5.2f} | "
        f"Percentge : {percentage[i]:5.2f}"
    )

#subject wise average 
subject_average = np.mean(marks,axis=0)
subject_max = np.max(marks,axis=0)
subject_min=np.min(marks,axis=0)
subject_div=np.std(marks,axis=0)

print('------------ SUBJECT ANALYSIS ---------------')

for i in range (len(subjects)):
    print(
        f"Subject : {subjects[i]} | "
        f"Average : {subject_average[i]:.2f} | "
        f"Max : {subject_max[i]} | "
        f"Min : {subject_min[i]} | "
        f"Deviation : {subject_div[i]:.2f}"
    )

grades = np.select([
    percentage>=90,
    percentage>=80,
    percentage>=70,
    percentage>=60,
    percentage>=50,
    
],
["S","A","B","C","D"], default="Fail"
)

print("\n----- Grades ------")
for name,per,grade in zip(students,percentage,grades):
    print(f"{name:8} | {per:6.2f}% | Grade : {grade}")


# index of student with max percentage
topper = np.argmax(percentage)
min_per = np.argmin(percentage)
print('Topper Index : ',topper)
print('Lowest Percentage : ',min_per)

sorted_per = np.argsort(percentage)[::-1]
print('Sorted Percentage : \n',sorted_per)
print('Topper Name : ', students[topper])
print('Topper Percentage : ',percentage[topper])
# print("top 3 Students : f"students[sorted_per[0:3]] ")
for rank,index in enumerate(sorted_per[:3],start=1):
    print(
        f"{rank} : {students[index]} | "
        f"{percentage[index]:.2f}%"
    )

print("\n---- Lowest Scoring Students ---")
print(students[min_per],percentage[min_per])
Less_60 = percentage<60
less_attendance_30 = attendance<30

Support=Less_60 | less_attendance_30
print("\n================ Students Requires Support ==================")
for i in np.where(Support)[0]:
    reason = []
    if Less_60[i]:
        reason.append("Low Marks")
    if less_attendance_30[i]:
        reason.append("Low Attendance")
    if less_attendance_30[i] & Less_60[i]:
        reason.append('Low Marks And Attendance')
    print(
        f"{students[i]} | "
        f"Percentage : {percentage[i]:.2f}% | "
        f"Attendance : {attendance[i]}% | "
        f"Reason : {', '.join(reason)}"
    )

min_marks_student = np.min(marks,axis=1)
min_marks_index = np.argmin(marks,axis=1)
print("\n======= Weakest Subject Analysis ==========")
for i in range(len(students)):
    weakest_subject = subjects[min_marks_index[i]]
    print(
        f"{students[i]:8} | "
        f"Weakest : {weakest_subject:25} | "
        f"Marks : {min_marks_student[i]}"
    )   

corr_matrix = np.corrcoef(attendance,percentage)
corelation = corr_matrix[0,1]
print('Corelation \n',corelation)
print("\n=== Attendance Correlation ===")
#print(corr_matrix)
if corelation>0:
    print("Both Attendance and Percentage  has Linear Association")
elif corelation < 0:
    print("Both Attendance and Percentaage has Negative Association")
else:
    print("No Lienaar ASsociation Detected")

unique_grades,grades_count = np.unique(
    grades,
    return_counts=True
)
print("\n===== Grade Distributions ====")
for grade,count in zip(unique_grades,grades_count):
    print(f"Grade : {grade} : {count} Students")
    

per_median=np.median(percentage)
per_med=np.median(marks,axis=0)
print('============= PERCENTAGE MEDIAN ============= \n')
print(per_median)

print('============= PERCENTAGE SUBJECT WISE MEDIAN ============= \n')
print(per_med)
