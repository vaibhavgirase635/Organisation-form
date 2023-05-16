from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    path('orga/', views.OrganisationView.as_view(), name='orga'),
    
    path('register/', views.UserRegistrationView.as_view(), name='success'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)