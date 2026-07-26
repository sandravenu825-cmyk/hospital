
from django.shortcuts import render, redirect
from .models import Department, Doctor, Booking


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def department(request):
    dept = Department.objects.all()
    return render(request, 'department.html', {'dept': dept})


def doctors(request):
    doctor = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctor': doctor})


def booking(request):
    doctor = Doctor.objects.all()

    if request.method == "POST":
        patient_name = request.POST.get('patient_name')
        patient_phone = request.POST.get('patient_phone')
        patient_email = request.POST.get('patient_email')
        booking_date = request.POST.get('booking_date')
        doctor_id = request.POST.get('doctor')

        selected_doctor = Doctor.objects.get(id=doctor_id)

        Booking.objects.create(
            patient_name=patient_name,
            patient_phone=patient_phone,
            patient_email=patient_email,
            doctor=selected_doctor,
            booking_date=booking_date
        )

        return redirect('booking')

    return render(request, 'booking.html', {'doctor': doctor})


def contact(request):
    return render(request, 'contact.html')