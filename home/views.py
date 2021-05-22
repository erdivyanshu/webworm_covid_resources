from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from home.models import Feedback
from home.models import Resources
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from math import ceil

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        text = request.POST['text']
        contact = Feedback(email=email, text=text)
        contact.save()
        messages.success(request, "Thanks! For Feedback")
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        need = request.POST['need']
        content = request.POST['content']

        if len(email) < 3 or len(content) < 4:
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(email=email, need=need, content=content)
            contact.save()
            messages.success(request, "Your message has been sent!")
            messages.warning(request, "Admin will respond back soon!")
    return render(request, 'contactus.html')

def resources(request):
    if request.method == 'POST':
        Hname = request.POST['Hname']
        category = request.POST['category']
        available =request.POST['available']
        add= request.POST['add']
        contact= request.POST['contact']
        resources = Resources(Hname=Hname, category=category, available=available, add=add, contact=contact)
        resources.save()
        messages.success(request, "You updated the data!")

    resources = Resources.objects.all()
    return render(request, 'resources.html', {'resources': resources})

def searchMatch(query, item):
    # if query in item.category.lower():
    #     return True
    # else:
        return False

def search(request):
    query = request.GET.get('search')
    allData =[]
    # CATEGORY = (('Vaccine', 'Vaccine'), ('General-Bed', 'General-Bed'), ('Oxygen-Bed', 'Oxygen-Bed'),
    #             ('Bed With-Ventilator', 'Bed With-Ventilator'))
    resources = Resources.objects.values('category','category')
    cats= {item['category'] for item in resources}
    for cat in cats:
        reso= Resources.objects.filter(category=cat)
        data = [item for item in resources if searchMatch(query, item)]
        n=len(data)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        if len(data) != 0:
            allData.append([data, range(1, nSlides), nSlides])
    info = {'allData': allData, "msg": ""}
    if len(allData) == 0 or len(query) < 3:
        info = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'search.html', info)

def plasma(request):
    return render(request, 'plasma.html')

def vaccine(request):
    return render(request, 'vaccine.html')

def gov(request):
    return render(request, 'gov.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def contact_info(request):
    return render(request, 'contact_info.html')


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        contactno = request.POST['contactno']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, "Username must be under 10 character")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username can be only alphanemuric")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        myuser.save()
        messages.success(request, " You are succesfully Registered for Covid-Resource Data-Updation")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, " You are succesfully Logged-In on Covid-Resource Data-Portal")
            return redirect('home')
        else:
            messages.error(request, "Input Correct Credentials!")


    return HttpResponse("404 - Not found")

def handleLogout(request):
        logout(request)
        messages.success(request, "You are Successfully Logged-Out!")
        return redirect('home')

# def search(request):
#     query= request.GET['query']
#     allData= Resources.objects.filter(Hname__icontains=query)
#     allData = Resources.objects.filter(category__icontains=query)
#     allData = Resources.objects.filter(available__icontains=query)
#     allData = Resources.objects.filter(contact__icontains=query)
#     data= {'allData': allData}
#     return render(request, 'search.html', data)