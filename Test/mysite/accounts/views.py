from django.shortcuts import render, redirect
from .models import Person, Faculty, User, Exam, Registration
from django.contrib import messages
from accounts.forms import ExamSelectionForm


# Create your views here.


# Temp storage (like memory)
stored_username = ""
stored_password = ""

def create_account(request):
    message = ""
    if request.method == "POST":
        stored_username = request.POST.get("username")

        stored_password = request.POST.get("password")
        if stored_username and stored_password:
            if "@csn.edu" in stored_username:
                if "@student.csn.edu" in stored_username:
                    p = User(email = stored_username, nshe = stored_password, role = "student")
                    p.save()
                    message = "Account created successfully for " + stored_username
                else:
                    q = User(email = stored_username, nshe = stored_password, role = "faculty")
                    q.save()
                    message = "Account created successfully for " + stored_username
                return redirect("login_account")
            else:
                message = "Invalid Email"
        else:
            message = "Please enter both username and password"
    return render(request, "create_account.html", {"message": message})

def login_account(request):
    message = ""
    if request.method == "POST":
        username_input = request.POST.get("login_username")
        password_input = request.POST.get("login_password")
        if User.objects.filter(email=username_input, nshe=password_input).exists():
            message = "Login successful. Welcome back " + username_input
            request.session['user_email'] = username_input
            request.session['user_nshe'] = password_input
            return render(request, "Exam_booking.html",)
        else:
            message = "Invalid username or password. Try again."
    return render(request, "login_account.html", {"message": message})


def register_exam_view(request):
    # This assumes you're using Django's built-in auth or a session to get the user
    # Replace this with your actual user fetching logic
    user = User.objects.get(email=request.email)

    # Prevent booking more than 3 exams
    if Registration.objects.filter(email=user).count() >= 3:
        messages.error(request, "You have already booked 3 exams.")
        return render(request, "Exam_booking.html", {
            'user': user,
            'subjects': [],
            'dates': [],
            'times': [],
            'locations': []
        })

    # Fetch distinct dropdown options
    subjects = Exam.objects.values_list('subject', flat=True).distinct()
    dates = Exam.objects.values_list('date', flat=True).distinct()
    times = Exam.objects.values_list('time', flat=True).distinct()
    locations = Exam.objects.values_list('location', flat=True).distinct()

    if request.method == "POST":
        selected_subject = request.POST.get("subject")
        selected_date = request.POST.get("date")
        selected_time = request.POST.get("time")
        selected_location = request.POST.get("location")

        exam = Exam.objects.filter(
            subject=selected_subject,
            date=selected_date,
            time=selected_time,
            location=selected_location
        ).first()

        if not exam:
            messages.error(request, "Exam not found.")
        elif exam.booked >= exam.capacity:
            messages.error(request, "Selected exam session is full.")
        else:
            Registration.objects.get_or_create(email=user, exam=exam)
            exam.booked += 1
            exam.save()
            messages.success(request, "Successfully registered for the exam.")
            return redirect("register_exam")

    return render(request, "Exam_booking.html", {
        'user': user,
        'subjects': subjects,
        'dates': dates,
        'times': times,
        'locations': locations
    })