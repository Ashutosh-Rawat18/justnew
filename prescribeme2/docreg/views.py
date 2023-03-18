# from django.shortcuts import render
# from django.contrib import messages
# from docreg.models import DocModel

# # Create your views here.


# def docreg(request):
#     if request.method == "POST":
#         if request.POST.get('docname') and request.POST.get('age') and request.POST.get('email') and request.POST.get('phoneno') and request.POST.get('address') and request.POST.get('licenseno') and request.POST.get('password'):
#             saverecord = DocModel()
#             saverecord.docname = request.POST.get('docname')
#             saverecord.age = request.POST.get('age')
#             saverecord.email = request.POST.get('email')
#             saverecord.phoneno = request.POST.get('phoneno')
#             saverecord.address = request.POST.get('address')
#             saverecord.licenseno = request.POST.get('licenseno')
#             saverecord.password = request.POST.get('password')
#             saverecord.save()
#             messages.success(request, 'Account' +
#                              saverecord.docname + ' is created successfully')
#             return render(request, 'doctor_signup.html')
#     else:
#         return render(request, 'doctor_signup.html')
