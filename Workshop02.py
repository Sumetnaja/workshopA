# 2. จงเขียนโปรแกรมPython ของโปรแกรมคำนวณหาค่าเฉลี่ยของคะแนนจากการสอบ 3 ครั้ง 
# โดยรับค่า รหัสนักเรียน ชื่อนักเรียน และคะแนนสอบแต่ละครั้งรวม 3 ครั้งทางแป้นพิมพ์ แล้วแสดงผลค่าเฉลี่ยที่คำนวณได้ทางหน้าจอ

def calculate_average(score1, score2, score3):
   return (score1 + score2 + score3) / 3

def get_student_info():
   student_id = input("กรุณาใส่รหัสนักเรียน: ")
   student_name = input("กรุณาใส่ชื่อนักเรียน: ")
   score1 = float(input("กรุณาใส่คะแนนสอบครั้งที่ 1: "))
   score2 = float(input("กรุณาใส่คะแนนสอบครั้งที่ 2: "))
   score3 = float(input("กรุณาใส่คะแนนสอบครั้งที่ 3: "))
   return student_id, student_name, score1, score2, score3

def display_result(student_id, student_name, average_score):
   print(f"รหัสนักเรียน: {student_id}")
   print(f"ชื่อนักเรียน: {student_name}")
   print(f"คะแนนเฉลี่ย: {average_score:.2f}")

student_id, student_name, score1, score2, score3 = get_student_info()
average_score = calculate_average(score1, score2, score3)
display_result(student_id, student_name, average_score)