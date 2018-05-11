from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import(
		authenticate,
		get_user_model,
		login,
		logout,
		)
from .forms import LoginForm,SignupForm,PostBook
from .models import Book,Genre,Language,Author

# Create your views here.
def index(request):
	title = 'SignUp'
	form = SignupForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username,password=password)
		login(request,new_user)
		return redirect('loginpage/')
	return render(request,"index.html",{'form':form,'title':title})

def loginpage(request):
	title = "login"
	form = LoginForm(request.POST or None)
	if form.is_valid():
		#username = form.cleaned_data.get("username")
		#password = form.cleaned_data.get("password")
		user = authenticate(username='username',password='password')
		login(request,user)
		return redirect('/home/inside')
	return render(request,"login.html",{"form":form,"title":title})


def inside(request):
	no_books=Book.objects.all().count()
	no_authors=Author.objects.all().count()
	no_genre=Genre.objects.all().count()
	return render(request,"inside.html",{'no_genre':no_genre,'no_books':no_books,'no_authors':no_authors})

def signout(request):
	logout(request)
	return redirect('/home')

def catalog(request):
	no_books=Book.objects.all().count()
	no_authors=Author.objects.all().count()
	no_genre=Genre.objects.all().count()

	return render(request,'catalog.html',{'no_genre':no_genre,'no_books':no_books,'no_authors':no_authors})

def book_list_view(request):
	book_list=Book.objects.all()
	return render(request,'book_list_view.html',{'book_list':book_list})

def author_list_view(request):
	author_list=Author.objects.all()
	return render(request,'author_list_view.html',{'author_list':author_list})

def book_detail(request,pk):
	book_detail=get_object_or_404(Book,pk=pk)
	return render(request,'book_detail.html',{'book_detail':book_detail})

def author_detail(request,pk):
	author_detail=get_object_or_404(Author,pk=pk)
	return render(request,'author_detail.html',{'author_detail':author_detail})

def postbook(request):
	form=PostBook(request.POST)
	if form.is_valid():
		form.save()
		return redirect('/home/inside')
	return render(request,'postbook.html',{'form':form})