from django.urls import path

from .views import TodoAppCreateView, TodoAppDetailView, TodoAppListView, TodoAppUpdateView


app_name = 'todo'

urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list/', TodoAppListView.as_view(), name='list'),
    path('detail/<int:pk>/', TodoAppDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TodoAppUpdateView.as_view(), name='update'),

]