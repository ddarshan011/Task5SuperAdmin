from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import user_passes_test
from .models import Student  # CHANGE to your model name

@user_passes_test(lambda u: u.is_superuser)  # Superuser only
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name'])  # CHANGE to your fields
    
    for obj in Student.objects.all():  # Exports ALL data
        writer.writerow([obj.id, obj.field1, obj.field2])  # CHANGE fields
    
    return response
