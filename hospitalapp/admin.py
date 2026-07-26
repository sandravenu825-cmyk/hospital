
from django.contrib import admin
from .models import Department, Doctor, Booking


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'doctor_name',
        'doctor_specialization',
        'department',
    )
    list_filter = ('department',)
    search_fields = ('doctor_name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'doctor',
        'booking_date',
        'booked_on',
    )
    list_filter = ('booking_date',)
    search_fields = ('patient_name',)