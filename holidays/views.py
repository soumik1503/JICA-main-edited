# holidays/views.py
import csv, io
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Holiday
from .forms import HolidayUploadForm
from .forms import HolidayUploadForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def upload_holidays(request):
    if request.method == "POST":
        form = HolidayUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]

            try:
                if file.name.endswith(".xlsx"):
                    df = pd.read_excel(file)
                    for _, row in df.iterrows():
                        Holiday.objects.update_or_create(
                            date=row["date"],
                            defaults={
                                "name": row["name"],
                                "description": row.get("description", ""),
                            },
                        )
                else:  # CSV
                    decoded_file = file.read().decode("utf-8")
                    io_string = io.StringIO(decoded_file)
                    reader = csv.DictReader(io_string)
                    for row in reader:
                        Holiday.objects.update_or_create(
                            date=row["date"],
                            defaults={
                                "name": row["name"],
                                "description": row.get("description", ""),
                            },
                        )
                messages.success(request, "✅ Holidays uploaded successfully!")
            except Exception as e:
                messages.error(request, f"❌ Error: {str(e)}")

            return redirect("upload_holidays")
    else:
        form = HolidayUploadForm()

    return render(request, "holidays/upload.html", {"form": form})


from django.http import JsonResponse, HttpResponseForbidden

def holiday_list(request):
    # Restrict direct access (must have Referer from same domain)
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return redirect('access_denied')
    
    # Optional: Strict check if referrer domain matches host
    # if request.get_host() not in referer:
    #    return HttpResponseForbidden("External access is restricted.")

    holidays = Holiday.objects.all().values("id", "name", "date", "description")
    return JsonResponse(list(holidays), safe=False)
