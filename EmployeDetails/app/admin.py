from django.contrib import admin

# Register your models here.
from app.models import employe_model

class employe_admin(admin.ModelAdmin):
    list_display = ['employe_name','employe_id','employe_salary']

admin.site.register(employe_model,employe_admin)