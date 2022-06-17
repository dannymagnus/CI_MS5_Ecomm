from .models import Course

def courses(request):
    return {
        'courses': Course.objects.all()
    }
