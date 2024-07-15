from django.urls import path
from . import views
urlpatterns = [
     path("", views.home, name="home"),
     path("login",views.login_view,name="login"),
     path("register",views.register,name="register"),
     path("logout",views.logout_view,name="logout"),
     path("create",views.create_news, name="create"),
     path("politics",views.politics, name="politics"),
     path("world",views.world, name="world"),
     path("business",views.business, name="business"),
     path("sports",views.sports, name="sports"),
     path("health",views.health, name="health"),
     path("article/<int:id>",views.article,name="article"),
     path("add_comment/<int:id>",views.add_comment,name="add_comment"),
     path("apple",views.apple, name="apple"),
     path("coldplay",views.coldplay, name="coldplay"),
]
