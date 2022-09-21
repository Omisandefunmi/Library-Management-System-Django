from djangoProject.urls import path

from . import views

app_name = 'first_app'

urlpatterns = [
    # path('index', views.index, name='hello'),
    # path('', views.redirect),
    # path('about/', views.about, name='about'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-details'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
]

