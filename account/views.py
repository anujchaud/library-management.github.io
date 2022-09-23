from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User,Book
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .form_vailidation import check_email,check_mobile,check_name

# Create your views here.

def signup_view(request):
    '''This signup Function resposible for student not admin'''
    if not request.user.is_authenticated:
        if request.method=="POST":            
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password1 = request.POST.get('pass1')
            password2 = request.POST.get("pass2")
            if not password1==password2:
                messages.error(request, "Password not matched!")
                return render(request,'account/signup.html')
            if name and email and phone and password1 and password2:
                if password1 == password2:
                    if check_mobile(phone):
                        if check_email(email):
                            if check_name(name):
                                check_usnique_mail = User.objects.filter(email=email)
                                if  not check_usnique_mail:
                                    User.objects.create_user(email, password1, name ,phone )
                                    messages.success(request, "Accounts has been created!")
                                else:
                                    messages.error(request, "Ragister with another email id!")
                            else:
                                messages.error(request, "Name should be alphabatical form!")
                        else:
                            messages.error(request, "Enter a vailed Email Id!")
                    else:
                        messages.error(request, "Mobile number should be 10 digit and digit form!")
                else:
                    messages.error(request, "password does not matched!")
            else:
                messages.error(request, "fill required field!")
        return render(request,'account/signup.html')
    else:
        return redirect("store")


def login_view(request):
    """This function is resposible to login for student not admin"""
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email and password:
                if check_email(email):
                    # authenticate(request=request,email=email,password=password)
                    authenticated_user = authenticate(email=email,password=password)
                    print(authenticated_user,"<<authenticate user----------------------")
                    if authenticated_user is not None:
                        ulogin(request, authenticated_user)
                        return redirect("store")
                    else:
                        messages.error(request, 'Invailed creadientials!')
                else:
                    messages.error(request, "Enter a valiled email!")
            else:
                messages.error(request, "Fill required all fields!")
        return render(request, "account/login.html")
    else:
        return redirect("store")


def logout_view(request):
    if request.user.is_authenticated:
        ulogout(request)
        return redirect('signup')
    else:
        return redirect('store') 

def library_view(request):
    '''This function Responsible for show all Library Stock only Authenticated Student'''
    if request.user.is_authenticated:
        data = Book.objects.filter(available_quantity__gte=1)
        d ={'data':data}
        return render(request,'account/libraryview.html',context=d)
    else:
        return HttpResponse("<h2>Only Authenticated Show Store Book</h2><a href='/store'>back to home</a>")

def library_OutStock(request):
    '''This function Responsible for OutofStock Library Stock only Authenticated Student'''
    if request.user.is_authenticated:
        data = Book.objects.filter(available_quantity__lte=0)
        return render(request,'account/listout.html',{'data':data})
    else:
        return HttpResponse("<h2>Only Authenticated OutStock Store Book</h2><a href='/store'>back to home</a>")


def addBook(request):
    '''This function Responsible for Add New Book Stock only Authenticated Student'''
    if request.user.is_authenticated:
        if request.method=="POST":
            bname=request.POST.get('name')
            bimage=request.FILES.get('image')
            btitle=request.POST.get('title')
            author=request.POST.get('author')
            total=request.POST.get('total')
            print(bname,bimage,btitle,author,total,"<--------")
            Book.objects.create(book_name=bname,book_photo=bimage,book_title=btitle,book_author=author,
                                 total_quantity=total,available_quantity=total)
            return redirect('/store/')
        return render(request,'account/addbook.html')
    else:
        return HttpResponse("<center>Invailed user login first<br><a href='/login/'>Login</a>")

def update_book(request,bid):
    '''This function Responsible for update Library Stock only Authenticated Student'''
    if request.user.is_authenticated:
        data = Book.objects.get(id = bid)
        if request.method=="POST":
            bname=request.POST.get('name')
            bimage=request.FILES.get('image',data.book_photo)
            btitle=request.POST.get('title')
            author=request.POST.get('author')
            avail = request.POST.get('avail')
            total=request.POST.get('total')
            print(bname,bimage,btitle,author,total,avail,"<--------")
            data.book_name = bname
            data.book_photo = bimage
            data.book_title = btitle
            data.book_author = author
            data.available_quantity=avail
            data.total_quantity = total
            data.save()
            return redirect('/store')
        return render(request,'account/update.html',{'data':data})
    else:
        return HttpResponse("<h2>Book Update Only Authenticated User </h2>< a href='/store'>back to store</a>")  
    
def deleteBook(request,bid):
    '''This function Responsible for Delete Library Stock only Authenticated Student'''
    if request.user.is_authenticated:
        data = Book.objects.filter(id=bid)
        print(data,'Data Deleted Successfully')
        data.delete()
        return redirect('/store')
    else:
        return HttpResponse("<h2>Stock Delete Only Authenticated User </h2>< a href='/store'>back to store</a>")

def BookListOut(request,bid):
    '''This function Responsible for BookListOut Library Stock only Authenticated Student'''
    if request.user.is_authenticated:
        data = Book.objects.get(id=bid)
        data.available_quantity=data.available_quantity-1
        data.save()
        return redirect('/store')
    else:
        return HttpResponse("<h2>Stock ListOut Only Authenticated User </h2>< a href='/store'>back to store</a>")

