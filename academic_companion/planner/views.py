from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Assignment, ClassSchedule
from .forms import AssignmentForm, ClassScheduleForm, ReminderForm
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView



def home(request):
    return render(request, 'planner/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or redirect to a dashboard
        else:
            return render(request, 'planner/login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'planner/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')




def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not email:
            return render(request, 'planner/register.html', {'error': 'Email is required'})

        if password1 != password2:
            return render(request, 'planner/register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'planner/register.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'planner/register.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)  # Automatically log them in
        return redirect('login')

    return render(request, 'planner/register.html')




from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm

def dashboard_view(request):
    
    assignments = Assignment.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.user = request.user  # Ensure it's tied to the logged-in user
            new_assignment.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving
    else:
        form = AssignmentForm()

    return render(request, 'planner/dashboard.html', {'form': form, 'assignments': assignments})




def edit_assignment(request, pk):  # Update the parameter name to pk
    # Get the assignment by primary key (pk)
    assignment = get_object_or_404(Assignment, pk=pk)

    if request.method == "POST":
        # If the form has been submitted, process the form data
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()  # Save the updated assignment
            return redirect('assignment_detail', pk=assignment.pk)  # Redirect to the detail view
    else:
        # If the request is GET, pre-populate the form with the current assignment data
        form = AssignmentForm(instance=assignment)

    return render(request, 'planner/edit_assignment.html', {'form': form, 'assignment': assignment})


def assignments_view(request):
    assignments = Assignment.objects.filter(user=request.user)
    form = AssignmentForm()

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user
            assignment.save()
            return redirect('assignments')

    return render(request, 'planner/assignments.html', {'assignments': assignments, 'form': form})
   





def set_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            # Process the form and save reminder to your database, for example
            reminder = form.cleaned_data['reminder']
            reminder_date = form.cleaned_data['reminder_date']
            reminder_time = form.cleaned_data['reminder_time']

            # For example, saving the reminder to a model (you'd need a model)
            # Reminder.objects.create(reminder=reminder, date=reminder_date, time=reminder_time)

            return HttpResponse("Reminder Set Successfully!")  # Or redirect to a confirmation page
    else:
        form = ReminderForm()

    return render(request, 'planner/set_reminder.html', {'form': form})






def class_schedule_view(request):
    # Fetch the class schedule for the currently logged-in user
    class_schedules = ClassSchedule.objects.filter(user=request.user)

    # Render the class schedule template with the retrieved data
    return render(request, 'planner/class_schedule.html', {'schedule': class_schedules})





def delete_assignment(request, id):
    assignment = get_object_or_404(Assignment, id=id)
    if request.method == 'POST':
        assignment.delete()
        return redirect('dashboard')  # Redirect to the dashboard or appropriate page
    return render(request, 'confirm_delete.html', {'assignment': assignment})




class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = PasswordResetForm
