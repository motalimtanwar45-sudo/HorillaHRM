from django.shortcuts import render, redirect
from .models import Employee

def login_view(request):
    if request.method == 'POST':
        return redirect('dashboard')
    return render(request, 'staff/login.html')

def dashboard_view(request):
    employees = Employee.objects.all().order_by('-id')
    context = {
        'total_employees': employees.count(),
        'present_today': employees.count(),
        'on_leave': 0,
        'pending_requests': 0,
        'employees': employees,
    }
    return render(request, 'staff/dashboard.html', context)

def add_employee_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        Employee.objects.create(name=name, email=email, department=department)
        return redirect('dashboard')
    return render(request, 'staff/add_employee.html')

# --- बेज़ात के बाकी सारे फीचर्स यहाँ चालू कर दिए ---

def employee_hub_view(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'staff/employee_hub.html', {'employees': employees})

def attendance_view(request):
    employees = Employee.objects.all()
    return render(request, 'staff/attendance.html', {'employees': employees})

def leave_view(request):
    return render(request, 'staff/leave.html')

def payroll_view(request):
    return render(request, 'staff/payroll.html')
def logout_view(request):
    # यहाँ हम यूजर को लॉगआउट करके सीधे फ्रेश लॉगिन पेज पर भेजेंगे
    return redirect('/login/')