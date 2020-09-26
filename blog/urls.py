from django.urls import path

from .views import (
    detail_blog_page_by_id,
    detail_blog_page_by_slug,
    blog_post_list_view,
    blog_post_retrieve_view,
    blog_post_update_view,
    blog_post_delete_view,
)

# url patterns are matched from top to bottom , first matched view will be rendered that's why create is different

urlpatterns = [
    path('<int:post_id>/', detail_blog_page_by_id),
    path('', blog_post_list_view),
    path('<str:slug>/', blog_post_retrieve_view),
    path('<str:slug>/edit', blog_post_update_view),
    path('<str:slug>/delete', blog_post_delete_view),
]


