from django.contrib import admin

# Register your models here.
from django.contrib import admin
from firstapp.models import User, Test, Contact, Tag, Book


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


# 自定义格式
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')  # 列表展示数据
    search_fields = ('name', 'age',)  # 添加搜索框
    inlines = [TagInline]  # 添加新行

    # 定义新 表单 格式
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )


class ContactUser(admin.ModelAdmin):
    list_display = ('username', 'userage')  # 列表展示数据
    search_fields = ('username', 'userage',)  # 添加搜索框

    # 定义新 表单 格式
    fieldsets = (
        ['Main', {
            'fields': ('username',),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('userage',),
        }]
    )


class ContactBook(admin.ModelAdmin):
    list_display = ('title', 'price', 'publish', 'pub_date')  # 列表展示数据
    search_fields = ('title', 'price', 'publish', 'pub_date')  # 添加搜索框

    # 定义新 表单 格式
    fieldsets = (
        ['Main', {
            'fields': ('title',),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('price', 'publish', 'pub_date'),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register(User, ContactUser)
admin.site.register(Book, ContactBook)
admin.site.register([Test, ])
