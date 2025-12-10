# Create your views here.
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import user_passes_test
from .models import Student  

@user_passes_test(lambda u: u.is_superuser)  # Superuser only
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name'])  
    
    for obj in Student.objects.all():  # export all data
        writer.writerow([obj.first_name, obj.last_name]) 
    return response
