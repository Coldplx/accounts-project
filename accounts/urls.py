from django.urls import path, include
from . import views


'''
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

'''

urlpatterns = [

    path('accounts/login/', views.login.as_view(), name='login'),
    path('accounts/logout/', views.logout.as_view(), name='logout'),
    path('accounts/password_change/', views.password_change.as_view(), name='password_change'),
    path('accounts/password_change/done/', views.password_change_done.as_view(),name='password_change_done'),
    path('accounts/password_reset/', views.password_reset.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', views.password_reset_done.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.password_reset_confirm.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', views.password_reset_complete.as_view(), name='password_reset_complete'),
    path('accounts/signup/', views.signup.as_view(), name='signup'),

]


