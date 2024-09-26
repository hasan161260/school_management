from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages


@login_required(login_url='/')
def Home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_female = Student.objects.filter(gender = 'Female').count()
    student_male = Student.objects.filter(gender = 'Male').count()

    context = {
        'student_count' : student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_female' : student_female,
        'student_male' : student_male
    }

    return render(request, 'Hod/home.html', context)

@login_required(login_url='/')
def Add_Student(request):
    course = Course.objects.all()
    session_year = Session_year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course = request.POST.get('course_id')
        session_year = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')

        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            course_id = Course.objects.get(id=course)
            session_year_id = Session_year.objects.get(id=session_year) 

            student = Student(
                admin=user,
                address=address,
                gender=gender,
                course_id=course_id, 
                session_year_id=session_year_id 
            )

            student.save()

            messages.success(request, 'Student successfully added!')
            return redirect('add_student')

    context = {
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'Hod/add_student.html', context)

@login_required(login_url='/')
def View_Student(request):
    student = Student.objects.all()
    context = {
        'student' : student
    }
    return render(request, 'Hod/view_student.html', context)

@login_required(login_url='/')
def Edit_Student(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_year.objects.all()
    context = {
        'student' : student,
        'course' : course,
        'session_year': session_year
    }
    return render(request, 'Hod/edit_student.html', context)

@login_required(login_url='/')
def Update_Student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course = request.POST.get('course_id')
        session_year = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        if password != None and password != "":
            user.set_password(password)
        user.save()
        
        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course)
        student.course = course

        session_year = Session_year.objects.get(id = session_year)
        student.session_year = session_year

        student.save()
        messages.success(request, 'Student Updated Successfully!')

        return redirect('view_student')


    return render(request, 'Hod/edit_student.html')

@login_required(login_url='/')
def Delete_Student(request, admin):
    user = CustomUser.objects.get(id=admin)
    user.delete()
    messages.success(request, 'Student is deleted!')
    return redirect('view_student')

@login_required(login_url='/')
def Add_Course(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request, 'Course is successfully added!')
        return redirect('add_course')
    
    return render(request, 'Hod/add_course.html')

@login_required(login_url='/')
def View_Course(request):
    course = Course.objects.all()
    context = {
        'course' : course,
    }
    return render(request, 'Hod/view_course.html', context)

@login_required(login_url='/')
def Edit_Course(request, id):
    course = Course.objects.get(id = id)
    context = {
        'course' : course,
    }
    return render(request, 'Hod/edit_course.html', context)

@login_required(login_url='/')
def Update_Course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')
        
        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course updated successfully!')
        return redirect('view_course')

    return render(request, 'Hod/edit_course.html')

@login_required(login_url='/')
def Delete_Course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course deleted successfully!')

    return redirect('view_course')

@login_required(login_url='/')
def Add_Staff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken!')
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken!')
            return redirect('add_staff')
        
        else:
            user = CustomUser(profile_pic = profile_pic, first_name = first_name, last_name = last_name, email = email, username = username, user_type = 2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender
            )
            staff.save()
            messages.success(request, 'Staff is added successfully')
            return redirect('add_staff')

    return render(request, 'Hod/add_staff.html')

@login_required(login_url='/')
def View_Staff(request):
    staff = Staff.objects.all()
    context = {
        'staff' : staff
    }
    return render(request, 'Hod/view_staff.html', context)

@login_required(login_url='/')
def Edit_Staff(request, id):
    staff = Staff.objects.get(id = id)
    context = {
        'staff' : staff
    }
    return render(request, 'Hod/edit_staff.html', context)

@login_required(login_url='/')
def Update_Staff(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
        if password != None and password != "":
            user.set_password(password)

        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request, 'Staff is updated!')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')

@login_required(login_url='/')
def Delete_Staff(request, admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request, 'staff deleted successfully.')
    return redirect('view_staff')

@login_required(login_url='/')
def Add_Subject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff
        )
        subject.save()
        messages.success(request, 'Subject added successfully!')
        return redirect('add_subject')

    context = {
        'staff' : staff,
        'course' : course
    }
    return render(request, 'Hod/add_subject.html', context)

@login_required(login_url='/')
def View_Subject(request):
    subject = Subject.objects.all()
    context = {
        'subject' : subject
    }
    return render(request, 'Hod/view_subject.html', context)

@login_required(login_url='/')
def Edit_Subject(request, id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject' : subject,
        'course' : course,
        'staff' : staff,

    }
    return render(request, 'Hod/edit_subject.html', context)

@login_required(login_url='/')
def Update_Subject(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff = staff,
        )

        subject.save()
        messages.success(request, 'Subject updated successfully!')
        return redirect('view_subject')

@login_required(login_url='/')    
def Delete_Subject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.success(request, 'subject deleted successfully.')
    return redirect('view_subject')

@login_required(login_url='/')
def Add_Session(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session = Session_year(
            session_start = session_start,
            session_end = session_end
        )

        session.save()
        messages.success(request, 'Session year added successfully!')
        return redirect('add_session')
    return render(request, 'Hod/add_session.html')

@login_required(login_url='/')
def View_Session(request):
    session = Session_year.objects.all()
    context = {
        'session' : session
    }
    return render(request, 'Hod/view_session.html', context)

@login_required(login_url='/')
def Edit_Session(request, id):
    session = Session_year.objects.filter(id = id)
    context = {
        'session' : session
    }
    return render(request, 'Hod/edit_session.html', context)

@login_required(login_url='/')
def Update_Session(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session_year(
            session_start = session_start,
            session_end = session_end
        )

        session.save()
        messages.success(request, 'Session updated successfully!')
        return redirect('view_session')
   
@login_required(login_url='/') 
def Delete_Session(request, id):
    session = Session_year.objects.get(id = id)
    session.delete()
    messages.success(request, 'Session deleted Successfully!')
    return redirect('view_session')

def Send_Notification(request):
    staff = Staff.objects.all()
    notification = StaffNotification.objects.all()
    context = {
        'staff' : staff,
        'notification' : notification
    }
    return render(request, 'Hod/send_notification.html', context)

def Save_Notification(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification = StaffNotification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification sent successfully!')
    return redirect('send_notification')



    