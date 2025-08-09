from django.contrib import admin
from .models import ComplaintsModel, SubmittedComplaintModel
# Register your models here.

admin.site.register(ComplaintsModel)
admin.site.register(SubmittedComplaintModel)