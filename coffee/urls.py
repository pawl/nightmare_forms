from coffee import views
from django.urls import path

app_name = "coffee"
urlpatterns = [
    path('vue-form-example/api/products/', views.ProductListAPIView.as_view(), name='vue_form_products'),
]
