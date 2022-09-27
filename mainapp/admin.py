from django.contrib import admin
from .models import student_extra, teacher_extra, admin_extra, answers, question

# Register your models here.
admin.site.register(student_extra)
admin.site.register(teacher_extra)
admin.site.register(admin_extra)


admin.site.register(answers)
admin.site.register(question)
