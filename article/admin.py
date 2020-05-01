from django.contrib import admin

# Register your models here.
from article.models import Article, ArticleLike,ArticleTags,Tag,Comment


class ArticleLikeAdmin(admin.TabularInline):
        model = ArticleLike


class ArticleTagAdmin(admin.TabularInline):
        model = ArticleTags


class ArticleCommentAdmin(admin.TabularInline):
        model = Comment



class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleLikeAdmin,ArticleTagAdmin,ArticleCommentAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Comment)