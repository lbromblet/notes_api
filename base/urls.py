from django.urls import path
from .views import routes_views, notes_views, users_views

urlpatterns = [
    path('', routes_views.getRoutes, name="routes"),
    path('notes', notes_views.getNotes, name="notes"),
    path('notes/<str:pk>', notes_views.getNote, name="note"),
    path('login', users_views.loginPage, name="login"),
]