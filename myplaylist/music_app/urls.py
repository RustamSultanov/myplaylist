from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm

urlpatterns = [
    path(
        '', views.track_list, name='base'),
    path(
        'accounts/login/',
        auth_view.LoginView.as_view(
            template_name='authentication_login.html',
            authentication_form=LoginForm), name='login'),
    path(
        'logout',
        auth_view.LogoutView.as_view(next_page="login"),
        name='logout'),
    path(
        'upload-track', views.upload_track_view, name='upload_track'),
    path(
        'edit-track/<int:track_id>', views.edit_track_view, name='edit_track'),
    path(
        'edit-profile/<int:user_id>', views.edit_profile_view, name='edit_employee'),
    path(
        'delete-<int:track_id>', views.delete_track, name='delete_track'),
]
