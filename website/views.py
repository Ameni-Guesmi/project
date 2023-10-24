from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect
from product.models import category, product
#from .models import  products_latest, products_picked, ProductCategory
from .forms import SearchForm 



def categories(request):
    return render(request,'website/parts/categories.html')

def category_products(request, id, slug):
    Category = category.objects.all()
    Products = product.objects.filter(category_id=id) 
    context ={'products':  Products,
              'Category': Category}
    return render(request,'website/parts/category_products.html')


def navbar(request):
   return render(request, 'website/parts/navbar.html')

def footer(request):
    return render(request, 'website/parts/footer.html')



def carousel(request):
    return render(request, 'website/parts/carousel.html')

def index(request):
    return render(request, 'website/parts/index.html')

def content(request):
    products_Latest=product.objects.all().order_by('-id')[:4] # Last 4 products
    products_picked=product.objects.all().order_by('?')[:2] # Random selected 2 products
    page="website"
    context={'page':page,
            'products_Latest':products_Latest,
            ' products_picked': products_picked,
            'category':category}
   
    return render(request, 'website/parts/content.html',context)

def nav(request):
    return render(request, 'website/parts/nav.html')

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = product.objects.filter(title__icontains=query)
            else:
                products = product.objects.filter(title__icontains=query, category_id=catid)
            
            # Retrieve all categories
            categories = category.objects.all()
            
            context = {
                'products': products,
                'query': query,
                'categories': categories,  # Pass all categories to the template
            }
            
            return render(request, 'website/parts/search_products.html', context)
    
    return HttpResponseRedirect('/')




def base(request):
    return render(request, 'base.html')













