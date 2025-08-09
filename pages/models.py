from django.db import models

# Create your models here.

class ComplaintsModel(models.Model):
    name = models.CharField(("اسم الشكوى"), max_length=50)
    desc = models.CharField(("وصف"), max_length=50)
    price = models.DecimalField(("السعر"), max_digits=6, decimal_places=2)
    days = models.IntegerField(("ايام انهاء الطلب"))
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
SubmittedComplaintProgressChoices = [
    ('1', 'ادخال المعلومات'),
    ('2', 'يتم مراجعة الطلب'),
    ('3', 'الدفع'),
    ('4', 'مكتمل')
]

class SubmittedComplaintModel(models.Model):
    user = models.ForeignKey("auth.User", verbose_name=("المستخدم"), on_delete=models.CASCADE)
    complaint = models.ForeignKey(ComplaintsModel, verbose_name=("الشكوى"), on_delete=models.CASCADE)
    username = models.CharField(("اسم المستخدم"), max_length=50)
    email = models.CharField(("بريد الالكتروني"), max_length=50)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    progress = models.CharField(("التقدم"), max_length=50, choices=SubmittedComplaintProgressChoices, default='1')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} -- {self.complaint} -- {self.email} -- {self.progress}'