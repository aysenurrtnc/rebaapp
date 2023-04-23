from django.shortcuts import render

# Create your views here.

employee_list = ["aysenur", "furkan", "zeynep"]
employee_age = []

def home(request):
  
    return render(request, "index.html")

def users(request):
    data = {
        "employees" : employee_list
        } #key-value bir key yani tanımladım ve bunu sayfaya data olarak gönderiyoruz
    return render(request, "users.html", data) #users.html access to data 


