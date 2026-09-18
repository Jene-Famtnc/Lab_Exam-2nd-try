class Student:
    def __init__(self, StudName, StudId, Course, YearLevel):
        self.StudName = StudName
        self.StudId = StudId                                     #serves as the blueprint, na naghohold ng data ng student na gagamitin para sa dynamic array
        self.Course = Course
        self.YearLevel = YearLevel

    def displayStudentinfo(self):
        print(f"Student ID: {self.StudId}")
        print(f"Student Name: {self.StudName}")                  #eto ung magdidisplay ng student info pag tinawag sa dynamic array
        print(f"Course: {self.Course}")
        print(f"Year Level: {self.YearLevel}")


class DynamicArray:          
    def __init__(self):
        self.capacity = 5                                           #this is the capacity na meron for the meantime and pag nadagdagan na ang student, tataas din ung capacity
        self.size = 0
        self.array = [None] * self.capacity


    def add(self, student):
        if self.size == self.capacity:                             #checheck muna if puno na ung array pag oo dadagdagan nya capacity pag inde continue lng sya
            self.resize()

        self.array[self.size] = student 
        self.size += 1

    def resize(self):
        old_capacity = self.capacity

        self.capacity = self.capacity * 2                                                  #ito ung gagana pag sa add eh puno na ung array kaya magdadagdag sya ng capacity
        new_array = [None] * self.capacity

        for i in range(self.size):                                                  #ilalagay nya ung laman ng old array sa new array
            new_array[i] = self.array[i]


        self.array = new_array                                                  #ito na ung magrereset ng array sa new array na may bagong capacity

        print(f"\nArray is full.")
        print(f"Capacity increased: {old_capacity} -> {self.capacity}")

    def get(self, index):
        if index < 0 or index >= self.size:             #no return if invalid pag valid rereturn ung student, ginagamit to para kunin ung student sa dynamic array
            return None

        return self.array[index]

    def set(self, index, student):
        if index < 0 or index >= self.size:             #same din sa get pero pag valid, ire-replace ung student sa index na yun sa dynamic array
            return False

        self.array[index] = student
        return True

    def remove(self, studentid):
        index = self.search(studentid)

        if index == -1:                                 #use this to check if student exists in the array, if not return false pag valid, tatanggalin ung student sa array and shift the remaining students to fill the gap
            return False

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None              

        self.size -= 1

        return True

    def search(self, studentid):
        for i in range(self.size):
            if self.array[i].StudId == studentid:      #chinecheck if nasa array ung studid na hinahanap, pag nahanap rereturn ung index ng student sa array, pag inde -1 na ung return value
                return i

        return -1

    def get_size(self):
        return self.size


    def display(self):
        if self.size == 0:
            print("\n⁂========== STUDENT RECORDS ==========⁂")                                               #tagadisplay ng student records, pag walang laman, magpi-print sya ng "No student records found."
            print("\nNo student records found.")
            return

        for i in range(self.size):
            print("\n⁂========== STUDENT RECORDS ==========⁂") 
            print(f"\nStudent {i + 1}")
            print("--------------------------------")
            self.array[i].displayStudentinfo()

students = DynamicArray()

while True:

    print("\n⁂===============================⁂")    #ito na ung main menu ng student record manager
    print("      STUDENT RECORD MANAGER")
    print("⁂===============================⁂")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")
    print("⁂===============================⁂")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n⁂========== ADD STUDENT ==========⁂")      #ito if magadd ng stud

        studentid = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        year_level = input("Enter Year Level: ")


        if students.search(studentid) != -1:
            print("\nStudent ID already exists.")               #taga check if meron ung studid sa array pag meron ito una mag priprintif hindi baba sya sa else
        else:
            new_student = Student(
                student_name,
                studentid,
                course,
                year_level
            )

            students.add(new_student)

            print("\nStudent added successfully.")


    elif choice == "2":

        students.display()          #display lng laman ng student records or if walang laman

    elif choice == "3":

        print("\n⁂========== SEARCH STUDENT ==========⁂")           #pag maghahanap ng student then display stud info pag hinde magfafall sya sa else

        studentid = input("Enter Student ID to search: ")

        index = students.search(studentid)

        if index != -1:
            print("\nStudent found!")
            print("--------------------------------")       

            student = students.get(index)
            student.displayStudentinfo()

        else:
            print("\nStudent not found.")

    elif choice == "4":                                                     

        print("\n⁂========== UPDATE STUDENT ==========⁂     ")

        studentid = input("Enter Student ID to update: ")

        index = students.search(studentid)

        if index != -1:                         # Check if student exists pag meron pwede mo na i update if hindi mapupunta sya sa else

            student = students.get(index)

            print("\nCurrent Information:")
            student.displayStudentinfo()

            print("\nEnter new information:")

            newname = input("Enter new Student Name: ")
            newourse = input("Enter new Course: ")
            newyearlevel = input("Enter new Year Level: ")

            student.StudName = newname
            student.Course = newourse
            student.YearLevel = newyearlevel

            print("\nStudent information updated successfully.")

        else:
            print("\nStudent not found.")

    elif choice == "5":

        print("\n⁂========== REMOVE STUDENT ==========⁂ ")

        studentid = input("Enter Student ID to remove: ")

        if students.remove(studentid):
            print("\nStudent removed successfully.")
        else:
            print("\nStudent not found.")


    elif choice == "6":

        print("\n⁂========== ARRAY INFORMATION ==========⁂")
        print(f"Number of Students: {students.get_size()}")
        print(f"Array Capacity: {students.capacity}")


    elif choice == "7":

        print("\nThank you for using Student Record Manager!")
        break

    else:
        print("\nInvalid choice. Please select 1-7.")