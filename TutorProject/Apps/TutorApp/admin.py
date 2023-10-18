from django.contrib import admin
from .models import Student, Tutor, Admin, CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Admin)
