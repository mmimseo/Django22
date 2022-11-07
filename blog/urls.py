from django.urls import path
from . import views

urlpatterns = [ # IP주소/blog/
    path('', views.PostList.as_view()),   ## Listview 목록페이지 : CBV ##
    path('<int:pk>/', views.PostDetail.as_view()),   ## DetailView : CBV##
    path('category/<str:slug>/', views.category_page),   #IP주소/blog/category/slug/
    path('tag/<str:slug>', views.tag_page),   #IP주소/blog/tag/slug


    #path('', views.index), # IP주소/blog/     ##view의 html : FBV 연결##
    #path('<int:pk>/', views.single_post_page)
]