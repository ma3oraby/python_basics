# student : 
    #- add new student ----> welcome msg
    #- add marks 
    #- get marks average 

class Stusdent () : 
    def __init__ (self , name) : 
        print (f"Welcome {name}")
        self.marks = []

    def add_marks (self , mark) : 
        self.marks.append(mark)

    def get_marks_avg (self) : 
        marks_avg = sum (self.marks) / len (self.marks)
        print (f"your marks average {marks_avg}")
        


student_1 = Stusdent ('ahmed')

student_1.add_marks(50)
student_1.add_marks(60)
student_1.add_marks(55)
student_1.add_marks(45)
student_1.add_marks(40)

student_1.get_marks_avg()
