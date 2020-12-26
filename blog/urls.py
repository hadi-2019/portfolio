from django.urls import path
from .views import blog_category, blog_detail, blog_index

urlpatterns = [
    path("blog/", blog_index, name="blog-page"),
    path("blog/<int:id>/", blog_detail, name="blog_detail"),
    path("blog/<category>/", blog_category, name="blog_category"),
]
