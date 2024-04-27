from django.contrib import admin
from django.urls import path
from gas_app import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/',views.home,name='home'),
    path('signup/',views.signup),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout),
    path('submit/',views.submit_service_request, name='submit_request'),
    path('tracking/',views.request_tracking, name='request_tracking'),
]