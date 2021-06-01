from django.urls import path
from application import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login_',views.sign,name = 'login_'),
    path('signup',views.signup,name = "signup"),
    path('dashbord',views.dashbord,name = "dashbord"),
    path('logout_',views.logout_,name = "logout_"),
    path('blogdetail/<int:id>',views.blogdetail,name = "blogdetail"),
    path('blogdetail/delete_post/<int:id>',views.delete_post,name = "delete_post"),
    path('blogdetail/edit/<int:id>',views.edit_post,name = "edit_post"),
]