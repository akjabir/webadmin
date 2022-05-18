from django.shortcuts import render
from .import models
from django.db.models import F,Q
from django.http import JsonResponse
from django.core.paginator import Paginator

def index(request):
    seo_contain   = models.SeoContent.objects.filter(status = True).first()
    service_data  = models.Service.objects.filter(status = True).order_by('catagory','ordering','title')
    context ={
        'seo_contain'  : seo_contain,
        'service_data' : service_data,
    }
    if request.method == "POST":
        product = request.POST['search']
        product_list = models.Service.objects.filter(title_url__icontains = product)
        return render(request, 'history/search_result.html',{'product_list' : product_list, 'product' : product})

    return render(request, 'history/index.html',context)

def service(request, nam):
    name = nam.replace('-', ' ') 
    request.session["category_name"] = name
    category_data   = models.Service.objects.filter(status = True, catagory_id__cat_name = name)
    seo_contain     = models.Service.objects.filter(status = True, catagory_id__cat_name = name).first()

    paginator = Paginator(category_data, 12) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    category_data = paginator.get_page(page_number)
    context ={
        'category_data' : category_data,
        'seo_contain' : seo_contain,
    }
    if request.method == "POST":
        product = request.POST['search']
        product_list = models.Service.objects.filter(title_url__icontains = product)
        return render(request, 'history/search_result.html',{'product_list' : product_list, 'product' : product})
    
    return render(request,'history/cat_data.html', context)

 
def single_post(request, name, nam):
    name1 = nam.replace('-', ' ') 
    single_data     = models.Service.objects.filter( title_url = name1 ).first()
    if single_data :
        single_data     = models.Service.objects.filter( title_url = name1 ).first()
    else:
        single_data = 0
        
    rel_post        = models.Service.objects.filter(status = True, catagory_id = single_data.catagory_id).exclude(title_url = name1).order_by("-id")
    popular_post    = models.Service.objects.filter(status = True,catagory_id = single_data.catagory_id).exclude(title_url = name1).order_by("views")
    models.Service.objects.filter(title_url = name1 ).update(views = F('views') + 1)

    context ={
        'single_data':single_data,
        'rel_post': rel_post,
        'popular_post': popular_post,
    }
    if request.method == "POST":
        product = request.POST['search']
        product_list = models.Service.objects.filter(title_url__icontains = product)
        return render(request, 'history/search_result.html',{'product_list' : product_list, 'product' : product})
    
    return render(request,'history/single_post.html', context)

def data_search(request):
	if request.is_ajax():
		src_data = request.GET['src_data']  
        
	if len(src_data) > 0:
		query_obj   = models.Service.objects.values('title_url','catagory_id__cat_name').filter(title_url__istartswith = src_data)

	if query_obj:
		return JsonResponse(list(query_obj), safe = False, content_type='application/json; charset=utf8')
	else:
		return HttpResponse("", content_type ="application/json")
    
	return HttpResponse("", content_type ="application/json")


def Privacy(request):
    privacy  = models.Privacy.objects.first()
    context = {
        'privacy' : privacy,
    }
    return render(request, 'history/privacy.html',context)

def Aboutus(request):
    aboutus = models.Aboutus.objects.first()
    context = {
        'aboutus' : aboutus,
    }
    return render(request, 'history/aboutus.html',context)

def Term(request):
    term = models.Term.objects.first()
    context = {
        'term'    : term,
    }
    return render(request, 'history/term.html',context)

def Contact(request):
    contact = models.Contact.objects.first()
    context = {
        'contact'  : contact,
    }
    return render(request, 'history/contact.html', context)
    