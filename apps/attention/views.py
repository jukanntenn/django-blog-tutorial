from django.shortcuts import render


# Create your views here.
# 关注某个帖子
@login_required
def follow_article(request):
    article_id = request.GET.get('ARTICLIE_ID')
    article = Article.objects.get(pk=article_id)
    user_id = request.user.id
    follow_article = FollowArticle(content_object=article, user_id=user_id)
    follow_article.save()
    return HttpResponse("关注成功.")
