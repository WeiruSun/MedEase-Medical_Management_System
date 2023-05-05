from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('MedEase_appointment_list_urlpattern')
