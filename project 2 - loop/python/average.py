
print("calculate you degree")
print("if u want to exit just write exit")

total_course = 0
number_course = 0

while True:
     course = input(f"enter you degree numer{number_course + 1}")
     if course == "exit":
          break
     
     try:
          course = float(course)
          number_course += 1
          total_course += course
     except ValueError:
          print("print number or exit")  
          continue   
if total_course > 0 :
    print(f"your average : {total_course / number_course}")
else: 
     print("invalid input")