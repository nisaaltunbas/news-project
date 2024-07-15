from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.db import IntegrityError 

from .models import Author,Category,Articles,Comments

# Create your views here.
def home(request):
    articles = Articles.objects.all()
    return render(request, "news/home.html",{
        "articles":articles
    })

def add_comment(request, id):
    current_user = request.user
    article_data = Articles.objects.get(pk=id)
    message = request.POST.get("add_comment")
    name = request.POST.get("name")

    new_comment = Comments(
        article = article_data,
        message = message,
        name = name
    )

    new_comment.save()

    return HttpResponseRedirect(reverse("article",args=(id, )))

def apple(request):
    return render(request, "news/apple.html",{
        "apple" : True,})

def coldplay(request):
    return render(request, "news/coldplay.html",{
        "coldplay" : True,})

def politics(request):
    politics = Articles.objects.filter(category__category_name="Politics")
    return render(request, "news/politics.html",{
        "politics" : True,
        "articles": politics,
    })

def world(request):
    world = Articles.objects.filter(category__category_name="World")
    return render(request, "news/world.html",{
        "world" : True,
        "articles": world,
    })

def business(request):
    business = Articles.objects.filter(category__category_name="Business")
    return render(request, "news/business.html",{
        "business" : True,
        "articles": business,
    })

def sports(request):
    sports = Articles.objects.filter(category__category_name="Sports")
    return render(request, "news/sports.html",{
        "sports" : True,
        "articles": sports,
    })

def health(request):
    health = Articles.objects.filter(category__category_name="Health")
    return render(request, "news/health.html",{
        "health" : True,
        "articles": health,
    })


def article(request, id):
    article_data = Articles.objects.get(pk=id)
    all_comments = Comments.objects.filter(article=article_data)
    return render(request,"news/article.html",{
        "article":article_data,
        "all_comments":all_comments
    })

def create_news(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        all_authors = Author.objects.all()
        return render(request,"news/create.html",{
            "categories":all_categories,
            "authors":all_authors
        })
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        short_description = request.POST.get("short_description")
        tags = request.POST.get("tags")
        imageurl = request.POST.get("imageurl")
        author = request.POST.get("author")
        category = request.POST.get("category")
        published_date = request.POST.get("published_date")


        category_data = Category.objects.get(category_name = category)
        author_data = Author.objects.get(author_name = author)

        new_articles = Articles(
            title = title,
            description = description,
            tags = tags,
            imageUrl = imageurl,
            short_description = short_description,
            published_date = published_date,
            category = category_data,
            author = author_data
        )

        
        new_articles.save()

        return HttpResponseRedirect(reverse(home))


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        author = authenticate(request, username=username, password=password)

        if author is not None:
            login(request, author)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "news/login.html",{
                "message": "Invalid username and/or password."
            })
    else:
        return render(request,"news/login.html")
    
def register(request):
    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "news/register.html",{
                "message":"Password do not match. Please try again."
            })
        
        try:
            author = Author.objects.create(username,email,password)
            author.save()
        except IntegrityError:
            return render(request,"news/register.html",{
                "message":"Username already taken."
            })
        login(request,author)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request,"news/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

