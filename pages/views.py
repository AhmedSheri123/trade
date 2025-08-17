from django.shortcuts import render, redirect
from .models import ComplaintsModel, SubmittedComplaintModel
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    
    complaints = ComplaintsModel.objects.all()
    return render(request, 'pages/index.html', {'complaints':complaints})

def SubmittedComplaints(request):
    user = request.user
    submitted_complaints = SubmittedComplaintModel.objects.filter(user=user).order_by('-id')
    return render(request, 'pages/SubmittedComplaints.html', {'submitted_complaints':submitted_complaints})

def SubmitInfo(request):
    id = request.GET.get('id')
    user = request.user
    complaint = ComplaintsModel.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        submitted_complaint = SubmittedComplaintModel.objects.create(user=user, complaint=complaint, username=username, email=email, image=image, progress='3')
        submitted_complaint.save()
        messages.success(request, 'طلبك قيد المراجعة, ياخذ عادة بين 12 الى 24 ساعة')
        return redirect('SubmittedComplaints')
    return render(request, 'pages/SubmitInfo.html', {'complaint':complaint})

def SubmitComplaint(request):
    id = request.GET.get('id')
    complaint = ComplaintsModel.objects.get(id=id)
    return render(request, 'pages/SubmitComplaint.html', {'complaint':complaint})