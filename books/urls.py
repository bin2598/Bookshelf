from django.urls import path
from . views import BooklistView,BookdetailView,BookcreateView,BookeditView,BookdeleteView, SignupView

urlpatterns = [
    path('', BooklistView.as_view(), name='book-list'),
    path('detail/<int:pk>', BookdetailView.as_view(), name='book-detail'),
    path('create', BookcreateView.as_view(), name='book-create'),
    path('edit/<int:pk>', BookeditView.as_view(), name='book-edit'),
    path('delete/<int:pk>', BookdeleteView.as_view(), name='book-delete'),
    path('signup/', SignupView.as_view(), name="signup")
]