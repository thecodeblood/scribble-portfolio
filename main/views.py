from django.shortcuts import render, get_object_or_404
from .models import Profile, Experience, Technology, Certification, Project, BlogPost, BlogCategory, Book
from django.core.paginator import Paginator

def home(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')
    technologies = Technology.objects.all()
    certifications = Certification.objects.all().order_by('-date_obtained')
    projects = Project.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'technologies': technologies,
        'certifications': certifications,
        'projects': projects,
    }
    
    return render(request, 'main/home.html', context)

def about(request):
    profile = Profile.objects.first()
    return render(request, 'main/about.html', {'profile': profile})

def experience(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')
    
    context = {
        'profile': profile,
        'experiences': experiences,
    }
    
    return render(request, 'main/experience.html', context)

def technologies(request):
    technologies = Technology.objects.all()
    certifications = Certification.objects.all().order_by('-date_obtained')
    return render(request, 'main/technologies.html', {
        'technologies': technologies,
        'certifications': certifications
    })

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    
    context = {
        'profile': profile,
        'projects': projects,
    }
    
    return render(request, 'main/projects.html', context)

def contact(request):
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        # Here you would process the form data
        # For example, send an email or save to database
        # This is a placeholder for form processing logic
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Add your email sending logic here
        # For now, we'll just return the same page with a success message
        return render(request, 'main/contact.html', {
            'profile': profile,
            'success_message': 'Thank you for your message! I will get back to you soon.'
        })
    
    return render(request, 'main/contact.html', {'profile': profile})

def blog_list(request):
    profile = Profile.objects.first()
    posts_list = BlogPost.objects.filter(is_published=True)
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        posts_list = posts_list.filter(categories=category)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(title__icontains=query) | posts_list.filter(content__icontains=query)
    
    # Pagination
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {
        'profile': profile,
        'posts': posts,
        'categories': BlogCategory.objects.all(),
        'current_category': category_slug,
        'search_query': query,
    }
    
    return render(request, 'main/blog.html', context)

def blog_detail(request, slug):
    profile = Profile.objects.first()
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    context = {
        'profile': profile,
        'post': post,
    }
    
    return render(request, 'main/blog_detail.html', context)

def books(request):
    profile = Profile.objects.first()
    books_list = Book.objects.all()
    
    context = {
        'profile': profile,
        'books': books_list,
    }
    
    return render(request, 'main/books.html', context)
