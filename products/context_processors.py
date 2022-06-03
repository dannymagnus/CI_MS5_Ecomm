from .models import Brand, Category

def brands(request):
    return {
        'brands': Brand.objects.all()
    }

def categories(request):
    return{
        'categories': Category.objects.all()
    }