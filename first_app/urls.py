from djangoProject.urls import path

from . import views

app_name = 'first_app'

urlpatterns = [
    # path('index', views.index, name='hello'),
    # path('', views.redirect),
    # path('about/', views.about, name='about'),
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-details'),
    path('publishers/', views.publisher_list, name='publisher-list'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher-detail'),
]

