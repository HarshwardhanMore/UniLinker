from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('createProfile', views.createProfile),
    path('editProfile', views.editProfile),

    path("login", views.loginpage, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.registerpage, name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
