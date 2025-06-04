from .models import Profile

def profile_context(request):
    return {
        'profile': Profile.objects.first(),
        'current_year': __import__('datetime').datetime.now().year
    }