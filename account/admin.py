from django.contrib import admin

# Register your models here.
from account.models import User

# class FolloweAdmin(admin.TabularInline):
#     model = UserFollow


# class UserAdmin(admin.ModelAdmin):
#     inlines = [FolloweAdmin]


# admin.site.register(UserProfile, UserAdmin)
admin.site.register(User)
