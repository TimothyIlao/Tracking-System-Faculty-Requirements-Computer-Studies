import sqlite3 
import os

folder = r'D:\School purposes (Codes)\Project DCIT-55A\Database'
os.makedirs(folder, exist_ok=True)
db_path = os.path.join(folder, "Facultylist.db")
print("Database path:", db_path)
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

#TEACHERS TABLE
Teacher_Info = ("CREATE TABLE IF NOT EXISTS TEACHERS (Emp_ID INT, First_Name TEXT NOT NULL, Last_Name TEXT NOT NULL, Email TEXT)")
cursor.execute(Teacher_Info)
connection.commit()

cursor.execute ("INSERT INTO TEACHERS (Emp_ID, First_Name, Last_Name, Email) VALUES (?, ?, ?, ?)", (1, "Ron Daniel", "Raymundo", "una.apelido@gmail.com"))
cursor.execute ("INSERT INTO TEACHERS (Emp_ID, First_Name, Last_Name, Email) VALUES (?, ?, ?, ?)", (2, "Christian Luke", "Zabala", "pangalawa.apelido@gmail.com"))
cursor.execute ("INSERT INTO TEACHERS (Emp_ID, First_Name, Last_Name, Email) VALUES (?, ?, ?, ?)", (3, "Aldrin Royce", "Aquino", "tatlo.apelido@gmail.com"))
cursor.execute ("INSERT INTO TEACHERS (Emp_ID, First_Name, Last_Name, Email) VALUES (?, ?, ?, ?)", (4, "Ben", "Marquez", "apat.apelido@gmail.com"))
cursor.execute ("INSERT INTO TEACHERS (Emp_ID, First_Name, Last_Name, Email) VALUES (?, ?, ?, ?)", (5, "Timotheo James", "Ilao", "lima.apelido@gmail.com"))
connection.commit()

cursor.execute("SELECT * FROM TEACHERS")

Sections = ("CREATE TABLE IF NOT EXISTS SECTIONS (Section_ID INT, Section_Name TEXT NOT NULL, Semester TEXT, Faculty_ID INTEGER, FOREIGN KEY (Faculty_ID) REFERENCES TEACHERS(Emp_ID))")
cursor.execute(Sections)
connection.commit()

#SECTION TABLE
cursor.execute ("INSERT INTO SECTIONS (Section_ID, Section_Name, Semester, Faculty_ID) VALUES (?, ?, ?, ?)", (1, "BSCS-1A", "2025-2026", 1))
cursor.execute ("INSERT INTO SECTIONS (Section_ID, Section_Name, Semester, Faculty_ID) VALUES (?, ?, ?, ?)", (2, "BSCS-1B", "2025-2026", 2))
cursor.execute ("INSERT INTO SECTIONS (Section_ID, Section_Name, Semester, Faculty_ID) VALUES (?, ?, ?, ?)", (3, "BSCS-1C", "2025-2026", 3))
cursor.execute ("INSERT INTO SECTIONS (Section_ID, Section_Name, Semester, Faculty_ID) VALUES (?, ?, ?, ?)", (4, "BSCS-1D", "2025-2026", 4))
connection.commit()

Subjects = ("CREATE TABLE IF NOT EXISTS SUBJECTS (Subject_ID INT, Subject_Name TEXT)")
cursor.execute(Subjects)
connection.commit()
#SUBJECTS TABLE
cursor.execute ("INSERT INTO SUBJECTS (Subject_ID, Subject_Name) VALUES (?, ?)", (1, "COSC 50A"))
cursor.execute ("INSERT INTO SUBJECTS (Subject_ID, Subject_Name) VALUES (?, ?)", (2, "DCIT 21A"))
cursor.execute ("INSERT INTO SUBJECTS (Subject_ID, Subject_Name) VALUES (?, ?)", (3, "DCIT 22A"))
cursor.execute ("INSERT INTO SUBJECTS (Subject_ID, Subject_Name) VALUES (?, ?)", (4, "DCIT 23A"))
cursor.execute ("INSERT INTO SUBJECTS (Subject_ID, Subject_Name) VALUES (?, ?)", (5, "ITEC 50A"))
connection.commit()

#TEACHING LOAD TABLE
Teaching_Load = ("CREATE TABLE IF NOT EXISTS TEACHING_LOAD (Load_ID INT, Faculty_ID INTEGER, Section_ID INTEGER, Subject_ID INTEGER, FOREIGN KEY (Faculty_ID) REFERENCES TEACHERS(Emp_ID), FOREIGN KEY (Section_ID) REFERENCES SECTIONS(Section_ID), FOREIGN KEY (Subject_ID) REFERENCES SUBJECTS(Subject_ID))")
cursor.execute(Teaching_Load)
connection.commit()

