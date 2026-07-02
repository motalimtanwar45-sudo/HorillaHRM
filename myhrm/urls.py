from django.contrib import admin
from django.urls import path
from staff import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add-employee/', views.add_employee_view, name='add_employee'),
    
    # बेज़ात फीचर्स के रास्ते
    path('employee-hub/', views.employee_hub_view, name='employee_hub'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('leave/', views.leave_view, name='leave'),
    path('payroll/', views.payroll_view, name='payroll'),
    
    # यह लाइन आपके कोड में गायब थी, इसे अब जोड़ दिया है:
    path('logout/', views.logout_view, name='logout'),
]