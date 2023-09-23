from django.urls import path, reverse, reverse_lazy
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),

    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("post/list/", views.post_list, name="post_list"),

    path('registrations/', views.register, name="register"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/search/", views.post_search, name="post_search"),
    path("post/hide/<str:pk>/", views.post_hide, name="post_hide"),
    path("post/detail/<str:pk>/", views.post_detail, name="post_detail"),
    path("post/list/simple/", views.post_list_simple, name="post_list_simple"),
    path("post/rating/<str:pk>/<str:is_like>/", views.post_rating, name="post_rating"),
    path("post/comment/create/<str:pk>/", views.post_comment_create, name="post_comment_create"),
    # path("try", views.tail, name="tail"),

]

