from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('view_post/<int:pk>', views.view_post, name='view_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout')

]