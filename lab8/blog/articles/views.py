# -*- coding: utf-8 -*-
from articles.models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.template import RequestContext

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()}, context_instance=RequestContext(request))

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post}, context_instance=RequestContext(request))
    except Article.DoesNotExist:
        raise Http404
    
def create_post(request):

    if not request.user.is_anonymous():
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Статья с таким названием уже существует!"
                    return render(request, 'create_post.html', {'form': form}, context_instance=RequestContext(request))

                new_article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect(get_article, article_id=new_article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
    
def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'email': request.POST["email"],
            'password': request.POST["password"]
        }
        
        if form["username"] and form["email"] and form["password"]:
            try:
                User.objects.get(username=form["username"])
                form['errors'] = u"Пользователь с таким именем уже зарегистрирован!"
                return render(request, 'register.html', {'form': form}, context_instance=RequestContext(request))
            except User.DoesNotExist:
                User.objects.create_user(
                    username=form["username"], 
                    email=form["email"], 
                    password=form["password"]
                )
                return redirect(archive)
        else:
            form['errors'] = u"Не все поля заполнены!"
            return render(request, 'register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return render(request, 'register.html', {}, context_instance=RequestContext(request))

def login_view(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        
        if form["username"] and form["password"]:

            user = authenticate(username=form["username"], password=form["password"])
            
            if user is not None:
                if user.is_active:

                    auth_login(request, user)
                    return redirect(archive)
            else:

                form['errors'] = u"Нет аккаунта с таким сочетанием никнейма и пароля."
                return render(request, 'login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            form['errors'] = u"Не все поля заполнены!"
            return render(request, 'login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return render(request, 'login.html', {}, context_instance=RequestContext(request))