#TEACHER 1
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (1, 1, 1, 1))
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (2, 1, 2, 2))
#TEACHER 2
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (3, 2, 3, 3))
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (4, 2, 4, 4))
#TEACHER 3
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (5, 3, 2, 5))
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (6, 3, 4, 3))
#TEACHER 4
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (7, 4, 1, 2))
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (8, 4, 4, 4))
#TEACHER 5
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (9, 5, 2, 5))
cursor.execute ("INSERT INTO TEACHING_LOAD (Load_ID, Faculty_ID, Section_ID, Subject_ID) VALUES (?, ?, ?, ?)", (10, 5, 3, 5))
connection.commit()

#REQUIREMENTS TABLE
Requirements = ("CREATE TABLE IF NOT EXISTS REQUIREMENTS (Requirement_ID INT, Requirement_Name TEXT NOT NULL)")
cursor.execute(Requirements)
connection.commit()

cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (1, "Grade Sheet"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (2, "Exam"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (3, "Major Exam"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (4, "Finals"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (5, "Midterms"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (6, "Class Record"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (7, "Portfolio"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (8, "Sample Quiz"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (9, "Sample Exam"))
cursor.execute ("INSERT INTO REQUIREMENTS (Requirement_ID, Requirement_Name) VALUES (?, ?)", (10, "Core syllabus"))      
connection.commit()   

#SUBMISSION TABLE
Submission = ("CREATE TABLE IF NOT EXISTS SUBMISSION (Submission_ID INT, Load_ID INTEGER, Requirement_ID INTEGER, Submission_Date TEXT, Status TEXT, FOREIGN KEY (Load_ID) REFERENCES TEACHING_LOAD(Load_ID), FOREIGN KEY (Requirement_ID) REFERENCES REQUIREMENTS(Requirement_ID))")  
cursor.execute(Submission)
connection.commit()

# TEACHER 1 - Load_ID 1
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (1, 1, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (2, 1, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (3, 1, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (4, 1, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (5, 1, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (6, 1, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (7, 1, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (8, 1, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (9, 1, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (10, 1, 10, "2026-06-23", "Not Submitted"))

# TEACHER 1 - Load_ID 2
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (11, 2, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (12, 2, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (13, 2, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (14, 2, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (15, 2, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (16, 2, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (17, 2, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (18, 2, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (19, 2, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (20, 2, 10, "2026-06-23", "Not Submitted"))

# TEACHER 2 - Load_ID 3
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (21, 3, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (22, 3, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (23, 3, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (24, 3, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (25, 3, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (26, 3, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (27, 3, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (28, 3, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (29, 3, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (30, 3, 10, "2026-06-23", "Not Submitted"))

# TEACHER 2 - Load_ID 4
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (31, 4, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (32, 4, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (33, 4, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (34, 4, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (35, 4, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (36, 4, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (37, 4, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (38, 4, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (39, 4, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (40, 4, 10, "2026-06-23", "Not Submitted"))

# TEACHER 3 - Load_ID 5
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (41, 5, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (42, 5, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (43, 5, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (44, 5, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (45, 5, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (46, 5, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (48, 5, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (50, 5, 10, "2026-06-23", "Not Submitted"))

# TEACHER 3 - Load_ID 6
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (51, 6, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (52, 6, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (53, 6, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (54, 6, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (55, 6, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (56, 6, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (57, 6, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (58, 6, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (59, 6, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (60, 6, 10, "2026-06-23", "Not Submitted"))

# TEACHER 4 - Load_ID 7
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (61, 7, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (62, 7, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (63, 7, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (64, 7, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (65, 7, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (66, 7, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (67, 7, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (68, 7, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (69, 7, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (70, 7, 10, "2026-06-23", "Not Submitted"))

# TEACHER 4 - Load_ID 8
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (71, 8, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (72, 8, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (73, 8, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (74, 8, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (75, 8, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (76, 8, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (77, 8, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (78, 8, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (79, 8, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (80, 8, 10, "2026-06-23", "Not Submitted"))

# TEACHER 5 - Load_ID 9
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (81, 9, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (82, 9, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (83, 9, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (84, 9, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (85, 9, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (86, 9, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (87, 9, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (88, 9, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (89, 9, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (90, 9, 10, "2026-06-23", "Not Submitted"))

# TEACHER 5 - Load_ID 10
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (91, 10, 1, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (92, 10, 2, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (93, 10, 3, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (94, 10, 4, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (95, 10, 5, "2026-03-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (96, 10, 6, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (97, 10, 7, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (98, 10, 8, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (99, 10, 9, "2026-06-23", "Not Submitted"))
cursor.execute("INSERT INTO SUBMISSION (Submission_ID, Load_ID, Requirement_ID, Submission_Date, Status) VALUES (?, ?, ?, ?, ?)", (100, 10, 10, "2026-06-23", "Not Submitted"))
connection.commit()

connection.close()