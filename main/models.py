from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class SocialLink(models.Model):
    PLATFORM_CHOICES = (
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('github', 'GitHub'),
    )
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    
    def __str__(self):
        return f"{self.profile.name}'s {self.get_platform_display()}"

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tech_icons/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_obtained = models.DateField()
    url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    
    def __str__(self):
        return self.title

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Blog Categories"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    categories = models.ManyToManyField(BlogCategory, related_name='posts')
    published_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='books/', blank=True, null=True)
    description = models.TextField()
    publication_date = models.DateField()
    purchase_link = models.URLField(blank=True, null=True)
    will_read = models.BooleanField(default=False)  # Add this field
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publication_date']
