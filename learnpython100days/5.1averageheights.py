# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height = 0
for h in student_heights:
    height+=h

students = 0
for i in student_heights:
    students+=1
print(round(height/students))