from django.http.response import JsonResponse
from django.urls import path

from .views import Login, LibroCreate, LibroDelete, LibroList, LibroSelect, LibroUpdate, Logout


urlpatterns = [
    path('', LibroList.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('libro/select/<int:id>/', LibroSelect.as_view()),
    path('libro/create/', LibroCreate.as_view()),
    path('libro/delete/<int:id>/', LibroDelete.as_view()),
    path('libro/update/<int:id>/', LibroUpdate.as_view()),
]