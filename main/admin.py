from django.contrib import admin
from .models import Profile, SocialLink, Experience, Technology, Certification, Project, BlogCategory, BlogPost
from .models import Book

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'is_published')
    list_filter = ('is_published', 'categories')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author', 'description')
