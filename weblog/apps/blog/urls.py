from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^archive/(?P<year>[0-9]{4})/$', views.ArticleYearArchiveView.as_view(), name='archive_year'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.ArticleMonthArchiveView.as_view(),
        name="archive_month_numeric"),
]
