from django.contrib import admin

# Register your models here.
from article.models import Article, ArticleLike


class ArticleLikeAdmin(admin.TabularInline):
        model = ArticleLike


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
