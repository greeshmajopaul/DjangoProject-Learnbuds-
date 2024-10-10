from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('',views.home),
    path('about/', views.about),
    path('details/',views.index),
    path('employee/',views.employeedetails),
    path('employeedata/',views.EmployeeView.as_view()),
]+router.urls