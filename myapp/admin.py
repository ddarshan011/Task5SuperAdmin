from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Student
from django.urls import reverse

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = ['export_csv']
    
    def export_csv(self, request, queryset):
        url = reverse('export_csv')
        return HttpResponseRedirect(url)
    
    export_csv.short_description = "Export to CSV"
