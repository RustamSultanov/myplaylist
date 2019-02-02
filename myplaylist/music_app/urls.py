from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_view
import django.urls
from .forms import LoginForm,RegistrationCustomForm,LoginImpForm
from django_registration.backends.activation.views import RegistrationView


urlpatterns = [
 path('', views.base, name='base'),
 # path('regist', RegistrationView.as_view(form_class=RegistrationCustomForm,template_name='register_form.html'),name='register'),
 # path('accounts/', include('django_registration.backends.activation.urls')),
 # path('accounts/login/', auth_view.LoginView.as_view(template_name='auth_form.html',authentication_form=LoginForm), name='login'),
 # path('imp/login/', auth_view.LoginView.as_view(template_name='authentication_login.html',authentication_form=LoginImpForm), name='login_2'),
 # path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
 # path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
 # path('password-reset/reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
 # path('password-reset/complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
 # path('logout', auth_view.LogoutView.as_view(next_page="base"), name='logout'),
 # path('imp/create-employee', views.create_employee_view, name='create_employee'),
 # path('imp/employee', views.employee_list, name='employee_list'),
 # path('imp/employee/<int:user_id>', views.employee_info, name='employee_info'),
 # path('lk/', views.lichniy_kabinet, name='lichniy-kabinet'),
 # path('lk-competence', views.competence_list, name='competence_list'),
 # path('imp/edit-employee/<int:user_id>', views.edit_employee_view, name='edit_employee'),
 # path('imp/appeal-cards/<int:appeal_id>', views.appeal_info, name='appeal_info'),
 # path('imp/appeal-accept/<int:appeal_id>', views.appeal_accept, name='appeal_accept'),
 # path('imp/appeal-failure/<int:appeal_id>', views.appeal_failure, name='appeal_failure'),
 # path('imp/appeal-cards', views.appeal_list, name='appeal_list'),
 # path('delete-<int:comment_id>', views.delete_comment, name='delete_comment'),
 # path('add-comment', views.add_comment, name='add_comment'),
 # path('lk-accept', views.lk_accept, name='lk_accept'),
 # path('lk-accept/accept-<int:comment_id>-comment', views.accept_comment, name='accept_comment'),
 # path('lk-accepted-list/info-<int:comment_id>-comment', views.comment_info, name='comment_info'),
 # path('lk-failure/failure-<int:comment_id>-comment', views.lk_failure, name='lk_failure'),
 # path('customer', views.show_genres, name='show_genres'),
 # path('customer1', views.customer1, name='customer1'),
 # path('customer2', views.customer2, name='customer2'),
 # path('customer3', views.customer3, name='customer3'),
]
