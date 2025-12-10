from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ['export_csv']
    
    def export_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        writer = csv.writer(response)
        writer.writerow(['first_name', 'last_name'])
        for obj in Student.objects.all():  # export all data
            writer.writerow([obj.first_name, obj.last_name])
        return response
    
    export_csv.short_description = "Export to CSV"
