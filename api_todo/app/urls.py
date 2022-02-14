from app.views import TodoListAndCreate, TodoDetailChangeAndDelete, TodoViewSet
from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('', TodoListAndCreate.as_view()),
#     path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
# ]