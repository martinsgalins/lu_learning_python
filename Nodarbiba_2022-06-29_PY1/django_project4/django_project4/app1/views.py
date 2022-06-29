from django.shortcuts import render, HttpResponse
from app1.forms import AddStudentForm
from app1.models import StudentModel


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades= list(map(int, grades.split(',')))
        
    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade 


def add_student(request):
    form = AddStudentForm(request.POST or None)
    if form.is_valid():
        student = Student(name=form.cleaned_data['name'],
                        grades=form.cleaned_data['grades'])
                        
        db_student = StudentModel(name = student.name,
                                  grades=student.grades,
                                  average_grade=student.get_average_grade())
        db_student.save()

        context = {
            'student': db_student,
        }

        return render(request,
                      template_name='student.html',
                      context=context)

    context = {
        'form': form,
    }

    return render(request,
                  template_name='add_student.html',
                  context=context)




def get_all_students(request):
    context = {
        'Students': StudentModel.objects.all()
    }

    return render(request,
                  template_name='all_students.html',
                  context=context)

def get_student(request, student_id):
    context = {
        'student': StudentModel.objects.get(id=student_id)
    }

    return render(request,
                  template_name='get_student.html',
                  context=context)
