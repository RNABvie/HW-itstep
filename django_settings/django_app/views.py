import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.cache import caches
from django.core.paginator import Paginator
from django_app import models
from django.contrib.auth.models import User
from .forms import PostForm


from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib import messages


RamCache = caches["default"]
def home(request):
    messages.success(request, "Сообщение отправлено")  # only JINJA

    form = PostForm()
    context = {"success": "Успешно загружено", "form": form}
    return render(request, "django_app/home.html", context=context)

def tail(request):
    return render(request, "django_app/trytailwind.html", context={})


def register(request: HttpRequest) -> HttpResponse:
    """Регистрация пользователя."""

    if request.method == "GET":
        return render(request, "django_app/register.html")
    elif request.method == "POST":
        email = str(request.POST.get("email", None)).strip()  # Admin1@gmail.com
        password = str(request.POST.get("password", None)).strip()  # Admin1@gmail.com
        valid_email = re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", email)
        valid_password = re.match(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!.]).*$", password)

        # print(f"valid_email: ", valid_email)
        # print(f"valid_password: ", valid_password)

        if valid_email is None or valid_password is None:
            return render(
                request,
                "django_app/register.html",
                {"error": "Некорректный формат email или пароль"},
            )
        try:
            user = User.objects.create(
                username=email,
                password=make_password(password),  # HASHING PASSWORD
                email=email,
            )
            # user_profile = models.UserProfile.objects.create(
            #     user=user,
            # )
        except Exception as error:
            return render(
                request,
                "django_app/register.html",
                {"error": str(error)},
            )
        return redirect(reverse("login"))
    else:
        raise ValueError("Invalid method")

def login_(request: HttpRequest) -> HttpResponse:
    """Вход в аккаунт пользователя."""

    if request.method == "GET":
        return render(request, "django_app/login.html")
    elif request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=email, password=password)
        if user is None:
            return render(request, "django_app/login.html", {"error": "Некорректный email или пароль"})
        login(request, user)
        return redirect(reverse("home"))
    else:
        raise ValueError("Invalid method")


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        user = request.user
        user_profile = user.profile  # models.Post.objects.get(user=user)
        context = {"profile": user_profile}

        return render(request, "django_app/profile.html", context)


@login_required
def logout_(request: HttpRequest) -> HttpResponse:
    """Выход из аккаунта"""

    logout(request)
    return redirect(reverse("login"))


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "django_app/post_create.html", context={})
    elif request.method == "POST":
        try:
            title = str(request.POST["title"])
            description = str(request.POST["description"])
            image = request.FILES["image"]
            models.Post.objects.create(
                author=request.user,
                title=title,
                description=description,
                image=image
            )


        except Exception as error:
            return render(
                request,
                "django_app/post_create.html",
                {"error": str(error)},
            )
        return redirect(reverse("home"))


@login_required
def post_list(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.filter(is_active=True)
    selected_page = request.GET.get(key="page", default=1)
    limit_post_by_page = 4
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)
    # return render(request, "django_app/post_list.html", context={"current_page": current_page, "is_detail_view": True})
    return render(request, "django_app/trytailwind.html", context={"current_page": current_page, "is_detail_view": True})

@login_required
def post_list_simple(request: HttpRequest) -> HttpResponse:
    posts = models.Post.objects.filter(is_active=True)
    selected_page = request.GET.get(key="page", default=1)
    limit_post_by_page = 3
    paginator = Paginator(posts, limit_post_by_page)
    current_page = paginator.get_page(selected_page)
    return render(request, "django_app/post_list.html", context={"current_page": current_page, "is_detail_view": False})


@login_required
def post_detail(request: HttpRequest, pk: str) -> HttpResponse:
    # 1. Проверяем, нет ли объект-а в кэш-е
    # 1.1 Если есть, возвращаем кэш
    # 2. Получаем объект из базы данных
    # 2.1 Кэшируем объект
    # 2.2 Возращаем объект

    post = RamCache.get(f"post_detail_{pk}")
    if post is None:
        post = models.Post.objects.get(id=pk)  # тяжёлое обращение к базе данных -- 100x - 1000x
        RamCache.set(f"post_detail_{pk}", post, timeout=30)

    # Если мы поставили лайк - то закрашиваем кнопку
    # post + user

    comments = models.PostComments.objects.filter(post=post)
    ratings = models.PostRatings.objects.filter(post=post)
    ratings = {
        "like": ratings.filter(status=True).count(),
        "dislike": ratings.filter(status=False).count(),
        "total": ratings.filter(status=True).count() - ratings.filter(status=False).count(),
    }

    return render(request, "django_app/post_detail.html", context={"post": post, "comments": comments, "ratings": ratings, "is_detail_view": True})


@login_required
def post_hide(request: HttpRequest, pk: str) -> HttpResponse:
    post = models.Post.objects.get(id=pk)
    post.is_active = False
    post.save()
    return redirect(reverse("post_list"))


@login_required
def post_comment_create(request: HttpRequest, pk: str) -> HttpResponse:
    """Создание комментария."""

    post = models.Post.objects.get(id=int(pk))
    text = request.POST.get("text", "")
    models.PostComments.objects.create(post=post, author=request.user, text=text)

    return redirect(reverse("post_detail", args=(pk,)))


@login_required
def post_rating(request: HttpRequest, pk: str, is_like: str) -> HttpResponse:
    post = models.Post.objects.get(id=int(pk))
    is_like = True if str(is_like).lower().strip() == "лайк" else False  # тернарный оператор

    print(post)
    print(is_like)

    # 1. Поставил ли я лайк ранее?
    # 2. "Отжатие лайка"

    ratings = models.PostRatings.objects.filter(post=post, author=request.user)
    if len(ratings) < 1:
        models.PostRatings.objects.create(post=post, author=request.user, status=is_like)
    else:
        rating = ratings[0]
        if is_like == True and rating.status == True:
            rating.delete()
        elif is_like == False and rating.status == False:
            rating.delete()
        else:
            rating.status = is_like
            rating.save()

    return redirect(reverse("post_detail", args=(pk,)))

@login_required
def post_search(request: HttpRequest) -> HttpResponse:
    search = str(request.POST.get("search", ""))
    posts = models.Post.objects.filter(is_active=True, title__icontains=search)
    return render(request, "django_app/post_search.html", {"posts": posts, "search": search})